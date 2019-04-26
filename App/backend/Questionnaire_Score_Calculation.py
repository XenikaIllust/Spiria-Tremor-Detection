class Questionnaire_Calculator():
    def __init__(self):
        self.score = 0
        self.weights = [[1,0.5,0], [1,0.5,0], [1,0.5,0], [1,0], [1,0], [1,0]]
        self.responses = []
        
    def set_responses(self, button_groups):
        for i, group in enumerate(button_groups):
            self.responses.append(group.button(group.checkedId()).text())

    def calculate_score(self, button_groups):
        print("Responses: ")
        for i, group in enumerate(button_groups):
            self.score += self.weights[i][group.checkedId()]
            
            print("Q" + str(i+1) + ": " + group.button(group.checkedId()).text())
                
        print("Score: " + str(self.score))
        
    def get_score(self):
        return self.score
    
    def get_responses(self):
        return self.responses
    
    def reset(self):
        self.score = 0
        self.responses = []