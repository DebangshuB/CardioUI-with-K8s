from flask import Flask, request
from predict import predict

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    result = predict(request.json["input"])[0]
    return {
        "prediction": int(result)
    }


if __name__ == '__main__':
    app.run()