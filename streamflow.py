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


def summarize(dates, flows, sites):
    """Print a formatted gauge summary and write it to a CSV file."""
    # Excel check for gauge 10163000: Max = 131.0, Avg = 57.0

    print(f"{'Gauge':<10} {'Max (cfs)':>10} {'Date of max':<20} {'Min (cfs)':>10} {'Avg (cfs)':>10}")

    with open("streamflow_summary.csv", "w", newline="") as f:
        f.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

        for i, site in enumerate(sites):
            col = flows[:, i]
            max_idx = np.argmax(col)
            max_val = col[max_idx]
            max_date = dates[max_idx]
            min_val = np.min(col)
            avg_val = np.mean(col)

            print(f"{site:<10} {max_val:>10.1f} {max_date:<20} {min_val:>10.1f} {avg_val:>10.1f}")
            f.write(f"{site},{max_val:.1f},{max_date},{min_val:.1f},{avg_val:.1f}\n")


sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)
