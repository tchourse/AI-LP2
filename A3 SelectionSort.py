""" Selection sort in Python

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [9678, 415, 0, 161, 7]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)"""


def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
             # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        array[step], array[min_idx] = array[min_idx], array[step]

# Take user input for the array
input_str = input("Enter numbers separated by spaces: ")
data = list(map(int, input_str.split()))

selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
