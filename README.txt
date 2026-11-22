# Student Scholarship Eligibility Analyzer

PS No.: 76

## Project
Student Scholarship Eligibility Analyzer using Python 3 and Pandas.

## Files
- `student_scholarship.py` - main Python program
- `students.csv` - input dataset
- `README.txt` - project instructions

## Scholarship Rules
A student is eligible when:
- Attendance >= 75
- Marks >= 75
- Income <= 500000

Eligible students receive:
- Full scholarship: Rs. 50000 when Marks >= 90 AND Income <= 300000
- Otherwise Partial scholarship: Rs. 25000

## How to Run in VS Code

1. Install Python 3.
2. Install Pandas:
   `pip install pandas`
3. Keep `student_scholarship.py` and `students.csv` in the same folder.
4. Open the folder in VS Code.
5. Run:
   `python student_scholarship.py`

## Menu
1. Show Eligibility
2. Summary
3. Filter by Minimum Marks
4. Exit
