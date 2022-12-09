#### Using `str`:
```python
# To verify that strip worked, you can use len() to return the index:
character_name = " Empress Svetlana "
print(len(character_name)) # Output: 18

# using strip() and len():
print(len(character_name.strip())) # Output 16
```

#### Using `split()`:
```python
# `split()` will return a `list`:
print(type(introduction.split(" "))) # Output: <class 'list'> 
```
