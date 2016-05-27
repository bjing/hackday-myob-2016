import requests
import json

def load_api_key():
    try:
        key = file('api_key', 'rb').read().strip()
        return key
    except Exception as e:
        print('Failed loading Free Online OCR api key')
        print(e)
        exit(1)

def extract_text(response_text):
    """ Extract text from the response returned from Free OCR API
    """
    print response_text
    ocr_result = json.loads(response_text.encode('ascii', 'ignore'))
    return ocr_result['ParsedResults'][0]['ParsedText']

def dump_text_to_file(text):
    """ Dump OCR result to disk
    """
    text_file_name = 'ocr_result.txt'
    f = open(text_file_name, 'w')
    f.write(text)
    f.close()

def format_text(text):
    """ Replace new line characters with what Confluence can recognise
    """
    lines = text.splitlines()
    lines = map(lambda line: '<p>' + line + '</p>', lines)
    return '\n'.join(lines)

def ocr(image, file_type):
    """ main function that calls the Free OCR API and gets a response back
    """
    api_key = load_api_key()

    payload = {
        'apikey': api_key,
        'language':'eng',
        'isOverlayRequired':'false'
    }
    if file_type == 'url':
        payload[file_type] = image
        files = {}
    else:
        files={image: open(image, 'rb')}

    ocr_api_url = 'https://api.ocr.space/parse/image'
    print 'Making request to %s' % ocr_api_url

    response = requests.post(ocr_api_url, data = payload, files=files)
    if response.status_code == 200:
        text = extract_text(response.text)
        dump_text_to_file(format_text(text))
    else:
        print "OCR request failed. Error code %s" % response.status_code

"""
    The following is test code only, you can safely delete it
"""
if __name__ == '__main__':
    ocr('/Users/brianjing/Pictures/ocr-a-font-sample.png')
