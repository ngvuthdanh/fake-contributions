def generate_report(results):
    with open("vulnerability_report.txt", "w") as f:
        for result in results:
            f.write(result + "\n")
