#快速排序
def quick_sort(arr):#取一个中心数，根据比较左右值与中心数的大小来进行交换。
    def partition(arr, start, end):
        tmp = arr[start]
        while start < end:
            while arr[end] >= tmp and start < end:
                end -= 1
            arr[start] = arr[end]
            while arr[start] <= tmp and start < end:
                start += 1
            arr[end] = arr[start]
        arr[start] = tmp
        return start

    def quick_sort(arr, start, end):#分割两部分后，递归。
        if start < end:
            mid = partition(arr, start, end)
            quick_sort(arr, start, mid - 1)
            quick_sort(arr, mid + 1, end)
    if arr is None or len(arr) <= 1:
        return arr

    result = arr.copy()
    quick_sort(result, 0, len(arr) - 1)
    return result


arr = [64,34,25,12,22,11,90]
sort_arr = quick_sort(arr)
print(sort_arr)


#冒泡排序
# def bubbles_sort(arr):
#     if arr is None or len(arr) <= 1:
#         return arr
#     result = arr.copy()
#     n = len(result)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n - i - 1):
#             if result[j] > result[j + 1]:
#                 result[j], result[j + 1] = result[j + 1], result[j]
#                 swapped = True
#         if not swapped:
#             break
#     return result
#
# arr = [64,34,25,12,22,11,90]
# sorted_arr = bubbles_sort(arr)
# print(sorted_arr)




