import cv2
import os
from glob import glob

# 원본 이미지가 있는 디렉토리 경로
hr_img_dir = "/content/drive/MyDrive/Set5"

# 16배 축소된 이미지 경로
lr_img_paths = ["C:\\int_img\\16x\\alphabet\\alphabet.jpg"]

# 출력될 디렉토리 경로
bilinear_img_dir = "C:\\algoTest\\bilinear16"
bicubic_img_dir = "C:\\algoTest\\bicubic16"

# 가정: 원본 이미지 크기 (확대된 이미지 크기)
original_width = 256  # 원본 이미지의 폭 (예시로 설정, 실제 크기로 변경 필요)
original_height = 256  # 원본 이미지의 높이 (예시로 설정, 실제 크기로 변경 필요)

# 출력 디렉토리 생성
os.makedirs(bilinear_img_dir, exist_ok=True)
os.makedirs(bicubic_img_dir, exist_ok=True)

# 해당 디렉토리 내의 모든 16배 축소된 이미지에 대해 작업을 반복합니다.
for lr_img_path in lr_img_paths:
    # 이미지 이름 추출
    img_name = os.path.basename(lr_img_path)
    img_name_without_ext = os.path.splitext(img_name)[0]

    # 16배 축소된 이미지 불러오기
    lr_img = cv2.imread(lr_img_path)

    # Bilinear로 보정된 이미지 생성
    bilinear_img = cv2.resize(
        lr_img, dsize=(original_width, original_height), interpolation=cv2.INTER_LINEAR
    )

    # Bicubic으로 보정된 이미지 생성
    bicubic_img = cv2.resize(
        lr_img, dsize=(original_width, original_height), interpolation=cv2.INTER_CUBIC
    )

    # 파일 경로 정의
    bilinear_img_path = os.path.join(
        bilinear_img_dir, f"{img_name_without_ext}_bilinear16.png"
    )
    bicubic_img_path = os.path.join(
        bicubic_img_dir, f"{img_name_without_ext}_bicubic16.png"
    )

    # 이미지 저장
    cv2.imwrite(bilinear_img_path, bilinear_img)
    cv2.imwrite(bicubic_img_path, bicubic_img)

    print(f"Processed {img_name} with Bilinear and Bicubic scaling")

# 처리 완료 메시지
print("All images have been processed with Bilinear and Bicubic scaling.")
