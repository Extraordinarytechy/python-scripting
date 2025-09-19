import csv

# Create CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Suresh", 85])
    writer.writerow(["Ramesh", 90])
    writer.writerow(["Riya", 78])
    writer.writerow(["Pallavi", 92])

# Read CSV
scores = []
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        scores.append(int(row["Score"]))

average_score = sum(scores) / len(scores)
print("Scores:", scores)
print("Average Score:", average_score)
print("Max Score:", max(scores))
