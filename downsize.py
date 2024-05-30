import cv2
import numpy as np

# 이미지를 로드합니다
image = cv2.imread("C:\\int_img\\color_grid.jpg")

# 이미지의 크기를 가져옵니다
height, width = image.shape[:2]

# 가로, 세로 16배 축소할 크기를 계산합니다
new_width = width // 16
new_height = height // 16

# 이미지를 축소합니다
resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

# 축소된 이미지를 저장합니다
cv2.imwrite("C:\\int_img\\color_grid_16.jpg", resized_image)

# 축소된 이미지를 보여줍니다 (선택 사항)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
