def max_activities(activities):
    # Sort the activities based on finishing time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # Initialize variables
    count = 1
    last_activity = 0
    
    # Iterate through the activities
    for i in range(1, len(sorted_activities)):
        if sorted_activities[i][0] >= sorted_activities[last_activity][1]:
            count += 1
            last_activity = i
    
    return count

# Function to take user input for activities
def get_activities_from_user():
    activities = []
    n = int(input("Enter the number of activities: "))
    for i in range(n):
        start, finish = map(int, input(f"Enter starting and finishing time of activity {i+1} (separated by space): ").split())
        activities.append((start, finish))
    return activities

# Example usage:
activities = get_activities_from_user()
max_activities_count = max_activities(activities)
print("Maximum number of activities performed by a single person:", max_activities_count)
