Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def linear_search_product(product_list, target_product):
...     indices = []
...     for i in range(len(product_list)):
...         if product_list[i] == target_product:
...             indices.append(i)
...     return indices
... 
... products = ["apple", "banana", "apple", "orange", "apple"]
... target = "apple"
... result = linear_search_product(products, target)
... if not result:
...     print("Product not found.")
... else:
...     print("Product found at indices: ", end="")
...     for index in result:
...         print(index, end=" ")
