# MAPML Back-end 📊

This directory contains the back-end code for the MAPML project, which is a web application for data preprocessing and model evaluation. The back-end is built using Flask, a Python web framework.

## Goals of the Project 🎯

### Streamlining the Data Analysis Workflow

- This project's importance rests in its capacity to streamline and simplify the data analysis process. Data preprocessing and model selection are typically labor-intensive manual processes that call for the creation of bespoke scripts or the usage of numerous tools by researchers.
- I hope to save researchers considerable time and energy by combining these duties into a single platform, allowing them to concentrate more on the fundamental analysis and interpretation of results.

### Empowering Researchers and Data Scientists

- This project's goal of enabling academics and data scientists to quickly preprocess their datasets and use a variety of machine learning models, independent of their programming experience, is another key driving force behind it.
- The platform promotes collaboration and knowledge-sharing among academics, thereby boosting the field of data science, by offering a user-friendly interface and including well-liked preprocessing methods and ML algorithms.

## Design Principles and Architectural Approach 🏛️

Several design principles and architectural approaches were followed to ensure a robust and scalable system:

- **Separation of Concerns:** The frontend and backend components are decoupled, with each responsible for distinct functionalities. This separation allows for independent development and deployment, facilitating testing, scalability, and maintenance.
- **RESTful API-based Framework:** The project follows REST principles for communication between the frontend and backend, promoting clear separation of concerns, standardized API endpoints, and scalability.
- **Component-Driven Architecture:** The frontend follows a component-driven approach, creating reusable and independent components for UI elements, data processing, and result visualization. This design encourages code reuse, maintainability, and scalability.
- **Best Practices:** The codebase emphasizes best practices such as error handling, input validation, and security measures to ensure reliability and security.
- **Modular Structure:** The backend codebase follows a modular structure, with separate modules for data processing, machine learning models, and result generation. Each module encapsulates its specific functionality, allowing for easier maintenance, testing, and enhancement of individual components. The codebase also emphasizes best practices such as proper error handling, input validation, and security measures to ensure the reliability and security of the application.

## System Architecture 🏗️

- **Modular Components:** The backend is structured into modular components, each responsible for specific functionalities such as data processing, model training, and result generation. This modular design enhances code maintainability and allows for easy updates or enhancements to individual components.
- **Data Handling:** Data processing tasks, including cleaning, transformation, and feature engineering, are encapsulated in dedicated modules to ensure data quality before model training.
- **Model Training:** Separate modules handle the training of machine learning models, allowing for scalability and easy integration of new models.
- **Interoperability:** The use of RESTful API endpoints follows industry standards for interoperability. This approach allows the backend to communicate seamlessly with the frontend and potentially with other services or systems in the future.

## Tech Stack 💻

### Python

**Language:** Python, a versatile and widely-used programming language, serves as the primary language for backend development. Its extensive ecosystem of libraries and packages, combined with Flask, streamlines development.

### Flask

- **Framework:** Flask, a lightweight and versatile Python web framework, serves as the foundation of the backend. It provides a simple and efficient way to build web applications, making it ideal for this project's requirements.
- **API Development:** Flask's capabilities for building RESTful APIs enable smooth communication between the frontend and backend components.

### scikit-learn

- **Machine Learning:** The scikit-learn library is extensively used for machine learning tasks. It offers a wide range of machine learning algorithms, evaluation measures, and tools for model training and performance evaluation.
- **Model Selection:** scikit-learn provides a rich collection of machine learning models, including Gaussian naive Bayes, support vector machines, decision trees, random forests, and linear regression, which can be easily integrated into the backend.

## Back-End Functionalities 📱

1. **Data Processing:** The back end handles the core data processing tasks, such as data cleaning, transformation, and feature engineering, ensuring that the data is ready for machine learning.
2. **Model Training:** This module manages the training of selected machine learning models using the processed data. It handles the training-validation splits and model hyperparameter tuning.
3. **Result Generation:** The back end generates results in the form of evaluation metrics and visualizations, such as scatter plots comparing predicted and actual values, to provide users with insights into model performance.
4. **Classification Evaluation:** For classification tasks, the system provides comprehensive evaluation metrics including accuracy, precision, recall, F1-score, and confusion matrices to help users understand model performance across different classes.
5. **Error Handling and Security:** The back end incorporates robust error handling mechanisms to ensure the reliability of the application. It performs input validation to prevent unauthorized access and malicious actions. Security measures are implemented to protect sensitive data and maintain the integrity of the system.

