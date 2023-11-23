from flask import Flask, render_template, request

app = Flask("Game")

pos = "0:0"

@app.route("/")
def index():
    return render_template("index.html", position = pos)

@app.route("/move")
def moveChar():
    global pos

    move = request.args.get("move")
    currentPosition = request.args.get("currentPosition")
    pos = currentPosition
    return render_template("index.html", position = getNewPosition(move, currentPosition))

def getNewPosition(move, currentPosition):
    currentPositionList = currentPosition.split(":")
    currentPositionList = list(map(lambda num: int(num), currentPositionList))

    match move:
        case "R":
            currentPositionList[0] += 1
        case "Up":
            currentPositionList[1] -= 1
        case "L":
            currentPositionList[0] -= 1
        case "Down":
            currentPositionList[1] += 1
    
    if checkPosition(currentPositionList) == False:
        currentPositionList = list(map(lambda num: str(num), currentPositionList))
        return ":".join(currentPositionList)
    else:
        return pos

def checkPosition(currentPositionList):
    if currentPositionList[0] == -1 or currentPositionList[1] == -1 or currentPositionList[0] == 3 or currentPositionList[1] == 3:
        return True
    else:
        return False

app.run(host="0.0.0.0", port=8080)