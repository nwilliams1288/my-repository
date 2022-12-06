from flask import Flask, render_template

app = Flask(__name__)

# create a function named 'head' which sends number 'number1' and 'number2'
# variables to the 'index.html' , Use these variables into 

@app.route('/')
def head():
    return render_template('index.html', number1=10, number2=20)

@app.route('/number/<string:num1>')
def number(num1):
    return render_template('index.html', number1=num1, number2=20)   

@app.route('/sum')
def number():
    x = 15
    y = 20
    return render_template('body.html', valu1e=x, value2=y, sum=x+y)

if __name__ == '__main__':
    app.run(debug=True)