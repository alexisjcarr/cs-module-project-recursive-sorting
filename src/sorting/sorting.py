# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """
    1) starting at the beginning of `a` and `b`
    2) compare the next value of each
    3) add smallest to `merged_arr`
    """
    merged_arr = []

    while arrA and arrB:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        else:
            merged_arr.append(arrA[0])
            arrA.pop(0)

    while arrA:
        merged_arr.append(arrA[0])
        arrA.pop(0)

    while arrB:
        merged_arr.append(arrB[0])
        arrB.pop(0)
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) == 0:
        return []

    elif len(arr) == 1:
        return arr

    elif len(arr) > 1:
        arr1 = merge_sort(arr[:len(arr)//2])
        arr2 = merge_sort(arr[len(arr)//2:])
        return merge(arr1, arr2)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
