import markdown, re
from bs4 import BeautifulSoup
import gdoc

bs4_parser = 'html.parser'

md_content_file = 'md/content.md'
html_template_file = 'templates/main.html'
html_output_file = 'public_html/index.html'

# Open and read template file
main_soup = gdoc.html_file_to_soup(html_template_file)

# Read Markdown and make a Beautiful soup
content_soup = gdoc.md_file_to_soup(md_content_file)

# Remove any strong-tags inside of headings
content_soup = gdoc.clean_up_headers(content_soup)

# Create sections
content_soup = gdoc.create_sections(content_soup)

# Create articles
content_soup = gdoc.create_articles(content_soup)

# Wrap tables in div
content_soup = gdoc.div_wrap(content_soup, 'table', 'table-container')
content_soup = gdoc.div_wrap(content_soup, 'pre', 'code-container')

# Generate and insert table of content
toc_soup = gdoc.create_toc(content_soup)

toc_title = main_soup.new_tag('h4')
toc_title.string = 'Grunderna i Python'
main_soup.aside.append(toc_title)
main_soup.aside.append(toc_soup)

# Append the content to <main> of the template
main_soup.main.append(content_soup)

# Render to HTML-string
html_output = main_soup.decode(formatter="html")

# Remove trailing slashes
html_output = gdoc.remove_trailing_slashes(html_output)

# Write the combined HTML to file
with open(html_output_file, 'w', encoding='utf-8') as output_file:
    output_file.write(html_output)