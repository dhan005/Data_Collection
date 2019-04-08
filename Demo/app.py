from flask import Flask, render_template, request 
from flask.ext.sqlalchemy import SQLalchemy 
from send_email import send_email 
from sqlalchemy.sql func 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost'
db = SQLalchemy(app)

class Data(db.model): 
    __tablename__="data"
    id=db.columns(db.Integer, primary_key=True)
    email_=db.columns(db.String(120), unique-True)
    height_=db.columns(db.Integer)

    def __init__(self, email_, height_): 
        self.email_=email_ 
        self.height_=height_


@app.route("/")
    def index(): 
        return render_template("index.html")

@app.route("/success", methods=['POST'])
    def success(): 
        if request.method=='POST': 
            email=request.form['email_name']
            height=request.form['height_name']
            send_email(email, height)
            if db.session.query(Data).filter(Data.email_==email).count() == 0: 
                data=Data(email,height)
                db.session.add(data)
                db.session.commit()
                average_height=db.session.query(func.avg(Data.height_)).scalar() 
                print(average_height)
                return render_template("success.html")
        return render_template('index.html', text="seems like we've received that email already")



if __name__ = "__main__": 
    app.debug=True 
