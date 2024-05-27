import cv2
import os
from glob import glob
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim


def calculate_metrics(original_img, compared_img):
    # PSNR 계산
    psnr_value = psnr(
        original_img, compared_img, data_range=compared_img.max() - compared_img.min()
    )

    # SSIM 계산
    min_dim = min(
        original_img.shape[0],
        original_img.shape[1],
        compared_img.shape[0],
        compared_img.shape[1],
    )
    win_size = min(7, min_dim)  # 이미지 크기에 맞게 win_size 설정, 최소 7 이하
    ssim_value, _ = ssim(
        original_img, compared_img, full=True, win_size=win_size, channel_axis=-1
    )

    return psnr_value, ssim_value


# 원본 이미지 경로
original_img_path = "C:\\int_img\\woman.png"
original_img = cv2.imread(original_img_path)

# 비교할 이미지들이 있는 디렉토리 경로
compared_img_dir = "C:\\int_img\\8x\\woman"
compared_img_paths = glob(os.path.join(compared_img_dir, "*.png"))

# 원본 이미지를 BGR에서 RGB로 변환 (OpenCV는 기본적으로 BGR 형식으로 이미지를 읽어옵니다)
original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

# 각 비교할 이미지에 대해 PSNR과 SSIM 계산
results = []
for img_path in compared_img_paths:
    compared_img = cv2.imread(img_path)
    compared_img = cv2.cvtColor(compared_img, cv2.COLOR_BGR2RGB)

    psnr_value, ssim_value = calculate_metrics(original_img, compared_img)
    img_name = os.path.basename(img_path)
    results.append((img_name, psnr_value, ssim_value))
    print(f"Processed {img_name}: PSNR = {psnr_value:.8f}, SSIM = {ssim_value:.8f}")
