#!/usr/bin/env python
import sys, os

INSTRUCTION_FOLDER = os.path.join(os.path.dirname(__file__), "instructions")

def append_file(f, filename):
    """Writes file "filename" to file descriptor f."""
    f.write("/-- File: " + filename + " --/\n")
    f.write(open(filename).read())
    f.write('\n')

def main():

    if len(sys.argv) == 2:
        instruction_folder = sys.argv[1]
    else:
        instruction_folder = INSTRUCTION_FOLDER
    if not os.path.isdir("./" + str(instruction_folder)):
        print str(instruction_folder) + "is not a folder in the current directory"

    with open("model.smv", 'w+') as f:

        # All files in instructions/
        for filename in os.listdir(instruction_folder):
            if filename.endswith(".smv"):
                append_file(f, os.path.join(instruction_folder, filename))

        append_file(f, "main.smv")

if __name__ == "__main__":
    main()
