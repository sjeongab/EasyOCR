import easyocr
import numpy as np
import cv2

#print(cv2.__version__)
r = easyocr.Reader(['ko','en'], gpu=False)
print(r.readtext('5.png'))
