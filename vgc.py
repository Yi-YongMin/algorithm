import numpy as np
import matplotlib.pyplot as plt

# 임의의 TPR과 FPR 값 생성
# 5개의 원본 이미지에 대해 4가지 기법으로 업스케일링
techniques = ["SRCNN", "SRGAN", "Bicubic", "Bilinear"]
n_images = 5  # 이미지 수
n_techniques = len(techniques)  # 기술 수
n_respondents = 100  # 평가자 수

np.random.seed(0)
tprs = np.random.rand(n_techniques) * 0.5 + 0.5  # TPR: 0.5에서 1.0 사이
fprs = np.random.rand(n_techniques) * 0.4  # FPR: 0에서 0.4 사이

# 곡선 그리기
plt.figure(figsize=(8, 6))
plt.plot(fprs, tprs, marker="o", linestyle="-", color="b")
for i, tech in enumerate(techniques):
    plt.annotate(tech, (fprs[i], tprs[i]))
plt.title("Simulated VGC Curve")
plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.grid(True)
plt.show()
