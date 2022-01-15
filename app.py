from flask import Flask, jsonify, render_template, request
import joblib
import pickle
import os
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def result():

    item_weight= request.form['item_weight']
    item_fat_content=request.form['item_fat_content']
    item_visibility= request.form['item_visibility']
    item_type= request.form['item_type']
    item_mrp = request.form['item_mrp']
    outlet_size= request.form['outlet_size']
    outlet_location_type= request.form['outlet_location_type']
    outlet_type= request.form['outlet_type']

    print("prediction",item_weight,item_fat_content,item_visibility,item_type,item_mrp,outlet_size,outlet_location_type,outlet_type)

    X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                 outlet_location_type,outlet_type,outlet_size]])
    file1 = open("random_model.pkl", "rb")
    model = pickle.load(file1)
    #model = joblib.load(finalized_model.sav)
   
    pred=model.predict(X)

    print("pred",pred)

    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)