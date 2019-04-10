class Questionnaire_Calculator():
    def __init__(self):
        self.score = 0
        self.weights = [[1,0.5,0], [1,0.5,0], [1,0.5,0], [1,0], [1,0], [1,0]]

    def calculate_score(self, button_groups):
        print("Responses: ")
        for i, group in enumerate(button_groups):
            self.score += self.weights[i][group.checkedId()]
            
            print("Q" + str(i+1) + ": " + group.button(group.checkedId()).text())
                
        print("Score: " + str(self.score))
                
if __name__ == "__main__":
    pass  