import pandas as pd
from lazypredict.Supervised import LazyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import HuberRegressor
from sklearn.ensemble import GradientBoostingRegressor


def lazy(X_train, X_test, y_train, y_test, model_type):
    reg = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None)
    models, predictions = reg.fit(X_train, X_test, y_train, y_test)
    return models[model_type], predictions[model_type]


def adaboost(X_train, X_test, y_train):
    reg = AdaBoostRegressor()
    reg.fit(X_train, y_train)
    return list(reg.predict(X_test))


def SVM(X_train, X_test, y_train):
    reg = SVR(kernel='rbf', C=1.0)
    reg.fit(X_train, y_train)
    return list(reg.predict(X_test))


def RFR(X_train, X_test, y_train):
    random_forest = RandomForestRegressor(n_estimators=50, random_state=42)
    random_forest.fit(X_train, y_train)
    return list(random_forest.predict(X_test))


def LR(X_train, X_test, y_train):
    linear_reg = LinearRegression()
    linear_reg.fit(X_train, y_train)
    output = linear_reg.predict(X_test)
    output = output.reshape(-1, 1)
    pred = []
    for i in output:
        pred.append(i[0])
    return pred


def BR(X_train, X_test, y_train):
    reg = DecisionTreeClassifier()
    bag = BaggingRegressor(
        base_estimator=reg, n_estimators=50, random_state=42)
    bag.fit(X_train, y_train)
    return list(bag.predict(X_test))


def XGB(X_train, X_test, y_train):
    reg = XGBRegressor()
    reg.fit(X_train, y_train)
    return list(reg.predict(X_test))


def ET(X_train, X_test, y_train):
    reg = ExtraTreesRegressor()
    reg.fit(X_train, y_train)
    return list(reg.predict(X_test))


def HR(X_train, X_test, y_train):
    reg = HuberRegressor(max_iter=2000)
    reg.fit(X_train, y_train)
    return list(reg.predict(X_test))


def GB(X_train, X_test, y_train):
    reg = GradientBoostingRegressor(n_estimators=70, random_state=42)
    reg.fit(X_train, y_train)
    return list(reg.predict(X_test))

def r_selection(X_train, X_test, y_train, model):
    o = []
    for i in model:
        if i == "Linear_Regression":
            pred = LR(X_train, X_test, y_train)
            o.append(["Linear Regression", pred])
        elif i == "Random_Forest_Regressor":
            pred = RFR(X_train, X_test, y_train)
            o.append(["Random Forest Regression", pred])
        elif i == "SVR":
            pred = SVM(X_train, X_test, y_train)
            o.append(["Support Vector Regressor", pred])
        elif i == "Adaptive_Boosting_Regressor":
            pred = adaboost(X_train, X_test, y_train)
            o.append(["Adaptive Boosting", pred])
        elif i == "Extra_Trees_Regressor":
            pred = ET(X_train, X_test, y_train)
            o.append(["Extra Trees Regressor", pred])
        elif i == "Huber_Regressor":
            pred = HR(X_train, X_test, y_train)
            o.append(["Huber Regressor", pred])
        elif i == "Gradient_Boosting_Regressor":
            pred = GB(X_train, X_test, y_train)
            o.append(["Gradient Boosting Regressor", pred])
    return o
