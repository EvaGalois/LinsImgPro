# humanseg = hub.Module( name="deeplabv3p_xception65_humanseg" )
# result = humanseg.segmentation( data={"image": [tmp_png_file_name]} )


import os
import sys
import paddlehub as hub
import cv2

# 加载模型
module = hub.Module(name = "deeplabv3p_xception65_humanseg")
results = module.segmentation(images=[cv2.imread('./inputImgs/test.jpg')])
# result = module.segmentation(paths='./inputImgs/test.jpg')

print(results[0]['data'].shape)