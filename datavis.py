import pandas as pd
from datapullingwithPandas import bist30_data
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10, 6))
sns.scatterplot(data=bist30_data, x=bist30_data["Brent"], y=bist30_data["Close"], hue=bist30_data["Usd"], palette='viridis')

# Grafik özelliklerini ayarlayın
plt.title('Kapanış Fiyatları vs. Benzin Fiyatı')
plt.xlabel('Benzin Fiyatı')
plt.ylabel('Kapanış Fiyatları')

# Grafiği gösterin
plt.show()