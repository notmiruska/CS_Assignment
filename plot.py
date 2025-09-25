import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats 

df = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")

r, p = scipy.stats.pearsonr(df["WO [x1000]"], df["NL Beer consumption [x1000 hectoliter]"])
print(f"The correlation is r = {r:.2f} with p = {p:.2f}")

sns.regplot(x="WO [x1000]", y="NL Beer consumption [x1000 hectoliter]", data=df, scatter_kws={"alpha":0.7}, line_kws={"color":"orange"})

plt.xlabel("WO")
plt.ylabel("NL Beer consumption")
plt.title("WO and NL Beer consumption")

plt.grid(True)
plt.savefig("correlation.png")
plt.show()