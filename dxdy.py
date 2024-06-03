# import cv2
# import os
# import numpy as np
# from skimage.metrics import peak_signal_noise_ratio as psnr
# from skimage.metrics import structural_similarity as ssim


# def calculate_psnr_ssim(original, compressed):
#     # Check if files exist
#     if not os.path.exists(original):
#         print(f"Original file not found: {original}")
#         return None, None
#     if not os.path.exists(compressed):
#         print(f"Compressed file not found: {compressed}")
#         return None, None

#     # Read images
#     original = cv2.imread(original)
#     compressed = cv2.imread(compressed)

#     # Ensure images are read correctly
#     if original is None or compressed is None:
#         print("Error reading one of the images.")
#         return None, None

#     # Convert images to grayscale
#     original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
#     compressed_gray = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)

#     # Calculate PSNR
#     psnr_value = psnr(original_gray, compressed_gray)

#     # Calculate SSIM
#     ssim_value, _ = ssim(original_gray, compressed_gray, full=True)

#     return psnr_value, ssim_value


# # Example usage
# original_path = "C:\\Set5\\head.png"
# compressed_path = "C:\\int_img\\bilinear_16\\head_bl16.png"
# psnr_value, ssim_value = calculate_psnr_ssim(original_path, compressed_path)
# if psnr_value is not None and ssim_value is not None:
#     print(f"PSNR: {psnr_value}")
#     print(f"SSIM: {ssim_value}")


import cv2
import os
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim


def resize_image(image, target_size):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)


def calculate_psnr_ssim(original, compressed):
    # Check if files exist
    if not os.path.exists(original):
        print(f"Original file not found: {original}")
        return None, None
    if not os.path.exists(compressed):
        print(f"Compressed file not found: {compressed}")
        return None, None

    # Read images
    original = cv2.imread(original)
    compressed = cv2.imread(compressed)

    # Ensure images are read correctly
    if original is None:
        print(f"Error reading the original image: {original}")
        return None, None
    if compressed is None:
        print(f"Error reading the compressed image: {compressed}")
        return None, None

    # Convert images to grayscale
    original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    compressed_gray = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)

    # Resize compressed image to match original image size
    if original_gray.shape != compressed_gray.shape:
        compressed_gray = resize_image(
            compressed_gray, (original_gray.shape[1], original_gray.shape[0])
        )

    # Calculate PSNR
    psnr_value = psnr(original_gray, compressed_gray)

    # Calculate SSIM
    ssim_value, _ = ssim(original_gray, compressed_gray, full=True)

    return psnr_value, ssim_value


# Example usage
original_path = "C:\\int_img\\16x\\color_stripes1.png"
compressed_path = "C:\\int_img\\16x\\color_stripes\\gan_.png"
psnr_value, ssim_value = calculate_psnr_ssim(original_path, compressed_path)
if psnr_value is not None and ssim_value is not None:
    print(f"PSNR: {psnr_value}")
    print(f"SSIM: {ssim_value}")
else:
    print("PSNR or SSIM calculation failed.")
