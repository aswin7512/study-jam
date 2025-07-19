from flask import Flask, render_template, request, redirect, url_for, session
from app_logic import get_random_questions, check_answer

app = Flask(__name__)
app.secret_key = 'StUdy_JaM01_KeY_UsElESs25'


@app.route('/', methods = ['GET', 'POST'])

def quiz():
    if 'index' not in session:
        session['index'] = 0
        session['score'] = 0
        session['questions'] = get_random_questions(count=5)

    index = session['index']
    questions = session['questions']

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()
        correct_answer = questions[index]['answer']
        if check_answer(user_answer=user_answer, correct_answer=correct_answer):
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
