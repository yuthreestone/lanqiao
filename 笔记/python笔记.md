保留2位小数点:

```python
a=3.141593
print('%.2f' % a)
```



保留2位有效数字：

```python
a=3.141593
print('%.2g' % a)
```



回文数：

```python
a=str(112)
b=a[::-1]
```



切片：

```python
object[start_index : end_index : step]
```

（左闭右开



进制转换：

- 先用`int(n,x)`将x进制转换为十进制

- 再用`bin(n), oct(n), hex(n)`转换成二进制，八进制，十六进制

| **↓**  | 2进制         | 8进制         | 10进制         | 16进制         |
| ------ | ------------- | ------------- | -------------- | -------------- |
| 2进制  | -             | bin(int(n,8)) | bin(int(n,10)) | bin(int(n,16)) |
| 8进制  | oct(int(n,2)) | -             | oct(int(n,10)) | oct(int(n,16)) |
| 10进制 | int(n,2)      | int(n,8)      | -              | int(n,16)      |
| 16进制 | hex(int(n,2)) | hex(int(n,8)) | hex(int(n,10)) | -              |



reduce函数：

```python
from functools import reduce
listn = [1,2,3,4,5]  
print(reduce(lambda x,y:x+y,listn))
```

上述代码表示`listn`所有值连加。



小写字母转大写字母upper()，大写字母转小写字母lower()：

```python
string="abc"
upperString=string.upper()
```



列表：

`list.reverse()` 反向列表中的元素

`list.index(obj)` 返回obj值第一个匹配项的索引位置

`list.count(obj)` 返回obj值在列表中出现的次数

`list.remove(obj)` 移除obj值的第一个匹配项

`list.insert(index,obj)` 将obj插入列表中索引为index的位置

`list.pop(index)`移除列表中index位置的元素，返回它的值



对列表排序：

```python
list.sort(key=None,reverse=False)   #对原列表排序
sorted(list,key=None,reverse=False) #返回排序后的新列表
```

key：用来进行比较的元素

reverse：reverse=True降序，reverse=False升序

```python
listn=[[1,2],[3,4],[3,1],[7,3],[3,3]]
listans=sorted(listn,key=lambda n:n[1])
print(listans)  #[[3, 1], [1, 2], [7, 3], [3, 3], [3, 4]]
listans=sorted(listn,key=lambda n:(n[1],n[0]))  #先按n[1]排列，n[1]相同按n[0]排
print(listans)  #[[3, 1], [1, 2], [3, 3], [7, 3], [3, 4]]
listans=sorted(listn,key=lambda n:n[1],reverse=True)
print(listans)  #[[3, 4], [7, 3], [3, 3], [1, 2], [3, 1]]
```



深拷贝浅拷贝：

```python
import copy
list1=[1,2,3,4,[5,6]]
list2=list1    #浅拷贝，完全复制list1的地址
list3=list1[:]           #浅拷贝，list3，4相同，list3对list1中的元素进行深拷贝，
list4=copy.copy(list1)   #但是对嵌套的列表直接复制地址，对嵌套的列表是浅拷贝
list5=copy.deepcopy(list1)  #深拷贝，嵌套的列表也是深拷贝
list1[0]=0
list1[4][1]=0
print(list1)			#[0, 2, 3, 4, [5, 0]]
print(list2)			#[0, 2, 3, 4, [5, 0]]
print(list3)			#[1, 2, 3, 4, [5, 0]]
print(list4)			#[1, 2, 3, 4, [5, 0]]
print(list5)			#[1, 2, 3, 4, [5, 6]]
```



比较两个列表相同位置元素是否相同：

```python
import operator
list1=[1,2,3]
list2=[1,2,3]
print(operator.eq(list1,list2))		#True
list1=[1,[2,3]]
list2=[1,[2,3]]
print(operator.eq(list1,list2))		#True
```



复数：

```python
x=complex(1,2)		#x=1+2j
y=complex("1+2j")	#y=1+2j
```



eval():

返回字符串表达的值

```python
print(eval("1+2"))           #3
print(eval("pow(3,2)"))		 #9
listn=eval("[1,2,3,[4,5]]")  #返回字符串表达的列表
print(listn[2])				 #3
```



print():

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

sep：存在多个输出对象的间隔符，默认为空格‘ ’

end：结尾符，默认为换行'\n'

file：要写入的文件对象，默认为sys.stdout即输出到屏幕

flush：输出是否被缓存



reversed():

```python
listn=[1,2,3]
print(list(reversed(listn)))		#[3,2,1]
```



format格式化函数：

```python
print("{1} {0} {1}".format("hello", "world") )
#world hello world
```

数字格式化：

| 数字       | 格式    | 输出      | 描述                         |
| :--------- | :------ | :-------- | :--------------------------- |
| 3.1415926  | {:.2f}  | 3.14      | 保留小数点后两位             |
| 3.1415926  | {:+.2f} | +3.14     | 带符号保留小数点后两位       |
| 0.25       | {:.2%}  | 25.00%    | 百分比格式                   |
| 1000000000 | {:.2e}  | 1.00e+09  | 指数记法                     |
| 13         | {:>10d} | 13        | 右对齐 (默认, 宽度为10)      |
| 13         | {:<10d} | 13        | 左对齐 (宽度为10)            |
| 13         | {:^10d} | 13        | 中间对齐 (宽度为10)          |
| 5          | {:0>2d} | 05        | 数字补零 (填充左边, 宽度为2) |
| 5          | {:x<4d} | 5xxx      | 数字补x (填充右边, 宽度为4)  |
| 1000000    | {:,}    | 1,000,000 | 以逗号分隔的数字格式         |



decimal模块 精确计算:

```python
import decimal

decimal.getcontext().prec=51		#将精度设为小数点后51位
num=decimal.Decimal(1)
for i in range(1000):
    num=1/(1+num)
print("{:.50f}".format(num))          #输出小数点后50位
#0.61803398874989484820458683436563811772030917980576
```

