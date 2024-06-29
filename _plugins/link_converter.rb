module Jekyll
  class LinkConverter < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      site.pages.each do |page|
        if page.ext == ".md"
          convert_links(page)
        end
      end
    end

    def convert_links(page)
      page.content.gsub!(/(\[.*?\])\((.*?)\.md\)/) do |match|
        link_text = $1
        link_path = $2
        "#{link_text}(#{link_path}.html)"
      end
    end
  end
end