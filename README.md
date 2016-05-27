
# Setup
## Python
Run the following commands in a terminal.

If you don't already have pip, install it
```
sudo easy_install pip
```
Make sure you have the latest tools
```
sudo pip install --upgrade pip
sudo pip install --upgrade setuptools
```
Now install the library dependency "requests".
```
sudo pip install requests
```
## Confluence
#### Auth token
Under app/, create file "auth_token" containing your Confluence auth_token
#### How to get your Confluence auth token
In postman, 

1. create a new request, 
2. Under Authentication tab, select "Basic Auth" and type in your username and password,
3. Click on "Update Request" on the right to apply the change
4. Now head over to "Headers" tab and you can see your auth token under the key "Authorization"

![basic auth]
(https://github.com/bjing/hackday-myob-2016/blob/master/misc/screenshots/basic_auth.png)

![auth token](https://github.com/bjing/hackday-myob-2016/blob/master/misc/screenshots/auth_token.png)

#### Confluence API url
In app/confluence.cfg, fill in your confluence api url. 

For me, it's 
```
https://brianjing.atlassian.net/wiki/rest/api/content/
```
## OCR API access key
Under app/, create file "api_key" containing the api key for accessing Free OCR Online API

# Run it
The entry point of the app is app.py
```
$ ./app.py --help
usage: app.py [-h] [--image-file IMAGE_FILE]

Extract text from Image and load it into Confluence

optional arguments:
  -h, --help            show this help message and exit
  --image-file IMAGE_FILE
                        Specify the image location
```
For example, you can run it like this:
```
./app.py --image-file "/Users/brianjing/Pictures/ocr-a-font-sample.png"
```
