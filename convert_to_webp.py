from pathlib import Path
from PIL import Image

########################
# Lists and Variables
########################

source_image_ext = [".gif", ".png", ".jpg", ".jpeg"]
source_image_path = "images/"

##############################
# FUNCTION BLOCK
##############################

# This is the function that actually does the conversion
def convert_to_webp(source):
    destination = source.with_suffix(".webp")
    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp
    return destination

# This function grabs the files you want to convert and feeds them to convert_to_webp() function
def legacy_to_webp(ext, source_path):
    paths = Path(f"{source_path}").glob(f"**/*{ext}")
    for path in paths:
        webp_path = convert_to_webp(source=path)
        print(webp_path)

##############################
# EXECUTION OF LOGIC
##############################

for i in source_image_ext: 
    print(i)
    print(type(i))
    legacy_to_webp(ext=i, source_path=source_image_path)
