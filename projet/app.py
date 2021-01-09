from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
from joblib import load
import sqlite3

app = Flask(__name__)
@app.route('/')
def index():
    conn = get_db_connection()
    online_shoppers_intention = conn.execute('SELECT * FROM online_shoppers_intention').fetchall()
    conn.close()
    return render_template('index.html', posts=online_shoppers_intention)



#def get_db_connection():
 #   conn = sqlite3.connect('database.db')
  #  conn.row_factory = sqlite3.Row
   # return conn

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'model_saved.joblib'
    model = load(modelfile)
    app.run(debug=True, host='127.0.0.1')
    