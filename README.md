# stable-diffusion-maskgen
Stable Diffusion IMG2IMG Mask Generator And Background Remover

# Image Processing Scripts

This repository contains three Python scripts for various image processing tasks:

1. **bg_remover.py**: Removes the background of an image.
2. **mask_maker.py**: Generates a black mask from the image.
3. **img2img_generator.py**: Combines the functionalities of the first two scripts, generating both a background-removed image and its corresponding mask.

## Installation

Before running the scripts, make sure you have the required libraries installed:

pip install rembg PIL


## Usage

### 1. Background Remover

To remove the background of an image:

python bg_remover.py <input_image_path> <output_image_path> [--size <canvas_size>] [--white]


- `<input_image_path>`: Path to the input image.
- `<output_image_path>`: Path where the image without background will be saved.
- `--size`: Optional. Canvas size: `"square"` for 1024x1024 or `"vertical"` for 1080x1920. If not specified, the canvas size will match the input image size.
- `--white`: Optional. If set, the output image will have a white background. By default, the background is transparent.

### 2. Mask Maker

To generate a black mask from the image:

python mask_maker.py <input_image_path> <output_mask_path> [--size <canvas_size>] [--white]


Arguments are similar to the ones described for the background remover.

### 3. Image to Image Generator

This script combines the functionalities of the first two:

python img2img_generator.py <input_image_path> <output_no_bg_path> <output_mask_path> [--size <canvas_size>] [--white]


- `<input_image_path>`: Path to the input image.
- `<output_no_bg_path>`: Path where the image without background will be saved.
- `<output_mask_path>`: Path where the black mask of the object will be saved.
- `--size` and `--white`: As described above.

## Example Output

![Example Image Output](<sample_image.png>)


