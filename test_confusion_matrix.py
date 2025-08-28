#!/usr/bin/env python3
"""
Test script to verify confusion matrix functionality
"""

import numpy as np
from utils.model_evaluation import getResult_c

def test_confusion_matrix():
    """Test the confusion matrix calculation"""
    
    # Create sample data
    y_test = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0])
    y_pred = np.array([0, 1, 2, 0, 1, 1, 0, 1, 2, 0])  # One prediction is wrong
    
    # Create mock model predictions
    model_predictions = [("TestModel", y_pred)]
    
    # Test the function
    result = getResult_c(y_test, model_predictions)
    
    print("Test Results:")
    print("=" * 50)
    
    for model_result in result:
        print(f"Model: {model_result['model']}")
        print(f"Accuracy: {model_result['acs']:.4f}")
        print(f"Precision: {model_result['ps']:.4f}")
        print(f"Recall: {model_result['rs']:.4f}")
        print(f"F1 Score: {model_result['f1s']:.4f}")
        print(f"Classes: {model_result['classes']}")
        print("Confusion Matrix:")
        for row in model_result['confusion_matrix']:
            print(f"  {row}")
        print()
    
    print("Test completed successfully!")
    return result

if __name__ == "__main__":
    test_confusion_matrix()
