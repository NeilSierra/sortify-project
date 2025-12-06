"""
Sortify - File Sorter & Duplicate Finder
Core Functions Module

This file contains all the business logic for the Sortify application.
It handles file scanning, sorting, duplicate detection, and logging operations.
"""

import os  # For file and directory operations
import sys  # For system-specific parameters and functions
import csv  # For reading/writing CSV log files
import time  # For time-related operations
import hashlib  # For generating file hashes to detect duplicates
import shutil  # For high-level file operations (copy, move, etc.)
import tkinter as tk  # Main GUI library
from tkinter import filedialog, messagebox, ttk  # GUI dialog boxes and themed widgets
from collections import deque  # For efficient queue operations (BFS algorithm)
from datetime import datetime  # For timestamp formatting


class SortifyFunctions:
    """
    Contains all the core functionality for the Sortify application.
    This class is meant to be inherited by the main application class.
    """
    
    def __init__(self):
        """
        Initialize function-related attributes.
        Note: This is a parent class that doesn't initialize everything on its own.
        The child class (main app) will have additional initialization.
        """
        pass

    # ==================== LOGGING FUNCTIONS ====================
    
    def init_logs_file(self):
        """
        Initialize the logs CSV file with headers if it doesn't exist yet.
        This creates a new log file when the application first runs.
        
        The log file tracks:
        - Timestamp: When the action occurred
        - Action: What operation was performed (e.g., "Delete Duplicates")
        - Details: Additional information about the action
        - Files Count: How many files were affected
        """
        # Check if the log file already exists
        if not os.path.exists(self.logs_file):
            # Create the file and write header row
            with open(self.logs_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # Write column headers
                writer.writerow(['Timestamp', 'Action', 'Details', 'Files Count'])

    def log_action(self, action, details, files_count):
        """
        Log an action to the CSV file for record-keeping.
        
        Args:
            action (str): Name of the action performed (e.g., "Sort Files")
            details (str): Additional details about the action
            files_count (int): Number of files affected by this action
        
        Example:
            self.log_action("Delete Duplicates", "Deleted from: C:/Users/Downloads", 15)
        """
        # Get current timestamp in readable format
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Append the log entry to the CSV file
        with open(self.logs_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, action, details, files_count])

    # ==================== FILE CATEGORIES ====================
    
    def get_file_extension_categories(self):
        """
        Get comprehensive file extension categories.
        
        Returns:
            dict: A dictionary where keys are category names and values are lists
                  of file extensions belonging to that category.
        
        This function defines how files will be sorted into folders.
        Each category becomes a folder in the destination directory.
        
        Example:
            categories["Audio"] = [".mp3", ".wav", ".flac", ...]
            When sorting, a file named "song.mp3" will go into the "Audio" folder.
        """
        return {
            # Music and sound files
            "Audio": [
                ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", 
                ".opus", ".ape", ".alac", ".aiff", ".aif", ".mid", ".midi",
                ".ra", ".ram", ".dts", ".ac3", ".mka"
            ],
            
            # Video and movie files
            "Video": [
                ".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm",
                ".m4v", ".mpg", ".mpeg", ".3gp", ".3g2", ".f4v", ".swf",
                ".vob", ".ogv", ".ts", ".mts", ".m2ts", ".divx", ".xvid"
            ],
            
            # Image and photo files
            "Images": [
                ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
                ".svg", ".ico", ".webp", ".heic", ".heif", ".raw", ".cr2",
                ".nef", ".orf", ".sr2", ".psd", ".ai", ".eps", ".indd"
            ],
            
            # Text documents
            "Documents": [
                ".txt", ".rtf", ".md", ".doc", ".docx", ".odt", ".pages",
                ".tex", ".wpd", ".wps"
            ],
            
            # Excel and spreadsheet files
            "Spreadsheets": [
                ".xls", ".xlsx", ".ods", ".csv", ".numbers", ".xlsm",
                ".xlsb", ".xltx", ".xltm"
            ],
            
            # PowerPoint and presentation files
            "Presentations": [
                ".ppt", ".pptx", ".odp", ".key", ".pps", ".ppsx", ".pptm"
            ],
            
            # PDF files (separate category because they're so common)
            "PDFs": [
                ".pdf"
            ],
            
            # Digital books
            "E-Books": [
                ".epub", ".mobi", ".azw", ".azw3", ".fb2", ".djvu", ".cbr",
                ".cbz", ".cb7", ".cbt"
            ],
            
            # Compressed/zipped files
            "Archives": [
                ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".z",
                ".tgz", ".tbz2", ".txz", ".lz", ".lzma", ".cab", ".arj",
                ".ace", ".sit", ".sitx", ".zipx"
            ],
            
            # Programming and source code files
            "Code": [
                ".py", ".js", ".java", ".c", ".cpp", ".cs", ".rb", ".html",
                ".css", ".php", ".go", ".rs", ".swift", ".kt", ".ts", ".jsx",
                ".tsx", ".vue", ".scala", ".r", ".m", ".pl", ".sh", ".bash",
                ".bat", ".ps1", ".vbs", ".lua", ".dart", ".sql", ".h", ".hpp"
            ],
            
            # Programs and installers
            "Executables": [
                ".exe", ".msi", ".app", ".deb", ".rpm", ".dmg", ".apk",
                ".jar", ".com", ".run", ".bin"
            ],
            
            # Font files
            "Fonts": [
                ".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon", ".fnt"
            ],
            
            # Database files
            "Databases": [
                ".db", ".sql", ".sqlite", ".sqlite3", ".mdb", ".accdb",
                ".dbf", ".odb", ".frm", ".myd", ".myi"
            ],
            
            # Configuration and settings files
            "Configuration": [
                ".ini", ".cfg", ".conf", ".config", ".json", ".xml", ".yaml",
                ".yml", ".toml", ".properties", ".plist", ".reg"
            ],
            
            # 3D model files
            "3D Models": [
                ".obj", ".fbx", ".dae", ".3ds", ".blend", ".stl", ".ply",
                ".gltf", ".glb"
            ],
            
            # Computer-aided design files
            "CAD": [
                ".dwg", ".dxf", ".dwf", ".dgn", ".rvt", ".skp"
            ],
            
            # Web page files
            "Web": [
                ".html", ".htm", ".xhtml", ".mhtml", ".mht", ".asp", ".aspx",
                ".jsp", ".php"
            ],
            
            # Script files
            "Scripts": [
                ".sh", ".bash", ".bat", ".cmd", ".ps1", ".vbs", ".ahk"
            ],
            
            # System files
            "System": [
                ".sys", ".dll", ".drv", ".ocx", ".cpl", ".scr", ".dmp",
                ".log", ".bak"
            ],
            
            # Temporary files
            "Temporary": [
                ".tmp", ".temp", ".bak", ".old", ".cache", ".swp", ".$$$"
            ],
            
            # Shortcut files
            "Shortcuts": [
                ".lnk", ".url", ".desktop", ".webloc"
            ],
            
            # Virtual machine files
            "Virtual Machines": [
                ".vdi", ".vmdk", ".iso", ".img", ".vhd", ".vhdx", ".ova",
                ".ovf", ".qcow", ".qcow2"
            ],
            
            # Disk image files
            "Disk Images": [
                ".iso", ".img", ".dmg", ".toast", ".nrg", ".cue", ".bin",
                ".mdf", ".mds"
            ],
            
            # Email files
            "Email": [
                ".eml", ".msg", ".pst", ".ost", ".mbox"
            ],
            
            # Calendar files
            "Calendar": [
                ".ics", ".ical", ".ifb", ".icalendar"
            ],
            
            # Contact files
            "Contact": [
                ".vcf", ".vcard"
            ],
            
            # Security certificate files
            "Certificates": [
                ".crt", ".cer", ".pem", ".p12", ".pfx", ".p7b", ".p7c"
            ],
            
            # Catch-all category for files that don't fit elsewhere
            "Other": []
        }

    # ==================== FILE SCANNING ====================
    
    def scan_files(self, root_path, exclude_extensions=None):
        """
        Scan files in a directory using BFS (Breadth-First Search) algorithm.
        
        Args:
            root_path (str): The directory path to scan
            exclude_extensions (set): Set of file extensions to skip (e.g., {'.mp3', '.exe'})
        
        Yields:
            dict: Information about each file found, containing:
                - path: Full path to the file
                - name: Just the filename
                - size: File size in bytes
                - mtime: Last modified time (timestamp)
                - depth: How deep in the directory tree
        
        BFS Algorithm Explanation:
            Instead of diving deep into one folder at a time (DFS - Depth First Search),
            BFS explores level by level. This means it checks all items in the current
            folder before moving to subfolders.
        
        Example:
            For a structure like:
            Downloads/
                file1.txt
                Folder1/
                    file2.txt
            
            BFS would check in this order:
            1. Downloads/file1.txt
            2. Downloads/Folder1/
            3. Downloads/Folder1/file2.txt
        """
        # Convert to absolute path (full path from root drive)
        root_path = os.path.abspath(root_path)
        
        # Check if the path exists
        if not os.path.exists(root_path):
            raise FileNotFoundError(f"Path not found: {root_path}")

        # Convert to set for faster lookup (O(1) instead of O(n))
        exclude_extensions = set(exclude_extensions or [])
        
        # Initialize queue with starting path and depth 0
        # deque = double-ended queue, efficient for adding/removing from both ends
        q = deque([(root_path, 0)])

        # Continue while there are items in the queue
        while q:
            # Remove and get the first item from queue (FIFO - First In First Out)
            cur_path, depth = q.popleft()

            try:
                # Get file/directory statistics
                stat = os.lstat(cur_path)
            except Exception as e:
                # If we can't access the file, print warning and skip it
                print(f"Warning: cannot stat {cur_path}: {e}", file=sys.stderr)
                continue

            # Check if current path is a file
            if os.path.isfile(cur_path):
                # Split filename into name and extension
                _, ext = os.path.splitext(cur_path)
                
                # Skip if extension is in exclusion list
                if ext.lower() not in exclude_extensions:
                    # Yield (return) file information as a dictionary
                    yield {
                        "path": cur_path,
                        "name": os.path.basename(cur_path),
                        "size": stat.st_size,
                        "mtime": stat.st_mtime,
                        "depth": depth,
                    }

            # Check if current path is a directory
            elif os.path.isdir(cur_path):
                try:
                    # Scan directory contents efficiently
                    with os.scandir(cur_path) as it:
                        # Sort entries alphabetically (case-insensitive)
                        entries = sorted(list(it), key=lambda e: e.name.lower())

                    # Add each entry to the queue
                    for entry in entries:
                        try:
                            # Skip symbolic links to avoid infinite loops
                            if not entry.is_symlink():
                                # Add to queue with increased depth
                                q.append((entry.path, depth + 1))
                        except Exception as e:
                            print(f"Warning: error checking {entry.path}: {e}", file=sys.stderr)

                except PermissionError:
                    # User doesn't have permission to access this folder
                    print(f"Warning: permission denied: {cur_path}", file=sys.stderr)
                except Exception as e:
                    # Other errors while scanning directory
                    print(f"Warning: error scanning directory {cur_path}: {e}", file=sys.stderr)

    def get_excluded_extensions(self):
        """
        Get list of excluded extensions based on which checkboxes are checked.
        
        Returns:
            list: List of file extensions to exclude from operations
        
        This function checks which file type checkboxes are selected in the UI
        and returns all the extensions that should be excluded from scanning.
        
        Example:
            If "Audio" checkbox is checked, returns ['.mp3', '.wav', '.flac', ...]
        """
        # Get all file categories
        categories = self.get_file_extension_categories()
        
        # Map each checkbox variable to its corresponding extensions
        exclusion_map = [
            (self.exclude_audio, categories["Audio"]),
            (self.exclude_code, categories["Code"]),
            (self.exclude_compressed, categories["Archives"]),
            (self.exclude_configuration, categories["Configuration"]),
            (self.exclude_database, categories["Databases"]),
            (self.exclude_document, categories["Documents"]),
            (self.exclude_ebook, categories["E-Books"]),
            (self.exclude_executable, categories["Executables"]),
            (self.exclude_font, categories["Fonts"]),
            (self.exclude_image, categories["Images"]),
            (self.exclude_presentation, categories["Presentations"]),
            (self.exclude_shortcuts, categories["Shortcuts"]),
            (self.exclude_spreadsheets, categories["Spreadsheets"]),
            (self.exclude_video, categories["Video"]),
            (self.exclude_virtual, categories["Virtual Machines"]),
            (self.exclude_system, categories["System"]),
            (self.exclude_temp, categories["Temporary"])
        ]

        # Collect all excluded extensions
        excluded = []
        for var, extensions in exclusion_map:
            # If checkbox is checked (True), add its extensions to excluded list
            if var.get():
                excluded.extend(extensions)

        return excluded

    # ==================== TREEVIEW DISPLAY ====================
    
    def populate_treeview(self, file_items=None):
        """
        Populate the treeview widget with file data.
        
        Args:
            file_items (list, optional): List of file dictionaries to display.
                                        If None, uses self.file_data
        
        The treeview is the table-like widget that shows all the files
        with columns for #, File Name, Date Modified, File Type, and Size.
        """
        # Clear all existing items from treeview
        for item in self.file_treeview.get_children():
            self.file_treeview.delete(item)

        # Use provided file_items or default to stored file_data
        if file_items is None:
            file_items = self.file_data

        # Add each file as a row in the treeview
        for i, file in enumerate(file_items, 1):  # Start counting from 1
            # Convert Unix timestamp to readable date format
            date_modified = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file["mtime"]))
            
            # Extract file extension
            _, ext = os.path.splitext(file["name"])
            file_type = ext.lstrip(".") if ext else ""  # Remove the dot from extension

            # Convert file size to human-readable format
            size = file["size"]
            if size < 1024:  # Less than 1 KB
                size_str = f"{size} B"
            elif size < 1024 * 1024:  # Less than 1 MB
                size_str = f"{size/1024:.1f} KB"
            elif size < 1024 * 1024 * 1024:  # Less than 1 GB
                size_str = f"{size/1024/1024:.1f} MB"
            else:  # 1 GB or more
                size_str = f"{size/1024/1024/1024:.2f} GB"

            # Insert row into treeview
            self.file_treeview.insert("", "end", values=(i, file["name"], date_modified, file_type, size_str))

    # ==================== SORTING ====================
    
    def sort_file_data(self):
        """
        Sort the file data based on the currently selected sort option.
        
        This function modifies self.file_data in place by sorting it
        according to the user's selection in the dropdown menu.
        
        Sort options include:
        - By name (A-Z or Z-A)
        - By date modified (newest/oldest first)
        - By file type (A-Z or Z-A)
        - By size (largest/smallest first)
        """
        # Get the currently selected sort option
        option = self.sort_option.get()
        
        # Sort based on the selected option
        if option == "File Name (A-Z)":
            # Sort alphabetically by name (case-insensitive)
            self.file_data.sort(key=lambda x: x["name"].lower())
        elif option == "File Name (Z-A)":
            # Sort reverse alphabetically
            self.file_data.sort(key=lambda x: x["name"].lower(), reverse=True)
        elif option == "Date Modified (Newest-Oldest)":
            # Sort by modification time, newest first
            self.file_data.sort(key=lambda x: x["mtime"], reverse=True)
        elif option == "Date Modified (Oldest-Newest)":
            # Sort by modification time, oldest first
            self.file_data.sort(key=lambda x: x["mtime"])
        elif option == "File Type (A-Z)":
            # Sort by file extension alphabetically
            self.file_data.sort(key=lambda x: os.path.splitext(x["name"])[1].lower())
        elif option == "File Type (Z-A)":
            # Sort by file extension reverse alphabetically
            self.file_data.sort(key=lambda x: os.path.splitext(x["name"])[1].lower(), reverse=True)
        elif option == "Size (Largest-Smallest)":
            # Sort by file size, largest first
            self.file_data.sort(key=lambda x: x["size"], reverse=True)
        elif option == "Size (Smallest-Largest)":
            # Sort by file size, smallest first
            self.file_data.sort(key=lambda x: x["size"])

    # ==================== DUPLICATE DETECTION ====================
    
    def hash_file(self, path, chunk_size=8192):
        """
        Compute SHA-256 hash of a file to identify duplicates.
        
        Args:
            path (str): Path to the file
            chunk_size (int): Size of chunks to read (8KB default)
        
        Returns:
            str: Hexadecimal hash string, or None if error
        
        Hash Explanation:
            A hash is like a unique fingerprint for a file. Even if two files
            have different names but identical content, they'll have the same hash.
            SHA-256 produces a 64-character hexadecimal string.
        
        Why read in chunks?
            Large files can't be loaded entirely into memory. Reading in chunks
            (8KB at a time) allows us to hash files of any size efficiently.
        """
        # Initialize SHA-256 hash object
        h = hashlib.sha256()
        
        try:
            # Open file in binary read mode
            with open(path, "rb") as f:
                # Read file in chunks until EOF (End Of File)
                while chunk := f.read(chunk_size):
                    # Update hash with this chunk
                    h.update(chunk)
        except Exception as e:
            # If we can't read the file, print error and return None
            print(f"Warning: cannot read {path}: {e}", file=sys.stderr)
            return None
        
        # Return hash as hexadecimal string
        return h.hexdigest()

    # ==================== BUTTON EVENT HANDLERS ====================
    
    def choose_target_path(self):
        """
        Open a dialog to choose target directory and scan its files.
        
        This function is called when the user clicks "Choose Path" button
        next to the Target File Path field.
        
        Steps:
        1. Show directory selection dialog
        2. Update the target path entry field
        3. Scan all files in the selected directory
        4. Sort and display the files
        """
        # Open directory selection dialog
        path = filedialog.askdirectory(title="Select Target Directory")
        
        # Only proceed if user selected a directory (didn't cancel)
        if path:
            # Clear and update the target path entry field
            self.target_path.delete(0, tk.END)
            self.target_path.insert(0, path)
            
            # Scan files with current exclusions, convert generator to list
            self.file_data = list(self.scan_files(path, self.get_excluded_extensions()))
            
            # Sort the files based on current sort option
            self.sort_file_data()
            
            # Display files in the treeview
            self.populate_treeview()

    def choose_destination_path(self):
        """
        Open a dialog to choose destination directory for sorted files.
        
        This function is called when the user clicks "Choose Path" button
        next to the Destination File Path field.
        
        Validation:
        - Destination cannot be the same as target path
        """
        # Open directory selection dialog
        path = filedialog.askdirectory(title="Select Destination Directory")
        
        # Get current target path for validation
        target = self.target_path.get()

        # Check if destination is same as target (not allowed)
        if path == target:
            messagebox.showerror("Invalid Destination", "Target and destination paths cannot be the same.")
        elif path:  # User selected a path and didn't cancel
            # Clear and update the destination path entry field
            self.destination_path.delete(0, tk.END)
            self.destination_path.insert(0, path)

    def clear_paths(self):
        """
        Clear all paths and reset the treeview.
        
        This function is called when the user clicks "Clear Selected Paths" button.
        It resets the application to its initial state.
        """
        # Clear target path entry
        self.target_path.delete(0, tk.END)
        
        # Clear destination path entry
        self.destination_path.delete(0, tk.END)
        
        # Clear stored file data
        self.file_data = []
        
        # Clear the treeview display
        self.populate_treeview()

    def on_sort_changed(self, event=None):
        """
        Handle sort option change event.
        
        Args:
            event: Event object from the combobox (not used but required by tkinter)
        
        This function is called automatically when the user selects
        a different option from the sort dropdown menu.
        """
        # Only sort if there's data to sort
        if self.file_data:
            # Apply the new sort
            self.sort_file_data()
            
            # Refresh the display
            self.populate_treeview()

    def delete_duplicates(self):
        """
        Find and delete duplicate files based on content (hash).
        
        Algorithm:
        1. Scan all files in target directory
        2. Calculate hash for each file
        3. Keep track of seen hashes
        4. If a hash is seen again, it's a duplicate
        5. Ask user for confirmation
        6. Delete all duplicates
        7. Log the action
        8. Refresh the display
        """
        # Get target path from entry field
        target = self.target_path.get()
        
        # Validate target path
        if not target or not os.path.exists(target):
            messagebox.showerror("Error", "Please select a valid target path.")
            return

        # Scan all files in target directory
        file_items = list(self.scan_files(target, self.get_excluded_extensions()))
        
        # Dictionary to store first occurrence of each hash
        # Key: hash, Value: file path
        seen_hashes = {}
        
        # List to store paths of duplicate files
        duplicates = []

        # Check each file
        for file in file_items:
            # Calculate file hash
            file_hash = self.hash_file(file["path"])
            
            # Skip if hash calculation failed
            if file_hash is None:
                continue
            
            # Check if we've seen this hash before
            if file_hash in seen_hashes:
                # This is a duplicate! Add to duplicates list
                duplicates.append(file["path"])
            else:
                # First time seeing this hash, record it
                seen_hashes[file_hash] = file["path"]

        # No duplicates found
        if not duplicates:
            messagebox.showinfo("Delete Duplicates", "No duplicate files found.")
            return

        # Ask user for confirmation before deleting
        confirm = messagebox.askyesno(
            "Delete Duplicates",
            f"{len(duplicates)} duplicate files found. Do you want to delete them?"
        )
        
        # User clicked "No", cancel operation
        if not confirm:
            return

        # Delete confirmed duplicates
        deleted_files = []
        for dup_path in duplicates:
            try:
                # Attempt to delete the file
                os.remove(dup_path)
                deleted_files.append(dup_path)
            except Exception as e:
                # If deletion fails, print warning but continue
                print(f"Warning: cannot delete {dup_path}: {e}", file=sys.stderr)

        # Show success message
        messagebox.showinfo("Delete Duplicates", f"Deleted {len(deleted_files)} duplicate files.")
        
        # Log this action
        self.log_action("Delete Duplicates", f"Deleted from: {target}", len(deleted_files))

        # Refresh the file list
        self.file_data = list(self.scan_files(target, self.get_excluded_extensions()))
        self.sort_file_data()
        self.populate_treeview()

    def delete_selected(self):
        """
        Delete files that the user has selected in the treeview.
        
        Steps:
        1. Get selected rows from treeview
        2. Map selected rows to actual file paths
        3. Ask for confirmation
        4. Delete confirmed files
        5. Log the action
        6. Refresh display
        """
        # Get IDs of selected items in treeview
        selected_items = self.file_treeview.selection()
        
        # Check if any files are selected
        if not selected_items:
            messagebox.showinfo("Delete Selected", "No files selected.")
            return

        # Build list of indices for selected files
        selected_indices = []
        for item in selected_items:
            # Get row values (first value is the index number)
            values = self.file_treeview.item(item, "values")
            # Convert to 0-based index (display starts at 1)
            selected_indices.append(int(values[0]) - 1)

        # Get actual file paths from stored data
        file_paths = [self.file_data[i]["path"] for i in selected_indices if i < len(self.file_data)]

        # Check if we found any valid paths
        if not file_paths:
            messagebox.showinfo("Delete Selected", "No valid files found to delete.")
            return

        # Ask for confirmation
        confirm = messagebox.askyesno(
            "Delete Selected",
            f"{len(file_paths)} file(s) selected. Do you want to delete them?"
        )
        
        # User clicked "No", cancel
        if not confirm:
            return

        # Delete confirmed files
        deleted_files = []
        for path in file_paths:
            try:
                os.remove(path)
                deleted_files.append(path)
            except Exception as e:
                print(f"Warning: cannot delete {path}: {e}", file=sys.stderr)

        # Show success message
        messagebox.showinfo("Delete Selected", f"Deleted {len(deleted_files)} file(s).")
        
        # Log the action
        self.log_action("Delete Selected", f"Deleted from: {self.target_path.get()}", len(deleted_files))

        # Refresh file list
        target = self.target_path.get()
        self.file_data = list(self.scan_files(target, self.get_excluded_extensions()))
        self.sort_file_data()
        self.populate_treeview()

    def sort_files(self):
        """
        Sort files into destination folders by file type.
        
        Algorithm:
        1. Validate paths
        2. Scan all files in target directory
        3. For each file:
           - Determine its category based on extension
           - Create category folder if needed
           - Copy file to category folder
           - Handle duplicate filenames by adding numbers
        4. Log the action
        5. Show success message
        
        Example:
            Target: C:/Downloads
            Destination: D:/Organized
            
            Files:
                song.mp3 -> D:/Organized/Audio/song.mp3
                photo.jpg -> D:/Organized/Images/photo.jpg
                document.pdf -> D:/Organized/PDFs/document.pdf
        """
        # Get paths from entry fields
        target = self.target_path.get()
        destination = self.destination_path.get()

        # Validate target path
        if not target or not os.path.exists(target):
            messagebox.showerror("Error", "Please select a valid target path.")
            return

        # Validate destination path
        if not destination or not os.path.exists(destination):
            messagebox.showerror("Error", "Please select a valid destination path.")
            return

        # Ensure target and destination are different
        if target == destination:
            messagebox.showerror("Error", "Target and destination paths cannot be the same.")
            return

        # Scan all files in target directory
        file_items = list(self.scan_files(target, self.get_excluded_extensions()))

        # Check if there are files to sort
        if not file_items:
            messagebox.showinfo("Sort Files", "No files found to sort.")
            return

        # Ask for confirmation before proceeding
        confirm = messagebox.askyesno(
            "Sort Files",
            f"Found {len(file_items)} files to sort. Continue?"
        )
        
        # User clicked "No", cancel
        if not confirm:
            return

        # Get all file categories and their extensions
        categories = self.get_file_extension_categories()

        # Counter for successfully sorted files
        sorted_count = 0
        
        # Process each file
        for file in file_items:
            # Extract file extension
            _, ext = os.path.splitext(file["name"])
            ext = ext.lower()  # Convert to lowercase for comparison

            # Find which category this file belongs to
            category = "Other"  # Default category
            for cat, extensions in categories.items():
                if ext in extensions:
                    category = cat
                    break

            # Create category folder in destination
            # Example: D:/Organized/Audio
            category_path = os.path.join(destination, category)
            os.makedirs(category_path, exist_ok=True)  # Create folder if it doesn't exist

            # Build destination file path
            dest_file = os.path.join(category_path, file["name"])
            
            # Handle duplicate filenames by adding numbers
            # If "song.mp3" exists, try "song_1.mp3", then "song_2.mp3", etc.
            if os.path.exists(dest_file):
                # Split filename into base name and extension
                base, extension = os.path.splitext(file["name"])
                counter = 1
                
                # Keep incrementing counter until we find an unused filename
                while os.path.exists(dest_file):
                    dest_file = os.path.join(category_path, f"{base}_{counter}{extension}")
                    counter += 1

            try:
                # Copy file to destination (preserves metadata like timestamps)
                shutil.copy2(file["path"], dest_file)
                sorted_count += 1
            except Exception as e:
                # If copy fails, print warning but continue with other files
                print(f"Warning: cannot copy {file['path']}: {e}", file=sys.stderr)

        # Show success message
        messagebox.showinfo("Sort Files", f"Successfully sorted {sorted_count} files into {destination}")
        
        # Log this action
        self.log_action("Sort Files", f"From: {target} -> To: {destination}", sorted_count)

    # ==================== LOGS VIEWER ====================
    
    def view_logs(self):
        """
        View application logs in a new window.
        
        Creates a popup window displaying all logged actions in a table format.
        Shows timestamp, action type, details, and number of files affected.
        """
        # Check if log file exists
        if not os.path.exists(self.logs_file):
            messagebox.showinfo("Logs", "No logs available yet.")
            return

        # Create new top-level window (popup)
        logs_window = tk.Toplevel(self)
        logs_window.title("Sortify Logs")
        logs_window.geometry("800x500")

        # Define columns for the logs table
        columns = ("Timestamp", "Action", "Details", "Files Count")
        
        # Create treeview widget to display logs
        logs_tree = ttk.Treeview(logs_window, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            logs_tree.heading(col, text=col)

        # Set column widths
        logs_tree.column("Timestamp", width=150)
        logs_tree.column("Action", width=150)
        logs_tree.column("Details", width=350)
        logs_tree.column("Files Count", width=100)

        # Add vertical scrollbar
        scrollbar = ttk.Scrollbar(logs_window, orient="vertical", command=logs_tree.yview)
        logs_tree.configure(yscrollcommand=scrollbar.set)

        # Pack widgets
        logs_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Load and display log entries
        try:
            with open(self.logs_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                
                # Insert each log entry as a row
                for row in reader:
                    logs_tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load logs: {e}")