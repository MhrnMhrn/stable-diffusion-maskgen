from rembg import remove
from PIL import Image
import io
import argparse

def create_centered_image_on_canvas(image, canvas_size=None, white_bg=False):
    # Crop the image to its content
    image = image.crop(image.getbbox())

    # Define the canvas size
    if canvas_size == "square":
        canvas = (1024, 1024)
    elif canvas_size == "vertical":
        canvas = (1080, 1920)
    else:
        canvas = image.size

    # Create a new image with the canvas size
    if white_bg:
        new_image = Image.new("RGBA", canvas, (255, 255, 255, 255))
    else:
        new_image = Image.new("RGBA", canvas, (255, 255, 255, 0))

    img_w, img_h = image.size
    bg_w, bg_h = canvas
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    
    # Adjusting the mask for pasting based on the image mode
    mask = image.split()[-1] if image.mode == 'LA' else None

    new_image.paste(image, offset, mask)

    return new_image



def process_image(input_path, output_no_bg_path, output_mask_path, canvas_size=None, white_bg=False):
    with open(input_path, 'rb') as i:
        input_image = i.read()

    output_image = remove(input_image)
    image_no_bg_raw = Image.open(io.BytesIO(output_image))
    image_no_bg = create_centered_image_on_canvas(image_no_bg_raw, canvas_size, white_bg)
    
    # Save the background removed image
    image_no_bg.save(output_no_bg_path, "PNG")

    # Convert the object to black, creating a mask
    black_image = Image.new("L", image_no_bg_raw.size, 0)
    alpha_channel = image_no_bg_raw.split()[3]
    image_mask_raw = Image.merge('LA', (black_image, alpha_channel))
    
    # Center the black mask image on canvas
    image_mask = create_centered_image_on_canvas(image_mask_raw, canvas_size, white_bg)

    # Save the black mask of the object
    image_mask.save(output_mask_path, "PNG")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove the background of an image, save it, and create a black mask of the object, then save it.')
    parser.add_argument('input', type=str, help='Path to the input image')
    parser.add_argument('output_no_bg', type=str, help='Path to save the image with background removed')
    parser.add_argument('output_mask', type=str, help='Path to save the black mask of the object')
    parser.add_argument('--size', type=str, choices=["square", "vertical"], default=None, help='Canvas size: "square" for 1024x1024 or "vertical" for 1080x1920')
    parser.add_argument('--white', action='store_true', help='Use a white background instead of transparent')

    args = parser.parse_args()

    process_image(args.input, args.output_no_bg, args.output_mask, args.size, args.white)
