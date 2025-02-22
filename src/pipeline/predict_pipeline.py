import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object



class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
              raise CustomException(e,sys)


class CustomData:
    def __init__(self,
                 age: int,
                 job: str,
                 marital: str,
                 education: str,
                 default: str,
                 housing: str,
                 loan: str,
                 contact: str,
                 month: str,
                 day_of_week: str,
                 campaign: int,
                 pday: int,
                 previous: int,
                 poutcome: str,
                 emp_var_rate: float,
                 cons_price_idx: float,
                 cons_conf_idx: float,
                 euribor3m: float,
                 nr_employed: float):
                
                self.age = age
                self.job = job
                self.marital = marital
                self.education=education
                self.default=default
                self.housing=housing
                self.loan=loan
                self.contact=contact
                self.month=month
                self.day_of_week=day_of_week
                self.campaign=campaign
                self.pday=pday
                self.previous=previous
                self.poutcome=poutcome
                self.emp_var_rate=emp_var_rate
                self.cons_price_idx=cons_price_idx
                self.cons_conf_idx=cons_conf_idx
                self.euribor3m=euribor3m
                self.nr_employed=nr_employed
    
    def get_data_as_data_frame(self):
          try:
                custom_data_input_dict = {
                    "age":[self.age],
                    "job":[self.job],
                    "marital":[self.marital] ,
                    "education":[self.education],
                    "defualt":[self.defualt],
                    "housing":[self.housing],
                    "loan":[self.loan],
                    "contact":[self.contact],
                    "month":[self.month],
                    "day_of_week":[self.day_of_week],
                    "campaign":[self.campaign],
                    "pday":[self.pday],
                    "previous":[self.previous],
                    "poutcome":[self.poutcome],
                    "emp_var_rate":[self.emp_var_rate],
                    "cons_price_idx":[self.cons_price_idx],
                    "cons_conf_idx":[self.cons_conf_idx],
                    "euribor3m":[self.euribor3m],
                    "nr_employed":[self.nr_employed],
                }

                return pd.DataFrame(custom_data_input_dict)
          except Exception as e:
                raise CustomException(e,sys)