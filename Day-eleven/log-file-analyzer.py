def analyze_logs():
    error_count = 0
    warning_count = 0

    with open("log.txt", "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

    print(f"❌ Errors: {error_count}")
    print(f"⚠️ Warnings: {warning_count}")

analyze_logs()