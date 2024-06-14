import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 제공된 MOS 데이터
mos_data = {
    "baby": [
        (4, 3.55, -0.71065),
        (4, 3.1, -0.196475),
        (4, 1.8, 0.662325),
        (4, 1.55, 0.2448),
        (8, 2.15, 0.40385),
        (8, 2.0, 1.0),
        (8, 1.9, 0.84615),
        (8, 3.95, -2.2),
    ],
    "bird": [
        (4, 2.7, -0.538425),
        (4, 2.7, -0.30725),
        (4, 2.55, 0.4559),
        (4, 2.05, 0.389775),
        (8, 2.25, -0.66285),
        (8, 2.35, -0.10135),
        (8, 2.2, 0.3219),
        (8, 3.2, 0.4423),
    ],
    "butterfly": [
        (4, 3.3, -0.909125),
        (4, 2.75, 0.072525),
        (4, 1.95, 0.8366),
        (4, 2.0, 0),
        (8, 3.5, -1.2657),
        (8, 2.4, 0.452175),
        (8, 2.05, 0.524075),
        (8, 2.05, 0.28945),
    ],
    "head": [
        (4, 2.5, 0.810975),
        (4, 2.45, 0.490575),
        (4, 2.4, 0.5057),
        (4, 2.65, -1.80725),
        (8, 1.85, 0.893975),
        (8, 2.3, 0.606025),
        (8, 1.85, 0.75),
        (8, 4.0, -2.25),
    ],
    "woman": [
        (4, 3.3, -1.145475),
        (4, 2.25, -0.216375),
        (4, 1.6, 1.427475),
        (4, 2.85, -0.065625),
        (8, 1.85, 0.893975),
        (8, 2.15, 0.701675),
        (8, 2.05, 0.65435),
        (8, 3.95, -2.25),
    ],
    "alphabet": [
        (16, 3.9, -1.870225),
        (16, 3.1, -0.30725),
        (16, 1.45, 0.773625),
        (16, 1.55, 1.40385),
    ],
    "grid": [
        (16, 1.75, 0.799325),
        (16, 1.85, 0.700675),
        (16, 4.0, -2.25),
        (16, 2.4, 0.75),
    ],
    "stripes": [
        (16, 1.75, 1.59615),
        (16, 1.75, 1.0966),
        (16, 2.5, -0.44275),
        (16, 4.0, -2.25),
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
def plot_mos_vs_jnd(mos_data):
    plt.figure(figsize=(10, 8))

    for key in mos_data.keys():
        data = mos_data[key]
        moss = [d[1] for d in data]
        jnds = [d[2] for d in data]
        plt.scatter(moss, jnds, label=key, color=colors[key])

    plt.xlabel("MOS")
    plt.ylabel("JND")
    plt.title("MOS vs JND")
    plt.legend()
    plt.grid(True)
    plt.show()


plot_mos_vs_jnd(mos_data)


# Pearson 상관계수 계산
def calculate_correlation(mos_data):
    mos_values = []
    jnd_values = []

    for key in mos_data.keys():
        data = mos_data[key]
        mos_values.extend([d[1] for d in data])
        jnd_values.extend([d[2] for d in data])

    correlation, _ = pearsonr(mos_values, jnd_values)
    return correlation


correlation = calculate_correlation(mos_data)
print(f"Pearson correlation between MOS and JND: {correlation}")
