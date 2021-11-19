from flask import Flask, render_template, request
from run_ml import predictions

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        print(request.form["age"])
        age = float(request.form["age"])
        gender = request.form["gender"]
        hypertension = request.form ["hypertension"]
        heart_disease = request.form["heart_disease"]
        ever_married = request.form["ever_married"]
        smoking_status = request.form["smoking_status"]

        model_age = 0
        model_gender = 0
        model_hyper = 0
        model_heart = 0
        model_married = 0
        model_smoking = 0

        #gender
        if(gender == "Male"):
            model_gender = 1
        elif(gender == "Female"):
            model_gender = 0
        elif(gender == "Other"):
            model_gender = 2
        
        #hypertension
        if(hypertension == "No"):
            model_hyper = 0
        elif(hypertension == "Yes"):
            model_hyper = 1

        #heart
        if(heart_disease == "No"):
            model_heart = 0
        elif(heart_disease == "Yes"):
            model_heart = 1

        #married
        if(ever_married == "No"):
            model_married = 0
        elif(ever_married == "Yes"):
            model_married = 1

        #smoking
        if(smoking_status == "former"):
            model_smoking = 0
        elif(smoking_status == "never smoked"):
            model_smoking = 1
        elif(smoking_status == "smokes"):
            model_smoking = 2
        elif(smoking_status == "unknown"):
            model_smoking = 3

        # data = float(request.form['exp'])
        # print("Data", model.predict([[data]]))
        prediction = predictions(model_age, model_gender, model_hyper, model_heart, 
        model_married, model_smoking)
        
        output = prediction[0]

        results = ""

        if(output == 0):
            results = "No Stroke - keep up the healthy habits!"
        elif(output == 1):
            results = "Stroke - sorry buddy."

        print(output)
        return render_template("results.html", results=results) 

