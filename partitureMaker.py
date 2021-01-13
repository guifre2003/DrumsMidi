from io import open

# get the filePath
filePath = input('FilePath: ')
#filePath = 'c:/temp/inputs.txt';
#filePath = '/home/guifre2003/Desktop/tr/virtualEnv/trLinux/inputs.txt';

txt = open(filePath, "r")
dictionaries = []
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
    for linepart in lineparts:
        if linepart.startswith('note_'):
            on = linepart[5:] == 'on'
        elif linepart.startswith('channel'):
            channel = int(linepart[8:])
        elif linepart.startswith('note'):
            note = int(linepart[5:])
        elif linepart.startswith('velocity'):
            velocity = int(linepart[9:])
        elif linepart.startswith('time'):
            time = float(linepart[5:])   
    
    if on:
        # create a dictionary for 'note_on'
        dictionary = {}
        dictionary['channel'] = channel;
        dictionary['note'] = note;
        dictionary['velocity'] = velocity;
        dictionary['time'] = time;
        dictionaries.append(dictionary) 
    else:
        # look for the corresponding dictionary for 'note_off' line and set its duration
        for dictionary in reversed(dictionaries):
            if dictionary['channel'] == channel and dictionary['note'] == note:
                dictionary['duration'] = time-dictionary['time']
                break

        
txt.close()

for dictionary in dictionaries:
    # print the dictionary
    print(dictionary)
