module Jekyll
  class LetterPageGenerator < Generator
    safe true

    SECTIONS = ['pedia', 'soft', 'brokers']

    def generate(site)
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
      letters = []
      Dir.entries(section_path).select { |entry| File.directory?(File.join(section_path, entry)) && entry != '.' && entry != '..' }.each do |letter_dir|
        letter = letter_dir.downcase
        letters << letter
        Jekyll.logger.info "LetterPageGenerator:", "Creating page for #{lang}/#{section}/#{letter}"
        site.pages << LetterPage.new(site, site.source, lang, section, letter)
        
        # Process individual Markdown files
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

      page.data['permalink'] = "/#{file.sub(site.source + '/', '').sub('.md', '.html')}"
  
      site.pages << page
    rescue => e
      Jekyll.logger.error "LetterPageGenerator:", "Error processing file #{file}: #{e.message}"
    end

    def extract_title_from_content(content)
      match = content.match(/^#\s*(.+)$/)
      match ? match[1].strip : nil
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
end