Consider the following code:

```python
svetlana  : tuple = ("Empress Svetlana",25,"Trance")

# *middle - is a list.
first_element, *middle, last_element = svetlana
print(type(middle)) # Output: <class 'list'>

print(*middle) # Output: 25
# With the *, it returns an int, because 25 is the only element left in the list.
print(type(*middle)) # Output: <class 'int'> 

# Suppose we had 4 elements in our tuple:
svetlana : tuple = ("Empress Svetlana",25,69,"Trance")
    
# Using *middle with print seems to extract the elements.
print(*middle) # Output: 25,69

# It's attempting to test the type of the two elements.
print(type(*middle)) # Output: TypeError: type() takes 1 or 3 arguments
```

All the operations availbe for `sequence` are availbe for `tuple`.

External Reading:

[Extended Iterable Unpacking](https://peps.python.org/pep-3132/)
