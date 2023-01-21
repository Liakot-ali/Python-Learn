# Implementing PCA using breast cancer dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load breast cancer dataset and set the data to dataframe
data = load_breast_cancer()
df = pd.DataFrame(data['data'], columns=data['feature_names'])

# Standardize the data
scaler = StandardScaler()
scaler.fit(df)

# Find the best components using PCA
scaled_data = scaler.transform(df)
pca = PCA()   # only 2 principal components will be selected
pca.fit(scaled_data)

# Get the components value
# print(pca.explained_variance_, pca.explained_variance_ratio_)
var = pca.explained_variance_ratio_
feature = pca.get_feature_names_out()

x_pca = pca.transform(scaled_data)
# print(pca.get_feature_names_out())
# print(pca.components_)
# print(x_pca)

# Plotting the value using two feature
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=data['target'])
plt.show()

plt.bar(feature, height=var)
plt.show()

# Showing in headmap
df_comp = pd.DataFrame(pca.components_, columns=data['feature_names'])
plt.figure(figsize=(10, 6))
sns.heatmap(df_comp)
plt.show()