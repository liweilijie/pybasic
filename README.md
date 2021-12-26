# python 基础

**python**的项目有时候一些基础知识不牢固,导致出了很多问题.所以需要多加强一下基础知识.


```python
# int(python也没有short,long之分)
# float(python没有单双精度之分,因为python里面默认是双精度一种类型)
type(1)
type(1.1)
type(1.1111111111111)
type(1+0.1)
type(1+1.0) # float

# TODO: 牢记下面这个知识点 // 表示整除
type(2/2) # float
type(2//2) # int
type(1//2) # int

# 2进制
0b10
# 8进制
0o10
# 16进制
0x1F
# 其他进制转换2进制
bin(10), bin(0o7), bin(0xE)
# 其他进制转换8进制
oct(0b111),oct(0x777)
# 其他进制转换10进制
int(0b11), int(0o77)
# 其他进制转换16进制
hex(888), hex(0o7777)

# 布尔类型
True, False
bool(0) # 表示False 非0表示True
# 复数 complex

# 字符串, 单引号,双引号,三引号(可以是三个单引号或者三个双引号)
# 单引号和双引号表示的意思是一样的.
a = "let's go" # 这样就很方便了
a = '''
hello 回车了
end.
'''
# r原始字符串 raw str 
print(r'c:\northwind\northwest')

# list 列表 非常灵活
type([1,2,3,4,5,6])
type(["hello", 1, 9, True, False, "world"])
type([[1,2],[3,4],[True, False]])

# tuple 元组
(1,2,3,4)
type((1)) # int
type((1,)) # tuple

# str, list, tuple序列 共有的操作
3 in [1,2,3,4,5] # True
3 not in [1,2,3,4,5] # False
len((1,2,3,4,5)) # 5
max([1,2,3,4,5,6]) # 6
min([1,2,3,4,5,6]) # 1

# 集合: set dict 
# 集合最大的特点是无序的, 无序的话就不能用下标或者切片操作来找值
# 集合是不重复的
# set
type({1,2,3,4,5,6}) # set 类型
len({1,2,3})
1 in {1,2,3}
1 not in {1,2,3}
type(set()) # 定义空set
type({}) # 定义空的dict

# dict
{1:"hello", "1": "world", (1,2,3):"ok"}

# 值类型和引用类型
# 值类型: 字符串,元组,数值 本身不允许被修改
# 引用类型: 列表,集合,字典 本身允许修改

```


包 >> 模块 >> 类 >> 函数,变量