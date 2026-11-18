import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    data = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)
    dates = data[:, 0]
    flows = data[:, 1:6].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    step = 250
    for index, site in enumerate(sites):
        plt.plot(dates, flows[:, index], label=f'Site {site}')

    plt.title('Provo River Streamflow Rates - June 2021')
    plt.xlabel('Date')
    plt.ylabel('Discharge (cfs)')
    plt.xticks(ticks=range(0, len(dates), step), labels=dates[::step], rotation=45)
    plt.legend()
    plt.grid(True)
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
