- การ กำหนดค่า ให้กับ x ,y, z พร้อมๆกัน

```python
>> z = y = x = 2 + 7 + 2
>> x, y, z
(11, 11, 11)
```




- การสลับค่าของตัวแปลได้เลยโดยไม่ต้องมี ตัวแปลอื่นรองรับก่อน

```Python
>>> c = "deepSecret" # Set current password.
>>> o = "you’ll never guess" # Set old password.
>>> c, o # See what passwords are.
(’deepSecret’, "you’ll never guess")
>>> c, o = o, c # Exchange the passwords.
>>> c, o # See what passwords are now.
("you’ll never guess", ’deepSecret’)
```




- การกำหนดค่าพร้อมกันอีกแบบ

```Python

>>> # A bad use of simultaneous assignment.
>>> x, y = (45 + 34) / (21 - 4), 56 * 57 * 58 * 59
>>> x, y
(4.647058823529412, 10923024)
>>> # A better way to set the values of x and y.
>>> x = (45 + 34) / (21 - 4)
>>> y = 56 * 57 * 58 * 59
>>> x, y
(4.647058823529412, 10923024)
```




- การใช้ Underscore บอกค่าล่าสุด

```Python
>>> 5 + 4 # Enter an expression.
9
>>> _ # See that _ is equal to value of last expression.
9
>>> _ + 27 # Use _ in new expression.
36
>>> print(_) # See that _ has been reset.
36
>>> _ - 15
21
>>> result = _ # Store value of _ to a variable.
>>> result
21
```




- ยกกำลังได้เลย ถ้าเป็นภาษาอื่นๆ ต้องเป็นการเรียกใช้ฟังก์ชันยกกำลัง

```Python

>>> 2 ** 3
8
>>> 2 ** 3 ** 4 # Operator is right associative.
2417851639229258349412352
>>> 3 ** 4
81
>>> (2 ** 3) ** 4 # Use parentheses to change order of operation.
4096
>>> 3 ** 400 # A big number. Exact value as an int.
70550791086553325712464271575934796216507949612787315762871223209262085
55158293415657929852944713415815495233482535591186692979307182456669414
5084454535257027960285323760313192443283334088001
>>> 3.0 ** 400 # A big number. Approximate value as a float.
7.055079108655333e+190
```




- หารแบบไม่เอาทศนิยมหลังจุด โดยใช้ //

```Python

>>> time = 257 # Time in seconds.
>>> minutes = time // 60 # Number of complete minutes in time.
>>> print("There are", minutes, "complete minutes in", time, "seconds.")
There are 4 complete minutes in 257 seconds.
>>> 143 // 25
5
>>> 143.4 // 25
5.0
>>> 9 // 2.5
3.0
```

- ฟังก์ชัน divmod(x, y) จะเหมือนกับการใช้ 
```Python
x // y, x % y
```
