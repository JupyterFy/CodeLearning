# 记录一些学习过程中的代码

a = [ 1, 342, 223, 'India', 'Fedora']

python  中有关下标的集合都满足左闭右开原则，切片中也是如此，也就是说集合左边界值能取到，右边界值不能取到。

a[0:-1] = [ 1, 342, 223, 'India']

a[2,-2] = [223]

 切片的索引有非常有用的默认值；省略的第一个索引默认为0，省略的第二个索引默认为切片的字符串的大小：
 
 a[:-2] = [ 1, 342, 223]
 
 a[-2:] = ['India', 'Fedora']
 
 对于非负索引，如果上下都在边界内，切片长度就是两个索引之差。例如a[2:4]切片的长度是2
 
 试图使用太大的索引会导致错误【Index Error: list index out of range】。另外Python能够优雅地处理那些没有意义的切片索引：
 
 （1）一个过大的索引值（即大于列表实际长度）将被列表实际长度所代替；
 
 a[2:32] =  [223, 'India', 'Fedora']
 
 （2）当上边界比下边界大时，返回空列表。
 
 a[32:] = []
 
 切片操作还可以设置步长，比如：
 
 a[1::2] = [342, 'India'] 
 它的意思是，从切片索引1到列表末尾，每隔两个元素取值。
 
 列表也支持连接这样的操作。列表1 + 列表2 = 新列表
 
 列表允许修改其中的元素。
 
 cubes = [1, 8, 27, 65, 125]
 
 cubes[3] = 64
 
 则cubes变为[1, 8, 27, 64, 125]
 
 
 
 
 
 
 
 
