require 'zip'

module Jekyll
  class SitemapGenerator < Generator
    safe true
    priority :lowest

    def generate(site)
      sitemap_content = generate_sitemap_content(site)
      
      create_zip(site, sitemap_content)
    end

    private

    def generate_sitemap_content(site)
      content = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
      content << "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"

      site.pages.each do |page|
        next if page.data['sitemap'] == false
        content << "  <url>\n"
        content << "    <loc>#{site.config['url']}#{page.url}</loc>\n"
        content << "    <lastmod>#{File.mtime(page.path).strftime('%Y-%m-%d')}</lastmod>\n"
        content << "  </url>\n"
      end

      content << "</urlset>"
      content
    end

    def create_zip(site, content)
      temp_dir = Dir.mktmpdir
      begin
        sitemap_path = File.join(temp_dir, 'sitemap.xml')
        File.write(sitemap_path, content)

        zip_path = File.join(site.dest, 'sitemap.zip')
        Zip::File.open(zip_path, Zip::File::CREATE) do |zipfile|
          zipfile.add('sitemap.xml', sitemap_path)
        end

        site.static_files << Jekyll::StaticFile.new(site, site.dest, '', 'sitemap.zip')
      ensure
        FileUtils.remove_entry temp_dir
      end
    end
  end
end