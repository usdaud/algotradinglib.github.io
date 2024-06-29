module Jekyll
  class LinkConverter < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      site.pages.each do |page|
        if page.output_ext == ".html"
          page.output.gsub!(/(<a href=".*?)\.md(["'])/, '\1.html\2')
        end
      end
    end
  end
end