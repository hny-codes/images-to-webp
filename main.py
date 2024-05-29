from pathlib import Path
from PIL import Image

# Current path
current_path = Path.cwd()

# DirNotFound error
class DirNotfoundError(Exception):
  pass

def create_paths():
  # Create output path
  new_path = Path(f'{current_path}/output')
  new_path.mkdir(exist_ok=True)
  return new_path

def convert_to_webp(img_generator):
  # Loop through each image, convert to webp, and save to output folder
  output = 'WebP'

  for image in img_generator:
    print("Converting: ", image)
    temp_image = Image.open(image)
    output_path.touch(temp_image.save(f'{output_path}/{image.stem}.webp', format=output))
    temp_image.close()

if __name__ == '__main__':
  image_types = ('*.png', '*.jpg')

  # Get output path
  output_path = create_paths()

  try:
    # Get input path
    input_path = Path(f'{current_path}/input')

    # Raise exception if input path does not exist
    if input_path.is_dir() == False:
      raise DirNotfoundError
    
    # Read all images via generator
    # REF: https://stackoverflow.com/a/57054058
    all_images = (p.resolve() for p in Path(input_path).glob("**/*") if p.suffix in {".png", ".jpg"})
    convert_to_webp(all_images)

  except DirNotfoundError:
    print(f'Error: there is no Input directory.')