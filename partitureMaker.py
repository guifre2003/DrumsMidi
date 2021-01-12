from io import open
import re

txt = open("inputs.txt", "r")

lines = {}
line_num = 1
while True:
    # read line
    line = txt.readline()
    if not line:
        break
    matches = re.match('note_on', line)
    if matches:
        lines[line_num] = line
        line_num += 1
txt.close()
print(lines)

total_lines_num = len(lines)
lines_num = 1
note_search = r'\w+note\w+'
while lines_num <= total_lines_num:
    notes = re.match(note_search, lines[lines_num])
    if notes:
        print(notes)
    lines_num += 1