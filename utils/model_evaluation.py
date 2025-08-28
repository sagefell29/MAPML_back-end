import pandas as pd
import numpy as np
from sklearn.metrics import root_mean_squared_error, mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


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


# def getResult_c(y_test, o):
#     # Ensure y_test is a flat numpy array of floats
#     y_test = np.array(y_test, dtype=float).ravel()
#     final = []

#     for model_name, y_pred in o:
#         y_pred = np.array(y_pred, dtype=float).ravel()

#         acs = accuracy_score(y_test, y_pred)
#         ps = precision_score(y_test, y_pred, average='weighted', zero_division=0)
#         rs = recall_score(y_test, y_pred, average='weighted', zero_division=0)
#         f1s = f1_score(y_test, y_pred, average='weighted', zero_division=0)
        
#         # Calculate confusion matrix
#         cm = confusion_matrix(y_test, y_pred)
#         cm_data = cm.tolist()
        
#         # Get unique class labels for better confusion matrix display
#         unique_classes = sorted(list(set(y_test) | set(y_pred)))

#         final.append({
#             'model': model_name,
#             'acs': acs,
#             'ps': ps,
#             'rs': rs,
#             'f1s': f1s,
#             'pred': y_pred.tolist(),
#             'y_test': y_test.tolist(),
#             'confusion_matrix': cm_data,
#             'classes': unique_classes
#         })
#     return final

def getResult_c(y_test, o, threshold=0.5):
    # Ensure y_test is a clean 1D array of labels
    if hasattr(y_test, "values"):  # handles DataFrame/Series
        y_test = y_test.values.ravel()
    else:
        y_test = np.array(y_test).ravel()

    final = []

    for model_name, y_pred in o:
        y_pred = np.array(y_pred)

        # Case 1: Multi-class probabilities → argmax
        if y_pred.ndim == 2 and y_pred.shape[1] > 1:
            y_pred_labels = np.argmax(y_pred, axis=1)

        # Case 2: Binary probs (shape (n,) or (n,1)) → threshold
        elif (y_pred.ndim == 2 and y_pred.shape[1] == 1) or (
            y_pred.ndim == 1 and np.issubdtype(y_pred.dtype, np.floating)
        ):
            y_pred_labels = (y_pred.ravel() >= threshold).astype(int)

        # Case 3: Already class labels
        else:
            y_pred_labels = y_pred.ravel()

        # Collect unique classes
        unique_classes = sorted(list(set(y_test) | set(y_pred_labels)))

        # Metrics
        acs = accuracy_score(y_test, y_pred_labels)
        ps = precision_score(y_test, y_pred_labels, labels=unique_classes, average='weighted', zero_division=0)
        rs = recall_score(y_test, y_pred_labels, labels=unique_classes, average='weighted', zero_division=0)
        f1s = f1_score(y_test, y_pred_labels, labels=unique_classes, average='weighted', zero_division=0)

        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred_labels, labels=unique_classes)

        final.append({
            'model': str(model_name),
            'acs': float(acs),
            'ps': float(ps),
            'rs': float(rs),
            'f1s': float(f1s),
            'pred': y_pred_labels.tolist(),
            'y_test': y_test.tolist(),
            'confusion_matrix': cm.tolist(),
            'classes': [int(c) if isinstance(c, (np.integer, int)) else str(c) for c in unique_classes]
        })

    return final