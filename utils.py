import pandas as pd
import numpy as np
import pickle
import json
import config1

class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region) :
        self.age= age
        self.gender= gender
        self.bmi= bmi
        self.smoker= smoker
        self.children= children
        self.region= 'region_' + region

    def load_model(self):
        with open (config1.MODEL_FILE_PATH,'rb') as f:
            self.model= pickle.load(f)

        with open (config1.JSON_FILE_PATH,'r') as f:
            self.json_data= json.load(f)

    def get_pred_price(self):
        self.load_model()
        reg_index= self.json_data['columns'].index(self.region)
        array1 = np.zeros(len(self.json_data['columns'])) 
        array1[0]=self.age
        array1[1]=self.json_data['gender'][self.gender]
        array1[2]= self.bmi
        array1[3]=self.children
        array1[4]= self.json_data['smoker'][self.smoker]
        array1[reg_index]=1

        pred_charge=self.model.predict([array1])[0]
        return np.around(pred_charge,3)    

# if __name__ == "__main__":
#     med_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)

