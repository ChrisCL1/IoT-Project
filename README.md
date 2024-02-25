# Bluetooth Scanner

This Python script utilizes the `bluetooth` library to scan for nearby Bluetooth devices and print their addresses and names.

## Requirements

- Python 3.7
- `bluetooth` library

## Installation

### 1. Install Python 3.7

You need to have Python 3.7 installed on your system, you can download and install it from the [official Python website](https://www.python.org/downloads/).

### 2. Install the Required `bluetooth` Library

After installing Python 3.7, you need to install the `bluetooth` library using pip, the Python package manager. Open a terminal or command prompt and run the following command:

pip install pybluez

This command will install the `pybluez` package, which provides Bluetooth functionality for Python.

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the `bluetooth_scanner.py` file.
3. Run the script:

python bluetooth_scanner.py

4. The script will perform a Bluetooth inquiry and print the addresses and names of the nearby devices.

## Explanation

- `BluetoothScanner` class: Represents a Bluetooth scanner object.
- `perform_inquiry()`: Performs a Bluetooth inquiry to discover nearby devices.
- `print_devices()`: Prints the addresses and names of the discovered devices.

## Notes

- Make sure your system has Bluetooth capability and is enabled.
- Depending on your system configuration, you might need appropriate permissions to perform Bluetooth operations.
- This script might require superuser privileges to run, especially on Linux systems.

## Troubleshooting

- If the script fails to run or doesn't detect any devices, ensure that Bluetooth is enabled on your system and that your system's Bluetooth adapter is functioning correctly.
- On Linux systems, you may need to run the script with superuser privileges (`sudo`) to access the Bluetooth adapter.
- Refer to the documentation of your operating system and Bluetooth adapter for troubleshooting specific issues related to Bluetooth connectivity.