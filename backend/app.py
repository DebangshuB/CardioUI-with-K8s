from flask import Flask, redirect, url_for, session
from flask import render_template
from forms import Strokedata
from parse import parse
from requests import post
from json import loads
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '18159e1647ba2975'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Strokedata()

    if form.validate_on_submit():
        user_data = parse(form)
        session['data'] = user_data
        return redirect(url_for('result'))

    return render_template('home.html', form=form)


@app.route('/results')
def result():
    endpoint = os.environ.get('ML_SERVER_ENDPOINT', 'localhost')
    prediction = post(f"http://{endpoint}:8001", json={"input": session['data']}).text

    prediction = int(loads(prediction)["prediction"])
    return render_template('result.html', res=prediction, title='Results')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title="Error !"), 404


if __name__ == '__main__':
    app.run()