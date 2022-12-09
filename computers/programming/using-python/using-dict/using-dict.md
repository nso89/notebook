Using `for` with `enumerate()`:
```python
# Using a for loop with enumerate() will assign the index to the key and the pair as the value:
weapons : Dict[str,int] = {"Sword" : 20, "Axe": 10, "Bow": 15}

for key, value in enumerate(weapons.items(), start = 1):
    # The first pair is Sword : 20, but because enumerate returns an index,
    # key will be 1 (the index returned from enumerate) and value will be the pair Sword:20.
    print(f"Key: {key} Value: {value}")

# Output:
Key: 1 Value: ('Sword', 20)
Key: 2 Value: ('Axe', 10)
Key: 3 Value: ('Bow', 15)
```
