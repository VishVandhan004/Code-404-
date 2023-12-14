import matplotlib.pyplot as plt 
import numpy as np
sales_data=[10000,12000,8000,11000,9500]
window_size=4
sma=np.convolve(sales_data, np.ones(window_size)/window_size, mode='valid')
# Generate corresponding weeks for the SMA calculation
weeks = np.arange(1, len(sales_data)+1)
sma_weeks = np.arange(window_size, len(sales_data)+1)
# Plotting the original data and the SMA line
plt.figure(figsize=(10, 6))
plt.plot(weeks, sales_data, label='Original Sales Data', marker="o")
plt.plot(sma_weeks, sma, label='4-Week SMA', marker='o', color="red")
plt.title('Retail Store Weekly Sales with 4-Week SMA')
plt.xlabel('Weeks')
plt.ylabel('Sales($USD)')
plt.legend()
plt.grid(True)
plt.show()