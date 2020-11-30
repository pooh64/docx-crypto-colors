import target_color 
import sys
import os

if len(sys.argv) != 5:
    print("usage: <cmd> target.docx in.data crypto.docx public_rsa_key.pem")
    sys.exit(1)

tmp_dir  = "/tmp/docx-colors/"
data_enc = tmp_dir + "data.enc"
key_enc  = tmp_dir + "key.bin.enc"
key      = tmp_dir + "key.bin"
os.system("mkdir -p "+tmp_dir)

os.system("openssl rand -base64 32 >"+key)
os.system("openssl rsautl -encrypt -inkey "+sys.argv[4]+" -pubin -in "+key+" -out "+key_enc)
os.system("openssl enc -aes-256-cbc -salt -pbkdf2 -in "+sys.argv[2]+" -out "+data_enc+" -pass file:"+key)
os.system("cat "+key_enc+" >> "+data_enc)

target_color.encode(sys.argv[1], data_enc, sys.argv[3])

os.system("rm -rf "+tmp_dir)
