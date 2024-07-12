module Jekyll
  class LetterPageGenerator < Generator
    safe true

    SECTIONS = ['pedia', 'soft', 'brokers', 'market-data', 'community']

    def generate(site)
      Jekyll.logger.info "LetterPageGenerator:", "Total pages: #{site.pages.size}"

      @page_cache = {}
      @processed_pages = Set.new
      base_url = site.config['url'] || ''

      languages = ['en', 'ru', 'zh']
      
      languages.each do |lang|
        locale = load_locale(site, lang)

        process_root_page(site, lang, locale, base_url)
        process_subscribe_page(site, lang, locale, base_url)
        
        SECTIONS.each do |section|
          section_path = File.join(site.source, lang, section)
          if Dir.exist?(section_path)
            process_section(site, lang, section, section_path, locale, base_url)
          else
            Jekyll.logger.warn "LetterPageGenerator:", "Directory not found: #{section_path}"
          end
        end
      end
    end

    def load_locale(site, lang)
      locale_file = File.join(site.source, lang, 'locales.yml')
      if File.exist?(locale_file)
        YAML.load_file(locale_file)
      else
        Jekyll.logger.warn "LetterPageGenerator:", "Locale file not found: #{locale_file}"
        {}
      end
    end

    def process_root_page(site, lang, locale, base_url)
      root_file = File.join(site.source, lang, 'index.md')
      if File.exist?(root_file)
        content = File.read(root_file, encoding: 'utf-8')
        page = Jekyll::Page.new(site, site.source, lang, 'index.md')
        page.content = content
        page.data['lang'] = lang
        page.data['locale'] = locale
        page.data['canonical_url'] = "#{base_url}/#{lang}/"
        site.pages << page
      else
        Jekyll.logger.warn "LetterPageGenerator:", "Root page not found for language: #{lang}"
      end
    end

    def process_subscribe_page(site, lang, locale, base_url)
      subscribe_file = File.join(site.source, lang, 'subscribe.md')
      unless File.exist?(subscribe_file)
        content = "---\nlayout: subscribe\ntitle: #{locale['subscribe']}\n---\n"
        File.write(subscribe_file, content)
      end

      page = Jekyll::Page.new(site, site.source, lang, 'subscribe.md')
      page.data['lang'] = lang
      page.data['locale'] = locale
      page.data['permalink'] = "/#{lang}/subscribe/"
      page.data['canonical_url'] = "#{base_url}/#{lang}/subscribe/"
      site.pages << page
    end

    def process_section(site, lang, section, section_path, locale, base_url)
      if ['soft', 'market-data', 'brokers', 'community'].include?(section)
        process_catalog_section(site, lang, section, section_path, locale, base_url)
      else
        process_pedia_section(site, lang, section, section_path, locale, base_url)
      end
    end

    def process_catalog_section(site, lang, section, section_path, locale, base_url)
      catalog_data = load_catalog_data(site, section_path)
      
      if ['market-data', 'brokers'].include?(section)
        soft_data = load_catalog_data(site, File.join(site.source, lang, 'soft'))
        catalog_data.each do |item|
          item['supported_software'] = soft_data.select do |soft|
            if section == 'market-data'
              soft['supported_data_providers']&.include?(item['name'])
            else
              soft['supported_brokers']&.include?(item['name'])
            end
          end.map { |soft| soft['name'] }
        end
      elsif section == 'soft'
        catalog_data.each do |item|
          item['supported_data_providers'] = item['supported_data_providers'] || []
          item['supported_brokers'] = item['supported_brokers'] || []
        end
      end

      site.pages << CatalogIndexPage.new(site, site.source, lang, section, catalog_data, locale, base_url)
    end

    def load_catalog_data(site, section_path)
      yaml_file = File.join(section_path, 'list.yml')
      if File.exist?(yaml_file)
        YAML.load_file(yaml_file)
      else
        Jekyll.logger.warn "LetterPageGenerator:", "Catalog YAML file not found: #{yaml_file}"
        []
      end
    end

    def process_pedia_section(site, lang, section, section_path, locale, base_url)
      letters = {}
      Dir.glob(File.join(section_path, '*')).each do |letter_path|
        if File.directory?(letter_path)
          letter = File.basename(letter_path).downcase
          count = count_posts(site, lang, section, letter, letter_path)
          letters[letter] = count if count > 0
        end
      end

      letters = letters.sort.to_h

      Jekyll.logger.info "LetterPageGenerator:", "Letters and counts: #{letters}"

      letters.each do |letter, count|
        Jekyll.logger.info "LetterPageGenerator:", "Creating page for #{lang}/#{section}/#{letter} with #{count} posts"
        site.pages << LetterPage.new(site, site.source, lang, section, letter, locale, base_url)
    
        Dir.glob(File.join(section_path, letter, '*.md')).each do |file|
          process_markdown_file(site, file, lang, locale, base_url)
        end
      end
      site.pages << PediaIndexPage.new(site, site.source, lang, section, letters, locale, base_url)
    end

    def process_markdown_file(site, file, lang, locale, base_url)
      return if @processed_pages.include?(file)
      
      content = File.read(file, encoding: 'utf-8')
      title = extract_title_from_content(content)

      page = Jekyll::Page.new(site, site.source, File.dirname(file), File.basename(file))
      page.data['layout'] = 'base'
      page.data['title'] = title if title
  
      page.data['lang'] = lang
      page.data['locale'] = locale

      page.data['permalink'] = "/#{file.sub(site.source + '/', '').sub('.md', '.html')}"
      page.data['canonical_url'] = "#{base_url}#{page.data['permalink']}"
  
      site.pages << page
      @processed_pages.add(file)
    rescue => e
      Jekyll.logger.error "LetterPageGenerator:", "Error processing file #{file}: #{e.message}"
    end

    def extract_title_from_content(content)
      match = content.match(/^#\s*(.+)$/)
      match ? match[1].strip : nil
    end

    def count_posts(site, lang, section, letter, letter_path)
      cache_key = "#{lang}/#{section}/#{letter}"
      return @page_cache[cache_key] if @page_cache.has_key?(cache_key)

      count = Dir.glob(File.join(letter_path, '*.md')).count { |file| File.basename(file) != 'index.md' }

      @page_cache[cache_key] = count
      Jekyll.logger.info "LetterPageGenerator:", "Counting posts for #{cache_key}: #{count}"
      count
    end
  end

  class LetterPage < Page
    def initialize(site, base, lang, section, letter, locale, base_url)
      @site = site
      @base = base
      @dir  = File.join(lang, section, letter)
      @name = "index.md"

      self.process(@name)
      layout_file = File.join(base, '_layouts', 'letter_index.html')

      if File.exist?(layout_file)
        self.read_yaml(File.dirname(layout_file), File.basename(layout_file))
      else
          Jekyll.logger.warn "LetterPageGenerator:", "Layout file 'letter_index.html' not found"
          self.data = {}
      end

      self.data['layout'] = 'letter_index'
      self.data['title'] = letter.upcase
      self.data['letter'] = letter
      self.data['lang'] = lang
      self.data['locale'] = locale
      self.data['section'] = section
      self.data['permalink'] = "/#{lang}/#{section}/#{letter}/index.html"
      self.data['canonical_url'] = "#{base_url}/#{lang}/#{section}/#{letter}/"
    end
  end

  class PediaIndexPage < Page
    def initialize(site, base, lang, section, letters, locale, base_url)
      @site = site
      @base = base
      @dir  = File.join(lang, section)
      @name = "index.md"

      self.process(@name)
      layout_file = File.join(base, '_layouts', 'section_index.html')
      if File.exist?(layout_file)
        self.read_yaml(File.dirname(layout_file), File.basename(layout_file))
      else
        Jekyll.logger.warn "LetterPageGenerator:", "Layout file 'section_index.html' not found"
        self.data = {}
      end
      self.data['layout'] = 'section_index'
      self.data['title'] = case lang
                           when 'en' then "Algopedia"
                           when 'ru' then "Алгопедия"
                           when 'zh' then "算法百科"
                           end
      self.data['letters'] = letters
      self.data['lang'] = lang
      self.data['locale'] = locale
      self.data['section'] = section
      self.data['canonical_url'] = "#{base_url}/#{lang}/#{section}/"
    end
  end

  class CatalogIndexPage < Page
    def initialize(site, base, lang, section, catalog_data, locale, base_url)
      @site = site
      @base = base
      @dir  = File.join(lang, section)
      @name = "index.md"

      self.process(@name)
      layout_file = File.join(base, '_layouts', 'catalog_index.html')
      if File.exist?(layout_file)
        self.read_yaml(File.dirname(layout_file), File.basename(layout_file))
      else
        Jekyll.logger.warn "LetterPageGenerator:", "Layout file 'catalog_index.html' not found"
        self.data = {}
      end
      self.data['layout'] = 'catalog_index'
      self.data['title'] = case section
                       when 'soft'
                         case lang
                         when 'en' then "Software"
                         when 'ru' then "Софт"
                         when 'zh' then "软件"
                         end
                       when 'market-data'
                         case lang
                         when 'en' then "Market Data"
                         when 'ru' then "Рыночные данные"
                         when 'zh' then "市场数据"
                         end
                       when 'brokers'
                         case lang
                         when 'en' then "Brokers"
                         when 'ru' then "Брокеры"
                         when 'zh' then "经纪人"
                         end
                       when 'community'
                         case lang
                         when 'en' then "Community"
                         when 'ru' then "Сообщества"
                         when 'zh' then "社区"
                         end
                       end
      self.data['catalog'] = catalog_data
      self.data['lang'] = lang
      self.data['locale'] = locale
      self.data['section'] = section
      self.data['permalink'] = "/#{lang}/#{section}/index.html"
      self.data['canonical_url'] = "#{base_url}/#{lang}/#{section}/"

      special_filters_file = File.join(base, lang, section, 'special_filters.yml')
      if File.exist?(special_filters_file)
        self.data['special_filters'] = YAML.load_file(special_filters_file)
      else
        self.data['special_filters'] = []
      end
    end
  end
end