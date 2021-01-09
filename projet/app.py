from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
from joblib import load




app = Flask(__name__)
@app.route('/site/')
def index():
    return render_template('index.html')

@app.route('/site/',methods=['POST'])
def form_online_shoppers():
    Administrative = int(request.form['Administrative'])
    Administrative_Duration = float(request.form['Administrative_Duration'])
    Informational = int(request.form['Informational'])
    Informational_Duration = float(request.form['Informational_Duration'])
    ProductRelated = int(request.form['ProductRelated'])
    ProductRelated_Duration = float(request.form['ProductRelated_Duration'])
    BounceRates = float(request.form['BounceRates'])
    ExitRates = float(request.form['ExitRates'])
    PageValues = float(request.form['PageValues'])
    SpecialDay = float(request.form['SpecialDay'])
    Month = int(request.form['Month'])
    OperatingSystems = int(request.form['OperatingSystems'])
    Browser = int(request.form['Browser'])
    Region = int(request.form['Region'])
    TrafficType = int(request.form['TrafficType'])
    VisitorType = int(request.form['VisitorType'])
    Weekend = int(request.form['Weekend'])
    data = [[Administrative,Administrative_Duration,Informational,Informational_Duration,ProductRelated,ProductRelated_Duration,BounceRates,ExitRates,PageValues,SpecialDay,Month,OperatingSystems,Browser,Region,TrafficType,VisitorType,Weekend]]
    prediction = np.array2string(model.predict(data))
    if prediction == '[0.]':
        prediction = "The visitor is not going to purchase."
    else:
        prediction = "The visitor is going to purchase."


    return render_template("result.html",resultat= prediction)


@app.route('/local/', methods=['POST'])
def local():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    if prediction == '[0.]':
        prediction = "The visitor is not going to purchase."
    else:
        prediction = "The visitor is going to purchase."
    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'model_saved.joblib'
    model = load(modelfile)
    app.run(debug=True, host='127.0.0.1')
    