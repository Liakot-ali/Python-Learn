import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()