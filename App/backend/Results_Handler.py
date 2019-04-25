import json
import cv2

class Results_Handler():
    def __init__(self):
        self.userid = None
        self.age = None
        self.spiral_image = None
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
        
    def set_spiral_image(self, spiral_points):
        pass
    
    def set_spiral_prediction(self, spiral_prediction):
        pass
        
    def set_tremor_data(self, frequency):
        self.tremor_frequency = frequency
        
        print("Set Tremor Data: " + str(self.tremor_frequency))
        
        if self.tremor_frequency <= 10 and self.tremor_frequency >= 2:
            self.tremor_bool = True
        else:
            self.tremor_bool = False
        
    def set_questionnaire_data(self, questionnaire_results, questionnaire_score):
        self.questionnaire_results = questionnaire_results
        self.questionnaire_score = questionnaire_score
        
    def to_json(self):
        pass
    
    '''
    def reset(self):
        self.userid = None
        self.age = None
        self.spiral_image = None
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
    '''