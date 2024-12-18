# USING THE GIVEN DATASET
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Polav\Downloads\simple_dataset.csv")
id=df['ID'].to_numpy()
h=df['Height (cm)'].to_numpy()
W=df['Weight (kg)'].to_numpy()
meanh=np.mean(h)
medianh=np.median(h)
print(f"the mean and median of heights are \n {meanh} \n {medianh}")

plt.bar(id,W)
plt.title('Weights of the given')
plt.xlabel('ID')
plt.ylabel('Weight (kg)')

plt.bar(id,h)
plt.title('Heights of the given')
plt.xlabel('ID')
plt.ylabel('Height (cm)')

plt.show()