import pandas as pd
import numpy as np
from sklearn.metrics import root_mean_squared_error, mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def getResult_r(y_test, o):
    # Ensure y_test is a flat numpy array of floats
    y_test = np.array(y_test, dtype=float).ravel()
    final = []

    for model_name, y_pred in o:
        y_pred = np.array(y_pred, dtype=float).ravel()

        rmse = root_mean_squared_error(y_test, y_pred)  # replaces root_mean_squared_error
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        final.append({
            'model': model_name,
            'rmse': rmse,
            'mse': mse,
            'mae': mae,
            'r2': r2,
            "pred": y_pred.tolist(),
            'y_test': y_test.tolist()
        })
    return final


def getResult_c(y_test, o):
    # Ensure y_test is a flat numpy array of floats
    y_test = np.array(y_test, dtype=float).ravel()
    final = []

    for model_name, y_pred in o:
        y_pred = np.array(y_pred, dtype=float).ravel()

        acs = accuracy_score(y_test, y_pred)
        ps = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        rs = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1s = f1_score(y_test, y_pred, average='weighted', zero_division=0)

        final.append({
            'model': model_name,
            'acs': acs,
            'ps': ps,
            'rs': rs,
            'f1s': f1s,
            'pred': y_pred.tolist(),
            'y_test': y_test.tolist()
        })
    return final