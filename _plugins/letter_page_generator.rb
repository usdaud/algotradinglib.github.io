module Jekyll
  class LetterPageGenerator < Generator
    safe true

    SECTIONS = ['pedia', 'soft', 'brokers', 'market-data', 'community']

    def generate(site)
      Jekyll.logger.info "LetterPageGenerator:", "Total pages: #{site.pages.size}"

      site.pages.each do |page|
        Jekyll.logger.info "LetterPageGenerator:", "Page path: #{page.path}"
      end

      languages = ['en', 'ru', 'zh']
      
      languages.each do |lang|
        SECTIONS.each do |section|
          section_path = File.join(site.source, lang, section)
          Jekyll.logger.info "LetterPageGenerator:", "Checking path: #{section_path}"
          if Dir.exist?(section_path)
            process_section(site, lang, section, section_path)
          else
            Jekyll.logger.warn "LetterPageGenerator:", "Directory not found: #{section_path}"
          end
        end
      end
    end

    def process_section(site, lang, section, section_path)
      if ['soft', 'market-data', 'brokers', 'community'].include?(section)
        process_catalog_section(site, lang, section, section_path)
      else
        process_regular_section(site, lang, section, section_path)
      end
    end

    def process_catalog_section(site, lang, section, section_path)
      catalog_data = load_catalog_data(site, section_path)
      site.pages << CatalogIndexPage.new(site, site.source, lang, section, catalog_data)
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

    def process_regular_section(site, lang, section, section_path)
      letters = Dir.entries(section_path)
                   .select { |entry| File.directory?(File.join(section_path, entry)) && entry != '.' && entry != '..' }
                   .map { |letter| [letter.downcase, count_posts(site, lang, section, letter)] }
                   .sort.to_h

      Jekyll.logger.info "LetterPageGenerator:", "Letters and counts: #{letters}"

      letters.each do |letter, count|
        Jekyll.logger.info "LetterPageGenerator:", "Creating page for #{lang}/#{section}/#{letter} with #{count} posts"
        site.pages << LetterPage.new(site, site.source, lang, section, letter)
    
        Dir.glob(File.join(section_path, letter, '*.md')).each do |file|
          Jekyll.logger.info "LetterPageGenerator:", "Processing file: #{file}"
          process_markdown_file(site, file)
        end
      end
      site.pages << SectionIndexPage.new(site, site.source, lang, section, letters)
    end

    def process_markdown_file(site, file)
      content = File.read(file, encoding: 'utf-8')
      title = extract_title_from_content(content)

      page = Jekyll::Page.new(site, site.source, File.dirname(file), File.basename(file))
      page.data['layout'] = 'base'
      page.data['title'] = title if title
  
      lang = file.split('/')[1]
      page.data['lang'] = lang

      page.data['permalink'] = "/#{file.sub(site.source + '/', '').sub('.md', '.html')}"
  
      site.pages << page
    rescue => e
      Jekyll.logger.error "LetterPageGenerator:", "Error processing file #{file}: #{e.message}"
    end

    def extract_title_from_content(content)
      match = content.match(/^#\s*(.+)$/)
      match ? match[1].strip : nil
    end

    def count_posts(site, lang, section, letter)
      count = 0
      site.pages.each do |page|
        page_path = page.path.split('/')
        starts_with_letter = page_path[2] && letter && page_path[2].to_s.downcase.start_with?(letter.to_s.downcase)

        if page_path.size >= 4 && 
           page_path[0] == lang && 
           page_path[1] == section && 
           starts_with_letter && 
           page.path.end_with?('.md') && 
           page.name != 'index.md'
          count += 1
          Jekyll.logger.info "LetterPageGenerator:", "Matched post: #{page.path}"
        else
          Jekyll.logger.info "LetterPageGenerator:", "Not matched: #{page.path}, " \
            "conditions: lang=#{page_path[0] == lang}, " \
            "section=#{page_path[1] == section}, " \
            "letter=#{starts_with_letter}, " \
            "md=#{page.path.end_with?('.md')}, " \
            "not_index=#{page.name != 'index.md'}"
        end
      end
      Jekyll.logger.info "LetterPageGenerator:", "Counting posts for #{lang}/#{section}/#{letter}: #{count}"
      count
    end
  end

  class LetterPage < Page
    def initialize(site, base, lang, section, letter)
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
      self.data['section'] = section
      self.data['permalink'] = "/#{lang}/#{section}/#{letter}/index.html"
    end
  end

  class SectionIndexPage < Page
    def initialize(site, base, lang, section, letters)
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
                           when 'en' then "#{section.capitalize} Index"
                           when 'ru' then "Индекс #{section_name_ru(section)}"
                           when 'zh' then "#{section_name_zh(section)}索引"
                           end
      self.data['letters'] = letters
      self.data['lang'] = lang
      self.data['section'] = section
    end

    private

    def section_name_ru(section)
      case section
      when 'pedia' then 'энциклопедии'
      when 'soft' then 'программного обеспечения'
      when 'brokers' then 'брокеров'
      else section
      end
    end

    def section_name_zh(section)
      case section
      when 'pedia' then '百科全书'
      when 'soft' then '软件'
      when 'brokers' then '经纪人'
      else section
      end
    end
  end

  class CatalogIndexPage < Page
    def initialize(site, base, lang, section, catalog_data)
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
      self.data['title'] = case lang
                           when 'en' then "Software Index"
                           when 'ru' then "Индекс программного обеспечения"
                           when 'zh' then "软件索引"
                           end
      self.data['catalog'] = catalog_data
      self.data['lang'] = lang
      self.data['section'] = section
      self.data['permalink'] = "/#{lang}/#{section}/index.html"
    end
  end
end