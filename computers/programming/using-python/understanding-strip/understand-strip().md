Just like <code>tuple</code> and <code>list</code>, <code>string</code> has an index for each element. You can visualize it like this:

```
h  e  l  l  o     w  o  r  l  d
-------------------------------
0  1  2  3  4  5  6  7  8  9 10
```

In code, this would look like:

```python
>>> introduction : str = "Hello World"
>>> print(len(introduction))
11
```

If you attempt to change any element like you would a <code>list</code>, it will return a <code>TypeError</code>:

```python
>>> introduction[1] = "w"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

When you have whitespace on both sides, you can think of them as empty indices:

```
      h  e  l  l  o     w  o  r   l   d
------------------------------------------------
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14
```

In code, this would look like:

```python
>>> introduction : str = "  Hello World  "
>>> print(len(introduction))
15
```

When we use <code>strip()</code>, we're removing the blank indices, no matter how many:

```python
>>> stripped_introduction = introduction.strip() # strip() returns a new string.
>>> print(len(stripped_introduction))
11
```
