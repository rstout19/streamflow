import matplotlib.pyplot as plt
import numpy as np

data_provo = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',', dtype=str, skip_header=1)

x = data_provo[:, 0]
y_1 = data_provo[:, 1].astype(float)
y_2 = data_provo[:, 2].astype(float)
y_3 = data_provo[:, 3].astype(float)
y_4 = data_provo[:, 4].astype(float)
y_5 = data_provo[:, 5].astype(float)

step = 250
plt.plot(x, y_1, label='Site 10163000')
plt.plot(x, y_2, label='Site 10155200')
plt.plot(x, y_3, label='Site 10155500')
plt.plot(x, y_4, label='Site 10154200')
plt.plot(x, y_5, label='Site 10155000')

plt.title('Provo River Streamflow Rates - June 2021')
plt.xlabel('Date')
plt.ylabel('Discharge (cfs)')

plt.xticks(ticks=range(0, len(x), step), labels=x[::step], rotation=45)
plt.legend()
plt.grid(True)
plt.show()
