from distutils.command.config import config 
from flask import Flask,render_template,redirect,request,jsonify,url_for
from utils import MedicalInsurance
import config1
app = Flask (__name__)

@app.route("/")
def hello_flask():
    return render_template("index.html")

@app.route("/price_pred",methods=['POST','GET'])
def get_prediction():
    if request.method== 'GET':
        age= eval(request.args.get('age'))
        gender= request.args.get('gender')
        bmi=eval(request.args.get('bmi'))
        children= eval(request.args.get('children'))
        smoker=request.args.get('smoker')
        region=request.args.get('region')
        med_ins= MedicalInsurance(age,gender,bmi,children,smoker,region)
        charges= med_ins.get_pred_price()
        return render_template("index.html", prediction = charges)

    
    else :
        age= eval(request.form.get('age'))
        gender= request.form.get('gender')
        bmi=eval(request.form.get('bmi'))
        children= eval(request.form.get('children'))
        smoker=request.form.get('smoker')
        region=request.form.get('region')

        med_ins= MedicalInsurance(age,gender,bmi,children,smoker,region)
        charges= med_ins.get_pred_price()
        return render_template("index.html", prediction = charges)


if __name__=="__main__":
    app.run(host="0.0.0.0",port= config1.PORT_NUMBER,debug=True)        
