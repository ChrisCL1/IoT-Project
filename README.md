# Bluetooth Scanner

This Python script utilizes the `bluetooth` library to scan for nearby Bluetooth devices and print their addresses and names.

## Requirements

- Python 3.7
- `bluetooth` library
- Docker installed on your system. You can download Docker from [Docker Hub](https://docs.docker.com/get-docker/).

## Installation

### 1. Install Python 3.7

You need to have Python 3.7 installed on your system, you can download and install it from the [official Python website](https://www.python.org/downloads/).

### 2. Install the Required `bluetooth` Library

After installing Python 3.7, you need to install the `bluetooth` library using pip, the Python package manager. Open a terminal or command prompt and run the following command:

    pip install pybluez

This command will install the `pybluez` package, which provides Bluetooth functionality for Python.

## Usage Instructions

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/bluetooth-scanner.git
    ```

2. Navigate to the project directory:

    ```bash
    cd bluetooth-scanner
    ```

3. Build the Docker image:

    ```bash
    docker build -t bluetooth-scanner .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 6000:6000 bluetooth-scanner
    ```

5. The application will now be available at `http://localhost:6000/app`. You can send POST requests to this endpoint to perform Bluetooth device scanning.

## API Endpoint

- `POST /app`: Performs a Bluetooth device scan and returns the found devices in JSON format.

## Project Structure

- `app.py`: Contains the definition of the Flask application and request routing.
- `func.py`: Contains the implementation of the `BluetoothScanner` class that performs Bluetooth device scanning.
- `Dockerfile`: Specifies how to build the Docker image for the application.
- `requirements.txt`: Text file containing the Python dependencies required for the application.

## Notes

- Make sure your system has Bluetooth capability and is enabled.
- Depending on your system configuration, you might need appropriate permissions to perform Bluetooth operations.
- This script might require superuser privileges to run, especially on Linux systems.

## Troubleshooting

- If the script fails to run or doesn't detect any devices, ensure that Bluetooth is enabled on your system and that your system's Bluetooth adapter is functioning correctly.
- On Linux systems, you may need to run the script with superuser privileges (`sudo`) to access the Bluetooth adapter.
- Refer to the documentation of your operating system and Bluetooth adapter for troubleshooting specific issues related to Bluetooth connectivity.