- การสร้าง Function
```python
def <function_name>(<params>):
    <body>
```

- OPTIONAL PARAMETERS
```python
>>> def power(x, exponent=2):
... return x ** exponent
...
>>> power(10) # 10 squared, i.e., 10 ** 2.
100
>>> power(3) # 3 squared, i.e., 3 ** 2.
9
>>> power(3, 0.5) # Square root of 3, i.e., 3 ** 0.5.
1.7320508075688772
>>> power(3, 4) # 3 ** 4
81
>>> power(2, exponent=3) # 2 ** 3
8
>>> power(x=3, exponent=3) # 3 ** 3
27
>>> power(exponent=3, x=5) # 5 ** 3
125
>>> power(exponent=3, 5) # Error!
File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
```
```python
>>> def line(x, m=1, b=0):
... return m * x + b
...
>>> line(10) # x=10 and defaults of m=1 and b=0.
10
>>> line(10, 3) # x=10, m=3, and default of b=0.
30
>>> line(10, 3, 4) # x=10, m=3, b=4.
34
>>> line(10, b=4) # x=10, b=4, and default of m=1.
14
>>> line(10, m=7) # x=10, m=7, and default of b=0.
70
```