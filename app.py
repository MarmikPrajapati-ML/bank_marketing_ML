from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
application =Flask(__name__)

app = application

## Route for Home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods = ['GET','POST'])
def predict_datapoints():
    if request.method =='GET':
        return render_template('home.html')
    else:
        try:
            data  = CustomData(
                    age = int(request.form.get('age')),
                    job = request.form.get('job'),
                    marital = request.form.get('marital'),
                    education = request.form.get('education'),
                    default = request.form.get('default'),
                    housing = request.form.get('housing'),
                    loan = request.form.get('loan'),
                    contact = request.form.get('contact'),
                    month = request.form.get('month'),
                    day_of_week = request.form.get('day_of_week'),
                    campaign = int(request.form.get('campaign')),
                    pday = int(request.form.get('pday')),
                    previous = int(request.form.get('previous')),
                    poutcome = request.form.get('poutcome'),
                    emp_var_rate = float(request.form.get('emp_var_rate')),
                    cons_price_idx = float(request.form.get('cons_price_idx')),
                    cons_conf_idx = float(request.form.get('cons_conf_idx')),
                    euribor3m = float(request.form.get('euribor3m')),
                    nr_employed = float(request.form.get('nr_employed'))
            )

            pred_df = data.get_data_as_data_frame()
            print(pred_df)

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            return render_template('home.html', results=results[0])
        except (ValueError, TypeError) as e:
            return render_template('home.html', error = str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)