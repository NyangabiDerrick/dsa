# By Ariel Boutcher
# Heap Sort - O(n log n) time complexity, O(1) space complexity
# Uses max-heap data structure for in-place sorting

def heapify(arr, n, i):
    """Maintain max-heap property for subtree rooted at index i"""
    largest = i           # Start by assuming current node is largest
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is bigger than current largest
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is bigger than current largest
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If a bigger child was found, swap and recursively heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Sort array using heap sort algorithm"""
    n = len(arr)

    # Phase 1: Build max-heap from unordered array
    # Start from last parent node and move up to root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr

# Example usage
if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Before:", numbers)
    heap_sort(numbers)
    print("After heap sort:", numbers)
