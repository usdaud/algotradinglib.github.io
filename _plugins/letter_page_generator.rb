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
            letters = []
            Dir.entries(section_path).select { |entry| File.directory?(File.join(section_path, entry)) && entry != '.' && entry != '..' }.each do |letter_dir|
              letter = letter_dir.downcase
              letters << letter
              Jekyll.logger.info "LetterPageGenerator:", "Creating page for #{lang}/#{section}/#{letter}"
              site.pages << LetterPage.new(site, site.source, lang, section, letter)
            end
            site.pages << SectionIndexPage.new(site, site.source, lang, section, letters)

            # Set layout for all section pages
            site.pages.each do |page|
              if page.path.start_with?(File.join(lang, section)) && !page.data['layout']
                page.data['layout'] = 'base'
              end
            end
          else
            Jekyll.logger.warn "LetterPageGenerator:", "Directory not found: #{section_path}"
          end
        end
      end
    end
  end

  class LetterPage < Page
    def initialize(site, base, lang, section, letter)
      @site = site
      @base = base
      @dir  = File.join(lang, section)
      @name = "#{letter}.md"

      self.process(@name)
      layout_file = File.join(base, '_layouts', 'letter_index.html')
      if File.exist?(layout_file)
        self.read_yaml(File.dirname(layout_file), File.basename(layout_file))
      else
        Jekyll.logger.warn "LetterPageGenerator:", "Layout file 'letter_index.html' not found"
        self.data = {}
      end
      self.data['layout'] = 'letter_index'
      self.data['title'] = case lang
                           when 'en' then "#{section.capitalize} topics starting with #{letter.upcase}"
                           when 'ru' then "Темы #{section_name_ru(section)} на букву #{letter.upcase}"
                           when 'zh' then "#{section_name_zh(section)}#{letter}开头的主题"
                           end
      self.data['letter'] = letter
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