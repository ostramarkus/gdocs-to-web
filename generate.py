import gdoc


md_content_file = 'md/github.md'
html_template_file = 'templates/main.html'
html_output_file = 'public_html/github.html'

html_output = gdoc.md_to_html(md_content_file, html_template_file, 'main')

# Write the combined HTML to file
with open(html_output_file, 'w', encoding='utf-8') as output_file:
    output_file.write(html_output)