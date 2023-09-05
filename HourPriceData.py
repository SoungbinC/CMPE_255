import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame(
    {
        "Price": [13300000, 12250000, 12250000, 12215000, 11410000],
        "Area": [7420, 8960, 9960, 7500, 7420],
    }
)

# Scatter plot
plt.scatter(df["Area"], df["Price"])
plt.title("Scatter Plot of Price vs Area")
plt.xlabel("Area (square feet)")
plt.ylabel("Price (dollars)")
plt.grid(True)
plt.show()
