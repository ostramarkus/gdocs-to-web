import md2html
import yaml

def main():
    # Open and parse site config file
    with open('site-config.yaml', encoding="utf-8") as config_file:
        site_config = yaml.safe_load(config_file.read())

    for page in site_config:
        md_content_file = 'md/' + page['md_file']
        html_template_file = 'templates/main.html'
        title = page['title']

        # Create navigation data
        navigation = [(page['id'], page['link_text'], page['html_file']) for page in site_config]
        testpage = md2html.Document('md/index.md', 'templates/main.html', 'Testpage')
        testpage.insert_main_nav(navigation)
        
        print(testpage.content_soup)
        print(testpage.template_soup)

if __name__ == '__main__':
    main()