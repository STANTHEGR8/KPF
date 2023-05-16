# Knight's Pathfinder

This is a Python program that finds the shortest path for a knight to move on an 8x8 chessboard, using either the Breadth-First Search (BFS) or Depth-First Search (DFS) algorithm.

## Table of Contents

-   [Overview](https://chat.openai.com/c/2401303c-7377-4faf-b49e-1563c063941c#overview)
-   [Requirements](https://chat.openai.com/c/2401303c-7377-4faf-b49e-1563c063941c#requirements)
-   [Usage](https://chat.openai.com/c/2401303c-7377-4faf-b49e-1563c063941c#usage)
-   [License](https://chat.openai.com/c/2401303c-7377-4faf-b49e-1563c063941c#license)

## Overview

The program creates a chessboard as a graph, where each vertex represents a position on the chessboard. It then uses the BFS and DFS algorithms to find the shortest paths from a starting position to an ending position.

The program provides a graphical user interface (GUI) using the tkinter library, allowing users to input the starting and ending positions and visualize the shortest path on the chessboard.

## Requirements

To run the program, you need:

-   Python 3.x
-   The following Python libraries:
    -   `collections`
    -   `queue`
    -   `tkinter`
    -   `pyttsx3`
    -   `customtkinter` (custom tkinter library)

## Usage

1.  Clone the repository or download the code files.
    
2.  Install the required Python libraries if not already installed. You can use pip to install the libraries:
    
    Copy code
    
    `pip install pyttsx3 customtkinter`
    
3.  Run the program by executing the following command in the terminal:
    
    Copy code
    
    `python knight_pathfinder.py`
    
4.  The GUI window will open. Enter the starting and ending positions (in algebraic notation, e.g., "a1", "b3", etc.) in the respective entry fields.
    
5.  Click the "Find Shortest Path" button to calculate and display the shortest path on the chessboard.
    
6.  The result will be shown in the "Shortest Path" label and announced through the system's text-to-speech engine.
    
7.  To exit the program, click the "Exit" button or close the GUI window.
    

## License

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/c/LICENSE) file for more details.

**Note:** This is a basic readme file providing an overview and instructions for running the program. You may want to include additional sections such as installation instructions, troubleshooting, or a detailed explanation of the algorithms used, depending on your requirements and the complexity of the project.
