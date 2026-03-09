import argparse
import os
import sys
from midi_steganography import read_message, hide_message

def main():
    parser = argparse.ArgumentParser(description="MIDI Steganography Tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # 'hide' command setup
    hide_parser = subparsers.add_parser("hide", help="Hide a message in a MIDI file")
    hide_parser.add_argument("-f", "--file", required=True, help="The source MIDI file")
    hide_parser.add_argument("-m", "--message", required=False, help="The secret message to hide")

    # 'read' command setup
    read_parser = subparsers.add_parser("read", help="Read a message from a MIDI file")
    read_parser.add_argument("-f", "--file", required=True, help="The MIDI file to decode")

    args = parser.parse_args()

    if args.command == "hide":
        if not os.path.exists(args.file):
            print(f"Error: The file '{args.file}' was not found.")
            return
        
        message = args.message

        # Capture from pipe if -m is missing
        if not message and not sys.stdin.isatty():
            message = sys.stdin.read().strip()

        if not message:
            print("Error: Message is required via -m or pipe (|)")
            return

        hide_message(message, args.file)

    elif args.command == "read":
        if not os.path.exists(args.file):
            print(f"Error: The file '{args.file}' was not found.")
            return

        decoded = read_message(args.file)
        print(f"[*] Decoded Message: {decoded}")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()