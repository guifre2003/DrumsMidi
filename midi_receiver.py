import time
import mido
import sys

# port_name = 'USB MIDI Interface 0'
port_name = 'USB MIDI Interface:USB MIDI Interface MIDI 1 20:0'
file1 = open('inputs.txt', 'w')

# Comprobem que haguem escrit el nom del port be y que el USB estigui connectat.
if not port_name in mido.get_input_names():
    raise Exception("No es troba el port '{port_name}' a la llista de ports d'entrada disponibles: {ports}")

# Aqui comenca realment el programa.
tempo = int(input("What BPM do you want?"))
milisecond_tempo = 60 / tempo * 1000
input_port = mido.open_input(port_name)
print(milisecond_tempo)
start = time.time()
timer = 0
while timer < 250:
    # El while acabarà als 10 segons.
    for msg in input_port.iter_pending():
        end = time.time()
        msg.time = ((end - start) * 1000)
        
        if msg.time < 0.5:
            msg.time = int(msg.time - ((end - start) * 1000) % (milisecond_tempo / 8))
        else:
            msg.time = int(msg.time - ((end - start) * 1000) % (milisecond_tempo / 8)) + milisecond_tempo
        # El mòdul serveix per quantitzar (ara esta a fusas, una quarta part de negra).
        file1.write(str(msg) + '\n')
        print(msg)
    time.sleep(0.02)
    timer += 1
file1.close()

sys.exit()
