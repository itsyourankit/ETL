# 🐍 Python ETL Pipeline with MySQL

This project demonstrates how to build a simple **ETL (Extract, Transform, Load)** pipeline using Python. It extracts university data from an open API, transforms it to focus on universities in California, and loads it into a **MySQL database**.

---

## 🚀 Features

- Extract data from [Hipolabs University API](http://universities.hipolabs.com/)
- Transform: Filters for universities with "California" in their name
- Load: Writes the clean data into a MySQL table using SQLAlchemy + PyMySQL

---

## 🛠 Requirements

Make sure you have the following installed:

- Python 3.7+
- MySQL Server (e.g., MySQL Workbench)
- pip (Python package manager)

### Install Python dependencies:

pip install pandas sqlalchemy pymysql requests
