def insertion_sort(arr):
  for i in range(1, len(arr)):
    current, j = arr[i], i - 1
    j = i - 1
    while j >= 0 and current < arr[j]:
      arr[j + 1], j = arr[j], j - 1
    arr[j + 1] = current
  return arr


arr = [5, 10, -1, -100, 3, 17]
print(insertion_sort(arr))
