import pandas as pd

data = pd.read_csv("grades.csv")

data["Average"] = data.iloc[:, 1:].mean(axis=1)
print(data)

print("Subject averages:")
print(data.iloc[:, 1:-1].mean())
