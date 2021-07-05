from flask import Flask,url_for,redirect,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score =0
    if request.method =='POST':
        sci = float(request.form['science'])
        math = float(request.form['maths'])
        his = float(request.form['history'])
        total_score = sci + math + his 
    return redirect(url_for('result',score =total_score))
@app.route('/result/<float:score>')
def result(score):
    if(score/3<35):
        res='Fail'
    else:
        res='Pass'
    return render_template('result.html',result=res,score=score/3)
   

if __name__=="__main__":
    app.run(debug=True)
