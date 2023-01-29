import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

cancer = load_breast_cancer()

data = pd.DataFrame(data=cancer['data'], columns=cancer['feature_names'])
print(data.keys())

scaler = StandardScaler()
scaler.fit(data)

scaled_data = scaler.transform(data)

lda = LinearDiscriminantAnalysis(n_components=2)

