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
        if lineparts.index('note_on'):
            switch = 'on'
            if linepart.startswith('channel'):
                channel = int(linepart[8:])
            elif linepart.startswith('note='):
                note = int(linepart[5:])
            elif linepart.startswith('velocity'):
                velocity = int(linepart[9:])
            elif linepart.startswith('time'):
                time = float(linepart[5:])
        elif lineparts.index('note_off') in lineparts and linepart.startswith('note='):
            # thing_index = thing_list.index(elem) if elem in thing_list else -1
            print('funciona!!!')
    print(switch, channel, note, velocity, time)
txt.close()

for dictionary in dictionaries:
    # print the dictionary
    print(dictionary)
