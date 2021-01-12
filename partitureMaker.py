from io import open

txt = open("c:/temp/inputs.txt", "r")
dictionaries = []
while True:
    # read line
    line = txt.readline()
    if not line:
        break
    
    # discard lines with 'note_off'
    if line.startswith('note_off'):
        continue
    
    # create a dictionary for each line
    dictionary = {}
    dictionaries.append(dictionary) 

    # trim 'note_on' and the trailing EOL from the line 
    line = line[8:-1]
    
    # split into substrings by key-value
    lineparts = line.split(' ')
    
    # extract the values from line and add them to the dictionary (as int or float)
    for linepart in lineparts:
        if linepart.startswith('channel'):
            dictionary['channel'] = int(linepart[8:])
        elif linepart.startswith('note'):
            dictionary['note'] = int(linepart[5:])
        elif linepart.startswith('velocity'):
            dictionary['velocity'] = int(linepart[9:])
        elif linepart.startswith('time'):
            dictionary['time'] = float(linepart[5:])   
        
txt.close()

for dictionary in dictionaries:
    # print the dictionary
    print(dictionary)
    # print only the note
    print('note -> '+str(dictionary['note']))
