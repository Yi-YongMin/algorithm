import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 제공된 PSNR 데이터
psnr_data = {
    "baby": {
        4: [29.45307754, 29.59910154, 27.26251153, 20.76206646],
        8: [24.87233847, 24.4944621, 24.2931403, 21.39190483],
    },
    "bird": {
        4: [27.31663851, 27.81895038, 24.59193513, 20.65648823],
        8: [22.13562494, 22.12472869, 21.87473094, 18.85946178],
    },
    "butterfly": {
        4: [19.65418105, 20.0030424, 18.040622, 14.7243704],
        8: [15.094307, 15.3345594, 15.07706164, 12.39981989],
    },
    "head": {
        4: [28.0439537, 27.78529091, 26.35763876, 20.01837571],
        8: [25.63788969, 25.21757796, 25.01218456, 22.66775775],
    },
    "woman": {
        4: [24.28061002, 24.52742064, 22.42159454, 18.09359141],
        8: [19.27445927, 18.8606367, 18.5749453, 16.48745998],
    },
    "alphabet": {16: [20.54140744, 21.07450263, 20.07225166, 20.54580133]},
    "grid": {16: [22.67245928, 22.74641324, 20.58856295, 22.42929974]},
    "stripes": {16: [18.83542189, 19.17984437, 15.50437105, 16.36395987]},
}

jnd_data = {
    "baby": {
        4: [-0.71065, -0.196475, 0.662325, 0.2448],
        8: [0.40385, 1, 0.84615, -2.2],
    },
    "bird": {
        4: [-0.538425, -0.30725, 0.4559, 0.389775],
        8: [-0.66285, -0.10135, 0.3219, 0.4423],
    },
    "butterfly": {
        4: [-0.909125, 0.072525, 0.8366, 0],
        8: [-1.2657, 0.452175, 0.524075, 0.28945],
    },
    "head": {
        4: [0.810975, 0.490575, 0.5057, -1.80725],
        8: [0.893975, 0.606025, 0.75, -2.25],
    },
    "woman": {
        4: [-1.145475, -0.216375, 1.427475, -0.065625],
        8: [0.893975, 0.701675, 0.65435, -2.25],
    },
    "alphabet": {16: [-1.870225, -0.30725, 0.773625, 1.40385]},
    "grid": {16: [0.799325, 0.700675, -2.25, 0.75]},
    "stripes": {16: [1.59615, 1.0966, -0.44275, -2.25]},
}

# Define colors for each image
colors = {
    "baby": "blue",
    "bird": "green",
    "butterfly": "red",
    "head": "purple",
    "woman": "orange",
    "alphabet": "brown",
    "grid": "pink",
    "stripes": "gray",
}

# Flatten the data to list format for correlation calculation
psnr_values = []
jnd_values = []
color_values = []

for image in psnr_data:
    for scale in psnr_data[image]:
        psnr_values.extend(psnr_data[image][scale])
        jnd_values.extend(jnd_data[image][scale])
        color_values.extend([colors[image]] * len(psnr_data[image][scale]))

# Calculate Pearson correlation coefficient
correlation, _ = pearsonr(psnr_values, jnd_values)

# Print the correlation
print("Pearson correlation coefficient between PSNR and JND:", correlation)

# Data visualization
plt.figure(figsize=(10, 6))
for i in range(len(psnr_values)):
    plt.scatter(psnr_values[i], jnd_values[i], color=color_values[i])

# Add legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[img], markersize=10) for img in colors]
labels = list(colors.keys())
plt.legend(handles, labels, title="Image")

plt.title("PSNR vs JND")
plt.xlabel("PSNR")
plt.ylabel("JND")
plt.grid(True)
plt.show()
