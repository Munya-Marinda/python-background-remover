# Importing Required Modules 
from rembg import remove 
from PIL import Image 

# Collection of images
images = ['banana', 'berries', 'empty-globe', 'icecream-cone']

# Remove background one-by-one
for image_name in images:
  input_path =  './inputs/' + image_name + ".jpg"
  output_path = './no-background/' + image_name + '.png'
  input = Image.open(input_path)
  output = remove(input)
  output.save(output_path)
  
print("Done!")