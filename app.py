from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/number_guesser', methods=['GET', 'POST'])
def number_guesser():
    target = 42
    attempts = 0
    result = ""

    if request.method == 'POST':
        guess = int(request.form['guess'])
        target = int(request.form.get('target', 42))
        attempts = int(request.form.get('attempts', 0)) + 1

        if guess < target:
            result = "Too low. Try again."
        elif guess > target:
            result = "Too high. Try again."
        else:
            result = f"🎉 Correct! You guessed it in {attempts} tries."

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

todos = []

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

@app.route('/countdown_timer')
def countdown_timer():
    return render_template('countdown_timer.html')

@app.route('/currency_converter', methods=['GET', 'POST'])
def currency_converter():
    result = None
    amount = 0
    from_currency = to_currency = ''
    
    rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'JPY': 146.5,
        'NGN': 1600.0,
    }

    currencies = list(rates.keys())

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']

            converted = amount * (rates[to_currency] / rates[from_currency])
            result = f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('currency_converter.html', result=result, currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)
