def merge(arr, left, mid, right):
    global k 
    left_half = arr[left:mid + 1] 
    right_half = arr[mid + 1:right + 1] 
    i = j = 0  
    idx = left  
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[idx] = left_half[i]
            i += 1
        else:
            arr[idx] = right_half[j]
            j += 1
            k += len(left_half) - i
        idx += 1
    while i < len(left_half):
        arr[idx] = left_half[i]
        i += 1
        idx += 1
    while j < len(right_half):
        arr[idx] = right_half[j]
        j += 1
        idx += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)  
        merge_sort(arr, mid + 1, right) 
        merge(arr, left, mid, right)  

n = int(input())  
a = list(map(int, input().split()))  

k = 0 
merge_sort(a, 0, n-1)  
print(k)
# grok.com qilib berdi
