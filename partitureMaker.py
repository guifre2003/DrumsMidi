from io import open

# instrument = input("Introdueix l'instrument ('bateria' o  'piano')")
# "c:/temp/inputs.txt"
txt = open("/home/guifre2003/Desktop/tr/virtualEnv/trLinux/inputs.txt", "r")
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
    values_line = line[8:-1]
    line = line[:-1]
    
    # split into substrings by key-value
    lineparts = line.split(' ')
    values_linepart = values_line.split(' ')

    # extract the values from line and add them to the dictionary (as int or float)
    for linepart in lineparts:
        if linepart.startswith('note_on'):
            for values_linepart in values_line:
                if values_linepart.startswith('channel'):
                    dictionary['channel'] = int(values_linepart[8:])
                elif values_linepart.startswith('note='):
                    dictionary['note'] = int(values_linepart[5:])
                elif values_linepart.startswith('velocity'):
                    dictionary['velocity'] = int(values_linepart[9:])
                elif values_linepart.startswith('time'):
                    dictionary['time'] = float(values_linepart[5:])   
txt.close()

for dictionary in dictionaries:
    # print the dictionary
    print(dictionary)
