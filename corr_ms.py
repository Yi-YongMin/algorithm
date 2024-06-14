import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 제공된 데이터
msssim_data = {
    "baby": [
        (4, 0.947457075, -0.71065),
        (4, 0.95020479, -0.196475),
        (4, 0.933794022, 0.662325),
        (4, 0.850125015, 0.2448),
        (8, 0.84717983, 0.40385),
        (8, 0.838304102, 1.0),
        (8, 0.836017132, 0.84615),
        (8, 0.780497968, -2.2),
    ],
    "bird": [
        (4, 0.95581454, -0.538425),
        (4, 0.96174866, -0.30725),
        (4, 0.92910409, 0.4559),
        (4, 0.888801575, 0.389775),
        (8, 0.829599559, -0.66285),
        (8, 0.837896824, -0.10135),
        (8, 0.830731153, 0.3219),
        (8, 0.758447587, 0.4423),
    ],
    "butterfly": [
        (4, 0.918577015, -0.909125),
        (4, 0.923306942, 0.072525),
        (4, 0.897556067, 0.8366),
        (4, 0.828168094, 0),
        (8, 0.713547945, -1.2657),
        (8, 0.725338459, 0.452175),
        (8, 0.727180064, 0.524075),
        (8, 0.642505825, 0.28945),
    ],
    "head": [
        (4, 0.923986018, 0.810975),
        (4, 0.918257058, 0.490575),
        (4, 0.893920243, 0.5057),
        (4, 0.774992228, -1.80725),
        (8, 0.839531243, 0.893975),
        (8, 0.827431381, 0.606025),
        (8, 0.82163614, 0.75),
        (8, 0.743273437, -2.25),
    ],
    "woman": [
        (4, 0.945264637, -1.145475),
        (4, 0.949143887, -0.216375),
        (4, 0.935816586, 1.427475),
        (4, 0.882874787, -0.065625),
        (8, 0.798136532, 0.893975),
        (8, 0.784943521, 0.701675),
        (8, 0.781386554, 0.65435),
        (8, 0.734754503, -2.25),
    ],
    "alphabet": [
        (16, 0.767123997, -1.870225),
        (16, 0.774894059, -0.30725),
        (16, 0.741060555, 0.773625),
        (16, 0.737435043, 1.40385),
    ],
    "grid": [
        (16, 0.697696388, 0.799325),
        (16, 0.69142586, 0.700675),
        (16, 0.678463936, -2.25),
        (16, 0.660444319, 0.75),
    ],
    "stripes": [
        (16, 0.823248088, 1.59615),
        (16, 0.831947744, 1.0966),
        (16, 0.673870623, -0.44275),
        (16, 0.760580361, -2.25),
    ],
}

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
def plot_msssim_vs_jnd(msssim_data, colors):
    plt.figure(figsize=(10, 8))

    for key in msssim_data.keys():
        data = msssim_data[key]
        msssims = [d[1] for d in data]
        jnds = [d[2] for d in data]
        plt.scatter(msssims, jnds, label=key, color=colors[key])

    plt.xlabel("MS-SSIM")
    plt.ylabel("JND")
    plt.title("MS-SSIM vs JND")
    plt.legend()
    plt.grid(True)
    plt.show()


plot_msssim_vs_jnd(msssim_data, colors)


# Pearson 상관계수 계산
def calculate_correlation(msssim_data):
    msssim_values = []
    jnd_values = []

    for key in msssim_data.keys():
        data = msssim_data[key]
        msssim_values.extend([d[1] for d in data])
        jnd_values.extend([d[2] for d in data])

    correlation, _ = pearsonr(msssim_values, jnd_values)
    return correlation


correlation = calculate_correlation(msssim_data)
print(f"Pearson correlation between MS-SSIM and JND: {correlation}")