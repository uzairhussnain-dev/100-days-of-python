import csv

def analyze_csv():
    total_salary = 0
    count = 0

    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            salary = int(row["salary"])
            total_salary += salary
            count += 1

    avg_salary = total_salary / count

    print(f"📊 Total Employees: {count}")
    print(f"💰 Average Salary: {avg_salary}")

analyze_csv()