import time, random, matplotlib.pyplot as plt, numpy as np
def comb_sort(arr):
    def swap(arr, one, two):
        copy = arr[one]
        copy2 = arr[two]
        arr[one] = copy2
        arr[two] = copy
    flag = True
    factor = len(arr)//2
    end_it = False
    while end_it == False:
        flag = False
        y = 0
        while y+factor < len(arr):
            if arr[y] > arr[y+factor]:
                swap(arr, y, y+factor)
                flag = True
            y += 1
        if flag == False:
            break
        if factor == 1:
            end_it = True
        if factor < 1:
            factor = 1
        else:
            factor = (factor * 10)//13
    return arr
def merge(list1, list2):
  posin1 = 0
  while True:
    try:
      if posin1 == 0 and list2[0] < list1[0]:
        list1.insert(0, list2[0])
        del list2[0]
      if len(list2) == 0:
        return list1
      if list1[posin1] <= list2[0] <= list1[posin1+1]:
        list1.insert(posin1+1, list2[0])
        posin1 += 1
        del list2[0]
      else:
        posin1 += 1
      if posin1 > len(list1)-1:
        break
    except IndexError:
      list1.extend(list2)
      return list1
  list1.extend(list2)
  return list1

def mergesort(arr):
  if len(arr) == 1:
    return arr
  middle = len(arr)//2
  left = arr[:middle]
  right = arr[middle:]
  return merge(mergesort(left), mergesort(right))

def bubble_sort(arr):
    def swap(arr, one, two):
        copy = arr[one]
        copy2 = arr[two]
        arr[one] = copy2
        arr[two] = copy
    flag = True
    for x in range(len(arr)-1):
        flag = False
        for y in range(len(arr)-x-1):
            if arr[y] > arr[y+1]:
                swap(arr, y, y+1)
                flag = True
        if flag == False:
            break
    return arr

comb_sort_times = []
merge_sort_times = []
bubble_sort_times = []
testing_range = int(input('Enter range to test: '))
for x in range(1, testing_range+1):
    arr = list(range(x))
    random.shuffle(arr)
    start = time.time()
    mergesort(arr)
    end = time.time()
    merge_sort_times.append(round(end-start, 6))
    random.shuffle(arr)
    start = time.time()
    comb_sort(arr)
    end = time.time()
    comb_sort_times.append(round(end-start, 6))
    random.shuffle(arr)
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    bubble_sort_times.append(round(end-start, 6))
plt.plot(np.array(range(1, testing_range+1)), np.array(comb_sort_times))
plt.plot(np.array(range(1, testing_range+1)), np.array(merge_sort_times))
plt.plot(np.array(range(1, testing_range+1)), np.array(bubble_sort_times))
plt.show()
