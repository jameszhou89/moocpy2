# 5W online class

## list
在这个小结里面，强调了list的用法，同时也记录了一个功能诞生的过程：求100以内的素数。

求素数的核心方法：把某个数字除以小于其的所有数字，并求余。如果余数有0，则不是素数。

* [d for d in range(2,x-1)]    #列出x以内的数字#
* [x%d for d in range(2,x-1)] #对x求x以内的数字的余数#
* 0 not in [x%d for d in range(2,x-1)] #判断哪些数的余数不是0#
* [p for p in range(2,x-1) if 0 not in [p%d for d in range(2,p-1)] ]





