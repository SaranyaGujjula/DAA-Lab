import heapq

def merge_sorted_lists(sorted_lists):
    result = []
    heap = []

    # Initialize the heap with the first element from each list along with their list index
    for i, lst in enumerate(sorted_lists):
        if lst:  # Check if the list is not empty
            heapq.heappush(heap, (lst[0], i, 0))  # (element, list_index, element_index)

    while heap:
        min_element, list_index, element_index = heapq.heappop(heap)
        result.append(min_element)

        # Check if there are more elements in the list, if yes, push the next element to the heap
        if element_index + 1 < len(sorted_lists[list_index]):
            next_element = sorted_lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_element, list_index, element_index + 1))

    return result

# Function to take user input for sorted lists
def get_sorted_lists_from_user():
    m = int(input("Enter the number of sorted lists: "))
    n = int(input("Enter the number of elements in each list: "))
    sorted_lists = []

    for i in range(m):
        print(f"Enter {n} elements for list {i + 1} (separated by spaces):")
        elements = list(map(int, input().split()))
        sorted_lists.append(elements)

    return sorted_lists

# Example usage:
sorted_lists = get_sorted_lists_from_user()

print("\nSorted Lists:")
for lst in sorted_lists:
    print(lst)

print("\nMerged Sorted List:")
result = merge_sorted_lists(sorted_lists)
print(result)
