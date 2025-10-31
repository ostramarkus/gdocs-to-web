import gdoc
import yaml


# Open and parse site config file
with open('site-config.yaml', encoding="utf-8") as config_file:
    site_config = yaml.safe_load(config_file.read())


# Create navigation data
navigation = [(page['id'], page['link_text'], page['html_file']) for page in site_config]

for page in site_config:
    md_content_file = 'md/' + page['md_file']
    html_template_file = 'templates/main.html'
    title = page['title']

    try:
        html_output = gdoc.md_to_html(md_content_file, html_template_file, navigation, title=title)
    except FileNotFoundError:
        print(md_content_file, 'not found. Skipping.')
        continue

    # Write the combined HTML to file
    html_output_file = 'public_html/' + page['html_file']

    with open(html_output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(html_output)