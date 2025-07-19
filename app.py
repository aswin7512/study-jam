from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'StUdy_JaM01_KeY_UsElESs25'

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

@app.route('/', methods = ['GET', 'POST'])

def quiz():
    if 'index' not in session:
        session['index'] = 0
        session['score'] = 0
        session['questions'] = random.sample(question_pool, 5)

    index = session['index']
    questions = session['questions']

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()
        correct_answer = questions[index]['answer']
        if user_answer == correct_answer:
            message = "Correct ! You got it !!"
            session['score'] += 1
        else:
            message = f"Wrong ! The correct answer was: {correct_answer}"
        
        session['index'] += 1
        index = session['index']

        if index >= 5:
            final_score = session['score']
            session.clear()
            return f"<h2>Quiz Finished !</h2><br><p>Your Score: {final_score}/{len(questions)}</p>"
        
        return render_template("question.html", question=questions[index]['question'], message=message)
    return render_template("question.html", question = questions[index]['question'])


if __name__ == '__main__':
    app.run(debug=True)
