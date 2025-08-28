import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from error_handling.custom_errors import CategoricalHandlingError
from error_handling.error_handlers import handle_categorical_handling_error, handle_value_error, handle_error
from utils.data_processing import preprocessing, make_dataset, handleCatVar_r, handleCatVar_c
from utils.pre_processing import select_odm, select_drm
from utils.model_evaluation import getResult_r, getResult_c
from models.classifiers import c_selection
from models.regressors import r_selection


app = Flask(__name__)
CORS(app)

# Registering Error Handlers
app.register_error_handler(CategoricalHandlingError, handle_categorical_handling_error)
app.register_error_handler(ValueError, handle_value_error)
app.register_error_handler(Exception, handle_error)


# Actual Routes

@app.route('/api/predict', methods=['POST'])
def predict():
    try:

        # Retrieving data and parameters from the request
        dataset = request.files['dataset']
        output_attribute = request.form['output_Attribute'].split(',')
        task = request.form['task']
        threshold = int(request.form['threshold'])
        model_type = request.form['model_Type'].split(',')
        od = request.form["Outlier_Detection"]
        odm = request.form["OD_Method"]
        dr = request.form["Dimensionality_Reduction"]
        drm = request.form["DR_Method"]
        hcv = request.form["handle_categorical_variable"]
        # print(output_attribute)
        print(request)

        df_init = preprocessing(dataset)

        if task == "regression":
            df_init = handleCatVar_r(df_init, hcv)
        elif task == "classification":
            df_init = handleCatVar_c(df_init, hcv, output_attribute)

        if od == "Yes":
            df_init = select_odm(df_init, odm)
        if dr == "Yes":
            df_init = select_drm(df_init, output_attribute, drm, threshold)

        X_train, X_test, y_train, y_test = make_dataset(
            df_init, output_attribute)

        if (task == "regression"):
            pred = r_selection(X_train, X_test, y_train, model_type)
        elif (task == "classification"):
            pred = c_selection(X_train, X_test, y_train, model_type)

        if (task == "regression"):
            final = getResult_r(y_test, pred)
        else:
            final = getResult_c(y_test, pred)

        # Returning the response with the output parameters
        response = {
            'status': 'success',
            'result': final,
        }
        return jsonify(response)

    except ValueError as e:
        return handle_value_error(e)
    
    except Exception as e:
        return handle_error(e)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
