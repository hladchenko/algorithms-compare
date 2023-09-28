import random
import time

import BubbleSort
import InsertionSort
import MergeSort


def get_execution_time(choice):
  i = 2
  while i < 10_000_000:
    total_time, repeats = 0, 10
    for j in range(repeats):
      arr = generate_array()
      start_time = time.time()
      if choice == 1:
        BubbleSort.bubble_sort(arr)
      elif choice == 2:
        InsertionSort.insertion_sort(arr)
      elif choice == 3:
        MergeSort.merge_sort(arr)
      execution_time = time.time() - start_time
      total_time += execution_time
    average_execution_time = total_time / repeats
    print(i, " ", average_execution_time)
    i *= 2


def generate_array():
  arr = []
  for i in range(10):
    arr.append(random.randint(0, 10))
  return arr


print("Bubble sort")
get_execution_time(1)

print("Insertion sort")
get_execution_time(2)

print("Merge sort")
get_execution_time(3)
