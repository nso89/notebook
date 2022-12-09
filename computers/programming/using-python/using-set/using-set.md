Using `[]` with `set()`:
```python
# Remeber to include the [] inside the set() constructor:
letters = set([a,b,c,d]) # -- Correct
letters = set("a","b","c","d") # -- Incorrect. Will return TypeError.
```
Using `__eq__()`:
```python
# It doesn't matter the order of the elements, __eq__() 
# will determine which sets are equal and which aren't:

first_set = set([47,69,21])
second_set = set([69,21,47])
third_set = set([69,88,27])
    
print(first_set) # Output: {21, 69, 47}
print(second_set) # Output: {21, 69, 47}

print(first_set == second_set) # Output: true
print(first_set == third_set) # Output: false
```
