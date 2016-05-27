__author__ = 'Brian Jing'

from PythonConfluenceAPI import ConfluenceAPI
import getpass

class ConfluenceAPIHelper:
    username = 'admin'
    password = ''
    base_url = 'https://brianjing.atlassian.net/wiki'

    def __init__(self):
        username = self.username
        password = self.password
        if not self.username:
            username = raw_input('Confluence user name: ')
        if not self.password:
            password = getpass.getpass('Confluence password (hidden): ')
        self.api = ConfluenceAPI(username, password, self.base_url)

    # api.create_new_space({
    #     'key': 'LOL',
    #     'name': 'My testing space',
    #     'description': {
    #         'plain': {'value': 'This is my new testing space', 'representation': 'plain'}
    #     }
    # })

    #Generate a page for our space
    def create_page(self, content):
        print content
        space_key = raw_input('Space key: ')
        page_title = raw_input('Page title: ')
        self.api.create_new_content({
            'type': 'page',
            'title': page_title,
            'space': {'key': space_key},
            'body': {
                'storage': {'value': content,
                            'representation': 'storage'}
            }
        })

    def test_create_page(self):
        #Generate a page for our space
        self.api.create_new_content({
            'type': 'page',
            'title': 'My landing page for TESTSPACE!',
            'space': {'key': 'HAC'},
            'body': {
                'storage': {'value': '<h1>Welcome to the landing page!</h1><p>Lorem Ipsum</p>',
                            'representation': 'storage'
                            }
            }
        })

if __name__ == '__main__':
    api = ConfluenceAPIHelper()
    api.test_create_page()
