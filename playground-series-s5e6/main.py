import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ファイル読み込み
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
sample_submission = pd.read_csv("sample_submission.csv")

# データの概要を表示
print(train.shape)
print(train.columns)
print(train.head())
