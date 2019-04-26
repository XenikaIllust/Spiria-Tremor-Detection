from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
import json
import requests
import os

G_PROJECT_ID = "bold-ethos-235619"
G_MODEL_ID = "ICN3286021728029437002"

SPIRIA_SERVER_ENDPOINT = "http://www.spiria.org/api/userdatas/"

class Request_Handler():
    def __init__(self):
        # subprocess.call(['export', 'GOOGLE_APPLICATION_CREDENTIALS="/home/pi/Desktop/ML-cc7141df989b.json"'], shell=True)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/pi/Desktop/ML-cc7141df989b.json'
        
        self.prediction_client = automl_v1beta1.PredictionServiceClient()
        self.project_id = G_PROJECT_ID
        self.model_id = G_MODEL_ID
        
        self.spiria_server_endpoint = SPIRIA_SERVER_ENDPOINT
    
    def get_google_prediction(self, image_path):
        with open(image_path, "rb") as image:
            image_bytes = image.read()
            name = 'projects/{}/locations/us-central1/models/{}'.format(self.project_id, self.model_id)
            payload = {'image': {'image_bytes': image_bytes }}
            params = {}
            request = self.prediction_client.predict(name, payload, params)
        print(request)
        return request
    
    def post_to_webserver(self, data_func, image_path):
        data = data_func()
        
        headers = {}
        with open(image_path, 'rb') as image:
            file_data = {
                'spiral': image
            }
            r = requests.request('post', SPIRIA_SERVER_ENDPOINT, data=data, headers=headers, files=file_data)
        print(r)
        return r
    
if __name__ == "__main__":
    request_handler = Request_Handler()
    res = request_handler.get_google_prediction("../spiral.jpg")
    print(type(res))
    print(res.payload[0].classification.score)
    print(request_handler.post_to_webserver(data={
                            'userid': 22,
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
                            'date': '2019-4-21 00:00:00'}, image_path="../spiral.jpg"))
