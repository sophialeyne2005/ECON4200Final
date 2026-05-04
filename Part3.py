import pandas as pd

daily = pd.read_csv("AAPL_close.txt", header=None)
daily.head()

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(daily[0], marker='o')
plt.title("AAPL Daily Closing Prices")
plt.xlabel("Day Index")
plt.ylabel("Closing Price")
plt.grid(True)
plt.savefig("AAPL_graph.png")
plt.show()
