from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

def dtc(X_train, X_test, y_train):
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return list(model.predict(X_test))

def rfc(X_train, X_test, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return list(model.predict(X_test))

def svc(X_train, X_test, y_train):
    model = SVC()
    model.fit(X_train, y_train)
    return list(model.predict(X_test))

def knn(X_train, X_test, y_train):
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    return list(model.predict(X_test))

def nbg(X_train, X_test, y_train):
    model = GaussianNB()
    model.fit(X_train, y_train)
    return list(model.predict(X_test))

def c_selection(X_train, X_test, y_train, model):
    o = []
    for i in model:
        if i == "Decision_Tree":
            pred = dtc(X_train, X_test, y_train)
            o.append(["Decision Tree Classification", pred])
        elif i == "Random_Forest":
            pred = rfc(X_train, X_test, y_train)
            o.append(["Random Forest Classification", pred])
        elif i == "Support_Vector":
            pred = svc(X_train, X_test, y_train)
            o.append(["Support Vector Classification", pred])
        elif i == "K_Neighbors":
            pred = knn(X_train, X_test, y_train)
            o.append(["K-Neighbors Classification", pred])
        elif i == "Naive_Bayes":
            pred = nbg(X_train, X_test, y_train)
            o.append(["Naive Bayes Classification", pred])
    return o