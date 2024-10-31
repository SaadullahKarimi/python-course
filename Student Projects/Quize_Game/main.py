# Importing the Question class from the question_model module
from question_model import Question  
# Importing the questions_data list from the data module
from data import questions_data  
# Importing the QuizBrain class from the quiz_brain module
from quiz_brain import QuizBrain  

# Initializing an empty list to hold Question objects
question_bank = []  
# Looping through each question in the questions_data list
for question in questions_data:  
    # Extracting the text of the question
    question_text = question['text']  
    # Extracting the answer for the question
    question_answer = question['answer']  
    # Creating a new Question object with the text and answer
    new_question = Question(question_text, question_answer)  
    # Appending the new Question object to the question_bank list
    question_bank.append(new_question)  

# Creating an instance of QuizBrain with the list of questions
quiz = QuizBrain(question_bank)  

# Loop to continue until there are no more questions
while quiz.still_has_question():  
    # Calling the next_question method to present the next question
    quiz.next_question()  

# Printing a completion message when the quiz is over
print("You have completed the quiz.")  
# Printing the final score of the quiz
print(f"Your final score was: {quiz.score}/{quiz.question_number}")  