from docx import Document
from docx.shared import RGBColor
from docx.text.run import Run
from docx.oxml.text.run import CT_R
import random
import mmap
import array
import sys

def encode_run(run, col):
    run.font.color.rgb = RGBColor(col[0], col[1], col[2])

def decode_run(run, col):
    rgb = run.font.color.rgb
    col[0] = rgb[0]
    col[1] = rgb[1]
    col[2] = rgb[2]
    #print("decode_run: ", col)

def build_c_run(c, para, run):
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

COLOR_MAGIC = bytearray([ord('L'), ord('E'), ord('H'), ord('A')])

class color_encoder:
    def __init__(self, path):
        self.fh = open(path, 'rb')
        self.mm = mmap.mmap(self.fh.fileno(), 0, access=mmap.ACCESS_READ)
        self.ba = bytearray(self.mm)
        self.ba_ind = 0
        self.hdr = bytearray()
        self.hdr.extend(COLOR_MAGIC)
        self.hdr.extend(len(self.ba).to_bytes(4, 'little'))
        self.hdr_ind = 0

    def __del__(self):
        self.mm.close()
        self.fh.close()

    def encode(self, col):
        b = 0
        if self.hdr_ind < len(self.hdr):
            b = self.hdr[self.hdr_ind]
            self.hdr_ind += 1
        elif self.ba_ind < len(self.ba):
            b = self.ba[self.ba_ind]
            self.ba_ind += 1
        else:
            return False
        #print("color_encoder: ", b)
        for i in range(3):
            col[i] = (col[i] & ~0x7) | (b & 0x7)
            b = b >> 3
        return True

class color_decoder:
    def __init__(self, path):
        self.fh = open(path, 'wb')
        self.ba = bytearray()
        self.hdr = bytearray()
        self.hdr_accepted = False

    def __del__(self):
        self.fh.close()

    def decode(self, col):
        b = 0
        for i in reversed(range(3)):
            b = b << 3
            b = b | (col[i] & 0x7)
        b = b & 0xff
        #print("color_decoder: ", b)
        if not self.hdr_accepted:
            self.hdr.append(b)
            if len(self.hdr) == len(COLOR_MAGIC) + 4:
                if self.hdr[0:len(COLOR_MAGIC)] != COLOR_MAGIC:
                    print("Magic check failed, file does not contain encrypted data")
                    sys.exit("Decoder failed")
                self.data_len = int.from_bytes(self.hdr[4:], 'little')
                self.hdr_accepted = True
            return True
        if len(self.ba) < self.data_len:
            #print("data: len, sz: ", len(self.ba), self.data_len)
            self.ba.append(b)
            return True
        return False

    def save(self):
        self.fh.write(self.ba)
        self.ba.clear()


