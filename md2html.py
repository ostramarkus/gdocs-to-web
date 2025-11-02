import re
import markdown
from slugify import slugify
from bs4 import BeautifulSoup

class Document:
    """Main class for md2html. Represents a document to be converted."""
    def __init__(self, md_path, template_path, title="Untitled", insert_tag="main"):
        self.bs4_parser = 'html.parser'
        self.md_path = md_path
        self.template_path = template_path
        self.title = title
        self.verbose = False

        self.content_soup = None 
        self.template_soup = None
        self.soup = None

        # Load and process content Markdown
        self.content_soup = self.load_markdown(md_path)
        self.content_soup = self.process_content(self.content_soup)

        # Load and process HTML template
        self.template_soup = self.html_file_to_soup(template_path)
        self.template_soup = self.insert_title(self.title, self.template_soup)

        # Create and insert table of contents
        toc = TOC(self)
        toc_title = self.template_soup.new_tag('h4')
        toc_title.string = self.title

        self.template_soup.aside.append(toc_title)
        self.template_soup.aside.append(toc.as_soup())

        # Merge content with template
        main_tag = self.template_soup.find(insert_tag)
        main_tag.append(self.content_soup)


    def process_content(self, soup):
        """Clean up and divide document"""
        soup = self.clean_up_headings(soup)

        # TODO : One method for both sections and articles: divide('h3', stop=['h2', 'h3'])
        soup = self.create_sections(soup)
        soup = self.create_articles(soup)

        soup = self.div_wrap(soup, 'table', class_name='table-container')
        soup = self.div_wrap(soup, 'pre', class_name='code-container')         
        return soup


    def insert_main_nav(self, nav_data, soup, id='#main-nav'):
        """Create and insert main navigation. Return as soup"""
        main_nav_soup = self.create_main_nav_soup(nav_data)
        main_nav_tag = soup.select(id)[0]
        main_nav_tag.append(main_nav_soup)
        return soup


    def create_main_nav_soup(self, nav_data):
        """Create HTML for main navigation. Return as soup."""
        nav_html= '<ul>'
        for link in nav_data:
            link_id, link_title, link_path = link
            nav_html += f'<li id="link-{link_id}"><a href="{link_path}">{link_title}</a></li>'
        nav_html += '</ul>'
        return BeautifulSoup(nav_html, self.bs4_parser)


    def load_markdown(self, md_path):
        """Loads a Markdown file and return soup."""
        try:
            with open(md_path, encoding='utf-8') as md_file:
                md_str = md_file.read()
                html_str = markdown.markdown(md_str, extensions=['fenced_code', 'tables'])
        except FileNotFoundError:
            print('File', md_path, 'not found.')
        return self.make_soup(html_str)


    def make_soup(self, html_str):
        """Convert an HTML string to a BeautifulSoup object."""
        return BeautifulSoup(html_str, self.bs4_parser)


    def clean_up_headings(self, soup):
        """Clean up headings by removing <strong> tags and empty headings."""
        for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            for strong in header.find_all("strong"):
                strong.unwrap()
            # Remove empty headings
            if not header.get_text(strip=True):
                header.decompose()    
        return soup


    def create_sections(self, soup):
        """Create <section> tags around each <h2> and its content"""
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


    def create_articles(self, soup):
        """Create <article> tags around each <h3> and its content"""
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


    def div_wrap(self, soup, tag_name, class_name='generic-div'):
        """Wrap tables in div"""
        for tag in soup.find_all(tag_name):
            div = soup.new_tag("div")
            div['class'] = class_name
            tag.wrap(div)
        return soup

    def html_file_to_soup(self, filename):
        """Read an HTML file and return a BeautifulSoup object"""
        with open(filename, encoding='utf-8') as html_file:
            html_str = html_file.read()
        return self.make_soup(html_str)

    def insert_title(self, title, soup):
        soup.find('h1').string = title
        soup.find('title').string = title


class TOC:
    """Class representiong a table of contents for a Document"""
    def __init__(self, document):
        self.document = document
        self.bs4_parser = document.bs4_parser

        self.structure = self.get_structure(document.content_soup)
        self.html = self.create_html(self.structure)

    def get_structure(self, soup):
        """Extract TOC structure from the soup object."""

        # Iterate all <section> save id-attribute and inner text of <h2>
        structure = []
        for section in soup.find_all('section'):
            section_id = section['id']
            section_title = section.find('h2').text
            section_data = {'id': section_id, 'title': section_title}

            # Iterate all <srticle> save id-attribute and inner text of <h3>            
            section_articles = []
            for article in section.find_all('article'):
                article_id = article['id']
                article_title = article.find('h3').text
                article_data = {'id': article_id, 'title': article_title}
                section_articles.append(article_data)
            
            section_data['articles'] = section_articles
            structure.append(section_data)
        return structure


    def create_html(self, toc_data):
        """Create a Table of Contents (TOC) as a BeautifulSoup object"""
        html_str = '<ul id="toc">\n'

        # Iterate sections
        for section in toc_data:
            section_id = section['id']
            section_title = section['title']
            section_link = f'  <li class="section-link"><a href="#{section_id}">{section_title}</a>\n'

            # If section has articles - iterate articles
            if len(section['articles']) > 0:
                section_link += '   <ul>\n'
                for article in section['articles']: 
                    article_id = article['id']
                    article_title = article['title']
                    article_link = f'      <li class="article-link"><a href="#{article_id}">{article_title}</a></li>\n'
                    section_link += article_link
                section_link += '    </ul>\n'
            section_link += '</li>\n'
            html_str += section_link
        html_str += '</ul>'
        return html_str

    def as_soup(self):
        return BeautifulSoup(self.toc_html, self.bs4_parser)

    def __str__(self):
        return self.html