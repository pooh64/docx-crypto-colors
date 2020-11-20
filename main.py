from docx import Document
from docx.shared import RGBColor
from docx.text.run import Run
from docx.oxml.text.run import CT_R
import random

def encode_run(run):
    c_r = random.randint(0, 255)
    c_g = random.randint(0, 255)
    c_b = random.randint(0, 255)
    run.font.color.rgb = RGBColor(c_r, c_g, c_b)

def build_c_run(c, run):
    c_run_el = para._element._new_r()
    run._element.addnext(c_run_el)
    c_run = Run(c_run_el, run._parent)
    c_run.text = c
    c_run.style = run.style
    c_run.italic = run.italic
    c_run.bold = run.bold
    c_run.underline = run.underline
    c_run.font.name = run.font.name
    c_run.font.size = run.font.size
    return c_run


document = Document('target.docx')
for para in document.paragraphs:
    for run in para.runs:
        if run.text == '':
            continue
        s = run.text
        run.text = ''
        for c in s: 
            c_run = build_c_run(c, run)
            encode_run(c_run)
            run = c_run

document.save('out.docx')
