from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import roc_auc_score
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run

run=Run.get_context()

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")
    parser.add_argument('--data_directory', type=str, help="Data directory")

    args = parser.parse_args()

    data_path = args.data_directory
    x_train = pd.read_csv(f"{data_path}/x_train.csv")
    x_test = pd.read_csv(f"{data_path}/x_test.csv")
    y_train = pd.read_csv(f"{data_path}/y_train.csv")
    y_test = pd.read_csv(f"{data_path}/y_test.csv")

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    auc_weighted = roc_auc_score(y_test, model.predict_proba(x_test)[:,1], average="weighted")
    run.log("AUC_weighted", np.float(auc_weighted))

    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.joblib')

if __name__ == '__main__':
    main()
    