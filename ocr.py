import requests
import simplejson as json

def extract_text(response_text):
    ocr_result = json.loads(response_text.encode('ascii', 'ignore'))
    return ocr_result['ParsedResults'][0]['ParsedText']

def dump_text_to_file(text):
    f = open(text_file_name, 'w')
    f.write(text)
    f.close()

text_file_name = 'ocr_result.txt'
payload = {
    'url':'http://cdn4.explainthatstuff.com/ocr-a-font-sample.png',
    'apikey':'',
    'language':'eng',
    'isOverlayRequired':'false'
}
ocr_api_url = 'https://api.ocr.space/parse/image'

print 'Making request to %s' % ocr_api_url
response = requests.post(ocr_api_url, data = payload)
if response.status_code == 200:
    text = extract_text(response.text)
    dump_text_to_file(text)
else:
    print "OCR request failed. Error code %s" % response.status_code
