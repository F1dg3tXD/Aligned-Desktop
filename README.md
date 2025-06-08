# qt6-browser-app

This project is a simple Qt6 application that displays an HTML file in its own browser window. It allows users to toggle between windowed and fullscreen modes.

## Project Structure

```
qt6-browser-app
├── src
│   ├── main.py          # Entry point of the application
│   └── ui
│       └── __init__.py  # UI-related components
├── index.html           # HTML content to be displayed
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Requirements

To run this application, you need to have Python installed along with the following dependencies:

- PyQt6

You can install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Running the Application

To run the application, execute the following command in your terminal:

```
python src/main.py
```

You can toggle between windowed and fullscreen modes using the designated key or button in the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.