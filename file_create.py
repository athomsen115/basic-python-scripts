#!/usr/bin/env python3.8

def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a filename. ")

    file_name = input("Destination file name: ").strip()
    return file_name or get_file_name(True)

file_name = get_file_name()

print(f"Please enter file content. If you enter an empty line, it will write the content to {file_name}:\n")

with open(file_name, 'w') as f:
    eof = False
    lines = []

    while not eof:
        line = input()
        if line.strip():
            lines.append(f"{line}\n")
        else:
            eof = True

    f.writelines(lines)
    print(f"Lines written to {file_name}")
