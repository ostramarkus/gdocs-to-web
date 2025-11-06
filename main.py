import md2html
import yaml

def main():
    # Open and parse site config file
    with open('site-config.yaml', encoding="utf-8") as config_file:
        site_config = yaml.safe_load(config_file.read())

    # Create navigation data
    navigation = [(page['id'], page['link_text'], page['html_file']) for page in site_config]

    # Iterate each page - process and save
    for page in site_config:
        md_path = 'md/' + page['md_file']
        template_path = 'templates/main.html'
        title = page['title']

        document = md2html.Document(md_path, template_path, title=title, id=page['id'])
        document.insert_main_nav(navigation)
        document.save_html('public_html/' + page['html_file'])

if __name__ == '__main__':
    main()