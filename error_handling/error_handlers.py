from flask import jsonify
from werkzeug.exceptions import HTTPException
from .custom_errors import CategoricalHandlingError


# General Error Handler Definition

def handle_value_error(error):
    m = error.args[0]
    if "could not convert string to float" in m:
        raise CategoricalHandlingError(error)
    response = {
        'status': 'error',
        'message': m
    }
    return jsonify(response), 400


# Custom Error Handler Definition

def handle_categorical_handling_error(error):
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400


def handle_error(error):
    m = error.args[0]
    response = {
        'status': 'error',
        'message': m
    }
    return jsonify(response)
