# 笨办法3


## 第39个习题1


mystuff.append('hello') 这样代码的执行过程

![](mystuff.png)
1）.(period)之后，python知道 mystuff支持一些函数，
2）然后python会将"append"和mystuff支持的所有函数对比，确认append这个函数
3）发了真正的事情，append(mystuff,"hello")



## 第39个习题2

```city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
```
Output: the city for the state "TX" is Does Not Exist.

Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
点击[参考](http://www.runoob.com/python/att-dictionary-get.html)链接



## 第40个习题

列表和字典的区别

你可以使用数字作为列表的索引，也就是你可以通过数字找到列表中的元素。而 dict 所作的，是让你可以通过任何东西找到元素，不只是数字。是的，字典可以将一个物件和另外一个东西关联，不管它们的类型是什么








