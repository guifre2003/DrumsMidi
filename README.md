# trLinux

## IDE
  PyCharm

## Python Version
  3.8.3150.1013


## Llibreries
- Python Mido (Detecció de notes)
- Python-Rtmidi (gestió dels ports)

## Installation (Ubuntu 18.04 LTS - Native & VirtualEnv)

```
pip3 list --format columns
sudo apt-get install libasound2-dev (#include <alsa/asoundlib.h> error solution)
pip3 install python-rtmidi --install-option="--no-jack"
pip3 install mido
  
```

## Execution 

```
python3 midi_receiver.py
```