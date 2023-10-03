import random
import time

import BubbleSort
import InsertionSort
import MergeSort


def get_execution_time(choice):
  i = 2
  while i < 20_000:
    total_time, repeats = 0, 10
    for j in range(repeats):
      arr = generate_array(i)
      start_time = time.time_ns()
      if choice == 1:
        BubbleSort.bubble_sort(arr)
      elif choice == 2:
        InsertionSort.insertion_sort(arr)
      elif choice == 3:
        MergeSort.merge_sort(arr)
      execution_time = time.time_ns() - start_time
      total_time += execution_time
    average_execution_time = total_time / repeats
    print(i, " ", average_execution_time)
    i *= 2


def generate_array(i):
  arr = []
  for i in range(i):
    arr.append(random.randint(0, i))
  return arr


print("Bubble sort")
get_execution_time(1)

print("Insertion sort")
get_execution_time(2)

print("Merge sort")
get_execution_time(3)
