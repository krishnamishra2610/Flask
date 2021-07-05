from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return "<html><h1>Hello World</h1></html>"
@app.route('/result/<int:marks>')
def results(marks):
    result =""
    if(marks <35):
        result = "fail"
    else:
        result='passs'
    return redirect(url_for(result,score =marks))
@app.route('/passs/<int:score>')
def passs(score):
    return "pass with " + str(score)
@app.route('/fail/<int:score>')
def fail(score):
    return "fail with " + str(score)

if __name__ == "__main__":
    app.run(debug=True)
