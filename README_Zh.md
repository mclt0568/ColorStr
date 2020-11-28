# ColorStr
ColorStr是一個可以使顏色輸出變得簡單好用的Python模塊

讓輸出文字的代碼不再看不懂！

### 安裝

在終端輸入 `pip install ColorStr` 安裝 (較推薦)，或者從 [Releases](https://www.github.com/mclt0568/ColorStr/releases) 下載代碼來使用。 

### 用法

一般要在終端中輸出帶有顏色的文字時，要使用`\033[XXm]`來做標識。
```python
print("\033[31mIm red") #輸出紅色的"Im red"
print("\033[32mIm green") #輸出綠色的"Im green"
```
當輸出的文字較爲簡單時，整體代碼還算工整。
但是當輸出的文字比較複雜時，整體代碼的可讀性也會指數型下降

```python
print("\033[32;1mLorem Ipsum!\033[0m\n\033[31;1mL\033[0;31moremipsum")
#以上代碼會輸出:
#Lorem Ipsum (加粗綠色)
#L(加粗紅色) oremipsum (紅色)
```

當使用 **ColorStr** 時

```python
from ColorStr import parse

print(parse("§rRed Line!")) #輸出紅色的"Red Line!"
print(parse("§gGreen Line!")) #輸出綠色的"Green Line!"

print(parse("§GLorem Ipsum!"))
print(parse("§RL§0§roremipsum"))
```
不僅用起來簡單，也大幅優化了可讀性。

### 對照表

**注：不是所有終端都支持所有顏色與格式，請在使用前先做測試* 

| 顏色名稱         | 前景顏色 | 背景顏色 |
| ---------------- | -------- | -------- |
| 黑               | §k       | ƒk       |
| 紅               | §r       | ƒr       |
| 綠               | §g       | ƒg       |
| 黃               | §y       | ƒy       |
| 藍               | §b       | ƒb       |
| 洋紅(品紅)       | §m       | ƒm       |
| 青               | §c       | ƒc       |
| 白               | §w       | ƒw       |
| 黑(加粗)         | §K       | ƒK       |
| 紅(加粗)         | §R       | ƒR       |
| 綠(加粗)         | §G       | ƒG       |
| 黃(加粗)         | §Y       | ƒY       |
| 藍(加粗)         | §B       | ƒB       |
| 洋紅(品紅)(加粗) | §M       | ƒM       |
| 青(加粗)         | §C       | ƒC       |
| 白(加粗)         | §W       | ƒW       |



| 格式 | 代碼 |
| ---------- | ---- |
| 重置所有格式 | §0  |
| 加粗  | §1  |
| 加深    | §2  |
| 斜體    | §3  |
| 下劃線（底線） | §4  |
| 閃爍   | §5  |
| 取消顏色反轉 | §6  |
| 顏色反轉（背景與前景） | §7  |
| 隱藏文字  | §8  |
| 中劃線   | §9  |

### 開發貢獻:
[@yxliang01](https://www.github.com/yxliang01)