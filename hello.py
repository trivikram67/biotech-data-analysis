import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df = df.drop(columns=['Unnamed: 32', 'id'], errors='ignore')

print("--- Mean Nuclei Measurements by Diagnosis ---")
print(df.groupby('diagnosis')[['radius_mean', 'texture_mean', 'smoothness_mean']].mean())

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x='radius_mean', y='texture_mean', hue='diagnosis', palette='coolwarm')

plt.title('Biotech Analysis: Cancer Cell Nuclei Radius vs. Texture')
plt.xlabel('Mean Radius')
plt.ylabel('Mean Texture')

plt.savefig('biotech_project_plot.png', dpi=300)
plt.show()