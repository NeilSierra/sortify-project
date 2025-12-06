"""
Sortify - File Sorter & Duplicate Finder
Main Application Entry Point

This is the main file that starts the Sortify application.
It creates the main window and initializes all components.
"""

import tkinter as tk
from package.widgets import SortifyWidgets
from package.functions import SortifyFunctions

class SortifyApp(tk.Tk, SortifyWidgets, SortifyFunctions):
    """
    Main Application Class
    
    This class inherits from three parent classes:
    - tk.Tk: The main Tkinter window class
    - SortifyWidgets: Contains all UI components (buttons, labels, etc.)
    - SortifyFunctions: Contains all the logic and functionality
    
    Multiple inheritance allows us to organize our code into separate files
    while keeping everything accessible through one main class.
    """
    
    def __init__(self):
        """
        Constructor - runs when the app is created
        
        This method initializes all parts of the application in order:
        1. Initialize the Tkinter window
        2. Initialize the functions/logic
        3. Set up the window properties
        4. Create all UI widgets
        5. Set up logging
        """
        # Initialize the Tkinter window first
        tk.Tk.__init__(self)
        
        # Initialize the functions class (sets up internal variables)
        SortifyFunctions.__init__(self)
        
        # Configure the main window (title, size, icon)
        self.setup_window()
        
        # Create all UI components (buttons, text boxes, etc.)
        self.create_widgets()
        
        # Set up the CSV file for logging user actions
        self.logs_file = "sortify_logs.csv"
        self.init_logs_file()

    def setup_window(self):
        """
        Configure the main window properties
        
        Sets the window title, minimum size, and icon.
        This makes the application look professional and prevents
        the window from being too small to use.
        """
        # Set the window title (appears in title bar)
        self.title("Sortify - File Sorter & Duplicate Finder")
        
        # Set minimum window size (width=1000px, height=700px)
        # Users can make it bigger, but not smaller than this
        self.minsize(1000, 700)
        
        # Try to set the window icon
        try:
            self.iconbitmap("src/images/sortify-logo.ico")
        except:
            # If icon file doesn't exist, just continue without it
            # This prevents the app from crashing if the icon is missing
            pass

# This is the entry point - only runs if this file is executed directly
# (not imported as a module)
if __name__ == "__main__":
    # Create an instance of the Sortify application
    app = SortifyApp()
    
    # Start the Tkinter event loop
    # This keeps the window open and responsive to user actions
    # The program will stay here until the user closes the window
    app.mainloop()