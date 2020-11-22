import target_color
import sys

if len(sys.argv) != 3 :
  print("Invalid input, to run try: python3 decode.py crypto.docx out.data")
target_color.decode(sys.argv[1], sys.argv[2])
