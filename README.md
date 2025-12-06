# sortify-project
A simple file sorting and duplicate finder.

================================================================================
                    SORTIFY - FILE SORTER & DUPLICATE FINDER
================================================================================

Version: 1.0
Author: [Your Name]
Last Updated: December 2025

================================================================================
TABLE OF CONTENTS
================================================================================

1. Overview
2. Features
3. System Requirements
4. Installation & Setup
5. How to Use
6. Project Structure
7. File Categories
8. Logging
9. Troubleshooting
10. Technical Details
11. License & Credits

================================================================================
1. OVERVIEW
================================================================================

Sortify is a powerful desktop application designed to help you organize your
files efficiently and eliminate duplicate files. Built with Python and Tkinter,
it provides an intuitive graphical interface for managing large collections of
files across your computer.

Key Capabilities:
- Automatic file sorting by type into organized folders
- Duplicate file detection using SHA-256 hashing
- Selective file type exclusion
- Comprehensive file preview and sorting options
- Activity logging for tracking all operations

================================================================================
2. FEATURES
================================================================================

FILE SORTING:
- Automatically organizes files into 30+ categories (Audio, Video, Images, 
  Documents, Code, Archives, etc.)
- Smart handling of duplicate filenames (adds numerical suffixes)
- Preserves original file metadata and timestamps
- Scans subdirectories recursively using BFS algorithm

DUPLICATE DETECTION:
- Identifies exact duplicates based on file content (not just name)
- Uses SHA-256 cryptographic hashing for accuracy
- Batch deletion of duplicate files
- Keeps first occurrence, removes subsequent duplicates

FILE MANAGEMENT:
- Delete selected files directly from the interface
- Preview files before taking action
- Sort and filter file lists by name, date, type, or size
- Exclude specific file types from operations

USER INTERFACE:
- Clean, intuitive layout with sidebar controls
- Real-time file table with 5-column display
- Checkbox-based file type exclusions
- Confirmation dialogs for destructive operations

LOGGING & TRACKING:
- CSV-based activity logging
- Tracks timestamps, actions, and affected file counts
- Built-in log viewer
- Persistent operation history

================================================================================
3. SYSTEM REQUIREMENTS
================================================================================

MINIMUM REQUIREMENTS:
- Operating System: Windows 7/8/10/11, macOS 10.12+, or Linux
- Python: Version 3.7 or higher (if running from source)
- RAM: 2 GB minimum (4 GB recommended for large file operations)
- Storage: 50 MB free space for application
- Display: 1024x768 resolution minimum (1920x1080 recommended)

REQUIRED PYTHON LIBRARIES (if running from source):
- tkinter (usually included with Python)
- PIL/Pillow (for image handling)
- Standard library: os, sys, csv, time, hashlib, shutil, collections, datetime

OPTIONAL:
- Administrator privileges (for accessing system-protected folders)

================================================================================
4. INSTALLATION & SETUP
================================================================================

METHOD 1: Using the Executable (Recommended for Windows users)
---------------------------------------------------------------
1. Navigate to the "src" folder
2. Double-click "Sortify.exe"
3. The application will launch immediately (no installation required)

Note: Windows may show a SmartScreen warning for unsigned applications.
Click "More info" then "Run anyway" to proceed.


METHOD 2: Running from Source Code (All platforms)
---------------------------------------------------
1. Ensure Python 3.7+ is installed on your system
2. Install required dependencies:
   
   pip install Pillow

3. Navigate to the "src" folder in your terminal/command prompt
4. Run the application:
   
   python main.py

5. The Sortify window will appear


FIRST RUN:
----------
On first launch, Sortify will automatically create a log file 
"sortify_logs.csv" in the application directory to track your operations.

================================================================================
5. HOW TO USE
================================================================================

BASIC WORKFLOW:
---------------

Step 1: SELECT TARGET DIRECTORY
   - Click "Choose Path" next to "Target File Path"
   - Select the folder you want to organize or scan for duplicates
   - Files will be scanned and displayed in the main table

Step 2: CONFIGURE EXCLUSIONS (Optional)
   - Check boxes for file types you want to exclude from operations
   - Examples: Exclude "System Files" to avoid touching OS files
              Exclude "Video" files if you only want to organize documents

Step 3: CHOOSE YOUR ACTION

   Option A - SORT FILES:
   1. Click "Choose Path" next to "Destination File Path"
   2. Select where you want organized files to go
   3. Click "Sort Selected Files"
   4. Confirm the operation
   5. Files will be copied to destination, organized by type

   Option B - DELETE DUPLICATES:
   1. Click "Find and Delete Duplicate Files"
   2. Review the number of duplicates found
   3. Confirm deletion
   4. Duplicate files will be permanently removed

   Option C - DELETE SELECTED FILES:
   1. Click on files in the table to select them (Ctrl+Click for multiple)
   2. Click "Delete Selected"
   3. Confirm deletion
   4. Selected files will be permanently removed

