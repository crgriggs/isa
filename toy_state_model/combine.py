#!/usr/bin/env python
import sys, os

def append_file(f, filename):
    """Writes file "filename" to file descriptor f."""
    f.write("(*----- " + filename + " -----*)\n")
    f.write(open(filename).read())
    f.write('\n')

def main():

    if len(sys.argv) == 2:
        propType = sys.argv[1]
    else:
        print "Enter folder that handles current property"
        return -1

    if not os.path.isdir("./" + str(propType)):
        print str(propType) + "is not a folder in the current directory"
        return -1

    f = open("state.ucl", 'w+')
    try:
        append_file(f, "header.txt")
        for filename in os.listdir("./" + str(propType)):
            if filename.endswith(".txt"):
                append_file(f, "./" + str(propType)+"/"+filename)
        append_file(f, "state.txt")
        append_file(f, "control.txt")
    except:
        f.close()
        raise

    return 0

if __name__ == "__main__":
    sys.exit(main())
