# !usr/bin/env python
# -*- coding:utf-8 -*-

"""
 Description  :
 Version      : 1.0
 Author       : huzhenhong
 Date         : 2022-03-28 15:21:56
 LastEditors  : huzhenhong
 LastEditTime : 2022-04-05 17:17:31
 FilePath     : \\FormatAndCommit\\main.py
 Copyright (C) 2022 huzhenhong. All rights reserved.
"""

import cv2

img= cv2.imread("circle.png")

img=  cv2.resize(img, (256, 256)) 
cv2.imshow("origin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


replicate = cv2.copyMakeBorder(img, 20, -20, 20, 20, cv2.BORDER_REPLICATE)
cv2.imshow("replicate", replicate)
cv2.waitKey()
cv2.destroyAllWindows()
