from quiz_question_model import Question
from quiz_data import question_data, logo
from quiz_brain import Brain


def quiz_game():
    print("This is a Quiz game of 12 questions")
    print(logo)
    ready = input("Are you ready, yes/no? ").lower()
    while True:
        if ready == 'no':
            break
        elif ready == 'yes':
            question_quiz = []
            for question in question_data:
                quiz = Question(question['text'], question['answer'])
                question_quiz.append(quiz)
            break
    quiz_question = Brain(question_quiz)
    quiz_question.ask_question()


quiz_game()