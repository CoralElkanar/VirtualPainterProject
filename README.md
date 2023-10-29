# virtual painter

**Table of Contents**
- Description
- Features
- Installation
- Usage
- How It Works

## Description

The Virtual Painter is a Python application that utilizes OpenCV and NumPy libraries to create a virtual canvas for drawing with various colors. 
By identifying colors displayed to the webcam, it allows users to paint virtually, turning any space into a canvas for creative expression.

## Features

- Real-time color detection from webcam input.
- Virtual painting with a variety of colors.
- Interactive and user-friendly interface.
- Option to clear the canvas.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x and the required libraries (OpenCV and NumPy) installed.
3. Run the application using the provided run file.

```shell
python run_virtual_painter.py
```

## Usage

1. Launch the application by running 'run_virtual_painter.py'.
2. Use the predefined color ranges to detect colors using your webcam.
3. Draw freely on the virtual canvas, and the program will replicate your brushstrokes.

## How It Works

### 'VirtualPainter' Class

* __'setup_camera'__: Initializes the webcam and sets camera parameters.
* __'get_contours'__: Finds the tip of an object for accurate color detection.
* __'color_detect'__: Identifies colors in the webcam feed and maps them to predefined colors.
* __'draw_on_screen'__: Draws points corresponding to color detection on the virtual canvas.
* __'clear_screen'__: Clears the canvas by removing all drawn points.
* __'run'__: Main program loop that continuously captures webcam input and updates the canvas.
