import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def preprocessing(data):
    data_rows = []
    for row in data:
        data_rows.append(row.decode('utf-8').rstrip().split(','))
    df = pd.DataFrame(data_rows[1:], columns=data_rows[0])
    for col in df.columns:
        try:
            df[col] = df[col].astype(float)
        except ValueError:
            df[col] = df[col].astype(str)
    return df


def make_dataset(df, output):
    X = df.drop(output, axis=1)
    y = df[output]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)
    return X_train, X_test, y_train, y_test


def handleCatVar_r(df, m):
    object_col = list(df.select_dtypes(include="object"))
    if object_col == []:
        return df
    if m == "remove":
        df_wo = df.drop(object_col, axis=1)
        return df_wo
    elif m == "label":
        le = LabelEncoder()
        df_new = df.drop(object_col, axis=1)
        for i in object_col:
            le.fit(df[i])
            df_new[i] = le.fit_transform(df[i])
        return df_new
    elif m == "one_hot":
        old_col = list(df.select_dtypes(exclude="object"))
        df_oh = pd.get_dummies(df, columns=object_col)
        new_cols = list(df_oh.columns)
        for i in new_cols:
            if i in old_col:
                new_cols.remove(i)
        df_oh[new_cols] = df_oh[new_cols].astype(int)
        return df_oh
    else:
        return df


def handleCatVar_c(df, m, output):
    object_col = list(df.select_dtypes(include="object"))
    if output[0] in object_col:
        l2 = LabelEncoder()
        y = df[output[0]]
        df = df.drop(output[0], axis = 1)
        l2.fit(y)
        df[output[0]] = l2.fit_transform(y)
        object_col.remove(output[0])
    if object_col == []:
        return df
    if m == "remove":
        df.drop(object_col, axis=1, inplace=True)
        return df
    elif m == "label":
        le = LabelEncoder()
        df_new = df.drop(object_col, axis=1)
        for i in object_col:
            le.fit(df[i])
            df_new[i] = le.fit_transform(df[i])
        return df_new
    elif m == "one_hot":
        old_col = list(df.select_dtypes(exclude="object"))
        df_oh = pd.get_dummies(df, columns=object_col)
        new_cols = list(df_oh.columns)
        for i in new_cols:
            if i in old_col:
                new_cols.remove(i)
        df_oh[new_cols] = df_oh[new_cols].astype(int)
        return df_oh
    else:
        return df
