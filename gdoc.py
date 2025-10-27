import re
import markdown
from slugify import slugify
from bs4 import BeautifulSoup

bs4_parser = 'html.parser'

def md_to_html(md_file, template_file, insert_tag):

    # Read Markdown and make a Beautiful soup
    content_soup = md_file_to_soup(md_file)

    # Cleanup and sectioning
    content_soup = clean_up_headers(content_soup)
    content_soup = create_sections(content_soup)
    content_soup = create_articles(content_soup)
    content_soup = div_wrap(content_soup, 'table', 'table-container')
    content_soup = div_wrap(content_soup, 'pre', 'code-container')

    # Open and read template file
    main_soup = html_file_to_soup(template_file)

    # Generate and insert table of content
    toc_soup = create_toc(content_soup)
    toc_title = main_soup.new_tag('h4')
    toc_title.string = 'Grunderna i Python'
    main_soup.aside.append(toc_title)
    main_soup.aside.append(toc_soup)

    # Append the content to <main> of the template
    main_soup.main.append(content_soup)

    # Render to HTML-string and cleanup HTML
    html_output = main_soup.decode(formatter="html")
    html_output = remove_trailing_slashes(html_output)
    return html_output

def html_file_to_soup(filename):
    ''' Read an HTML file and return a BeautifulSoup object '''
    with open(filename, encoding='utf-8') as html_file:
        html_str = html_file.read()
    return make_soup(html_str)


def md_file_to_soup(filename):
    ''' Read a Markdown file, convert to HTML, and return a BeautifulSoup object '''
    with open(filename, encoding='utf-8') as md_file:
        md_str = md_file.read()
    html_str = markdown.markdown(md_str, extensions=['fenced_code', 'tables'])
    return make_soup(html_str)


def make_soup(html_str):
    ''' Convert an HTML string to a BeautifulSoup object '''
    return BeautifulSoup(html_str, bs4_parser)


def clean_up_headers(soup):
    ''' Clean up headers by removing <strong> tags and empty headings '''
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        for strong in header.find_all("strong"):
            strong.unwrap()
        # and removes empty headings
        if not header.get_text(strip=True):
            header.decompose()    
    return soup


def create_sections(soup):
    ''' Create <section> tags around each <h2> and its content '''
    for h2 in list(soup.find_all("h2")):  # copy list to avoid iteration issues
        section = soup.new_tag("section")
        header_slug = slugify(h2.text)
        section['id'] = header_slug
        h2.insert_before(section)   # insert <section> before <h2>
        section.append(h2)          # move <h2> into section

        # Move all following siblings into section until next <h2> or end of document
        next_node = section.next_sibling
        while next_node and not (next_node.name == "h2"):
            sibling = next_node.next_sibling
            section.append(next_node)
            next_node = sibling
    return soup


def create_articles(soup):
    ''' Create <article> tags around each <h3> and its content '''
    for h3 in list(soup.find_all("h3")):  # Make a copy of the list to avoid iteration issues
        article = soup.new_tag("article")
        header_slug = slugify(h3.text)
        article['id'] = header_slug
        # Insert <article> before <h3>
        h3.insert_before(article)
        
        # Move <h3> into the <article>
        article.append(h3)

        # Move all following siblings into the <article> until next <h2> or <h3>
        next_node = article.next_sibling
        while next_node and not (next_node.name in ["h2", "h3"]):
            sibling = next_node.next_sibling
            article.append(next_node)
            next_node = sibling
    return soup


def remove_trailing_slashes(html_str):
    ''' Remove trailing slashes from void HTML tags '''
    void_tags = ["area", "base", "br", "col", "embed", "hr", "img",
                "input", "link", "meta", "param", "source", "track", "wbr"]

    for tag in void_tags:
        html_str = re.sub(rf'<{tag}([^>]*)\s*/>', rf'<{tag}\1>', html_str)
    return html_str


def get_toc_data(soup):
    ''' Extract TOC data from the soup object '''
    toc_data = []
    for section in soup.find_all('section'):
        section_id = section['id']
        section_title = section.find('h2').text
        section_data = {'id': section_id, 'title': section_title}

        section_articles = []
        for article in section.find_all('article'):
            article_id = article['id']
            article_title = article.find('h3').text
            article_data = {'id': article_id, 'title': article_title}
            section_articles.append(article_data)
        
        section_data['articles'] = section_articles
        toc_data.append(section_data)
    return toc_data


def create_toc(soup):
    ''' Create a Table of Contents (TOC) as a BeautifulSoup object '''
    toc_data = get_toc_data(soup)

    toc_html = '<ul id="toc">\n'

    for section in toc_data:
        section_link = f'  <li class="section-link"><a href="#{section['id']}">{section['title']}</a>\n'
        if len(section['articles']) > 0:
            section_link += '   <ul>\n'
            for article in section['articles']: 
                article_link = f'      <li class="article-link"><a href="#{article['id']}">{article['title']}</a></li>\n'
                section_link += article_link
            section_link += '    </ul>\n'
        section_link += '</li>\n'
        toc_html += section_link
    toc_html += '</ul>'
    return BeautifulSoup(toc_html, bs4_parser)


def div_wrap(soup, tag_name, class_name):
    ''' Wrap tables in div '''
    for tag in soup.find_all(tag_name):
        div = soup.new_tag("div")
        div['class'] = class_name
        tag.wrap(div)
    return soup