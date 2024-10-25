# 1.b
# 2.b
# 3.c
# 4.a
# 5.c
# 6.a
# 7.a 
# 7.1.c
# 8.c 
# 9.a
# 10.d
# 11.b 
# 12.b
# 13.oroltiin elementuudiig daraalaltai hadgaldag hadgalah zai n todorhoi
# sanah oin zalgah hurd sain (0(1)) ghde hemjee n togtmol
# 14. systemd heregldeg ugugdliin butets LIFO(last in first out) zarchmaar ajildag
# tree olon hemjeest ugudliin butets tuhain elementees garah olon salbartai
# 15.c
# 16.a
# 17.b
# 18.c
import time

# Bubble Sort алгоритм
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# # Insertion Sort алгоритм
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# # Эхлэл
# input_list = [64, 34, 25, 12, 22, 11, 90]

# # Bubble Sort
# start_time = time.time()
# bubble_sorted = bubble_sort(input_list.copy())
# bubble_sort_time = time.time() - start_time

# # Insertion Sort
# start_time = time.time()
# insertion_sorted = insertion_sort(input_list.copy())
# insertion_sort_time = time.time() - start_time

# # Үр дүнг хэвлэх
# print("Bubble Sort үр дүн:", bubble_sorted)
# print("Insertion Sort үр дүн:", insertion_sorted)
# print("Bubble Sort хугацаа:", bubble_sort_time)
# print("Insertion Sort хугацаа:", insertion_sort_time)


# import heapq

# class Node:
#     def __init__(self, char, freq):
#         self.char = char
#         self.freq = freq
#         self.left = None
#         self.right = None

#     def __lt__(self, other):
#         return self.freq < other.freq

# def huffman_code(frequencies):
#     heap = [Node(char, freq) for char, freq in frequencies.items()]
#     heapq.heapify(heap)

#     while len(heap) > 1:
#         left = heapq.heappop(heap)
#         right = heapq.heappop(heap)

#         merged = Node(None, left.freq + right.freq)
#         merged.left = left
#         merged.right = right

#         heapq.heappush(heap, merged)

#     root = heap[0]
#     codes = {}
    
#     def generate_codes(node, current_code):
#         if node is not None:
#             if node.char is not None:
#                 codes[node.char] = current_code
#             generate_codes(node.left, current_code + "0")
#             generate_codes(node.right, current_code + "1")

#     generate_codes(root, "")
#     return codes

# # Жишээ дүн
# frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
# result = huffman_code(frequencies)
# print("Хаффман код:", result)

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert_rec(self.root, key)

#     def _insert_rec(self, root, key):
#         if key < root.val:
#             if root.left is None:
#                 root.left = Node(key)
#             else:
#                 self._insert_rec(root.left, key)
#         else:
#             if root.right is None:
#                 root.right = Node(key)
#             else:
#                 self._insert_rec(root.right, key)

#     def search(self, key):
#         return self._search_rec(self.root, key)

#     def _search_rec(self, root, key):
#         if root is None or root.val == key:
#             return root
#         if key < root.val:
#             return self._search_rec(root.left, key)
#         return self._search_rec(root.right, key)

#     def find_min(self):
#         return self._find_min_rec(self.root)

#     def _find_min_rec(self, root):
#         current = root
#         while current.left is not None:
#             current = current.left
#         return current.val

#     def find_max(self):
#         return self._find_max_rec(self.root)

#     def _find_max_rec(self, root):
#         current = root
#         while current.right is not None:
#             current = current.right
#         return current.val

# # Жишээ
# input_values = [20, 9, 25, 5, 12, 15, 30]
# bst = BinarySearchTree()

# for value in input_values:
#     bst.insert(value)

# # Хамгийн бага болон хамгийн их утгыг олох
# print("Minimum value:", bst.find_min())
# print("Maximum value:", bst.find_max())

# # Утга хайх
# search_value_1 = 12
# search_value_2 = 18
# print(f"Search {search_value_1}: {'Found' if bst.search(search_value_1) else 'Not found'}")
# print(f"Search {search_value_2}: {'Found' if bst.search(search_value_2) else 'Not found'}")

# def test_func(x):
#     if x % 2 == 0:  # x тэгш (even) эсэхийг шалгаж байна
#         return x * 2  # Хэрвээ тэгш бол, x-ийг 2 дахин ихэсгэж буцаана
#     else:
#         return x + 2  # Хэрвээ сондгой (odd) бол, x-ийг 2-оор ихэсгэж буцаана

# print(test_func(5))  # test_func-д 5 оруулна