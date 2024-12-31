# Certificate Generator
A Python script that automates the process of generating personalized certificates by overlaying student names onto a certificate template.

# Features:
- **Template-based Generation**: Uses a pre-designed PNG certificate template.
- **Batch Processing**: Reads student names from a text file and generates certificates for all of them.
- **Font Customization**: Allows easy configuration of font, size, and position for the text overlay.
- **Dynamic Name Placement**: Supports easy configuration of the X, Y coordinates to position the student names on the certificate.
- **Output Directory**: Saves generated certificates in a specified directory.

# How to Get the XY Coordinates for Name Placement:
- Open the Certificate Template in any image editor (e.g., GIMP, Photoshop, or MS Paint).
- Note the XY Coordinates: As you move the cursor, most image editors display the X, Y coordinates at the current cursor position. This is the exact spot where the name will appear.
- Set in Script: In the script, set the text_position variable to the desired X, Y coordinates:
```text_position = (X, Y)```

# Requirements:
- Python 3.x
- Pillow (```pip install pillow```)

# How to Use:
- Clone the repository:
```git clone https://github.com/mrfox2003/certificate-generator```
- Navigate to the project directory:
```cd certificate-generator```
- Place the certificate template (certificate_template.png) in the project directory.
- Create a text file (names.txt) with one student name per line.
- Ensure the font file (arial.ttf or any .ttf file) is in the correct location, or modify the script to point to your font.
- Set the X, Y coordinates where you want the student name to appear.
- Run the script:
```python certificate-generator.py```
- The generated certificates will be saved in the certificates/ directory.
