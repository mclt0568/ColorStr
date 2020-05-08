# ColorStr
A python lib, A better way. 
Rainbowlize your Terminal

ColorStr is a library simplifies outputting color and readable!

### How To Install

Still registering in pypi.
For now, download from [Releases](/mclt0568/ColorStr/releases/latest)

### How To Use

This is usually how you print a colored output.
```python
print("\033[31mIm red") #Prints a red line
print("\033[32mIm green") #Prints a green line.
```
As you can see, this is still readable.
But when the line is long, it's not going to be human-friendly. Like this:
```python
print("\033[32;1mLorem Ipsum!\033[0m\n\033[31;1mL\033[0;31moremipsum")
#Prints:
#Lorem Ipsum (green, bold)
#L(red,bold) oremipsum (red, non-bold)
```

This is **ColorStr**

```python
from ColorStr import parse

print(parse("§rRed Line!")) #Prints red line
print(parse("§gGreen Line!")) #Prints green line

print(parse("§GLorem Ipsum!"))
print(parse("§RL§0§roremipsum"))
```
This is not only easier to use, it's also much more readable.
