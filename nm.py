# import numpy as np
# import cv2
# from skimage.metrics import structural_similarity as ssim
# from pytorch_msssim import ms_ssim
# import torch


# def calculate_composite_metric(original, compressed, grayscale_threshold=0.7):
#     # 이미지 읽기
#     original_img = cv2.imread(original)
#     compressed_img = cv2.imread(compressed)

#     # 이미지 흑백 비율 계산
#     original_gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
#     black_white_ratio = np.sum(original_gray < 128) / original_gray.size

#     # PSNR 계산
#     psnr_value = cv2.PSNR(original_img, compressed_img)
#     # PSNR 값을 0-1 사이로 정규화
#     psnr_value = (psnr_value - 20) / (50 - 20)  # 20-50 범위로 정규화

#     # SSIM 계산 (win_size 조정)
#     min_dim = min(original_img.shape[:2])
#     win_size = 7 if min_dim >= 7 else min_dim
#     ssim_value = ssim(original_img, compressed_img, win_size=win_size, channel_axis=2)

#     # MS-SSIM 계산
#     original_tensor = (
#         torch.tensor(original_img).permute(2, 0, 1).unsqueeze(0).float() / 255.0
#     )
#     compressed_tensor = (
#         torch.tensor(compressed_img).permute(2, 0, 1).unsqueeze(0).float() / 255.0
#     )
#     ms_ssim_value = ms_ssim(original_tensor, compressed_tensor, data_range=1.0).item()

#     # 가중치 설정
#     if black_white_ratio > grayscale_threshold:
#         w1, w2, w3 = 0.1, 0.4, 0.5  # 흑백 비율이 높을 때 가중치
#     else:
#         w1, w2, w3 = 0.3, 0.3, 0.4  # 일반적인 경우의 가중치

#     # 복합 평가 지표 계산
#     composite_index = w1 * psnr_value + w2 * ssim_value + w3 * ms_ssim_value

#     return composite_index


# # 사용 예시
# original_path = "C:\\int_img\\baby.png"
# compressed_path = "C:\\int_img\\4x\\baby\\bc_4x.png"
# metric = calculate_composite_metric(original_path, compressed_path)
# print(f"Composite Metric: {metric}")
a = [[] for I in range(7)]
