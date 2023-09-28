def merge_sort(arr):
  if len(arr) > 1:
    middle = round(len(arr) / 2)
    left = array_copy(arr, 0, middle)
    right = array_copy(arr, middle, len(arr))
    merge_sort(left)
    merge_sort(right)
    return merge(arr, left, right)


def merge(arr, left, right):
  i, j, k = 0, 0, 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k], k, i = left[i], k + 1, i + 1
    else:
      arr[k], k, j = right[j], k + 1, j + 1
  while i < len(left):
    arr[k], k, i = left[i], k + 1, i + 1
  while j < len(right):
    arr[k], k, j = right[j], k + 1, j + 1
  return arr


def array_copy(arr, start, end):
  res = []
  for i in range(start, end):
    res.append(arr[i])
  return res
