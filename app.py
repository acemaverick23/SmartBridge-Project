from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
import joblib
model=pickle.load(open("risk.pkl",'rb'))
sc=pickle.load(open("scale.pkl",'rb'))
ct=joblib.load('column')

@app.route('/')
def hello_world():
        return render_template("index.html")
@app.route('/guest', methods=["POST"])
def Guest():
    Age= int(request.form["Age"])
    Sex= request.form["Sex"]
    Job= int(request.form["Job"])
    Housing= request.form["Housing"]
    Saving= request.form["Saving"]
    Checking= request.form["Checking"]
    Credit= int(request.form["Credit"])
    Duration= int(request.form["Duration"])
    Purpose= request.form["Purpose"]
    data=[[Age,Sex,Job,Housing,Saving,Checking,Credit,Duration,Purpose]]
    pred=model.predict(sc.transform(ct.transform(data)))
    xx=pred[0];
    if xx==0:
        return render_template('index.html',y="Loan not sanctioned")
    else:
        return render_template('index.html', y="Loan sanctioned")


@app.route('/user')
def User():
    return "user"

app.run(debug=True)