Step 4: VIEW RESULTS
   - Check the confirmation message for operation summary
   - View "Logs" to see detailed history of actions
   - The file table will automatically refresh


SORTING AND FILTERING:
-----------------------
Use the "Sorted by:" dropdown to organize your file list:
- File Name (A-Z / Z-A): Alphabetical sorting
- Date Modified: Newest or Oldest first
- File Type: Group by extension
- Size: Largest or Smallest first


VIEWING FILE INFORMATION:
--------------------------
Click "More Info" to see the complete reference guide of all supported
file extensions organized by category. This helps you understand which
folder each file type will be sorted into.


IMPORTANT SAFETY NOTES:
-----------------------
⚠ DELETE OPERATIONS ARE PERMANENT - Files are not sent to Recycle Bin
⚠ Always verify target and destination paths before sorting
⚠ Test on a small sample folder first to familiarize yourself
⚠ Consider backing up important files before bulk operations
⚠ Review duplicate file list carefully before deleting

================================================================================
6. PROJECT STRUCTURE
================================================================================

Project Folder/
│
├── docs/
│   └── Sortify Documentation.docx     # Detailed technical documentation
│
├── src/                                # Main application directory
│   ├── images/                         # Application graphics
│   │   ├── sortify-logo.ico          # Window icon
│   │   └── sortify-logo.png          # UI logo
│   │
│   ├── package/                        # Core application modules
│   │   ├── functions.py              # Business logic and file operations
│   │   └── widgets.py                # User interface components
│   │
│   ├── main.py                        # Application entry point
│   └── Sortify.exe                    # Compiled Windows executable
│
├── test/
│   └── Test Cases.mp4                 # Video demonstration of features
│
└── README.txt                          # This file


FILE DESCRIPTIONS:
------------------
main.py         - Initializes the application and main window
functions.py    - Contains all file scanning, sorting, and duplicate detection
widgets.py      - Creates the GUI layout and all interface elements
sortify_logs.csv - Auto-generated log file (created on first run)

================================================================================
7. FILE CATEGORIES
================================================================================

Sortify organizes files into 30+ intelligent categories:

MEDIA FILES:
- Audio: mp3, wav, flac, aac, ogg, m4a, wma, and 12+ more formats
- Video: mp4, mkv, avi, mov, flv, wmv, webm, and 14+ more formats
- Images: jpg, png, gif, bmp, svg, webp, psd, and 13+ more formats

DOCUMENTS:
- Documents: txt, doc, docx, rtf, md, odt, pages, and 3+ more
- PDFs: pdf files (separate category due to high usage)
- Spreadsheets: xls, xlsx, csv, ods, numbers, and 4+ more
- Presentations: ppt, pptx, odp, key, and 3+ more
- E-Books: epub, mobi, azw, fb2, and 6+ more

DEVELOPMENT:
- Code: py, js, java, c, cpp, html, css, php, and 30+ more languages
- Configuration: json, xml, yaml, ini, cfg, and 6+ more
- Scripts: sh, bash, bat, ps1, vbs, ahk
- Databases: db, sql, sqlite, mdb, and 6+ more

SYSTEM & UTILITIES:
- Archives: zip, rar, 7z, tar, gz, and 14+ more formats
- Executables: exe, msi, app, apk, jar, and 5+ more
- System: dll, sys, log, bak, and 5+ more
- Temporary: tmp, cache, old, bak, swp

SPECIALIZED:
- Fonts: ttf, otf, woff, woff2, and 3+ more
- 3D Models: obj, fbx, blend, stl, and 5+ more
- CAD: dwg, dxf, skp, and 3+ more
- Virtual Machines: iso, vmdk, vdi, vhd, and 6+ more
- Email: eml, msg, pst, ost, mbox
- Certificates: crt, cer, pem, p12, and 4+ more
- And many more specialized categories!

OTHER:
- Catch-all category for unrecognized file types

Click "More Info" in the application to see the complete list with all
extensions for each category.

================================================================================
8. LOGGING
================================================================================

Sortify maintains a detailed CSV log file of all operations:

LOG FILE LOCATION:
- Same directory as the application executable/script
- Filename: sortify_logs.csv

LOGGED INFORMATION:
- Timestamp: Exact date and time of operation
- Action: Type of operation (Sort Files, Delete Duplicates, Delete Selected)
- Details: Source and destination paths
- Files Count: Number of files affected

VIEWING LOGS:
Click the "Logs" button in the top-right corner of the main window to view
all logged activities in a sortable table format.

