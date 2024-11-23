from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import os


def preprocess_image(image_path):
    image = Image.open(image_path)
    
    gray_image = image.convert('L')
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2)  

    enhanced_image = enhanced_image.filter(ImageFilter.SHARPEN)
    
    return enhanced_image

def perform_ocr(image):
    text = pytesseract.image_to_string(image)
    return text

def save_text_to_file(text, output_path):
    with open(output_path, 'w') as file:
        file.write(text)

def main(image_path, output_text_path):
    try:
       
        processed_image = preprocess_image(image_path)

        recognized_text = perform_ocr(processed_image)

        print("Recognized Text:")
        print(recognized_text)

        save_text_to_file(recognized_text, output_text_path)
        print(f"Recognized text has been saved to: {output_text_path}")

    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

image_path = 'download.jpeg'  
output_text_path = 'recognized_text.txt' 

main(image_path, output_text_path)
