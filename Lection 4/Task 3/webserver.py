from flask import Flask, render_template, request

app = Flask("Gallery")

photoList = ['static/images/autumn.jpg', '/static/images/camping.jpg', '/static/images/field.jpg', '/static/images/mountain.jpg', '/static/images/tree.jpg', '/static/images/tropicalBeach.jpg']
photoSrcPosition = 0

@app.route("/")
def index():
    return render_template("index.html", photo = photoList[photoSrcPosition])


@app.route("/change_photo")
def changePhoto():
    buttonMoveValue = request.args.get("change_photo")
    return render_template("index.html", photo = photoMoveTracker(buttonMoveValue))

def photoMoveTracker(buttonMoveValue):
    global photoSrcPosition

    match buttonMoveValue:
        case "next":
            photoSrcPosition += 1
        case "prev":
            photoSrcPosition -= 1
    
    photoSrcPosition = checkPosition(photoSrcPosition)
    print(photoSrcPosition)
    return photoList[photoSrcPosition]

def checkPosition(photoSrcPosition):
    if photoSrcPosition == -1:
        photoSrcPosition += 1
        return photoSrcPosition
    elif photoSrcPosition == 6:
        photoSrcPosition -= 1
        return photoSrcPosition
    else:
        return photoSrcPosition

app.run(host = "0.0.0.0", port = 8080)