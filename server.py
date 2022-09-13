from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'any string you want'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form', methods=['POST'])
def handle_form():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['date'] = request.form['date']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    print(session)
    return render_template('result.html')



if __name__ == "__main__":
    app.run(debug=True)