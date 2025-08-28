"""
Custom exception classes for MAPML application
"""

class CategoricalHandlingError(Exception):
    """Raised when there's an issue with categorical variable handling"""
    def __init__(self, error):
        self.message = error.args[0]
        self.tip = "You probably did not select a way of handling Categorical values."
        super().__init__(self.message)


class DatasetValidationError(Exception):
    """Raised when dataset validation fails"""
    def __init__(self, message, tip=None):
        self.message = message
        self.tip = tip or "Please check your dataset format and ensure it contains valid data."
        super().__init__(self.message)


class ModelSelectionError(Exception):
    """Raised when there's an issue with model selection"""
    def __init__(self, message, tip=None):
        self.message = message
        self.tip = tip or "Please select at least one model for analysis."
        super().__init__(self.message)


class PreprocessingError(Exception):
    """Raised when preprocessing operations fail"""
    def __init__(self, message, tip=None):
        self.message = message
        self.tip = tip or "Please check your preprocessing settings and try again."
        super().__init__(self.message)


class FileFormatError(Exception):
    """Raised when file format is not supported"""
    def __init__(self, message, tip=None):
        self.message = message
        self.tip = tip or "Please upload a CSV file with proper formatting."
        super().__init__(self.message)


class InsufficientDataError(Exception):
    """Raised when dataset has insufficient data for analysis"""
    def __init__(self, message, tip=None):
        self.message = message
        self.tip = tip or "Please ensure your dataset has enough data points for analysis."
        super().__init__(self.message)