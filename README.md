# MAPML Backend

Machine Learning Analysis Platform Backend - A comprehensive Flask-based API for machine learning model training and evaluation.

## Features

### Core Functionalities
- **Regression Analysis**: Support for multiple regression algorithms
- **Classification Analysis**: Support for multiple classification algorithms
- **Data Preprocessing**: Comprehensive data cleaning and preparation
- **Model Evaluation**: Detailed performance metrics and analysis
- **Confusion Matrix**: Visual representation for classification results

### Back-End Functionalities
1. **Data Processing**: Handles CSV file uploads and data preprocessing
2. **Model Training**: Supports multiple ML algorithms for both regression and classification
3. **Performance Evaluation**: Calculates accuracy, precision, recall, F1-score, and confusion matrices
4. **Preprocessing Options**: Outlier detection and dimensionality reduction
5. **Categorical Variable Handling**: Multiple encoding strategies
6. **Classification Evaluation**: Confusion matrix generation and visualization

### New Features
- **Enhanced Error Handling**: Comprehensive error management with custom exceptions
- **Input Validation**: Robust validation for all input parameters
- **Health Check Endpoint**: API health monitoring
- **Request Timeout Handling**: Proper timeout management for long-running operations
- **Detailed Error Messages**: User-friendly error messages with helpful tips

## API Endpoints

### POST `/api/predict`
Main prediction endpoint for both regression and classification tasks.

**Request Parameters:**
- `dataset`: CSV file upload
- `output_Attribute`: Target variable name
- `task`: "regression" or "classification"
- `threshold`: Number of columns for dimensionality reduction
- `model_Type`: Array of selected models
- `Outlier_Detection`: "Yes" or "No"
- `OD_Method`: Outlier detection method ("lof", "isf", "None")
- `Dimensionality_Reduction`: "Yes" or "No"
- `DR_Method`: Dimensionality reduction method ("pca", "rfe", "None")
- `handle_categorical_variable`: Categorical handling strategy ("None", "remove", "label", "one_hot")

**Response:**
```json
{
  "status": "success",
  "result": [
    {
      "model": "model_name",
      "acs": 0.95,
      "ps": 0.94,
      "rs": 0.95,
      "f1s": 0.94,
      "pred": [...],
      "y_test": [...],
      "confusion_matrix": [[...]],
      "classes": [...]
    }
  ]
}
```

### GET `/api/health`
Health check endpoint to verify API status.

**Response:**
```json
{
  "status": "success",
  "message": "MAPML Backend is running",
  "version": "1.0.0"
}
```

## Error Handling

The backend implements comprehensive error handling with custom exceptions:

### Custom Error Types
- **CategoricalHandlingError**: Issues with categorical variable processing
- **DatasetValidationError**: Dataset format or content issues
- **ModelSelectionError**: Problems with model selection
- **PreprocessingError**: Errors in data preprocessing steps
- **FileFormatError**: Unsupported or corrupted file formats
- **InsufficientDataError**: Dataset too small for analysis

### Error Response Format
```json
{
  "status": "error",
  "message": "Descriptive error message",
  "tip": "Helpful suggestion for resolution"
}
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MAPML_back-end
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

The server will start on `http://127.0.0.1:8000`

## Dependencies

Key dependencies include:
- Flask: Web framework
- scikit-learn: Machine learning algorithms
- pandas: Data manipulation
- numpy: Numerical computing
- flask-cors: Cross-origin resource sharing

## Project Structure

```
MAPML_back-end/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── error_handling/                 # Error handling modules
│   ├── custom_errors.py           # Custom exception classes
│   └── error_handlers.py          # Error handler functions
├── models/                        # ML model implementations
│   ├── classifiers.py             # Classification models
│   └── regressors.py              # Regression models
├── utils/                         # Utility functions
│   ├── data_processing.py         # Data preprocessing
│   ├── model_evaluation.py        # Model evaluation metrics
│   └── pre_processing.py          # Preprocessing techniques
└── README.md                      # This file
```

## Usage Examples

### Regression Analysis
```python
import requests

url = "http://127.0.0.1:8000/api/predict"
files = {'dataset': open('data.csv', 'rb')}
data = {
    'output_Attribute': 'target',
    'task': 'regression',
    'model_Type': ['Linear_Regression', 'Random_Forest_Regressor'],
    'Outlier_Detection': 'No',
    'Dimensionality_Reduction': 'No',
    'handle_categorical_variable': 'None'
}

response = requests.post(url, files=files, data=data)
print(response.json())
```

### Classification Analysis
```python
import requests

url = "http://127.0.0.1:8000/api/predict"
files = {'dataset': open('data.csv', 'rb')}
data = {
    'output_Attribute': 'target',
    'task': 'classification',
    'model_Type': ['Decision_Tree', 'Random_Forest'],
    'Outlier_Detection': 'Yes',
    'OD_Method': 'lof',
    'Dimensionality_Reduction': 'No',
    'handle_categorical_variable': 'label'
}

response = requests.post(url, files=files, data=data)
print(response.json())
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
