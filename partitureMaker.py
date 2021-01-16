from io import open
import ly

# get the filePath
filePath = input('FilePath: ')
# filePath = 'c:/temp/inputs.txt';
# filePath = '/home/guifre2003/Desktop/tr/virtualEnv/trLinux/inputs.txt';

NOTES_TABLE = {
    "38": "b'",
    "40": "b'",
    "36": "d'",
    "48": "e''",
    "45": "d'",
    "43": "f'",
    "51": "a''",
    "42": "g''",
    "55": "f''",
}

txt = open(filePath, "r")
midi_events = []
while True:
    # read line
    line = txt.readline()
    if not line:
        break

    # discard lines without 'note_'
    if line.startswith('note_') == False:
        continue

    # trim 'note_on' and the trailing EOL from the line 
    line = line[:-1]

    # split into substrings by key-value
    lineparts = line.split(' ')

    # extract the values from line (as boolean, int or float)
    is_note_on = False

    for linepart in lineparts:
        splitted_linepart = linepart.split('=')
        left = splitted_linepart[0]
        if len(splitted_linepart) > 1:
            right = splitted_linepart[1]
        else:
            right = None

        if linepart == 'note_on':
            is_note_on = True

        elif left == 'channel':
            channel = int(right)

        elif left == 'note':
            note = NOTES_TABLE[right]

        elif left == 'velocity':
            velocity = int(right)

        elif left == 'time':
            time = float(right)

    if is_note_on:
        # create a dictionary for 'note_on'
        midi_event = {
            'channel': channel,
            'note': note,
            'velocity': velocity,
            'time': time,
        }
        midi_events.append(midi_event)
    else:
        # look for the corresponding dictionary for 'note_off' line and set its duration
        for midi_event in reversed(midi_events):
            if midi_event['channel'] == channel and midi_event['note'] == note:
                midi_event['duration'] = time - midi_event['time']
                break

txt.close()


def template(pitch, duration):
    pdf.write()


for midi_event in midi_events:
    # print the dictionary
    print(midi_event)

pdf = open('notes.ly', 'a')
pdf.write("\\relative {\n" + "  \\time 4/4\n")
pdf.close()
