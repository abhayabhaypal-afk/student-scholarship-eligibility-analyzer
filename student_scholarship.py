import pandas as pd

CSV_FILE = "students.csv"


def load_students():
    """Load and validate the student CSV file."""
    try:
        df = pd.read_csv(CSV_FILE, dtype=str)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
        return pd.DataFrame()

    required = ["Name", "Marks", "Income", "Attendance"]
    missing_columns = [col for col in required if col not in df.columns]

    if missing_columns:
        print("Missing CSV columns:", ", ".join(missing_columns))
        return pd.DataFrame()

    valid_rows = []

    for _, row in df.iterrows():
        name = str(row["Name"]).strip()

        if not name:
            print("Invalid name. Row skipped.")
            continue

        try:
            marks = float(str(row["Marks"]).strip())
        except (ValueError, TypeError):
            print(f"Invalid marks for {name}: '{row['Marks']}'. Row skipped.")
            continue

        try:
            income = float(str(row["Income"]).strip())
        except (ValueError, TypeError):
            print(f"Invalid income for {name}: '{row['Income']}'. Row skipped.")
            continue

        try:
            attendance = float(str(row["Attendance"]).strip())
        except (ValueError, TypeError):
            print(f"Invalid attendance for {name}: '{row['Attendance']}'. Row skipped.")
            continue

        if pd.isna(marks) or pd.isna(income) or pd.isna(attendance):
            print(f"Missing value for {name}. Row skipped.")
            continue

        valid_rows.append(
            {
                "Name": name,
                "Marks": marks,
                "Income": income,
                "Attendance": attendance,
            }
        )

    return pd.DataFrame(valid_rows)


def calculate_eligibility(df):
    """Apply eligibility and scholarship rules."""
    if df.empty:
        return df

    df = df.copy()

    df["Eligible"] = (
        (df["Attendance"] >= 75)
        & (df["Marks"] >= 75)
        & (df["Income"] <= 500000)
    )

    def scholarship(row):
        if not row["Eligible"]:
            return "Not Eligible"
        if row["Marks"] >= 90 and row["Income"] <= 300000:
            return "Full"
        return "Partial"

    df["Scholarship"] = df.apply(scholarship, axis=1)

    def amount(row):
        if row["Scholarship"] == "Full":
            return 50000
        if row["Scholarship"] == "Partial":
            return 25000
        return 0

    df["Amount"] = df.apply(amount, axis=1)

    return df


def display_eligibility(df):
    """Display each student's eligibility result."""
    for _, row in df.iterrows():
        if row["Scholarship"] == "Not Eligible":
            print(f"{row['Name']} | Not Eligible")
        else:
            print(f"{row['Name']} | {row['Scholarship']} | Rs. {int(row['Amount'])}")


def show_summary(df):
    """Display scholarship summary."""
    eligible_count = int(df["Eligible"].sum())
    not_eligible_count = len(df) - eligible_count
    full_count = int((df["Scholarship"] == "Full").sum())
    partial_count = int((df["Scholarship"] == "Partial").sum())
    total_amount = int(df["Amount"].sum())

    eligible_marks = df.loc[df["Eligible"], "Marks"]
    average_marks = eligible_marks.mean() if not eligible_marks.empty else 0

    print(f"(a) Eligible: {eligible_count} | Not Eligible: {not_eligible_count} | "
          f"Full: {full_count} | Partial: {partial_count}")
    print(f"Total scholarship: Rs. {total_amount}")
    print(f"Average marks (eligible): {average_marks:.2f}")


def filter_by_marks(df):
    """Filter students using a minimum marks value."""
    while True:
        try:
            minimum = float(input("Enter minimum marks: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    filtered = df[df["Marks"] >= minimum]

    if filtered.empty:
        print("No students found.")
        return

    for _, row in filtered.iterrows():
        print(f"{row['Name']} | {row['Marks']:.0f}")


def main():
    students = load_students()

    if students.empty:
        print("No valid student records found.")
        return

    students = calculate_eligibility(students)

    while True:
        print("\n===== Student Scholarship Eligibility Analyzer =====")
        print("1. Show Eligibility")
        print("2. Summary")
        print("3. Filter by Minimum Marks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_eligibility(students)

        elif choice == "2":
            show_summary(students)

        elif choice == "3":
            filter_by_marks(students)

        elif choice == "4":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
