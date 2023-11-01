# Write your solution for algorithm 3 below
def sort_list_descending(unsorted_list):
    sorted_list_descending = sorted(unsorted_list, reverse=True)
    return sorted_list_descending

# Example usage:
my_list = [4, 2, 7, 1, 9, 5]
sorted_descending_result = sort_list_descending(my_list)
print(sorted_descending_result)
