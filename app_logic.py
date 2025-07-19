import random

question_pool = [
    {'question': "What is the captial of France ?", 'answer': "paris"},
    {'question': "Which Planet is knows as the Red Planet ?", 'answer': "mars"},
    {'question': "What is the largest planet in our solar system ?", 'answer': "jupiter"},
    {"question": "What color is the sky on a clear day?", "answer": "blue"},
    {"question": "How many continents are there on Earth?", "answer": "7"},
    {"question": "Which ocean is the largest?", "answer": "pacific"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
    {"question": "What is the largest mammal in the world?", "answer": "blue whale"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "japan"},
    {"question": "Which gas do plants absorb from the atmosphere?", "answer": "carbon dioxide"}
]


def get_random_questions(count = 5):
    return random.sample(question_pool, count)

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()