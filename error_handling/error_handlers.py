"""
Error handlers for MAPML application
"""

from flask import jsonify
from werkzeug.exceptions import HTTPException
from .custom_errors import (
    CategoricalHandlingError, 
    DatasetValidationError, 
    ModelSelectionError, 
    PreprocessingError, 
    FileFormatError, 
    InsufficientDataError
)


def handle_value_error(error):
    """Handle ValueError exceptions"""
    m = error.args[0]
    if "could not convert string to float" in m:
        raise CategoricalHandlingError(error)
    response = {
        'status': 'error',
        'message': m,
        'tip': "Please check your input data and ensure all values are in the correct format."
    }
    return jsonify(response), 400


def handle_categorical_handling_error(error):
    """Handle CategoricalHandlingError exceptions"""
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400


def handle_dataset_validation_error(error):
    """Handle DatasetValidationError exceptions"""
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400


def handle_model_selection_error(error):
    """Handle ModelSelectionError exceptions"""
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400


def handle_preprocessing_error(error):
    """Handle PreprocessingError exceptions"""
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400


def handle_file_format_error(error):
    """Handle FileFormatError exceptions"""
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400


def handle_insufficient_data_error(error):
    """Handle InsufficientDataError exceptions"""
    response = {
        'status': 'error',
        'message': error.message,
        'tip': error.tip
    }
    return jsonify(response), 400


def handle_error(error):
    """Handle general exceptions"""
    m = error.args[0] if error.args else "An unexpected error occurred"
    response = {
        'status': 'error',
        'message': m,
        'tip': "Please try again or contact support if the problem persists."
    }
    return jsonify(response), 500


def handle_http_exception(error):
    """Handle HTTP exceptions"""
    response = {
        'status': 'error',
        'message': error.description,
        'tip': "Please check your request and try again."
    }
    return jsonify(response), error.code
