from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import NMF

data = load_breast_cancer()
# print(data.keys())
df = pd.DataFrame(data['data'], columns=data['feature_names'])

X = np.array(df)
# scaler = StandardScaler()
# scaler.fit(df)
# scaled_data = scaler.transform(df)

nmf = NMF(n_components=2, init='random', random_state=0)
W = nmf.fit_transform(X)
H = nmf.components_
# print(nmf.components_)

