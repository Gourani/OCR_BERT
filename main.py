from transformers import pipeline
import pdf2image
import pytesseract
import pandas as pd
import os
from tqdm import tqdm
from transformers import pipeline
# Load the summarization pipeline
summarizer = pipeline("summarization", model="bert-base-uncased", tokenizer="bert-base-uncased")

filenames = os.listdir("data")
df = pd.DataFrame(columns=['filename','text_extraction',"text_summary"])



def extract_text_from_pdf(file_path) :
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

    # Convert PDF pages to images
    images = pdf2image.convert_from_path(file_path,poppler_path=r"C:\poppler-0.67.0_x86\poppler-0.67.0\bin",fmt='jpeg')

    # Loop through each image and extract text using OCR
    text = ""
    for i, image in enumerate(images):
        text += pytesseract.image_to_string(image) 

    return text


### start work 

for i, filename in tqdm(enumerate(filenames), total=len(filenames)):
    full_path = os.path.join("data", filename)
    text = extract_text_from_pdf(full_path)
    #
    # Generate a summary of the input text
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)  
    #
    df.loc[i] = [full_path, text,summary[0]['summary_text']]



df.to_csv('output.csv', index=False)






