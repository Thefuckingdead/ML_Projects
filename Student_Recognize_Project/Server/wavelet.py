import numpy as np
import pywt
import cv2

def w2d(img, mode='haar', level=1):
    imArray = img

    # Datatype conversion
    # Convert to gray scale
    imArray = cv2.cvtColor(imArray, cv2.COLOR_BGR2GRAY)
    # Convert to float
    imArray = np.float32(imArray)
    imArray = imArray / 255
    # Compute Coefficients
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    # Process Coefficients
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;

    # Reconstruction
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    return imArray_H