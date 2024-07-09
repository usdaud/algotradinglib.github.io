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
      page.content.gsub!(/(\[.*?\])\((.*?)\)/) do |match|
        link_text = $1
        link_url = $2

        if internal_link?(link_url)
          if link_url.end_with?('.md')
            "#{link_text}(#{link_url.sub('.md', '.html')})"
          else
            "#{link_text}(#{link_url})"
          end
        else
          "#{link_text}(#{link_url}){:target=\"_blank\" rel=\"noopener noreferrer\"}"
        end
      end
    end

    private

    def internal_link?(link_url)
      !link_url.start_with?('http', 'https', 'www.', '/', 'mailto:')
    end
  end
end