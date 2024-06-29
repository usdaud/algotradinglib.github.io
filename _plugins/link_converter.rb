module Jekyll
  class LinkConverter < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      site.pages.each do |page|
        if page.output_ext == ".html"
          if page.output
            page.output.gsub!(/(<a href=".*?)\.md(["'])/, '\1.html\2')
          else
            Jekyll.logger.warn "LinkConverter:", "No output for page: #{page.path}"
          end
        end
      end
    end
  end
end