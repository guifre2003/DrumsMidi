from io import open

# instrument = input("Introdueix l'instrument ('bateria' o  'piano')")
# "c:/temp/inputs.txt"
txt = open("inputs.txt", "r")
dictionaries = []
while True:
    # read line
    line = txt.readline()
    if not line:
        break
    
    # discard lines with 'note_off'
    # if line.startswith('note_off'):
    #     continue

    # discard lines with no information
    if len(line) < 49:
        continue
    
    # create a dictionary for each line
    dictionary = {}
    dictionaries.append(dictionary) 

    # trim 'note_on' and the trailing EOL from the line 
    line = line[:-1]
    
    # split into substrings by key-value
    lineparts = line.split(' ')
    
    # extract the values from line and add them to the dictionary (as int or float)
    for linepart in lineparts:
        if line.startswith('note_on'):
            if linepart.startswith('channel'):
                dictionary['channel'] = int(linepart[8:])
            elif linepart.startswith('note'):
                dictionary['note'] = int(linepart[5:])
            elif linepart.startswith('velocity'):
                dictionary['velocity'] = int(linepart[9:])
            elif linepart.startswith('time'):
                dictionary['time'] = float(linepart[5:])
        elif line.startswith('note_off'):
            print(dictionaries.index)
txt.close()

for dictionary in dictionaries:
    # print the dictionary
    print(dictionary)
    # print only the note
    print('note -> '+str(dictionary['note']))