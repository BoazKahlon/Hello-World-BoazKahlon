from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return " in home"

@app.route('/main')
def main():
    logged_in = False
    if logged_in:
        #  redirect is mooving to other route
        return redirect('/ContactList')
    else:
        #  url_for is mooving to  function
        return redirect(url_for('vip'))


@app.route('/ContactList')
def contacts():
    return "used the redirect func"


@app.route('/vip')
def vip():
    return " used the url_for func"

# @app.route('/name', get,post,)

if __name__ == '__main__':
    app.run(debug=True)