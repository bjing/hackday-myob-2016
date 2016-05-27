import requests
import json

class ConfluenceAPI:
    def __init__(self):
        self.__load_base_url()
        self.__load_auth_token()

    def __load_base_url(self):
        try:
            self.base_url = file('confluence.cfg', 'rb').read().strip()
        except Exception as e:
            print('Cannot find confluence base url in file "confluence.cfg"')
            print(e)
            exit(1)

    def __load_auth_token(self):
        try:
            print 'Loading Confluence auth token from disk...'
            self.auth_token = file('auth_token', 'rb').read().strip()
            print 'Auth token successfully loaded'
        except Exception as e:
            print('Cannot load auto token from file "auth_token"')
            print(e)
            exit(1)

    def create_page(self, page_content):
        space_key = raw_input('Space key: ')
        page_title = raw_input('Page title: ')

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

        response = requests.post(self.base_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print 'Page titled "%s" successfully created' % page_title
        else:
            print 'Oops error encountered!'
            print 'Status code: %s' % response.status_code
            print 'Response text: %s' % response.text



"""
    This is test code only. Feel free to remove it!
"""
if __name__ == '__main__':
    api = ConfluenceAPI()
    api.create_page('This is some test content')
