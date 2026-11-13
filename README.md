# About
A simple Python program that accurately converts real-world geographic coordinates (latitude and longitude) into corresponding positions on a block-based grid — such as a Minecraft map or other virtual coordinate system.

There are both an app version of the program with a GUI and a simple script version.

To use the script version of the program, go to: https://www.onlineide.pro/playground/share/4cf82677-93f9-4465-b8bf-1be14d523054

Video tutorial and example walkthrough: https://www.youtube.com/watch?v=wq1AePig_z4


# Details

The user needs to provide:
1.  The real-world coordinate boundaries (in latitude and longitude decimal degree format) of the area that you're trying to convert
2.  The grid's boundary positions (top-left and bottom-right block positions)
3.	A target position in real-world coordinates to convert

Using linear interpolation, the program calculates the equivalent block position by scaling longitude to the grid's x-axis and latitude (inverted north-to-south) to the grid's z-axis.

This tool helps ensure accurate mapping between real-world locations and virtual grids, making it useful for projects such as building real-world map replicas or visualizing GPS data in a block-based environment.


# App with GUI Version – Usage
Sometimes it might be more convenient to use this tool with a graphical user interface. So I have redone the program and implemented a GUI using the PySide6 library (https://pyside.org).

## To run the app:
Clone this repository. It is best to run the app in a virtual environment.

Navigate to the repository directory and run the following Bash commands in order:
```
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python main.py
```

<img width="494" height="1002" alt="Screenshot 2026-11-13 at 1 59 51 PM" src="https://github.com/user-attachments/assets/de8614f5-5bb2-4b63-b9d2-e765992830d3" />
