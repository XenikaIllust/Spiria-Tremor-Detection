import uuid
import json
import cv2
import datetime

class Results_Handler():
    def __init__(self):
        self.userid = None
        self.age = 80
        self.tremor_frequency = None
        self.tremor_bool = None
        self.questionnaire_score = None
        self.spiral_prediction = None
        self.date = None
        self.response1 = None
        self.response2 = None
        self.response3 = None
        self.response4 = None
        self.response5 = None
        self.response6 = None
        self.overall_prediction = None
        
    def set_userid(self):
        self.userid = uuid.uuid4()
        
    def set_date(self):
        self.date = datetime.datetime.today().strftime('%Y-%m-%d')
    
    def set_spiral_prediction(self, spiral_predict_function):
        self.spiral_prediction = spiral_predict_function().payload[0].classification.score
        
    def set_tremor_data(self, frequency_function):
        self.tremor_frequency = frequency_function()
        
        print("Set Tremor Data: " + str(self.tremor_frequency))
        
        if self.tremor_frequency <= 10 and self.tremor_frequency >= 2:
            self.tremor_bool = True
        else:
            self.tremor_bool = False
            
    def get_tremor_data(self):
        return self.tremor_frequency
        
    def set_questionnaire_data(self, questionnaire_results, questionnaire_score):
        self.questionnaire_score = questionnaire_score
        self.response1 = questionnaire_results[0]
        self.response2 = questionnaire_results[1]
        self.response3 = questionnaire_results[2]
        self.response4 = questionnaire_results[3]
        self.response5 = questionnaire_results[4]
        self.response6 = questionnaire_results[5]
        
    def calculate_overall_prediction(self):
        self.overall_prediction = self.spiral_prediction * 0.2 + int(self.tremor_bool) * 0.5 + self.questionnaire_score * 0.3
        
    def get_results(self):
        return {
                'userid': self.userid,
                'age': self.age,
                'spiral': '',
                'spiral_test': self.spiral_prediction,
                'tremor': self.tremor_frequency,
                'tremor_test': self.tremor_bool,
                'questionnaire': self.questionnaire_score,
                'response1': self.response1,
                'response2': self.response2,
                'response3': self.response3,
                'response4': self.response4,
                'response5': self.response5,
                'response6': self.response6,
                'prediction': self.overall_prediction,
                'date': self.date
                }
    
    def reset(self):
        self.userid = None
        self.age = None
        self.tremor_frequency = None
        self.tremor_bool = None
        self.questionnaire_score = None
        self.spiral_prediction = None
        self.date = None
        self.response1 = None
        self.response2 = None
        self.response3 = None
        self.response4 = None
        self.response5 = None
        self.response6 = None
        self.overall_prediction = None