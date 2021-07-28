# pdf_list_generation_with_qr_codes
Simple function that obtain header info and some raws to print plus some data to make it QR-coded.
dependencies:
#python 3.6 only because of fpdf
from fpdf import FPDF
import pyqrcode
import time
# also, it's important to mention that fpdf doesn support utf-8 by default, so this code also show an example how to add support of latin (Italian exactly) to fpdf with import of fonts- bold and normal, included.
