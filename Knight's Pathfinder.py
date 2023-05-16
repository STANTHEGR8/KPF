from collections import deque
from queue import Queue
import tkinter
import pyttsx3

DIRECTIONS = [    (-2, -1), (-2, 1), (-1, -2), (-1, 2),    (1, -2), (1, 2), (2, -1), (2, 1)]

# Define the chessboard as a graph
def create_chessboard():
    # Initialize the chessboard with all vertices unvisited
    chessboard = {}
    for i in range(8):
        for j in range(8):
            chessboard[(i, j)] = {"visited": False, "distance": float("inf"), "shortest_path": []}

    # Define the possible moves of the knight
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    # Add edges to the chessboard graph
    for i in range(8):
        for j in range(8):
            for move in moves:
                x = i + move[0]
                y = j + move[1]
                if x >= 0 and x < 8 and y >= 0 and y < 8:
                    chessboard[(i, j)][(x, y)] = 1

    return chessboard

def get_neighbors(chessboard, current):
    """Get all unvisited neighbors of the current position on the chessboard."""
    row, col = current
    for row_diff, col_diff in DIRECTIONS:
        neighbor_row, neighbor_col = row + row_diff, col + col_diff
        if is_valid(neighbor_row, neighbor_col) and not chessboard[(neighbor_row, neighbor_col)]["visited"]:
            chessboard[(neighbor_row, neighbor_col)]["visited"] = True
            yield neighbor_row, neighbor_col

def bfs(chessboard, start, end):
    queue = Queue()
    queue.put(start)
    memo = {}
    memo[start] = None

    while not queue.empty():
        current = queue.get()

        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = memo[current]
            return path[::-1]

        for neighbor in get_neighbors(chessboard, current):
            if neighbor not in memo:
                memo[neighbor] = current
                chessboard[neighbor]["distance"] = chessboard[current]["distance"] + 1
                chessboard[neighbor]["visited"] = True
                queue.put(neighbor)

    return None

# Define the DFS algorithm
def dfs(chessboard, start, end, path=[], min_distance=float('inf')):
    path = path + [start]
    chessboard[start]["visited"] = True

    if start == end:
        # Update shortest path for each vertex in the path
        for vertex in path:
            chessboard[vertex]["shortest_path"] = path.copy()
        return [path]

    paths = []
    for neighbor in get_neighbors(chessboard, start):
        if not chessboard[neighbor]["visited"]:
            new_path = dfs(chessboard, neighbor, end, path, min_distance)
            if new_path:
                path_distance = len(new_path) - 1
                if path_distance < min_distance:
                    min_distance = path_distance
                    paths = [new_path]
                elif path_distance == min_distance:
                    paths.append(new_path)

    return paths

# Define a memoization function to cache previously computed results
def memoize(func):
    memo = {}
    def wrapper(*args):
        key = tuple(map(tuple, args))
        if key in memo:
            return memo[key]
        else:
            result = func(*args)
            memo[key] = result
            return result
    return wrapper

def is_valid(row, col):
    """
    Check if a given position (row, col) is a valid position on the chessboard
    """
    return row >= 0 and row < 8 and col >= 0 and col < 8

# Use memoization to cache the BFS and DFS results
@memoize
def find_shortest_path_bfs(chessboard, start, end):
    return bfs(chessboard, start, end)

@memoize
def find_shortest_path_dfs(chessboard, start, end):
    return dfs(chessboard, start, end)

# Example usage
if __name__ == '__main__':
    import tkinter as tk
    import customtkinter as ctk
    from tkinter import *

voice = pyttsx3.init()

def find_shortest_path():
    start = start_entry.get()
    end = end_entry.get()

    if not start or not end:
        ctk.CTktextbox.showerror("Error", "Please enter both starting and ending positions.")
        return

    start_row, start_col = ord(start[0]) - ord('a'), int(start[1]) - 1
    end_row, end_col = ord(end[0]) - ord('a'), int(end[1]) - 1

    shortest_path_bfs = find_shortest_path_bfs(chessboard, (start_row, start_col), (end_row, end_col))
    shortest_path = [chr(row + ord('a')) + str(col + 1) for row, col in shortest_path_bfs]

    bfs_result_label.configure(text='     '.join(shortest_path))
    
    # Convert the shortest path to voice output
    voice.say("Shortest path is " + ', '.join(shortest_path))
    voice.runAndWait()

def exit_program():
    window.destroy()

#System Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Create the main window
window = ctk.CTk()
window.geometry('300x400')
window.title("Knight's Pathfinder")
voice.say("Wel come   to Knight's   Path,finder")


# Create the chessboard
chessboard = create_chessboard()

# Create labels and entry fields
start_label = ctk.CTkLabel(window, text="StartPosition:")
start_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
start_label.pack(ipadx=10, ipady=10)
start_entry = ctk.CTkEntry(master=window, width=200, height=25, corner_radius=10, text_color= 'white')
start_entry.pack()

end_label = ctk.CTkLabel(window, text="End Position:")
end_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
end_label.pack(ipadx=10, ipady=10)
end_entry = ctk.CTkEntry(master=window, width=200, height=25, corner_radius=10, text_color= 'white')
end_entry.pack()

# Create a button to find the shortest path
find_path_button = ctk.CTkButton(window, text="Find Shortest Path", command=find_shortest_path, corner_radius=15, fg_color='purple', hover_color='green')
find_path_button.pack(ipadx=5, ipady=10, padx=30, pady=20)

result = ctk.CTkLabel(window, text="Shortest Path:")
result.pack(ipadx=5, ipady=5)

# Create labels to display the results
bfs_result_label = ctk.CTkLabel(window, text="  ", text_color='Orange',)
bfs_result_label.pack(ipadx=3, ipady=3)

# Create a button to exit
find_path_button = ctk.CTkButton(window, text="Exit", command=exit_program, corner_radius=15, fg_color='orange', hover_color='red', text_color='black')
find_path_button.pack(ipadx=5, ipady=10, padx=30, pady=20)

# Run the GUI main loop
voice.runAndWait()
window.mainloop()