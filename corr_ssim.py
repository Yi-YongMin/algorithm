import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 제공된 데이터
ssim_data = {
    "baby": [
        (4, 0.83245406, -0.71065),
        (4, 0.83999955, -0.196475),
        (4, 0.80181104, 0.662325),
        (4, 0.50479401, 0.2448),
        (8, 0.68659525, 0.40385),
        (8, 0.67404294, 1.0),
        (8, 0.6707283, 0.84615),
        (8, 0.59382816, -2.2),
    ],
    "bird": [
        (4, 0.85467257, -0.538425),
        (4, 0.86460084, -0.30725),
        (4, 0.76969359, 0.4559),
        (4, 0.60460081, 0.389775),
        (8, 0.64561998, -0.66285),
        (8, 0.64093871, -0.10135),
        (8, 0.62319616, 0.3219),
        (8, 0.5280426, 0.4423),
    ],
    "butterfly": [
        (4, 0.71677579, -0.909125),
        (4, 0.70998918, 0.072525),
        (4, 0.64337158, 0.8366),
        (4, 0.48195079, 0),
        (8, 0.46496718, -1.2657),
        (8, 0.44830315, 0.452175),
        (8, 0.45020838, 0.524075),
        (8, 0.35111706, 0.28945),
    ],
    "head": [
        (4, 0.68458752, 0.810975),
        (4, 0.68153169, 0.490575),
        (4, 0.63415187, 0.5057),
        (4, 0.33676094, -1.80725),
        (8, 0.57163936, 0.893975),
        (8, 0.56130794, 0.606025),
        (8, 0.54718296, 0.75),
        (8, 0.47841295, -2.25),
    ],
    "woman": [
        (4, 0.82420277, -1.145475),
        (4, 0.82860461, -0.216375),
        (4, 0.7823643, 1.427475),
        (4, 0.58135859, -0.065625),
        (8, 0.61983148, 0.893975),
        (8, 0.59295461, 0.701675),
        (8, 0.59000835, 0.65435),
        (8, 0.5226642, -2.25),
    ],
    "alphabet": [
        (16, 0.693633567, -1.870225),
        (16, 0.688508273, -0.30725),
        (16, 0.662855654, 0.773625),
        (16, 0.6566298, 1.40385),
    ],
    "grid": [
        (16, 0.774256725, 0.799325),
        (16, 0.733754279, 0.700675),
        (16, 0.624107792, -2.25),
        (16, 0.679852471, 0.75),
    ],
    "stripes": [
        (16, 0.608197014, 1.59615),
        (16, 0.607209165, 1.0966),
        (16, 0.430360603, -0.44275),
        (16, 0.539258812, -2.25),
    ],
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


# 각 항목의 데이터를 추출하여 시각화
def plot_ssim_vs_jnd(ssim_data):
    plt.figure(figsize=(10, 8))

    for key in ssim_data.keys():
        data = ssim_data[key]
        ssims = [d[1] for d in data]
        jnds = [d[2] for d in data]
        plt.scatter(ssims, jnds, label=key, color=colors[key])

    plt.xlabel("SSIM")
    plt.ylabel("JND")
    plt.title("SSIM vs JND")
    plt.legend()
    plt.grid(True)
    plt.show()


plot_ssim_vs_jnd(ssim_data)


# Pearson 상관계수 계산
def calculate_correlation(ssim_data):
    ssim_values = []
    jnd_values = []

    for key in ssim_data.keys():
        data = ssim_data[key]
        ssim_values.extend([d[1] for d in data])
        jnd_values.extend([d[2] for d in data])

    correlation, _ = pearsonr(ssim_values, jnd_values)
    return correlation


correlation = calculate_correlation(ssim_data)
print(f"Pearson correlation between SSIM and JND: {correlation}")