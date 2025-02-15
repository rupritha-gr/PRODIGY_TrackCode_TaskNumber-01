
import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic age data for a population
np.random.seed(42)
ages = np.random.randint(0, 100, 200)  # 200 individuals with ages between 0 and 100

# Create histogram for age distribution
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, edgecolor='black', alpha=0.7)
plt.xlabel("Age Groups")
plt.ylabel("Frequency")
plt.title("Age Distribution in Population")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()