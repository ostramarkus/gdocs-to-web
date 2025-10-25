import markdown, re
from bs4 import BeautifulSoup
import gdoc

bs4_parser = 'html.parser'
md_content_file = 'md/content.md'
html_template_file = 'templates/main.html'

preserve_whitespace_tags = ["p", "h1", "h2", "h3", "li", "span", "em", "b", "i", "strong"]

# Open and read template file
main_soup = gdoc.html_file_to_soup(html_template_file)

# Make a Beautiful soup of the content
content_soup = gdoc.md_file_to_soup(md_content_file)

# Remove any strong-tags inside of headings
content_soup = gdoc.clean_up_headers(content_soup)

# Create sections
content_soup = gdoc.create_sections(content_soup)

# Create article
content_soup = gdoc.create_articles(content_soup)

toc = gdoc.create_toc(content_soup)

# Append the content to <main> of the template 
main_soup.main.append(content_soup)

# Render to HTML-string
html_output = main_soup.decode(formatter="html")

# Remove trailing slashes to conform with HTML5
void_tags = ["area", "base", "br", "col", "embed", "hr", "img",
             "input", "link", "meta", "param", "source", "track", "wbr"]

for tag in void_tags:
    html_output = re.sub(rf'<{tag}([^>]*)\s*/>', rf'<{tag}\1>', html_output)

# Write the combined HTML to file
with open('index.html', 'w', encoding='utf-8') as output_file:
    output_file.write(html_output)