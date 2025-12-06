"""
Sortify - File Sorter & Duplicate Finder
UI Widgets and Interface Components

This file contains all the user interface code for the Sortify application.
It creates the visual elements like buttons, text fields, checkboxes, and tables.

The interface is divided into two main sections:
1. Sidebar (left) - Controls for selecting files and configuring options
2. Main Area (right) - Table displaying scanned files
"""

import tkinter as tk  # Main GUI library
from tkinter import ttk  # Themed widgets (better looking than basic tk widgets)
from PIL import Image, ImageTk  # Python Imaging Library for handling images


class SortifyWidgets:
    """
    Contains all the UI widget creation methods.
    This class is meant to be inherited by the main application class.
    """
    
    def create_widgets(self):
        """
        Master function that creates all UI widgets.
        
        This is the main entry point for setting up the user interface.
        It's called once when the application starts.
        """
        # Create the left sidebar with controls
        self.create_sidebar()
        
        # Create the right main area with file display
        self.create_main_area()

    # ==================== SIDEBAR CREATION ====================
    
    def create_sidebar(self):
        """
        Create the sidebar with all controls and options.
        
        The sidebar contains:
        - Logo and app title
        - File path selection (target and destination)
        - File exclusion checkboxes
        - Action buttons (delete duplicates, sort files)
        
        Layout: Fixed width (350px) on the left side of the window
        """
        # Create sidebar frame with fixed width
        sidebar = tk.Frame(self, width=350, padx=10, pady=10)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)  # Pack on left, fill vertical space
        sidebar.pack_propagate(False)  # Don't shrink to fit contents

        # -------------------- LOGO SECTION --------------------
        
        # Create frame to hold logo and title
        logo_frame = tk.Frame(sidebar)
        logo_frame.pack(padx=10, pady=5)

        try:
            # Try to load and display the logo image
            logo_img = ImageTk.PhotoImage(Image.open("src/images/sortify-logo.png").resize((30, 30)))
            logo_label = tk.Label(logo_frame, image=logo_img)
            logo_label.image = logo_img  # Keep a reference to prevent garbage collection
            logo_label.pack(side=tk.LEFT)
        except:
            # If logo image not found, just skip it (app will work without logo)
            pass

        # Add application title next to logo
        tk.Label(logo_frame, text="Sortify", font=("Helvetica", 20, "bold"), fg="#12612E").pack(side=tk.LEFT)

        # -------------------- FILE SELECTION SECTION --------------------
        
        # Create labeled frame for file path selection
        file_selection = tk.LabelFrame(sidebar, text="  File Selection  ", padx=10, pady=10)
        file_selection.pack(fill=tk.X, pady=5)

        # Target Path Row
        tk.Label(file_selection, text="Target File Path:").pack(anchor=tk.W)
        
        # Container for entry and button
        target_frame = tk.Frame(file_selection)
        target_frame.pack(anchor=tk.W, fill=tk.X, expand=True)
        
        # Text entry for target path
        self.target_path = tk.Entry(target_frame)
        self.target_path.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Button to open directory chooser
        tk.Button(target_frame, text="  Choose Path  ", command=self.choose_target_path).pack(side=tk.LEFT, padx=(5, 0))

        # Destination Path Row (similar structure to target path)
        tk.Label(file_selection, text="Destination File Path:").pack(anchor=tk.W)
        
        dest_frame = tk.Frame(file_selection)
        dest_frame.pack(anchor=tk.W, fill=tk.X, expand=True)
        
        self.destination_path = tk.Entry(dest_frame)
        self.destination_path.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Button(dest_frame, text="  Choose Path  ", command=self.choose_destination_path).pack(side=tk.LEFT, padx=(5, 0))

        # Clear button to reset both paths
        tk.Button(file_selection, text="Clear Selected Paths", command=self.clear_paths).pack(fill=tk.X, pady=(10, 0))

        # -------------------- FILE EXCLUSIONS SECTION --------------------
        
        # Create labeled frame for exclusion options
        exclusions = tk.LabelFrame(sidebar, text="  File Exclusions  ", padx=10, pady=10)
        exclusions.pack(fill=tk.X, pady=5)

        # Initialize all checkbox variables
        self.init_exclusion_vars()
        
        # Create the actual checkboxes
        self.create_exclusion_checkboxes(exclusions)

        # -------------------- FILE OUTPUT SECTION --------------------
        
        # Create labeled frame for action buttons
        output = tk.LabelFrame(sidebar, text="  File Output  ", padx=10, pady=10)
        output.pack(fill=tk.X, pady=5)

        # Button to find and delete duplicate files
        tk.Button(output, text="Find and Delete Duplicate Files", command=self.delete_duplicates).pack(fill=tk.X, expand=True, pady=(0, 2))
        
        # Button to sort files into folders
        tk.Button(output, text="Sort Selected Files", command=self.sort_files).pack(fill=tk.X, expand=True)

    def init_exclusion_vars(self):
        """
        Initialize all exclusion BooleanVars.
        
        BooleanVar is a special tkinter variable that stores True/False values.
        Each checkbox is linked to one of these variables.
        When a checkbox is checked, its BooleanVar becomes True.
        
        These variables are used later to determine which file types to exclude.
        """
        # Common file types
        self.exclude_audio = tk.BooleanVar()           # Music files
        self.exclude_code = tk.BooleanVar()            # Programming files
        self.exclude_compressed = tk.BooleanVar()      # ZIP, RAR, etc.
        self.exclude_configuration = tk.BooleanVar()   # Config files
        self.exclude_database = tk.BooleanVar()        # Database files
        self.exclude_document = tk.BooleanVar()        # Word documents, text files
        self.exclude_ebook = tk.BooleanVar()           # EPUB, MOBI, etc.
        self.exclude_executable = tk.BooleanVar()      # .exe, .app, etc.
        self.exclude_font = tk.BooleanVar()            # Font files
        self.exclude_image = tk.BooleanVar()           # Pictures
        self.exclude_presentation = tk.BooleanVar()    # PowerPoint, etc.
        self.exclude_shortcuts = tk.BooleanVar()       # Shortcut files
        self.exclude_spreadsheets = tk.BooleanVar()    # Excel files
        self.exclude_video = tk.BooleanVar()           # Video files
        self.exclude_virtual = tk.BooleanVar()         # Virtual machine files
        
        # Additional file types
        self.exclude_hidden = tk.BooleanVar()          # Hidden files
        self.exclude_misc = tk.BooleanVar()            # Miscellaneous
        self.exclude_system = tk.BooleanVar()          # System files
        self.exclude_temp = tk.BooleanVar()            # Temporary files

    def create_exclusion_checkboxes(self, parent):
        """
        Create exclusion checkboxes in a grid layout.
        
        Args:
            parent: The parent widget to place checkboxes in
        
        The checkboxes are organized into two sections:
        1. Common Files - Most frequently used file types (15 checkboxes)
        2. More Files - Additional specialized types (4 checkboxes)
        
        Each section uses a 2-column grid layout to save space.
        """
        
        # -------------------- COMMON FILES SECTION --------------------
        
        tk.Label(parent, text="Common Files:").pack(anchor=tk.W)
        
        # Create frame for common file checkboxes
        common_frame = tk.Frame(parent)
        common_frame.pack(anchor=tk.W, fill=tk.X, expand=True, pady=(0, 10))
        
        # Configure grid to have 2 equal-width columns
        for col in range(2):
            common_frame.columnconfigure(col, weight=1, uniform="col")

        # List of (label, variable) pairs for common file types
        common_checkboxes = [
            ("Audio", self.exclude_audio),
            ("Code", self.exclude_code),
            ("Compressed", self.exclude_compressed),
            ("Configuration", self.exclude_configuration),
            ("Database", self.exclude_database),
            ("Document", self.exclude_document),
            ("E-Book", self.exclude_ebook),
            ("Executable", self.exclude_executable),
            ("Font", self.exclude_font),
            ("Image", self.exclude_image),
            ("Presentation", self.exclude_presentation),
            ("Shortcuts", self.exclude_shortcuts),
            ("Spreadsheets", self.exclude_spreadsheets),
            ("Video", self.exclude_video),
            ("Virtual", self.exclude_virtual)
        ]

        # Create checkboxes in 2-column grid
        # First 8 items go in column 0, remaining items in column 1
        for i, (text, var) in enumerate(common_checkboxes):
            tk.Checkbutton(common_frame, text=f"{text} Files", variable=var).grid(
                column=0 if i < 8 else 1,  # Column selection
                row=i % 8,                  # Row number (0-7)
                sticky=tk.W                 # Align to west (left)
            )

        # -------------------- MORE FILES SECTION --------------------
        
        tk.Label(parent, text="More Files:").pack(anchor=tk.W)
        
        # Create frame for additional file type checkboxes
        more_frame = tk.Frame(parent)
        more_frame.pack(anchor=tk.W, fill=tk.X, expand=True)
        
        # Configure grid to have 2 equal-width columns
        for col in range(2):
            more_frame.columnconfigure(col, weight=1, uniform="col")

        # List of (label, variable) pairs for additional file types
        more_checkboxes = [
            ("Hidden", self.exclude_hidden),
            ("Miscellaneous", self.exclude_misc),
            ("System", self.exclude_system),
            ("Temporary", self.exclude_temp)
        ]

        # Create checkboxes in 2-column grid (2 items per column)
        for i, (text, var) in enumerate(more_checkboxes):
            tk.Checkbutton(more_frame, text=f"{text} Files", variable=var).grid(
                column=0 if i < 2 else 1,   # Column selection
                row=i % 2,                   # Row number (0-1)
                sticky=tk.W                  # Align to west (left)
            )

    # ==================== MAIN AREA CREATION ====================
    
    def create_main_area(self):
        """
        Create the main content area with file display table.
        
        The main area contains:
        - Top bar with sort dropdown and action buttons
        - Treeview (table) showing all scanned files
        
        Layout: Takes up remaining space on the right side
        """
        # Create main content frame
        main = tk.Frame(self, padx=10)
        main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # -------------------- TOP BAR --------------------
        
        # Create fixed-height top bar
        top_frame = tk.Frame(main, height=40)
        top_frame.pack(fill=tk.X)
        top_frame.pack_propagate(False)  # Maintain fixed height

        # --- Left Side of Top Bar: Sort Options ---
        
        top_left = tk.Frame(top_frame)
        top_left.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.W, expand=True)

        tk.Label(top_left, text="Sorted by:  ").pack(side=tk.LEFT)

        # Define all available sort options
        sort_options = [
            "File Name (A-Z)", 
            "File Name (Z-A)",
            "Date Modified (Newest-Oldest)", 
            "Date Modified (Oldest-Newest)",
            "File Type (A-Z)", 
            "File Type (Z-A)",
            "Size (Largest-Smallest)", 
            "Size (Smallest-Largest)"
        ]

        # Create dropdown (combobox) for sort options
        self.sort_option = ttk.Combobox(top_left, values=sort_options, state="readonly", width=30)
        self.sort_option.current(0)  # Select first option by default
        
        # Bind event handler to detect when selection changes
        self.sort_option.bind("<<ComboboxSelected>>", self.on_sort_changed)
        self.sort_option.pack(side=tk.LEFT)

        # --- Right Side of Top Bar: Action Buttons ---
        
        top_right = tk.Frame(top_frame)
        top_right.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.E, expand=True)

        # Buttons packed from right to left (reverse order in code)
        tk.Button(top_right, text="Logs", width=10, command=self.view_logs).pack(side=tk.RIGHT)
        tk.Button(top_right, text="More Info", width=10, command=self.show_file_extensions_guide).pack(side=tk.RIGHT, padx=5)
        tk.Button(top_right, text="Delete Selected", width=15, command=self.delete_selected).pack(side=tk.RIGHT)

        # -------------------- FILE TABLE (TREEVIEW) --------------------
        
        # Create frame to hold treeview and scrollbar
        tree_frame = tk.Frame(main)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

        # Create vertical scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")

        # Define columns for the file table
        treeview_columns = ("#", "File Name", "Date Modified", "File Type", "Size")
        
        # Create treeview widget (table)
        self.file_treeview = ttk.Treeview(
            tree_frame, 
            columns=treeview_columns,  # Column IDs
            show="headings",            # Show only column headers (no tree structure)
            yscrollcommand=vsb.set      # Connect scrollbar
        )

        # Connect scrollbar to treeview
        vsb.config(command=self.file_treeview.yview)

        # Set column headers
        for col in treeview_columns:
            self.file_treeview.heading(col, text=col)

        # Configure column widths
        self.file_treeview.column("#", width=40, stretch=False)           # Index number
        self.file_treeview.column("File Name", stretch=True)               # Expandable
        self.file_treeview.column("Date Modified", width=150, stretch=False)
        self.file_treeview.column("File Type", width=100, stretch=False)
        self.file_treeview.column("Size", width=70, stretch=False)

        # Use grid layout for precise positioning
        self.file_treeview.grid(row=0, column=0, sticky="nsew")  # Stretch in all directions
        vsb.grid(row=0, column=1, sticky="ns")                   # Stretch vertically only

        # Configure grid weights (make treeview expandable)
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # Initialize empty file data list
        # This will store information about all scanned files
        self.file_data = []

    # ==================== FILE EXTENSIONS GUIDE ====================
    
    def show_file_extensions_guide(self):
        """
        Show a guide window with all file extensions organized by category.
        
        This creates a popup window that displays all the file types
        the application can recognize, organized by category.
        
        Useful for users to understand:
        - What file types are supported
        - Which category each extension belongs to
        - What extensions to look for in their files
        """
        # Create new popup window
        guide_window = tk.Toplevel(self)
        guide_window.title("File Extensions Guide")
        guide_window.geometry("900x600")

        # -------------------- SCROLLABLE CONTENT SETUP --------------------
        
        # Create main container frame
        main_frame = tk.Frame(guide_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas (required for scrolling)
        canvas = tk.Canvas(main_frame)
        
        # Create scrollbar and connect it to canvas
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        
        # Create frame that will hold all the content
        scrollable_frame = tk.Frame(canvas)

        # Update scroll region whenever content size changes
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Place scrollable frame inside canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # -------------------- CONTENT --------------------
        
        # Add title
        title = tk.Label(
            scrollable_frame, 
            text="File Extensions Reference Guide",
            font=("Helvetica", 16, "bold"),
            fg="#12612E"  # Green color matching app theme
        )
        title.pack(pady=(0, 20))

        # Get all file categories from the function
        categories = self.get_file_extension_categories()

        # Create container for two-column layout
        columns_frame = tk.Frame(scrollable_frame)
        columns_frame.pack(fill=tk.BOTH, expand=True)

        # Create left and right columns
        left_column = tk.Frame(columns_frame)
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        right_column = tk.Frame(columns_frame)
        right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # -------------------- DISPLAY CATEGORIES --------------------
        
        # Split categories into two columns for better layout
        category_items = list(categories.items())
        mid_point = (len(category_items) + 1) // 2  # Calculate middle point

        # Create a labeled frame for each category
        for i, (category, extensions) in enumerate(category_items):
            # Determine which column to place this category in
            parent = left_column if i < mid_point else right_column

            # Create labeled frame for this category
            cat_frame = tk.LabelFrame(
                parent, 
                text=f"  {category}  ",
                font=("Helvetica", 10, "bold"),
                padx=10,
                pady=5
            )
            cat_frame.pack(fill=tk.X, pady=(0, 10))

            # Display extensions or "no extensions" message
            if extensions:
                # Join all extensions with commas
                ext_text = ", ".join(extensions)
                
                # Create label with word wrapping
                ext_label = tk.Label(
                    cat_frame,
                    text=ext_text,
                    wraplength=380,      # Wrap text at 380 pixels
                    justify=tk.LEFT,
                    font=("Courier", 9)  # Monospace font for extensions
                )
                ext_label.pack(anchor=tk.W)
            else:
                # For "Other" category which has no specific extensions
                ext_label = tk.Label(
                    cat_frame,
                    text="No specific extensions",
                    font=("Helvetica", 9, "italic"),
                    fg="gray"
                )
                ext_label.pack(anchor=tk.W)

        # -------------------- FINALIZE LAYOUT --------------------
        
        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # -------------------- MOUSE WHEEL SCROLLING --------------------
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            """Handle mouse wheel events for scrolling"""
            # Scroll up or down based on wheel direction
            # event.delta is positive for scroll up, negative for scroll down
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # Bind mouse wheel event to canvas
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # -------------------- CLOSE BUTTON --------------------
        
        # Add close button at bottom of window
        close_btn = tk.Button(
            guide_window,
            text="Close",
            command=guide_window.destroy,
            width=15
        )
        close_btn.pack(pady=10)

        # -------------------- CLEANUP --------------------
        
        # Clean up mouse wheel binding when window closes
        def on_closing():
            """Cleanup function called when window is closed"""
            canvas.unbind_all("<MouseWheel>")  # Remove mouse wheel binding
            guide_window.destroy()              # Destroy the window
        
        # Set window close handler
        guide_window.protocol("WM_DELETE_WINDOW", on_closing)