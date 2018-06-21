from pandas import Series
import numpy as np
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose

def decomposition(rawData_path, picture_path, decomposition_path):
    """

    :param file_path: the path of the raw data file
    :param picture_path: the picture of the decomposition
    :return:the picture saved and the data of the decomposition, including trend part, seasonal part, residual part
    """
    rawDataPath = rawData_path
    picturePath = picture_path
    decompositionPath = decomposition_path

    series = Series.from_csv(rawDataPath, header=0)
    result = seasonal_decompose(series, model="additive", freq=4, two_sided=False)

    # return the picture of the decomposition to the picture path
    result.plot()
    if picture_path != None:
        pyplot.savefig(picturePath)

    # return decomposition to the decomposition path
    trend = result.trend
    seasonal = result.seasonal
    residual = result.resid
    n = trend.shape[0]
    if decompositionPath != None:
        with open(decompositionPath, "w") as f:
            for i in range(n):
                s = []
                s.append(str(trend[i]))
                s.append(str(seasonal[i]))
                s.append(str(residual[i]))
                s.append(str(series[i]))
                f.write("\t".join(s) + "\n")




if __name__ == "__main__":
    decomposition('./data/international-airline-passengers.csv', "./picture/Decomposition.pdf", "./data/decomposition")


