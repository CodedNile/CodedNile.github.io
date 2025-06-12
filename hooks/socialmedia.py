from textwrap import dedent
import urllib.parse

def on_page_markdown(markdown, page, config, **kwargs):
    if not page.file.src_path.startswith("posts/"):
        return markdown

    page_url = config['site_url'] + page.url
    page_title = urllib.parse.quote(page.title)

    return markdown + dedent(f"""
    <div style="text-align: center; margin-top: 2em;">
      <h2 style="text-align: center; font-weight: bold; text-decoration: underline; color: #fff;">
        Share on Socials
      </h2>
      <div style="margin-top: 1em; display: flex; justify-content: center; gap: 1em; flex-wrap: wrap;">
        <!-- X -->
        <a href="https://x.com/intent/tweet?text={page_title}&url={page_url}"
           target="_blank" rel="noopener"
           style="display: inline-flex; align-items: center; border: 2px solid #ff5722; color: #ff5722;
                  padding: 0.6em 1.2em; font-weight: 600; border-radius: 6px; text-decoration: none;">
          <span class="twemoji" style="margin-right: 0.5em;"></span> Share on X
        </a>

        <!-- Facebook -->
        <a href="https://facebook.com/sharer/sharer.php?u={page_url}"
           target="_blank" rel="noopener"
           style="display: inline-flex; align-items: center; border: 2px solid #ff5722; color: #ff5722;
                  padding: 0.6em 1.2em; font-weight: 600; border-radius: 6px; text-decoration: none;">
          <span class="twemoji" style="margin-right: 0.5em;"></span> Share on Facebook
        </a>

        <!-- WhatsApp -->
        <a href="https://api.whatsapp.com/send?text={page_title}%20{page_url}"
           target="_blank" rel="noopener"
           style="display: inline-flex; align-items: center; border: 2px solid #ff5722; color: #ff5722;
                  padding: 0.6em 1.2em; font-weight: 600; border-radius: 6px; text-decoration: none;">
          <span class="twemoji" style="margin-right: 0.5em;"></span> Share on WhatsApp
        </a>

      </div>
    </div>
    """)
