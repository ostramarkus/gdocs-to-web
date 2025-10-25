import markdown, re
from bs4 import BeautifulSoup

bs4_parser = 'html.parser'

preserve_whitespace_tags = ["p", "h1", "h2", "h3", "li", "span", "em", "b", "i", "strong"]

# Open and read template file
with open('templates/main.html', encoding='utf-8') as template_file:
    template_html = template_file.read()

# Open and read Markdown file (with the content)
with open('md/content.md', encoding='utf-8') as md_file:
    md_content = md_file.read()

# Make a Beautiful soup of the template
main_soup = BeautifulSoup(template_html, bs4_parser)

# Convert Markdown to HTML
content_html = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])

# Make a Beautiful soup of the content
content_soup = BeautifulSoup(content_html, bs4_parser)

# Remove any strong-tags inside of headings
for header in content_soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    for strong in header.find_all("strong"):
        strong.unwrap()
    # and removes empty headings
    if not header.get_text(strip=True):
        header.decompose()

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