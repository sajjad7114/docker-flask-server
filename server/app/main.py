from flask import Flask, request, jsonify
import os
import cv2
import base64

app = Flask(__name__)
path = './volume'


def face_detection(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)
    return img, len(faces)


def serialize(p, ext):
    img = cv2.imread(p)
    img, num = face_detection(img)
    _, buffer = cv2.imencode('.' + ext, img)
    ext_as_text = base64.b64encode(buffer)
    return ext_as_text, num


@app.route('/')
def send_image():
    directories = os.listdir(path)
    image = request.args.get("pic name")

    for file in directories:
        ext = file.split('.')[-1]
        name = ''.join(part + '.' for part in file.split('.')[:-1])[:-1]
        if image == name:
            ext_as_text, num = serialize(path + '/' + name + '.' + ext, ext)

            return jsonify({
                "message": str(num) + " faces found",
                "status": 200,
                "image": ext_as_text,
                "ext": ext
            })
    return jsonify({
                "status": 404,
                "message": "not found",
            })


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
