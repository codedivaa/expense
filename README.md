# 💰 Smart Expense Tracker

A simple command-line Expense Tracker built with Python that helps users record and manage daily expenses. The application stores data locally using JSON and provides basic spending analysis features.

## 📖 Overview

Smart Expense Tracker is a beginner-friendly Python project designed to practice:

* File Handling
* JSON Data Storage
* Functions
* Loops and Conditional Statements
* Data Processing

Users can add expenses, view saved records, calculate total spending, and analyze expenses by category through an interactive menu-driven interface.

---

## ✨ Features

* Add new expenses
* View all recorded expenses
* Calculate total spending
* View category-wise spending
* Store data permanently using JSON
* Easy-to-use command-line interface

---

## 🛠️ Technologies Used

* Python 3
* JSON
* File Handling

---

## 📂 Project Structure

```text
expense/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/codedivaa/expense.git
cd expense
```

Run the application:

```bash
python expense_tracker.py
```

---

## 🚀 Usage

When the program starts, the following menu is displayed:

```text
===== SMART EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Total Spending
4. Category Spending
5. Exit
```

### Add Expense

```text
Enter expense name: Groceries
Enter amount: 1200
Enter category: Food
```

### View Expenses

```text
1. Groceries | ₹1200 | Food
2. Bus Fare | ₹100 | Transport
```

### Total Spending

```text
Total Spending: ₹1300
```

### Category Spending

```text
Food: ₹1200
Transport: ₹100
```

---

## 🔄 Program Workflow

```text
Start Program
      │
      ▼
Load Expenses
      │
      ▼
Display Menu
      │
      ├── Add Expense
      ├── View Expenses
      ├── Total Spending
      ├── Category Spending
      └── Exit
```

---

## 🎯 Future Improvements

* Edit Expenses
* Delete Expenses
* Search Expenses
* Monthly Reports
* Expense Charts and Graphs
* SQLite Database Integration
* GUI Version using Tkinter

---

## 👨‍💻 Author

GitHub: https://github.com/codedivaa

---

⭐ If you found this project useful, consider giving it a star.
