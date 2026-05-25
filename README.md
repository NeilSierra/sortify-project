# Sortify - File Sorter & Duplicate Finder

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)

A powerful desktop application designed to help you organize your files efficiently and eliminate duplicate files. Built with Python and Tkinter, it provides an intuitive graphical interface for managing large collections of files across your computer.

![Sortify Logo](src/images/sortify-logo.png)

## ✨ Features

### 📁 File Sorting
- Automatically organizes files into **30+ categories** (Audio, Video, Images, Documents, Code, Archives, etc.)
- Smart handling of duplicate filenames (adds numerical suffixes)
- Preserves original file metadata and timestamps
- Scans subdirectories recursively using BFS algorithm

### 🔍 Duplicate Detection
- Identifies exact duplicates based on file content (not just name)
- Uses **SHA-256 cryptographic hashing** for accuracy
- Batch deletion of duplicate files
- Keeps first occurrence, removes subsequent duplicates

### 🎯 File Management
- Delete selected files directly from the interface
- Preview files before taking action
- Sort and filter file lists by name, date, type, or size
- Exclude specific file types from operations

### 💻 User Interface
- Clean, intuitive layout with sidebar controls
- Real-time file table with 5-column display
- Checkbox-based file type exclusions
- Confirmation dialogs for destructive operations

### 📊 Logging & Tracking
- CSV-based activity logging
- Tracks timestamps, actions, and affected file counts
- Built-in log viewer
- Persistent operation history

## 🖥️ System Requirements

- **Operating System:** Windows 7/8/10/11, macOS 10.12+, or Linux
- **Python:** Version 3.7 or higher
- **RAM:** 2 GB minimum (4 GB recommended for large file operations)
- **Storage:** 50 MB free space for application
- **Display:** 1024x768 resolution minimum (1920x1080 recommended)

## 📦 Installation

### Method 1: Using the Executable (Windows)

1. Download the latest release from the [Releases](../../releases) page
2. Extract the ZIP file
3. Navigate to the `src` folder
4. Double-click `Sortify.exe`

> **Note:** Windows may show a SmartScreen warning for unsigned applications. Click "More info" then "Run anyway" to proceed.

### Method 2: Running from Source (All Platforms)

1. Clone this repository:
```bash
git clone https://github.com/yourusername/sortify.git
cd sortify
```

2. Install required dependencies:
```bash
pip install Pillow
```

3. Run the application:
```bash
cd src
python main.py
```

## 🚀 Quick Start Guide

### Basic Workflow

**1. Select Target Directory**
- Click "Choose Path" next to "Target File Path"
- Select the folder you want to organize or scan for duplicates
- Files will be scanned and displayed in the main table

**2. Configure Exclusions (Optional)**
- Check boxes for file types you want to exclude from operations
- Example: Exclude "System Files" to avoid touching OS files

**3. Choose Your Action**

#### Option A - Sort Files:
1. Click "Choose Path" next to "Destination File Path"
2. Select where you want organized files to go
3. Click "Sort Selected Files"
4. Confirm the operation
5. Files will be copied to destination, organized by type

#### Option B - Delete Duplicates:
1. Click "Find and Delete Duplicate Files"
2. Review the number of duplicates found
3. Confirm deletion
4. Duplicate files will be permanently removed

#### Option C - Delete Selected Files:
1. Click on files in the table to select them (Ctrl+Click for multiple)
2. Click "Delete Selected"
3. Confirm deletion

**4. View Results**
- Check the confirmation message for operation summary
- View "Logs" to see detailed history of actions

## ⚠️ Important Safety Notes

- **DELETE OPERATIONS ARE PERMANENT** - Files are not sent to Recycle Bin
- Always verify target and destination paths before sorting
- Test on a small sample folder first to familiarize yourself
- Consider backing up important files before bulk operations
- Review duplicate file list carefully before deleting

## 📂 Project Structure

```
sortify/
│
├── docs/
│   └── Sortify Documentation.docx      # Detailed technical documentation
│
├── src/                                # Main application directory
│   ├── images/                         # Application graphics
│   │   ├── sortify-logo.ico            # Window icon
│   │   └── sortify-logo.png            # UI logo
│   │
│   ├── package/                        # Core application modules
│   │   ├── functions.py                # Business logic and file operations
│   │   └── widgets.py                  # User interface components
│   │
│   ├── main.py                         # Application entry point
│   └── Sortify.exe                     # Compiled Windows executable
│
├── test/
│   └── Test Cases.mp4                  # Video demonstration
│
└── README.md                           # This file
```

