module Jekyll
  class LetterPageGenerator < Generator
    safe true

    def generate(site)
      languages = ['en', 'ru', 'zh']
      
      languages.each do |lang|
        pedia_path = File.join(site.source, lang, 'pedia')
        if Dir.exist?(pedia_path)
          Dir.entries(pedia_path).select { |entry| File.directory?(File.join(pedia_path, entry)) && entry != '.' && entry != '..' }.each do |letter_dir|
            letter = letter_dir.downcase
            site.pages << LetterPage.new(site, site.source, "#{lang}/pedia", letter, lang)
          end
        end
      end
    end
  end

  class LetterPage < Page
    def initialize(site, base, dir, letter, lang)
      @site = site
      @base = base
      @dir  = dir
      @name = "#{letter}.md"

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'letter_index.html')
      self.data['layout'] = 'letter_index'
      self.data['title'] = "Topics starting with #{letter.upcase}"
      self.data['letter'] = letter
      self.data['lang'] = lang
    end
  end
end