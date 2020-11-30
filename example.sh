#!/bin/sh
set -x

rm -rf test
mkdir -p test

openssl genrsa -out test/id_rsa.pem 1024
openssl rsa -in test/id_rsa.pem -outform PEM -pubout -out test/id_rsa.pub.pem

python3 encode.py target/target.docx target/random.data test/crypto.docx test/id_rsa.pub.pem
python3 decode.py test/crypto.docx test/orig.data test/id_rsa.pem
diff target/random.data test/orig.data
