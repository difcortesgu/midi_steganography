import mido
import os

def string_to_binary(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def binary_to_string(binary):
    return ''.join(chr(int(binary[i : i+8], 2)) for i in range(0, len(binary), 8))

def hide_message(message, input_filename):

    name, ext = os.path.splitext(input_filename)
    output_filename = f"{name}_hidden{ext}"

    midi_in = mido.MidiFile(input_filename)
    midi_out = mido.MidiFile(type=midi_in.type, ticks_per_beat=midi_in.ticks_per_beat)

    binary_message = string_to_binary(message)
    total = len(binary_message)

    index = 0
    capacity = 0

    for track in midi_in.tracks:
        new_track = mido.MidiTrack()

        for msg in track:

            if msg.type == 'note_on' and msg.velocity > 0:
                if index < total:
                    if (msg.velocity % 2 != int(binary_message[index])):
                        if msg.velocity == 1:
                            msg.velocity += 1
                        else:
                            msg.velocity -= 1

                index += 1
                capacity += 1

            new_track.append(msg)
        midi_out.tracks.append(new_track)

    print(f"Capacity = {capacity}")
    print(f"Message Length = {total}")

    if index < total:
        print(f"¡Advertencia! El MIDI es muy corto. Solo se ocultaron {index} bits.")
    else:
        midi_out.save(output_filename)
        print(f"Mensaje oculto con éxito en {output_filename}")

def read_message(filename):
    midi = mido.MidiFile(filename)

    binary_message = ""

    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0:
                binary_message += str(msg.velocity % 2)

    message = binary_to_string(binary_message)

    return message