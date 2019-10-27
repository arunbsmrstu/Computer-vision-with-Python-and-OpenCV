# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:41:26 2019

@author: Arun Biswas
"""

import cv2
import numpy as np
input =cv2.imread("images/input.jpg");
cv2.imshow('Input Image',input)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(input.shape)
