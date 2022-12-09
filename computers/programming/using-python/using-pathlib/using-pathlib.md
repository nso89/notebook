Consider the following code:
```python
documents = Path(Path.home()).joinpath("Documents").iterdir()
print(type(documents)) # Output: <class 'generator'>
```
