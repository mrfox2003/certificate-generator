import os
from PIL import Image, ImageDraw, ImageFont

# Paths
template_path = "certificate_template.png"  # Path to your PNG certificate template
names_file = "names.txt"  # Path to the text file with names
output_folder = "certificates/"  # Folder to save generated certificates

# Font setting
font_path = os.path.expanduser("~/certificate/PinyonScript-Regular.ttf")
font_size = 78.3

# Text placement on the certificate (adjust based on your template)
text_position = (657,591)  # (x, y) coordinates

def generate_certificates():
    # Load the template
    template = Image.open(template_path)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Read names from the file
    with open(names_file, "r") as file:
        names = [line.strip() for line in file]

    # Ensure output folder exists
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate certificates
    for name in names:
        # Copy the template to avoid overwriting
        certificate = template.copy()
        draw = ImageDraw.Draw(certificate)
        
        # Add name to the certificate
        draw.text(text_position, name, fill="black", font=font)
        
        # Save the certificate
        output_path = os.path.join(output_folder, f"{name}.png")
        certificate.save(output_path)
        print(f"Generated certificate for {name}")

if __name__ == "__main__":
    generate_certificates()
