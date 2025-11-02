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
        self.content_soup = (SoupProcessor(self.content_soup)
            .wrap_elements('h2', 'section', ['h2'])
            .wrap_elements('h3', 'section', ['h2', 'h3'])
            .div_wrap('table', class_name='table-container')
            .div_wrap('pre', class_name='code-container')      
            .soup
        )

        template = Template(self, template_path)
        template.set_title(self.title)
        template.insert_content(self.content_soup, 'main')

        
        # Create and insert table of contents
        toc = TOC(self)
        toc_title = self.template_soup.new_tag('h4')
        toc_title.string = self.title

        self.template_soup.aside.append(toc_title)
        self.template_soup.aside.append(toc.as_soup())

        # Merge content with template
        self.soup = self.template_soup
        main_tag = self.soup.find(insert_tag)
        main_tag.append(self.content_soup)

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

    def remove_trailing_slashes(self, html_str):
        """Remove trailing slashes from void HTML tags"""
        void_tags = ["area", "base", "br", "col", "embed", "hr", "img",
                    "input", "link", "meta", "param", "source", "track", "wbr"]

        for tag in void_tags:
            html_str = re.sub(rf'<{tag}([^>]*)\s*/>', rf'<{tag}\1>', html_str)
        return html_str

    def as_html(self):
        """Decode soup to HTML. Remove trailing slashes and return as str."""
        html_output = self.soup.decode(formatter="html")
        html_output = self.remove_trailing_slashes(html_output)
        return html_output

    def save_html(self, save_path):
        html_str = self.as_html()
        with open(save_path, 'w', encoding='utf-8') as output_file:
            output_file.write(html_str)

    def __repr__(self):
        return self.as_html()

class SoupProcessor:
    """Processes Beautiful Soup objects"""
    def __init__(self, soup):
        self.soup = soup   

    def wrap_elements(self, header_tag, wrapper_tag, stop_tags):
        for header in list(self.soup.find_all(header_tag)):
            wrapper = self.soup.new_tag(wrapper_tag)
            wrapper['id'] = slugify(header.text)
            header.insert_before(wrapper)
            wrapper.append(header)
            next_node = wrapper.next_sibling
            while next_node and next_node.name not in stop_tags:
                sibling = next_node.next_sibling
                wrapper.append(next_node)
                next_node = sibling
        return self

    def clean_up_headings(self):
        """Clean up headings by removing <strong> tags and empty headings."""
        for header in self.soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            for strong in header.find_all("strong"):
                strong.unwrap()
            # Remove empty headings
            if not header.get_text(strip=True):
                header.decompose()    
        return self

    def div_wrap(self, tag_name, class_name='generic-div'):
        """Wrap elements in div"""
        for tag in self.soup.find_all(tag_name):
            div = self.soup.new_tag("div")
            div['class'] = class_name
            tag.wrap(div)
        return self


class Template:
    """A class representing a HTML template"""
    def __init__(self, document, template_path):
        self.document = document
        self.template_soup = self.load_template(template_path)

    def html_file_to_soup(self, path):
        """Read an HTML file and return a BeautifulSoup object"""
        with open(path, encoding='utf-8') as html_file:
            html_str = html_file.read()
        return self.make_soup(html_str)

    def set_title(self):
        self.template_soup.find('title').string = self.document.title

    def make_soup(self, html_str):
        """Convert an HTML string to a BeautifulSoup object."""
        return BeautifulSoup(html_str, self.document.bs4_parser)

    def insert_content(self, content_soup, tag_name):
        pass

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
        return BeautifulSoup(self.html, self.bs4_parser)

    def __str__(self):
        return self.html