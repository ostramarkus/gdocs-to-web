import yaml

with open('../site-config.yaml', encoding="utf-8") as config_file:
    site_config = yaml.safe_load(config_file.read())


for page in site_config:
    print(page['title'])