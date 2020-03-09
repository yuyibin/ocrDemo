import sys
sys.path.append("D:/ocr/CHINESE-OCR/ctpn/lib/utils")
import bbox
import cython_nms

try:
    from . import gpu_nms
except:
    gpu_nms = cython_nms
