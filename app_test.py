from PIL import Image
import pytesseract

# Open the image
image = Image.open("images/img1_ocr.jpg")  # Replace "your_image.jpg" with the path to your image file
# text = pytesseract.image_to_string(image, lang='eng', config="--psm 1 --oem 3")
# Use pytesseract to extract text from the image
for i in range(3, 4):
  try:
    text = pytesseract.image_to_string(image, lang='eng', config=f"--psm {6} --oem 3")
    # Print the extracted text
    print(f"Extracted Text for {i}:", text.strip())
  except:
    print(f"error for {i}")