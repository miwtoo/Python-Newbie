- ใช้ input() รับค่า 
```python
>>> name = input("Enter your name: ") # Prompt for and obtain name.
Enter your name: Ishmael
>>> # Greet user. However, the following produces an undesired space.
>>> print("Greetings", name, "!")
Greetings Ishmael !
>>> # Remove undesired spaces using the sep optional argument.
>>> print("Greetings ", name, "!", sep="")
Greetings Ishmael!
>>> age = input("Enter your age: ") # Prompt for and obtain age.
Enter your age: 37
```

- การใช้ int() , float() แปลงค่า
```python
>>> int("1492") # Convert string to an int.
1492
>>> int("1.414") # String must look like an int to succeed.
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ’1.414’
>>> # Explicit conversion of string allows following to succeed.
>>> int("1492") + 520
2012
>>> int(1.414) # Can convert a float to an int.
1
>>> int(2.999999) # Fractional part discarded -- rounding not done.
2
>>> int(-2.999999) # Same behavior for negative numbers.
-2
>>> float("1.414") # Conversion of string that looks like a float.
1.414
>>> float("1.414") * 1.414 # Arithmetic operation now works.
1.9993959999999997
>>> 1.414 * 1.414 # Result is same if we enter floats directly.
1.9993959999999997
```

- การใช้ eval() เป็นการแปลง สตริงให้อยู่ในรูปแบบต่างๆ ตามที่ใส่มา

```python
>>> string = "5 + 12" # Create a string.
>>> print(string) # Print the string.
5 + 12
>>> eval(string) # Evaluate the string.
17
>>> print(string, "=", eval(string))
5 + 12 = 17
>>> eval("print(’Hello World!’)") # Can call functions from eval().
Hello World!
>>> # Using eval() we can accept all kinds of input...
>>> age = eval(input("Enter your age: "))
Enter your age: 57.5
>>> age
57.5
>>> age = eval(input("Enter your age: "))
Enter your age: 57
>>> age
57
>>> age = eval(input("Enter your age: "))
Enter your age: 40 + 17 + 0.5
>>> age
57.5
```

```python
>>> eval("10, 32") # String with comma-separated values.
(10, 32)
>>> x, y = eval("10, 20 + 12") # Use simultaneous assignment.
>>> x, y
(10, 32)
>>> # Prompt for multiple values. Must separate values with a comma.
>>> x, y = eval(input("Enter x and y: "))
Enter x and y: 5 * 2, 32
>>> x, y
(10, 32)
```