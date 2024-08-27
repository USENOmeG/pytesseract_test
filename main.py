from PIL import Image
import cv2
import pytesseract

# Load the image (画像を開く)
source_image = cv2.imread('image/tesse_image6.png')

# Label (品番)
label_box = (220, 196, 325, 220)
# IP (IPアドレス), Image1, Image6のみ
ip_box = (185, 275, 390, 600)
# Flag (フラグ), Image1, Image6のみ
flag_box = (425, 275, 550, 600)

# Define the region of interest (クロップ範囲を選択)
crop_area = ip_box

# Crop the image to the ROI (指定したエリアをクロップ)
cropped_image = source_image[crop_area[1]
    :crop_area[3], crop_area[0]:crop_area[2]]

# Convert to grayscale (画像を灰色に変える)
gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

# Increase contrast (コントラストを変更)
alpha = 1.5
beta = 0
contrasted_image = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

# Apply thresholding　(画像をシンプルに)
_, threshold_img = cv2.threshold(
    contrasted_image, 190, 190, cv2.THRESH_BINARY_INV)

# OCR with Tesseract (文字認識)
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(
    threshold_img, config=custom_config, lang='eng')

print(text)

if __name__ == '__main__':
    pass
