from rembg import remove
from PIL import Image
import io
import argparse

def remove_background(input_path, output_path, canvas_size=None, white_bg=False):
    with open(input_path, 'rb') as i:
        input_image = i.read()

    output_image = remove(input_image)
    image_no_bg = Image.open(io.BytesIO(output_image))

    # Crop the image to its content
    image_no_bg = image_no_bg.crop(image_no_bg.getbbox())

    # Define the canvas size
    if canvas_size == "square":
        canvas = (1024, 1024)
    elif canvas_size == "vertical":
        canvas = (1080, 1920)
    else:
        canvas = image_no_bg.size

    # Create a new image with the canvas size and paste the image with no background on its center
    if white_bg:
        new_image = Image.new("RGBA", canvas, (255, 255, 255, 255))  # White background
    else:
        new_image = Image.new("RGBA", canvas, (255, 255, 255, 0))  # Transparent background

    img_w, img_h = image_no_bg.size
    bg_w, bg_h = canvas
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    new_image.paste(image_no_bg, offset, image_no_bg)

    new_image.save(output_path, "PNG")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove the background of an image and optionally set canvas size.')
    parser.add_argument('input', type=str, help='Path to the input image')
    parser.add_argument('output', type=str, help='Path to save the output image')
    parser.add_argument('--size', type=str, choices=["square", "vertical"], default=None, help='Canvas size: "square" for 1024x1024 or "vertical" for 1080x1920')
    parser.add_argument('--white', action='store_true', help='Use a white background instead of transparent')

    args = parser.parse_args()

    remove_background(args.input, args.output, args.size, args.white)
