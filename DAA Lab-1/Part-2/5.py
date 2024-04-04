def merge_overlapping_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on start times
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = [sorted_intervals[0]]

    for interval in sorted_intervals[1:]:
        last_interval = merged_intervals[-1]

        # Check for overlap
        if interval[0] <= last_interval[1]:
            # Merge intervals
            merged_intervals[-1] = (last_interval[0], max(last_interval[1], interval[1]))
        else:
            # No overlap, add interval to merged list
            merged_intervals.append(interval)

    return merged_intervals

# Function to take user input for intervals
def get_intervals_from_user():
    intervals = []
    n = int(input("Enter the number of intervals: "))
    for i in range(n):
        start, end = map(int, input(f"Enter start and end of interval {i+1} (separated by space): ").split())
        intervals.append((start, end))
    return intervals

# Example usage:
intervals = get_intervals_from_user()
merged_intervals = merge_overlapping_intervals(intervals)
print("Non-overlapping intervals after merging:", merged_intervals)
