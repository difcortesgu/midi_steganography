# MIDI Velocity Steganography Tool
A Python-based command-line interface (CLI) tool designed to conceal and retrieve secret text messages within MIDI files. This tool utilizes LSB (Least Significant Bit) Steganography applied specifically to the velocity values of MIDI note events.

## 🛠 Features
Invisible Encoding: Modifies the velocity of notes by a maximum of 1 unit, making the change virtually indistinguishable to the human ear.

Automatic File Management: Automatically generates output filenames (e.g., song_hidden.mid) to prevent overwriting originals.

Easy CLI: Simple sub-commands for hiding and reading messages.

## 🚀 Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/midi-stego.git
cd midi-stego
```

Install dependencies:
This tool requires the mido library to parse MIDI files.

```bash
pip install mido
```

## 📖 Usage
The tool uses a sub-command structure (hide or read).

1. Hiding a Message
To hide a message, provide the source MIDI file and the text string. The tool will create a new file with the _hidden suffix.

```Bash
python main.py hide -f "your_song.mid" -m "This is a secret message"
```
    
-f, --file: Path to the input .mid file.

-m, --message: The text you wish to conceal.

2. Reading a Message
To extract a hidden message from a modified MIDI file:

```Bash
python main.py read -f "your_song_hidden.mid"
```

## 🔬 How it Works
The MIDI Velocity Byte
In the MIDI protocol, a Note On message contains a velocity value ranging from 0 to 127 (7 bits).

LSB Substitution
The tool iterates through each note in the MIDI file and modifies the Least Significant Bit of its velocity to match a bit from your message.

Original Velocity: 80 (Binary: 1010000)

Message Bit to hide: 1

New Velocity: 81 (Binary: 1010001)

Since a change of 1 in velocity is a microscopic change in volume/intensity, the musical integrity of the file remains intact while acting as a carrier for data.

## ⚠️ Requirements
Python 3.6+

mido library

Input File: Must be a standard MIDI file (.mid).

Capacity: The length of your message is limited by the number of Note events available in the MIDI file.
