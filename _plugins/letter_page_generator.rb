module Jekyll
  class LetterPageGenerator < Generator
    safe true

    def generate(site)
      languages = ['en', 'ru', 'zh']
      
      languages.each do |lang|
        pedia_path = File.join(site.source, lang, 'pedia')
        Jekyll.logger.info "LetterPageGenerator:", "Checking path: #{pedia_path}"
        if Dir.exist?(pedia_path)
          letters = []
          Dir.entries(pedia_path).select { |entry| File.directory?(File.join(pedia_path, entry)) && entry != '.' && entry != '..' }.each do |letter_dir|
            letter = letter_dir.downcase
            letters << letter
            Jekyll.logger.info "LetterPageGenerator:", "Creating page for #{lang}/#{letter}"
            site.pages << LetterPage.new(site, site.source, lang, letter)
          end
          site.pages << PediaIndexPage.new(site, site.source, lang, letters)
        else
          Jekyll.logger.warn "LetterPageGenerator:", "Directory not found: #{pedia_path}"
        end
      end
    end
  end

  class LetterPage < Page
    def initialize(site, base, lang, letter)
      @site = site
      @base = base
      @dir  = File.join(lang, 'pedia')
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
                           when 'en' then "Topics starting with #{letter.upcase}"
                           when 'ru' then "Темы на букву #{letter.upcase}"
                           when 'zh' then "#{letter} 开头的主题"
                           end
      self.data['letter'] = letter
      self.data['lang'] = lang
    end
  end

  class PediaIndexPage < Page
    def initialize(site, base, lang, letters)
      @site = site
      @base = base
      @dir  = File.join(lang, 'pedia')
      @name = "index.md"

      self.process(@name)
      layout_file = File.join(base, '_layouts', 'pedia_index.html')
      if File.exist?(layout_file)
        self.read_yaml(File.dirname(layout_file), File.basename(layout_file))
      else
        Jekyll.logger.warn "LetterPageGenerator:", "Layout file 'pedia_index.html' not found"
        self.data = {}
      end
      self.data['layout'] = 'pedia_index'
      self.data['title'] = case lang
                           when 'en' then "Encyclopedia Index"
                           when 'ru' then "Индекс Энциклопедии"
                           when 'zh' then "百科索引"
                           end
      self.data['letters'] = letters
      self.data['lang'] = lang
    end
  end
end