#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}', 200

@app.route('/count/<int:number>')
def count_number(number):
    result = ""
    n = 0
    while n < number:
        result += f"{n}\n"
        n += 1
    return result, 200

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '-':
        return f'{num1 - num2}'
    elif operation == '+':
        return f"{num1 + num2}"
    elif operation == '*':
        return f"{num1 * num2}"
    elif operation == 'div':
        return f"{num1 / num2}"
    elif operation == '%':
        return f"{num1 % num2}"
    return {"error": "Invalid Operation"}
  


if __name__ == '__main__':
    app.run(port=5555, debug=True)