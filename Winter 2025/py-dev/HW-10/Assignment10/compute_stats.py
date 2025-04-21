# compute_stats.py
import sys
import statistics

def my_stats():
    data = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        val = float(line)
        # Ignore missing-data indicator
        if val == -9999:
            continue
        data.append(val)

    if not data:
        print("No valid data provided.")
        return

    mn = min(data)
    mx = max(data)
    avg = sum(data) / len(data)
    med = statistics.median(data)

    print(f"min: {mn}, max: {mx}, average: {avg}, median: {med}")

if __name__ == "__main__":
    my_stats()