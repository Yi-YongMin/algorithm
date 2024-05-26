import cv2


def crop_image_bottom(image_path, output_path, target_height):
    # 이미지 읽기
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return

    # 이미지 크기 확인
    height, width = image.shape[:2]
    print(f"Original size: {width}x{height}")

    # 새로운 높이 설정
    if height < target_height:
        print("Error: Target height is greater than the original height.")
        return

    cropped_image = image[:target_height, :]

    # 이미지 저장
    cv2.imwrite(output_path, cropped_image)
    print(f"Image saved to {output_path}")


# 예시 사용법
image_path = "path_to_input_image.jpg"
output_path = "path_to_output_image.jpg"
target_height = 288
crop_image_bottom(image_path, output_path, target_height)