LOG FORMAT EXAMPLE:
Timestamp           | Action            | Details                    | Files Count
--------------------|-------------------|----------------------------|------------
2025-12-06 14:30:15 | Sort Files        | From: C:/Downloads ...     | 127
2025-12-06 14:45:22 | Delete Duplicates | Deleted from: C:/Docs      | 15
2025-12-06 15:10:08 | Delete Selected   | Deleted from: C:/Temp      | 3

You can open sortify_logs.csv in Excel or any spreadsheet application for
advanced analysis and reporting.

================================================================================
9. TROUBLESHOOTING
================================================================================

PROBLEM: Application won't start
SOLUTION: 
- Ensure Python 3.7+ is installed (if running from source)
- Install required dependencies: pip install Pillow
- Check that all files in the package folder are present
- Try running from command line to see error messages

PROBLEM: "Permission Denied" errors when scanning
SOLUTION:
- Run the application as Administrator (Windows) or with sudo (Linux/Mac)
- Ensure you have read permissions for the target directory
- Avoid scanning system-protected folders like C:/Windows

PROBLEM: Logo/icon not displaying
SOLUTION:
- Verify images exist in src/images/ folder
- Application will work without images, this is cosmetic only
- Check file names match exactly: sortify-logo.ico and sortify-logo.png

PROBLEM: Some files not being detected
SOLUTION:
- Check if file types are excluded in the checkbox options
- Uncheck relevant exclusion boxes to include those file types
- Some hidden/system files may require administrator access

PROBLEM: Duplicate detection not finding duplicates
SOLUTION:
- Duplicate detection is based on file CONTENT, not name
- Files must be binary-identical to be considered duplicates
- Check that file type exclusions aren't hiding duplicates

PROBLEM: Sorting operation creates strange folder names
SOLUTION:
- This is expected behavior - folders match category names
- Categories are predefined (Audio, Video, Images, etc.)
- Check "More Info" for complete category list

PROBLEM: Files disappearing or being deleted unexpectedly
SOLUTION:
- Sortify NEVER deletes files automatically
- All destructive operations require explicit confirmation
- Check sortify_logs.csv to see what operations were performed
- Deleted files do not go to Recycle Bin - they are permanently removed

PROBLEM: Application freezing with large file collections
SOLUTION:
- Scanning thousands of files may take time - be patient
- Close other applications to free up system resources
- Consider scanning smaller directory sections separately
- For very large operations (50,000+ files), increase system RAM

================================================================================
10. TECHNICAL DETAILS
================================================================================

ALGORITHMS USED:

Breadth-First Search (BFS):
- Used for directory traversal and file scanning
- Explores directory tree level-by-level
- More predictable memory usage than depth-first search
- Handles deep directory structures efficiently

SHA-256 Hashing:
- Cryptographic hash function for duplicate detection
- Creates unique 64-character fingerprint for each file
- Files with identical content produce identical hashes
- Chunk-based reading (8KB chunks) for memory efficiency

File Categorization:
- Extension-based classification system
- 30+ predefined categories with 200+ extensions
- Case-insensitive matching
- Fallback to "Other" category for unknown types

ARCHITECTURE:

Multiple Inheritance Design:
- SortifyApp inherits from tk.Tk, SortifyWidgets, and SortifyFunctions
- Separates UI (widgets.py) from logic (functions.py)
- Main class (main.py) coordinates all components
- Modular structure for easy maintenance and updates

Data Structures:
- deque: Double-ended queue for efficient BFS implementation
- Dictionaries: Fast O(1) lookup for hash checking and categorization
- Lists: File data storage and manipulation

Performance Considerations:
- Generator-based scanning (yield) for memory efficiency
- Chunk-based file reading to handle large files
- Set-based exclusion checking for O(1) lookup time
- Minimal file loading (stats only, not full content)

SECURITY NOTES:
- File operations are irreversible (no Recycle Bin)
- Hash collisions are theoretically possible but astronomically rare
- Application requires appropriate file system permissions
- No network communication or external data collection

================================================================================
11. LICENSE & CREDITS
================================================================================

SOFTWARE LICENSE:
This application is provided as-is for personal and educational use.

THIRD-PARTY LIBRARIES:
- Tkinter: Python's standard GUI library
- Pillow (PIL): Python Imaging Library for image handling
- Python Standard Library: os, sys, csv, hashlib, shutil, etc.

ACKNOWLEDGMENTS:
Built with Python and Tkinter for cross-platform compatibility.

DISCLAIMER:
This software is provided "as is" without warranty of any kind. Users are
responsible for backing up important data before performing file operations.
The authors are not liable for any data loss or system issues arising from
the use of this application.

================================================================================

For additional information, see:
- docs/Sortify Documentation.docx - Complete technical documentation
- test/Test Cases.mp4 - Video demonstration of features

Support: [Your contact information]
Website: [Your website]
GitHub: [Your repository URL]

================================================================================
                              END OF README
================================================================================