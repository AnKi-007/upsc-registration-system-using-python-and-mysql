# upsc-registration-system-using-python-and-mysql
A simple Python-based UPSC Registration System using MySQL for storing and retrieving candidate information.
# UPSC Registration System using Python and MySQL

This is a terminal-based UPSC Registration System built using **Python** and **MySQL**. It allows users to securely log in, register for UPSC exams, and view registration details based on their registration number.

## 🔧 Features

- Secure login for users
- Input and store candidate registration details
- Retrieve and display registration data using reg. no
- Uses MySQL for data storage
- Modular structure with DB configuration

## 🛠 Technologies Used

- Python 3
- MySQL
- MySQL Connector (Python)

## 📂 Project Structure

project/
│
├── db_config.py # Database connection module
├── login_info (MySQL Table) # Stores usernames and passwords
├── registration_information # Main table for candidate data
├── main.py # Main application file


## 🚀 Getting Started

1. Clone the repo or download the source code.
2. Set up your MySQL server and update credentials in `db_config.py`.
3. Run the project:
   ```bash
   python main.py

🧑‍💻 Author
Anand Kishore – GitHub


---

## ✅ .gitignore for Python Projects

Create a `.gitignore` file with the following content to exclude unnecessary files:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Environment variables
.env

# Distribution / packaging
build/
dist/
*.egg-info/

# IDE specific files
.vscode/
.idea/

# OS generated files
.DS_Store
Thumbs.db
