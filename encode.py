import target_color 

def encode(doc_path, data_path, out_path):
    ce = target_color.color_encoder(data_path)
    col = bytearray([0, 0, 0])
    document = target_color.Document(doc_path)
    done = False
    for para in document.paragraphs:
        if done:
            break
        for run in para.runs:
            if run.text == '':
                continue
            s = run.text
            run.text = ''
            for c in s: 
                c_run = target_color.build_c_run(c, para, run)
                done = not ce.encode(col)
                target_color.encode_run(c_run, col)
                run = c_run
    if ce.encode(col):
        print('Document is too small to contain entire data')
    document.save(out_path)

import sys
encode(sys.argv[1], sys.argv[2], sys.argv[3])
