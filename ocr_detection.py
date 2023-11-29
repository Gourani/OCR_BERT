import pytesseract 
from tkinter import Tk , filedialog 
from PIL import Image
root = Tk()

root.withdraw()

def extract_text_from_pdf() :
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract'

    img_path = filedialog.askopenfile()
    img = Image.open(img_path.name)
    text = pytesseract.image_to_string(img) 

    return text

t = extract_text_from_pdf()
print(t)