import re
import markdown
from slugify import slugify
from bs4 import BeautifulSoup

class Document:
    """Main class for md2html. Represents a document to be converted."""
    def __init__(self, md_path, template_path, title="Untitled"):
        self.bs4_parser = 'html.parser'
        self.md_path = md_path
        self.template_path = template_path
        self.verbose = False
        self.markdown = None
        self._content_soup = None 
        self._template_soup = None
        
        self._content_soup = self.load_markdown(md_path)

    def load_markdown(self, md_path):
        """Loads a Markdown file"""
        try:
            with open(md_path, encoding='utf-8') as md_file:
                md_str = md_file.read()
                html_str = markdown.markdown(md_str, extensions=['fenced_code', 'tables'])
        except FileNotFoundError:
            print('File', md_path, 'not found.')
        return self._make_soup(html_str)
    
    def make_soup(self, html_str):
        """Convert an HTML string to a BeautifulSoup object"""
        return BeautifulSoup(html_str, self.bs4_parser)