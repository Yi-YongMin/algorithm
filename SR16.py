# import cv2


# def crop_image_bottom(image_path, output_path, target_height):
#     # 이미지 읽기
#     image = cv2.imread(image_path)
#     if image is None:
#         print("Error: Could not read image.")
#         return

#     # 이미지 크기 확인
#     height, width = image.shape[:2]
#     print(f"Original size: {width}x{height}")

#     # 새로운 높이 설정
#     if height < target_height:
#         print("Error: Target height is greater than the original height.")
#         return

#     cropped_image = image[:target_height, :]

#     # 이미지 저장
#     cv2.imwrite(output_path, cropped_image)
#     print(f"Image saved to {output_path}")


# # 예시 사용법
# image_path = "C:\\Set5\\woman.png"
# output_path = "C:\\Set5\\edit_woman.png"
# target_height = 288
# crop_image_bottom(image_path, output_path, target_height)
# import cv2


# def resize_image(image_path, output_path, target_size=(256, 256)):
#     # 이미지 읽기
#     image = cv2.imread(image_path)
#     if image is None:
#         print("Error: Could not read image.")
#         return

#     # 이미지 크기 확인
#     height, width = image.shape[:2]
#     print(f"Original size: {width}x{height}")

#     if width != 512 or height != 512:
#         print("Warning: The original image size is not 512x512.")

#     # 이미지 크기 조정
#     resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)

#     # 이미지 저장
#     cv2.imwrite(output_path, resized_image)
#     print(f"Resized image saved to {output_path}")


# # 예시 사용법
# image_path = "C:\\Set5\\baby.png"
# output_path = "C:\\Set5\\edit_baby.png"
# resize_image(image_path, output_path)
import cv2


def shrink_image(image_path, output_path, scale_factor=16):
    # 이미지 읽기
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return

    # 이미지 크기 확인
    height, width = image.shape[:2]
    print(f"Original size: {width}x{height}")

    # 새로운 크기 계산
    new_width = width // scale_factor
    new_height = height // scale_factor
    print(f"New size: {new_width}x{new_height}")

    # 이미지 크기 조정
    resized_image = cv2.resize(
        image, (new_width, new_height), interpolation=cv2.INTER_LINEAR
    )

    # 이미지 저장
    cv2.imwrite(output_path, resized_image)
    print(f"Resized image saved to {output_path}")


# 예시 사용법
image_path = "C:\\Set5\\edit_woman.png"
output_path = "C:\\Set5\\edit_woman16.png"
shrink_image(image_path, output_path)
