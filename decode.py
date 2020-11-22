import target_color

def decode(doc_path, data_path):
    def decode_loop():
        for para in document.paragraphs:
            for run in para.runs:
                for c in run.text:
                    target_color.decode_run(run, col)
                    if not cd.decode(col):
                        return

    cd = target_color.color_decoder(data_path)
    col = bytearray([0, 0, 0])
    document = target_color.Document(doc_path)
    decode_loop()
    cd.save()

import sys

decode(sys.argv[1], sys.argv[2])
