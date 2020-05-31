from flask import Flask, render_template, redirect, request, jsonify
import json
import numpy as np 
import pandas as pd 

# SQL
import mysql.connector

# Model ML
import joblib

# Database
dblogin = mysql.connector.connect(
host = 'localhost',
port = 3306,
user = 'root',
passwd = '0101steven',
database = 'loginfp')
db = dblogin.cursor()

sukses = 'tidaksukses'

# Function

def income(x) :
    if x == 'working' :
        return [0,0,0,0,1]
    elif x == 'commercial' :
        return [1,0,0,0,0]
    elif x == 'pensioner' :
        return [0,1,0,0,0]
    elif x == 'state' :
        return [0,0,1,0,0]
    else :
        return [0,0,0,1,0]

def education(x) :
    if x == 'higher' :
        return [0,1,0,0,0]
    elif x == 'secondary' :
        return [0,0,0,0,1]
    elif x == 'incomplete' :
        return [0,0,1,0,0]
    elif x == 'lower' :
        return [0,0,0,1,0]
    else :
        return [1,0,0,0,0]

def martial(x) :
    if x == 'm' :
        return [0,1,0,0,0]
    elif x == 'w' :
        return [0,0,0,0,1]
    elif x == 's' :
        return [0,0,1,0,0]
    elif x == 'nm' :
        return [0,0,0,1,0]
    else :
        return [1,0,0,0,0]

def housing(x) :
    if x == 'ra' :
        return [0,0,0,0,1,0]
    elif x == 'h' :
        return [0,1,0,0,0,0]
    elif x == 'ma' :
        return [0,0,1,0,0,0]
    elif x == 'p' :
        return [0,0,0,0,0,1]
    elif x == 'ca' :
        return [1,0,0,0,0,0]
    else :
        return [0,0,0,1,0,0]

