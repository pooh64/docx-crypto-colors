import target_color 
import sys

if len(sys.argv) != 4:
  print("Invalid input, to run try: python3 encode.py target.docx in.data crypto.docx")
else :
  target_color.encode(sys.argv[1], sys.argv[2], sys.argv[3])
