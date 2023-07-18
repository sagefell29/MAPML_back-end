# MAPML Back-end

This directory contains the back-end code for the MAPML project, which is a web application for data preprocessing and model evaluation. The back-end is built using Flask, a Python web framework.

## Installation

To set up the back-end for the MAPML project, follow these steps:

1. Ensure that you have Python and pip installed on your system.
2. Open the terminal and navigate to the `back_end/` directory.
3. Run the following command to install the required Python packages: ```pip install -r requirements.txt```

## Usage

To run the back-end server:

1. Open the terminal and navigate to the `back_end/` directory.
2. Run the following command: ```python app.py```
3. The back-end server will start running on `http://localhost:8000`.

## File Structure

- `app.py`: Main Flask application file.
- `models/`: Contains regression and classification models used in the project.
- `error_handling/`: Includes custom error handling classes and functions.
- `utils/`: Contains utility functions for data preprocessing, model evaluation, and more.
- `data/`: Placeholder directory for datasets (not included in the repository).

## Sister Repository

This repository's front-end is found [here](https://github.com/sagefell29/MAPML_front-end).

## Contributing

Contributions to the MAPML project are welcome! If you would like to contribute to the back-end code, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request, describing your changes in detail.

## Acknowledgements

🙏 We express our heartfelt gratitude to all the contributors and researchers who have provided valuable guidance and support throughout the development of the MAPML project. Your insights and feedback have been instrumental in shaping this application and advancing its capabilities. This project was carried out under the direct supervision of [Dr. Manoj Semwal](mailto:m.semwal@cimap.res.in).

## License

This project is licensed under the MIT License.
