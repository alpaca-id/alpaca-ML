import cv2
import pytesseract
from gtts import gTTS
from PIL import Image
from playsound import playsound
from IPython.display import Audio

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img1 = cv2.imread(
    'C:/Users/user/Documents/AI/image/083656400_1462936078-Ini_Budi_edit_1.jpg')

data1 = pytesseract.image_to_data(img1)

text = pytesseract.image_to_string(img1)

for z, a in enumerate(data1.splitlines()):
    # Counter
    if z != 0:
        # Converts 'data1' string into a list stored in 'a'
        a = a.split()
        # Checking if array contains a word
        if len(a) == 12:
            # Storing values in the right variables
            x, y = int(a[6]), int(a[7])
            w, h = int(a[8]), int(a[9])
            # Display bounding box of each word
            cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)
            # Display detected word under each bounding box
            cv2.putText(img1, a[11], (x - 15, y),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
    # Output the bounding box with the image
    cv2.imshow('Image output', img1)
    cv2.waitKey(0)
