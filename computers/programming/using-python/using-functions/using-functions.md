Consider the following code:
```python
def team_members(*members):
    print(type(member)) # Output: <class 'tuple'>

def character_attributes(**attribs):
    print(type(attribs)) # Output: <class 'dict'>

# Order matters, so this code will produce an error:
def order_matters(**kwargs, *positional_arguments): 
# Output: SyntaxError: invalid syntax
```
