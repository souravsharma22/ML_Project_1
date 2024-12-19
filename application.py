from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler

# importing the model
ridge_model  = pickle.load(open('Models/Ridgemodel.pkl','rb'))
Stdscaler = pickle.load(open('Models/Scaler.pkl','rb'))



application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route('/predictdata',methods=['GET','POST'])
def predict_data():
    if request.method=='POST':
        Temperature = float(request.form.get('Temprature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        region = float(request.form.get('region'))

        new_data_scaled=Stdscaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,region]])
        result_pred =ridge_model.predict(new_data_scaled)

        return render_template('home.html', result=result_pred[0])
    else:
        return render_template('home.html')


if __name__=='__main__':
    app.run(host="0.0.0.0")