import json
import pandas as pd
import joblib
from azureml.core.model import Model
import os

def init():
    global model

    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.joblib')
    model = joblib.load(model_path)

def run(data):
    df = pd.read_json(data)
    result = model.predict(df)

    return model_path, json.dumps({'result': result.to_list()})
    