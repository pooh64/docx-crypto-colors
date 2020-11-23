import target_color
import sys

if len(sys.argv) != 3:
    print("usage: <cmd> crypto.docx out.data")
    sys.exit(1)

target_color.decode(sys.argv[1], sys.argv[2])
