Consider the following code:
```python
print(type(filter(divide_by_two,zero_reminder))) # Output: <class 'filter'>
print(type(map(multiply_by_two, zero_reminder))) # Output: <class 'map'>
```
In other words, we'll get the return values as they're coming in (on the fly).

When using a <code>for</code> loop and an <code>if</code> statement to perform an operation, we can use <code>filter()</code> to generate the results:
```python
zero_reminder : List[int] = [1,2,3,4,5,6,7,8,9,10]
for number in zero_reminder:
    if number % 2 == 0:
        print(number)
            
filter(divide_by_two,zero_reminder)
```

When using a <code>for</code> loop perform an operation of all elements of an <code>iterable</code>:
```python
for number in zero_reminder:
    print(number * 2)

map(multiply_by_two, zero_reminder)
```
