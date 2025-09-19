# Basic File Operations
with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("We are practicing Python file operations.\n")

with open("sample.txt", "a") as f:
    f.write("This is an appended line.\n")

with open("sample.txt", "r") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)

print(f"Total lines: {line_count}")
print(f"Total words: {word_count}")
