import pandas as pd

# Load dataset
df = pd.read_csv("../data/academic_stress.csv")

# Show basic information
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Show first rows
print("\nPreview:")
print(df.head())

# Save a clean copy
df.to_csv("../data/academic_stress_clean.csv", index=False)

print("\nClean file saved successfully.")