## 📋 Supported File Categories

Sortify organizes files into **30+ intelligent categories**:

### Media Files
- **Audio:** mp3, wav, flac, aac, ogg, m4a, wma, and 12+ more formats
- **Video:** mp4, mkv, avi, mov, flv, wmv, webm, and 14+ more formats
- **Images:** jpg, png, gif, bmp, svg, webp, psd, and 13+ more formats

### Documents
- **Documents:** txt, doc, docx, rtf, md, odt, pages, and more
- **PDFs:** pdf files (separate category due to high usage)
- **Spreadsheets:** xls, xlsx, csv, ods, numbers, and more
- **Presentations:** ppt, pptx, odp, key, and more
- **E-Books:** epub, mobi, azw, fb2, and more

### Development
- **Code:** py, js, java, c, cpp, html, css, php, and 30+ more languages
- **Configuration:** json, xml, yaml, ini, cfg, and more
- **Scripts:** sh, bash, bat, ps1, vbs, ahk
- **Databases:** db, sql, sqlite, mdb, and more

### System & Utilities
- **Archives:** zip, rar, 7z, tar, gz, and 14+ more formats
- **Executables:** exe, msi, app, apk, jar, and more
- **System:** dll, sys, log, bak, and more
- **Temporary:** tmp, cache, old, bak, swp

### Specialized Categories
- Fonts, 3D Models, CAD, Virtual Machines, Email, Certificates, and more!

Click "More Info" in the application to see the complete list.

## 🔧 Technical Details

### Algorithms

**Breadth-First Search (BFS):**
- Used for directory traversal and file scanning
- Explores directory tree level-by-level
- Predictable memory usage
- Handles deep directory structures efficiently

**SHA-256 Hashing:**
- Cryptographic hash function for duplicate detection
- Creates unique 64-character fingerprint for each file
- Chunk-based reading (8KB chunks) for memory efficiency

**File Categorization:**
- Extension-based classification system
- 30+ predefined categories with 200+ extensions
- Case-insensitive matching
- Fallback to "Other" category for unknown types

### Architecture

**Multiple Inheritance Design:**
- `SortifyApp` inherits from `tk.Tk`, `SortifyWidgets`, and `SortifyFunctions`
- Separates UI (widgets.py) from logic (functions.py)
- Modular structure for easy maintenance

**Performance Considerations:**
- Generator-based scanning for memory efficiency
- Chunk-based file reading to handle large files
- Set-based exclusion checking for O(1) lookup time
- Minimal file loading (stats only, not full content)

## 🐛 Troubleshooting

<details>
<summary><strong>Application won't start</strong></summary>

- Ensure Python 3.7+ is installed (if running from source)
- Install required dependencies: `pip install Pillow`
- Check that all files in the package folder are present
- Try running from command line to see error messages
</details>

<details>
<summary><strong>"Permission Denied" errors when scanning</strong></summary>

- Run the application as Administrator (Windows) or with sudo (Linux/Mac)
- Ensure you have read permissions for the target directory
- Avoid scanning system-protected folders like C:/Windows
</details>

<details>
<summary><strong>Duplicate detection not finding duplicates</strong></summary>

- Duplicate detection is based on file CONTENT, not name
- Files must be binary-identical to be considered duplicates
- Check that file type exclusions aren't hiding duplicates
</details>

<details>
<summary><strong>Application freezing with large file collections</strong></summary>

- Scanning thousands of files may take time - be patient
- Close other applications to free up system resources
- Consider scanning smaller directory sections separately
- For very large operations (50,000+ files), increase system RAM
</details>

## 📊 Logging

Sortify maintains a detailed CSV log file of all operations:

- **Location:** Same directory as the application
- **Filename:** `sortify_logs.csv`
- **Contents:** Timestamp, Action, Details, Files Count

Click the "Logs" button in the application to view all logged activities in a sortable table format.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Tkinter for cross-platform compatibility
- Uses Pillow (PIL) for image handling
- Icons and graphics created for Sortify

## ⚖️ Disclaimer

This software is provided "as is" without warranty of any kind. Users are responsible for backing up important data before performing file operations. The authors are not liable for any data loss or system issues arising from the use of this application.

## 📞 Support

- **Issues:** Report bugs via [GitHub Issues](../../issues)
- **Documentation:** See `docs/Sortify Documentation.docx`
- **Demo:** Watch `test/Test Cases.mp4` for a video demonstration

---

**Made with ❤️ using Python and Tkinter**
