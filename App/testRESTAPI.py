import json
import requests
import os

###POST
ENDPOINT = "http://www.spiria.org/api/userdatas/"
###UPDATE
#ENDPOINT = "http://www.spiria.org/api/userdatas/"+"2"+"/update/"
###DELETE
#ENDPOINT = "http://www.spiria.org/api/userdatas/"+"22"+"/delete/"
###DETAIL
#ENDPOINT = "http://www.spiria.org/api/userdatas/1"

image_path = '/Users/lingessrajoo/Desktop/test3.jpg'

def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if image_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'spiral': image
            }
            r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    return r

#post put delete
do_img(method='delete', data={'userid': 22,
                            'age': 30,
                            'spiral': '',
                            'spiral_test': 'True',
                            'tremor': 5,
                            'tremor_test': 'False',
                            'questionnaire': 90,
                            'response1': 'True',
                            'response2': 'False',
                            'response3': 'True',
                            'response4': 'False',
                            'response5': 'True',
                            'response6': 'Unsure',
                            'prediction': 'True',
                            'date': '2019-4-21 00:00:00'}, is_json=False, img_path=image_path)
