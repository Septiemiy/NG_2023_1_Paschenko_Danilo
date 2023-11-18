from flask import Flask, render_template, request
from math import sqrt

app = Flask("Calculator")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    exercise = request.args.get("inputArea")
    return render_template("index.html", exerciseResult = getResult(getExerciseElements(exercise)))

def getExerciseElements(exercise):
    exerciseElements = exercise.split(" ")
    return exerciseElements

def addition(numberOne, numberTwo):
    result = int(numberOne) + int(numberTwo)
    return result

def subtraction(numberOne, numberTwo):
    result = int(numberOne) - int(numberTwo)
    return result

def multiplication(numberOne, numberTwo):
    result = int(numberOne) * int(numberTwo)
    return result

def division(numberOne, numberTwo):
    try:
        result = round(int(numberOne) / int(numberTwo), 3)
    except ZeroDivisionError as exc:
        return "Division by zero"
    
    return result

def power(numberOne, numberTwo):
    result = int(numberOne) ** int(numberTwo)
    return result

def squareRoot(number):
    try:
        result = round(sqrt(int(number)), 3)
    except ValueError as exc:
        return "A negative number"
    
    return result

def getResult(exerciseElements):
    match exerciseElements[1]:
        case "+":
            return addition(exerciseElements[0], exerciseElements[2])
        case "-":
            return subtraction(exerciseElements[0], exerciseElements[2])
        case "*":
            return multiplication(exerciseElements[0], exerciseElements[2])
        case "/":
            return division(exerciseElements[0], exerciseElements[2])
        case "^":
            return power(exerciseElements[0], exerciseElements[2])
    
    if exerciseElements[0] == "√":
        return squareRoot(exerciseElements[1])

app.run(host="0.0.0.0", port=8082)