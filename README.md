# 🔍 Suspicious File Scanner – Python Semester Project

## 🧠 Overview

This project was developed as part of a final semester assignment in a Software Engineering program at the Technion.  
It is a **Python-based system that scans a user-selected folder**, identifies suspicious files based on various criteria (filename, extension, size), and provides tools to manage them.  
The system is fully menu-driven and includes logging, exception handling, user interaction, and persistent storage of "safe files."

---

## ⚙️ Features

- 📂 **Folder scanning**: Lists all files in a selected directory and collects key metadata (name, extension, size).
- 🛡️ **Suspicious file detection**: Based on:
  - File name matches suspicious names list
  - File extension in suspicious extensions list
  - File size exceeds 10MB
- 📝 **Logging**: Generates a `.log` file with suspicious files info, including a Unix timestamp and salt in the filename.
- ✅ **Safe files management**: Mark files to be ignored in future scans.
- 📊 **Statistics view**: Displays stats on the most recent scan (e.g., file count, largest/smallest file, number of suspicious files).
- 🗑️ **Delete suspicious files**: Allows selective deletion of suspicious files after user confirmation.
- ❌ **Robust error handling**: Handles invalid input, file system issues, and access restrictions.

---

## 🧩 Technologies Used

- Python 3.x
- `os` – file system interaction
- `datetime` – timestamps
- `random` / `secrets` – salt generation
- `json` / `txt` – storing lists and log output
- Exception handling and modular programming

---

Follow the menu prompts to:

Scan a folder

Detect suspicious files

Mark files as safe

View statistics

Delete suspicious files

Exit safely

## 👨‍💻 Author

Neo Zino

Student, Software Engineering – Technion

📧 neozi2014@gmail.com

## 📌 Notes

This project was completed individually as part of an academic course.

All code is written in Python and organized into clean, modular files.

Documentation is included inside each module and function for clarity and maintainability.
