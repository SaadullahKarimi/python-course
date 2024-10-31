# Defining the Question class to represent a single quiz question
class Question:  
    # Constructor method to initialize the question's text and answer
    def __init__(self, q_text, q_answer):  
        self.text = q_text  # Setting the question text
        self.answer = q_answer  # Setting the correct answer