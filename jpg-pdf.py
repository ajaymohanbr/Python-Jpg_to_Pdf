from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_images_to_pdf(image_folder, output_pdf):
    # Get list of image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.JPG')]

    # Create a new PDF file
    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        # Open each image file
        img = Image.open(os.path.join(image_folder, image_file))

        # Get image size and aspect ratio
        width, height = img.size
        aspect_ratio = width / height

        # Calculate new dimensions for fitting into PDF page
        if aspect_ratio > 1:
            new_width = letter[0] - 100  # Reduce width to leave margins
            new_height = new_width / aspect_ratio
        else:
            new_height = letter[1] - 100  # Reduce height to leave margins
            new_width = new_height * aspect_ratio

        # Add the image to the PDF
        c.drawImage(os.path.join(image_folder, image_file), 50, 50, width=new_width, height=new_height)
        c.showPage()

    # Save the PDF
    c.save()

# Example usage:
convert_images_to_pdf(r'C:\Users\Padam\Desktop\docs', "certd-casamento.pdf")
