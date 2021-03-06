
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
Create file ```app/auth_token``` containing your Confluence auth_token
#### How to get your Confluence auth token
In Postman, 

1. create a new request, 
2. Under Authentication tab, select "Basic Auth" and type in your username and password,
3. Click on "Update Request" on the right to apply the change
4. Now head over to "Headers" tab and you can see your auth token under the key "Authorization"
5. Copy the whole token string into file ```app/auth_token```. Create it if it doesn't already exist.

![basic auth]
(https://github.com/bjing/hackday-myob-2016/blob/master/misc/screenshots/basic_auth.png)

![auth token](https://github.com/bjing/hackday-myob-2016/blob/master/misc/screenshots/auth_token.png)

#### Confluence API url
In file ```app/confluence.cfg```, fill in your confluence api url. 

For me, it's 
```
https://brianjing.atlassian.net/wiki/rest/api/content/
```
## OCR API access key
Copy and past the api key for accessing Free OCR Online API into file app/api_key.

# Run it
The entry point of the app is app.py
```
$ ./app.py --help
usage: app.py [-h] [--image-file IMAGE_FILE] [--image-url IMAGE_URL]

Extract text from Image and load it into Confluence

optional arguments:
  -h, --help            show this help message and exit
  --image-file IMAGE_FILE
                        Specify the image location
  --image-url IMAGE_URL
                        Specify the image url
```
For example, you can run it like this if you have the image on your computer:
```
./app.py --image-file "/Users/brianjing/Pictures/ocr-a-font-sample.png"
```
Or like this if you have an image from the web:
```
./app.py --image-url http://www.prepressure.com/images/fonts_sample_ocra_medium.png
```