def occupation(x) :
    if x == 'acc' :
        return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'clean' :
        return [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'cooking' :
        return [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'core' :
        return [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'driver' :
        return [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'hr' :
        return [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'tech' :
        return [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'it' :
        return [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    elif x == 'labor' :
        return [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif x == 'ls' :
        return [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif x == 'man' :
        return [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif x == 'med' :
        return [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif x == 'other' :
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    elif x == 'private' :
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    elif x == 'ra' :
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    elif x == 'sales' :
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    elif x == 'secre' :
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    elif x == 'security' :
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    else :
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
            


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('cclogin.html')

@app.route('/sign-up', methods=['GET'])
def signup():
    return render_template('ccsignup.html')

@app.route('/success', methods=['GET','POST'])
def success():
    if request.method == "GET" :
        return redirect('/')
    else :
        datasignup = request.form
        username = datasignup['username']
        password = datasignup['pass']
        email = datasignup['email']
        gender = datasignup['gender']
        age = datasignup['usia']

        queryread = 'select * from usercc'
        dfusercc = pd.read_sql(queryread,dblogin)

        if username not in list(dfusercc['username']) and email not in list(dfusercc['email']):
            querysignup = 'insert into usercc (username,password,email,gender,age) values (%s,%s,%s,%s,%s)'
            insertdata = (username,password,email,gender,age)
            db.execute(querysignup,insertdata)
            dblogin.commit()
            return render_template('ccsukses.html')
        else :
            return render_template('ccerror.html', error = 'Username/Email Already Registered', page='sign-up')

        

@app.route('/home', methods=['GET','POST'])
def home():
    global sukses
    if request.method == "GET" and sukses == 'sukses' :
        return render_template('cchome.html') 
    elif request.method == "GET" and sukses == 'tidaksukses':
        return redirect('/')
    else : 
        datalogin = request.form
        loginuser = datalogin['username']
        loginpass = datalogin['pass']

        queryread = 'select * from usercc'
        dfusercc = pd.read_sql(queryread,dblogin)

        if loginuser in list(dfusercc['username']) or loginuser in list(dfusercc['email']):
                if loginpass in list(dfusercc['password']):
                    sukses = 'sukses'
                    return render_template('cchome.html')
                else :
                    return render_template('ccerror.html', error = 'Incorrect Password', page='')    
        else :
            return render_template('ccerror.html', error = 'Incorrect Username/Email', page='')   

@app.route('/credit-card-approval')
def ccapproval():
    global sukses
    if request.method == "GET" and sukses == 'sukses' :
        return render_template('ccapproval.html')
    elif request.method == "GET" and sukses == 'tidaksukses':
        return redirect('/')
    

@app.route('/credit-card-approval-result', methods=['GET','POST'])
def ccaresult() :
    global sukses
    if request.method == "GET" and sukses == 'sukses' :
        return render_template('cchome.html') 
    elif request.method == "GET" and sukses == 'tidaksukses':
        return redirect('/')
    else :
        dataccform = request.form

        # Processing Form => Data
        dfx = pd.DataFrame([{
            'Gender' : int(dataccform['gender']),
            'Car' :  int(dataccform['car']),
            'Property' :  int(dataccform['property']),
            'NoChild' : int(dataccform['child']),
            'Income' : int(dataccform['income']),
            'Age' : int(dataccform['usia']),
            'LOE' : int(dataccform['loe']),
            'Workphone' : int(dataccform['workphone']),
            'Phone' : int(dataccform['phone']),
            'Email' : int(dataccform['email']),
            'FamSize' : int(dataccform['famsize'])
        }])


        # Multi Class 
        # Income
        IC = ['IncomeType_Commercial associate', 'IncomeType_Pensioner', 'IncomeType_State servant', 'IncomeType_Student', 'IncomeType_Working']
        IV = income(str(dataccform['incometype']))
        dfID = pd.DataFrame([dict(zip(IC,IV))])
        dfx = pd.concat([dfx,dfID], axis='columns')

        # Education

        EC = ['Education_Academic degree', 'Education_Higher education', 'Education_Incomplete higher', 'Education_Lower secondary', 'Education_Secondary / secondary special']
        EV = education(str(dataccform['education']))
        dfED = pd.DataFrame([dict(zip(EC,EV))])
        dfx = pd.concat([dfx,dfED], axis='columns')

        # Martial Stat

        MC = ['MartialStat_Civil marriage', 'MartialStat_Married', 'MartialStat_Separated', 'MartialStat_Single / not married', 'MartialStat_Widow']
        MV = martial(str(dataccform['martial']))
        dfMD = pd.DataFrame([dict(zip(MC,MV))])
        dfx = pd.concat([dfx,dfMD], axis='columns')

        # Housing Type
        HC = ['HousingType_Co-op apartment', 'HousingType_House / apartment', 'HousingType_Municipal apartment', 'HousingType_Office apartment', 'HousingType_Rented apartment', 'HousingType_With parents']
        HV = housing (str(dataccform['housing']))
        dfHD = pd.DataFrame([dict(zip(HC,HV))])
        dfx = pd.concat([dfx,dfHD], axis='columns')

        # Occupation Type

        OC = ['Occupation_Accountants', 'Occupation_Cleaning staff', 
            'Occupation_Cooking staff', 'Occupation_Core staff',
            'Occupation_Drivers', 'Occupation_HR staff',
            'Occupation_High skill tech staff', 'Occupation_IT staff',
            'Occupation_Laborers', 'Occupation_Low-skill Laborers',
            'Occupation_Managers', 'Occupation_Medicine staff', 'Occupation_Others',
            'Occupation_Private service staff', 'Occupation_Realty agents',
            'Occupation_Sales staff', 'Occupation_Secretaries',
            'Occupation_Security staff', 'Occupation_Waiters/barmen staff']
        OV = occupation (str(dataccform['occupation']))
        dfOD = pd.DataFrame([dict(zip(OC,OV))])
        dfx = pd.concat([dfx,dfOD], axis='columns')

        FPP = finalmodel.predict_proba(dfx)

        probability = int(FPP[:,1]*100)

        if probability <= 25 :
            return render_template('ccaresult.html', probability = probability, recommendation ="It's better to APPROVE this credit card form", color = '#00FF00')
        elif probability >= 75 :
            return render_template('ccaresult.html', probability = probability, recommendation ="It's better to DECLINE this credit card form", color = '#ff0000' )
        else:
            return render_template('ccaresult.html', probability = probability, recommendation ="You should RECONSIDER to approve this credit card form", color = '#9CC0E7')

@app.route('/credit-card-segmentation')
def ccsegmentation():
    global sukses
    if request.method == "GET" and sukses == 'sukses' :
        return render_template('ccsegmentation.html')
    elif request.method == "GET" and sukses == 'tidaksukses':
        return redirect('/')

@app.route('/credit-card-segmentation-result', methods=['GET','POST'])
def ccsresult():
    global sukses
    if request.method == "GET" and sukses == 'sukses' :
        return render_template('ccsegmentation.html')
    elif request.method == "GET" and sukses == 'tidaksukses':
        return redirect('/')
    else :
        dataccsform = request.form

        # Processing Form => Data
        dfxs = pd.DataFrame([{
            'BALANCE' : int(dataccsform['balance']),
            'BALANCE_FREQUENCY' :  int(dataccsform['bf']),
            'PURCHASES' :  int(dataccsform['purchase']),
            'ONEOFF_PURCHASES' : int(dataccsform['mp']),
            'INSTALLMENTS_PURCHASES' : int(dataccsform['ip']),
            'CASH_ADVANCE' : int(dataccsform['ca']),
            'PURCHASES_FREQUENCY' : int(dataccsform['pf']),
            'ONEOFF_PURCHASES_FREQUENCY' : int(dataccsform['pfo']),
            'PURCHASES_INSTALLMENTS_FREQUENCY' : int(dataccsform['pfi']),
            'CASH_ADVANCE_FREQUENCY' : int(dataccsform['caf']),
            'CASH_ADVANCE_TRX' : int(dataccsform['cft']),
            'PURCHASES_TRX' : int(dataccsform['pt']),
            'CREDIT_LIMIT' : int(dataccsform['ccl']),
            'PAYMENTS' : int(dataccsform['pay']),
            'MINIMUM_PAYMENTS' : int(dataccsform['minpay']),
            'PRC_FULL_PAYMENT' : float(int(dataccsform['perpay'])/100),
            'TENURE' : int(dataccsform['tenure'])
        }])

        rst = scaler.transform(dfxs)

        dffeaturexs=pd.DataFrame()
        s = 0
        for i in dfxs.columns:
            dffeaturexs[i] =  rst[:, s]
            s += 1

        FPS = finalmodels.predict(dffeaturexs)
        cluster =FPS[0]

        if cluster == 0 :
            return render_template('ccsresult.html',result='hometemplate/images/result0.jpg')
        elif cluster == 1 :
            return render_template('ccsresult.html',result='hometemplate/images/result1.jpg')
        elif cluster == 2 : 
            return render_template('ccsresult.html',result='hometemplate/images/result2.jpg')
        elif cluster == 3 :
            return render_template('ccsresult.html',result='hometemplate/images/result3.jpg')
        elif cluster == 4 :
            return render_template('ccsresult.html',result='hometemplate/images/result4.jpg')
        elif cluster == 5 :
            return render_template('ccsresult.html',result='hometemplate/images/result5.jpg')
        elif cluster == 6 :
            return render_template('ccsresult.html',result='hometemplate/images/result6.jpg')
        elif cluster == 7 :
            return render_template('ccsresult.html',result='hometemplate/images/result7.jpg')
        elif cluster == 8 :
            return render_template('ccsresult.html',result='hometemplate/images/result8.jpg')
        else :
            return render_template('ccsresult.html',result='hometemplate/images/result9.jpg')
 

@app.route('/credit-card-data-visualization', methods=['GET','POST'])
def ccdataviz():
    global sukses
    if request.method == "GET" and sukses == 'sukses' :
        return render_template('ccdataviz.html')
    elif request.method == "GET" and sukses == 'tidaksukses':
        return redirect('/')
        
if __name__ == "__main__":

    finalmodel = joblib.load('finalmodelcc')
    finalmodels = joblib.load('finalmodelccs')
    scaler = joblib.load('scalerccs')

    app.run(debug=True, port=5000)

