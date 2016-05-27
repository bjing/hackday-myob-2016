import requests
import json

class ConfluenceAPI:
    def __init__(self):
        self.__load_base_url()
        self.__load_auth_token()

    def __load_base_url(self):
        """ Load confluence api url from config file
        """
        try:
            self.base_url = file('confluence.cfg', 'rb').read().strip()
        except Exception as e:
            print 'Cannot find confluence base url in file "confluence.cfg"'
            print e
            exit(1)

    def __load_auth_token(self):
        """ Load confluence auth token from config file
        """
        try:
            print '\nLoading Confluence auth token...'
            self.auth_token = file('auth_token', 'rb').read().strip()
            print 'Auth token successfully loaded'
        except Exception as e:
            print 'Cannot load auth token from file "auth_token"'
            print e
            exit(1)

    def create_page(self, page_content):
        """ Create a page given page_content
            Space and page title are given by user at run time
        """
        space_key = raw_input('Confluence space key: ')
        page_title = raw_input('Confluence page title: ')

        payload = {
            "type": "page",
            "space": {
                "key": space_key
            },
            "title": page_title,
            "body": {
                "storage":{
                    "value": page_content,
                    "representation": "storage"
                }
            }
        }

        headers = {"Authorization": "%s" % self.auth_token,
                  "Content-Type": "application/json"}

        print 'Please wait while a new Confluence page is being created...'
        response = requests.post(self.base_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print 'Page titled "%s" successfully created!' % page_title
        else:
            print 'Oops error encountered!'
            print 'Status code: %s' % response.status_code
            print 'Response text: %s' % response.text
        print ""


"""
    This is test code only. Feel free to remove it!
"""
if __name__ == '__main__':
    api = ConfluenceAPI()
    api.create_page('This is some test content')
