from PIL import Image
import os
print(os.getcwd())
image_path = os.getcwd()+"\\media\\test\\test.jpg"
im = Image.open(image_path) # 이미지 불러오기
im.show() 
