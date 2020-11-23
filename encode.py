import target_color 
import sys

if len(sys.argv) != 4:
    print("usage: <cmd> target.docx in.data crypto.docx")
    sys.exit(1)

target_color.encode(sys.argv[1], sys.argv[2], sys.argv[3])
