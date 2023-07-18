import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score


def getResult_r(y_test, o):
    a = []
    for i in np.array(y_test):
        a.append(float(i[0]))
    final = []
    for i in o:
        rmse = mean_squared_error(y_test, i[1], squared=False)
        mse = mean_squared_error(y_test, i[1], squared=True)
        mae = mean_absolute_error(y_test, i[1])
        r2 = r2_score(y_test, i[1])
        final.append({'model': i[0], 'rmse': rmse, 'mse': mse, 'mae': mae,
                     'r2': r2, "pred": list(i[1]), 'y_test': a})
    return final


def getResult_c(y_test, o):
    a = []
    for i in np.array(y_test):
        a.append(float(i[0]))
    final = []
    for i in o:
        pred = [float(j) for j in i[1]]
        acs = accuracy_score(y_test, i[1])
        ps = precision_score(y_test, i[1], average='weighted')
        rs = recall_score(y_test, i[1], average='weighted')
        f1s = f1_score(y_test, i[1], average='weighted')
        final.append({'model': i[0], 'acs': acs, 'ps': ps,
                     'rs': rs, 'f1s': f1s, 'pred': pred, 'y_test': a})
    return final
