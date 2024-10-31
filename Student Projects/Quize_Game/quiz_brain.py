# Defining the QuizBrain class to manage the quiz logic
class QuizBrain:  
    
    # Constructor method to initialize the quiz with a list of questions
    def __init__(self, q_list):  
        self.question_number = 0  # Keeping track of the current question number
        self.question_list = q_list  # Storing the list of questions
        self.score = 0  # Initializing the score to zero
    
    # Method to display the next question
    def next_question(self):  
        current_question = self.question_list[self.question_number]  # Getting the current question
        self.question_number += 1  # Incrementing the question number
        # Asking the user for their answer and displaying the question text
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  
        # Checking if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)  

    # Method to check if there are still questions left
    def still_has_question(self):  
        return self.question_number < len(self.question_list)  # Returns True if there are more questions
    
    # Method to check the user's answer against the correct answer
    def check_answer(self, user_answer, correct_answer):  
        # Comparing the user's answer with the correct answer (case insensitive)
        if user_answer.lower() == correct_answer.lower():  
            print("You got it right!")  # Informing the user of a correct answer
            self.score += 1  # Incrementing the score for a correct answer
        else:
            print("That's Wrong!!")  # Informing the user of an incorrect answer
        print(f"The correct answer was: {correct_answer}")  # Displaying the correct answer
        print(f"Your current score is: {self.score}/{self.question_number}")  # Displaying the current score
        print("\n")  # Adding a newline for better readability