## Back-End Development Process 🛠️

1. **Basic Backend Functionality:** The backend development initiated with the implementation of a basic functionality to handle the JSON object received from the frontend. A critical challenge involved converting the UTF-8 encoded JSON into a DataFrame compatible with Python.
2. **Extracting and Formatting Output:** After successfully converting the JSON data into a DataFrame, the developer focused on extracting and formatting the output attribute from the dataset. Addressing Flask's extensive stack trace and debugging minor errors were crucial for smooth backend operation.
3. **Resource Constraints:** Understanding the limited resources allocated to Flask applications, such as restricted RAM and disk space, presented a significant challenge. The developer optimized memory usage and ensured efficient execution of machine learning algorithms within these constraints.
4. **Result JSON API:** The backend was responsible for formatting the result JSON API object and handling encoding for seamless transmission to the frontend. This required careful consideration of data structure and encoding techniques.
5. **Modularization:** Organizing the codebase into separate modules based on functionality and ensuring smooth integration and coordination among different components were essential tasks in the backend development.
6. **Preprocessing Techniques:** Similar to the frontend, the backend underwent multiple iterations to implement various preprocessing techniques. Each technique was rigorously tested and validated to ensure its proper functioning within the system.
7. **Classification Functionality:** After completing the core functionalities, the developer extended the platform to support classification tasks. This involved duplicating and adapting both frontend and backend codebases to accommodate classification-specific requirements and challenges.

## Installation 🚀

To set up the back-end for the MAPML project, follow these steps:

1. Ensure that you have Python and pip installed on your system.
2. Open the terminal and navigate to the `back_end/` directory.
3. Run the following command to install the required Python packages: ```pip install -r requirements.txt```

## Usage 📝

To run the back-end server:

1. Open the terminal and navigate to the `back_end/` directory.
2. Run the following command: ```python app.py```
3. The back-end server will start running on `http://localhost:8000`.

## File Structure 📂

- `app.py`: Main Flask application file.
- `models/`: Contains regression and classification models used in the project.
- `error_handling/`: Includes custom error handling classes and functions.
- `utils/`: Contains utility functions for data preprocessing, model evaluation, and more.
- `data/`: Placeholder directory for datasets (not included in the repository).
- `test_confusion_matrix.py`: Test script to verify confusion matrix functionality.

## New Features 🆕

### Confusion Matrix for Classification Tasks

The latest update includes comprehensive confusion matrix functionality for classification tasks:

- **Backend Enhancement:** The `getResult_c` function in `utils/model_evaluation.py` now calculates and returns confusion matrix data along with traditional metrics (accuracy, precision, recall, F1-score).
- **Frontend Integration:** The `ConfusionMatrix` component displays a visually appealing confusion matrix with:
  - Color-coded cells (green for correct predictions, gray for incorrect)
  - Clear row and column labels with blue theme
  - Always visible matrix for consistent PDF exports
  - Responsive design that works on different screen sizes
  - High contrast colors for better visibility and accessibility
- **Data Structure:** The confusion matrix is returned as a 2D array with corresponding class labels, making it easy to interpret and visualize.
- **PDF Export:** Confusion matrices are included in PDF exports for comprehensive result documentation.

This feature helps users better understand:
- Which classes are being predicted correctly vs. incorrectly
- The distribution of prediction errors across different classes
- Model performance patterns and potential areas for improvement

## Sister Repository 🤝

This repository's front-end is found [here](https://github.com/sagefell29/MAPML_front-end).

## Contributing

Contributions to the MAPML project are welcome! If you would like to contribute to the back-end code, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request, describing your changes in detail.

## Acknowledgements 🙏

We express our heartfelt gratitude to all the contributors and researchers who have provided valuable guidance and support throughout the development of the MAPML project. Your insights and feedback have been instrumental in shaping this application and advancing its capabilities. This project was carried out under the direct supervision of [Dr. Manoj Semwal](mailto:m.semwal@cimap.res.in).

## License

This project is licensed under the MIT License.
