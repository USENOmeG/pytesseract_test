import cv2
from PIL import Image
import pytesseract

'''
To check the coordinates (座標確認用)
'''

image = Image.open('image/tesse_image1.png')

# Specify the coordinates (left, upper, right, lower)
box = (185, 275, 390, 600)

# Crop the area of interest
cropped_image = image.crop(box)

# Perform OCR on the cropped area
text = pytesseract.image_to_string(cropped_image)

print(text)
