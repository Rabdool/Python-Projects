from flask import Flask, render_template, request, redirect, url_for, session
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'

todos = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/number_guesser', methods=['GET', 'POST'])
def number_guesser():
    result = ""

    if request.method == 'POST':
        if 'reset' in request.form:
            target = random.randint(1, 100)
            attempts = 0
            result = "Game has been reset. Try guessing the new number!"
        else:
            guess = int(request.form['guess'])
            target = int(request.form['target'])
            attempts = int(request.form['attempts']) + 1

            if guess < target:
                result = "Too low. Try again."
            elif guess > target:
                result = "Too high. Try again."
            else:
                result = f"Correct! You guessed it in {attempts} tries."
    else:
        target = random.randint(1, 100)
        attempts = 0

    return render_template('number_guesser.html', result=result, target=target, attempts=attempts)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('calculator.html', result=result)

@app.route('/stopwatch')
def stopwatch():
    return render_template('stopwatch.html')

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todos.append(task)
    return render_template('todo.html', tasks=todos)

@app.route('/delete_task/<int:index>', methods=['POST'])
def delete_task(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('todo'))

@app.route('/password_generator', methods=['GET', 'POST'])
def password_generator():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
    return render_template('password_generator.html', password=password)

@app.route('/dice_roller', methods=['GET', 'POST'])
def dice_roller():
    result = None
    if request.method == 'POST':
        result = random.randint(1, 6)
    return render_template('dice_roller.html', result=result)

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Leo Tolstoy", "Mark Twain", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Iron", "Hydrogen"],
        "answer": "Oxygen"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Arctic", "Indian", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1942", "1945", "1948", "1950"],
        "answer": "1945"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["90°C", "95°C", "100°C", "105°C"],
        "answer": "100°C"
    }
]

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        questions = random.sample(quiz_questions, 5)
        session['quiz_questions'] = questions
        return render_template('quiz.html', questions=questions)

    elif request.method == 'POST':
        questions = session.get('quiz_questions', [])
        results = []
        score = 0

        for i, q in enumerate(questions):
            selected = request.form.get(f'q{i}')
            correct = q['answer']
            is_correct = selected == correct
            if is_correct:
                score += 1

            results.append({
                'question': q['question'],
                'options': q['options'],
                'correct': correct,
                'selected': selected,
                'is_correct': is_correct
            })

        return render_template('quiz_result.html', score=score, total=len(questions), results=results)

if __name__ == '__main__':
    app.run(debug=True)
