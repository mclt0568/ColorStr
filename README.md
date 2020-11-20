# ColorStr
A python lib, A better way. 
Rainbowlize your Terminal

ColorStr is a library simplifies outputting color and readable!

### How To Install

Use `pip install ColorStr` Or download from [Releases](https://www.github.com/mclt0568/ColorStr/releases)

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

### List of formatting

**Note : not all terminal supports formatting. Please check before using it in your project* 

| Color Name   | Foreground | Background |
| ------------ | ---------- | ---------- |
| Black        | §k         | ƒk         |
| Red          | §r         | ƒr         |
| Green        | §g         | ƒg         |
| Yellow       | §y         | ƒy         |
| Blue         | §b         | ƒb         |
| Megenta      | §m         | ƒm         |
| Cyan         | §c         | ƒc         |
| White        | §w         | ƒw         |
| Bold Black   | §K         | ƒK         |
| Bold Red     | §R         | ƒR         |
| Bold Green   | §G         | ƒG         |
| Bold Yellow  | §Y         | ƒY         |
| Bold Blue    | §B         | ƒB         |
| Bold Megenta | §M         | ƒM         |
| Bold Cyan    | §C         | ƒC         |
| Bold White   | §W         | ƒW         |



| Formatting | Code |
| ---------- | ---- |
| Reset All Formatting       | §0  |
| Bold (or brighter color)      | §1  |
| Darken      | §2  |
| Italic      | §3  |
| Underlined      | §4  |
| Blinking      | §5  |
| Un-Inverse Color      | §6  |
| Inverse Color (Forground and Background)      | §7  |
| Hide Charactors      | §8  |
| Crossover      | §9  |

### Contributor:
[@yxliang01](https://www.github.com/yxliang01)
