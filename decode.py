import target_color
import sys
import os

if len(sys.argv) != 4:
    print("usage: <cmd> crypto.docx out.data")
    sys.exit(1)

tmp_dir  = "/tmp/docx-colors/"
data_enc = tmp_dir + "data.enc"
key_enc  = tmp_dir + "key.bin.enc"
key      = tmp_dir + "key.bin"
os.system("mkdir -p "+tmp_dir)

target_color.decode(sys.argv[1], data_enc)

dataLen = str(os.path.getsize(data_enc) - 128)

os.system("tail -c 128 "+data_enc+" >"+key_enc)
os.system("truncate -s "+dataLen+" "+data_enc)

os.system("openssl rsautl -decrypt -inkey "+sys.argv[3]+" -in "+key_enc+" -out "+key)
os.system("openssl enc -d -aes-256-cbc -pbkdf2 -in "+data_enc+" -out "+sys.argv[2]+" -pass file:"+key)

os.system("rm -rf "+tmp_dir)
