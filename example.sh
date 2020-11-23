#!/bin/sh
set -x

mkdir -p test
python3 encode.py target/target.docx target/random.data test/crypto.docx
python3 decode.py test/crypto.docx test/orig.data
diff target/random.data test/orig.data
