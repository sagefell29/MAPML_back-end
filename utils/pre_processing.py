
import numpy as np
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def lof(df):
    lof = LocalOutlierFactor()
    outlier_scores = lof.fit_predict(df)
    df_lof = df[outlier_scores == 1]
    df_lof = df_lof.reset_index(drop=True)
    return df_lof


def isf(df):
    model = IsolationForest()
    model.fit(df)
    outliers = model.predict(df)
    df = df[outliers == 1]
    df_final = df.reset_index(drop=True)
    return df_final


def pca(df, output, th):
    ss = StandardScaler()
    y = df[output]
    X = df.drop(output, axis=1)
    scaled_data = ss.fit_transform(X)
    pca = PCA(n_components=th)
    new_data = pca.fit_transform(scaled_data)
    df_pca = pd.DataFrame(data=new_data)
    df_pca_final = pd.concat([df_pca, y], axis=1)
    df_pca_final.columns = df_pca_final.columns.astype(str)
    return df_pca_final


def rfe(df, output, th):
    y = df[output]
    X = df.drop(output, axis=1)
    model = XGBRegressor()
    rfe = RFE(estimator=model, n_features_to_select=th)
    rfe.fit(X, y)
    selected_features = list(X.columns[rfe.support_])
    for i in output:
        selected_features.append(i)
    df_final = df[selected_features]
    return df_final
    
def select_odm(df, m):
    if m == "isf":
        df_od = isf(df)
    elif m == "lof":
        df_od = lof(df)
    else:
        df_od = df
    return df_od


def select_drm(df, output, m, t):
    if m == "rfe":
        df_col = rfe(df, output, t)
    elif m == "pca":
        df_col = pca(df, output, t)
    else:
        df_col = df
    return df_col