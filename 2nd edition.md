# 第2个版本


## The code

第二个版本加入了持续性输入以及回看输入历史的功能，代码如下。
    # -*- coding: utf-8 -*-
    import sys
    import time

    line2=""
    line1=""
    
    target = open("diary.txt", 'a+')
    
    def writedairy():
    	target = open("diary.txt", 'a+')
    	
    	print "what do u want to say TODAY?"
    	line1 = raw_input("line 1: ")
    	
    	print "I'm going to write these to the file diary.txt."
    	target.write(line1+"  ")
    	target.write(time.strftime("%Y/%m/%d%H:%M:%S"))
    	target.write("\n")
    	
    	#print "here is what you have written"
    	#target = open("diary.txt", 'a+')
    	#print target.read()
    
    #def askforcontinue():
    	#print "do u want to continue?if you want to continue print Y, want to quit print N"
    	#line2 = raw_input("Y/N ")
    
    writedairy()
    #askforcontinue()
    print "here is what you have written"
    target = open("diary.txt")
    print target.read()
    
    while True:
    	line2 = raw_input("do u want to continue?if you want to continue print Y, want to quit print N ")
    	if line2=="Y":
    		writedairy()
    		print "here is what you have written"
    		target = open("diary.txt")
    		print target.read()
    	elif line2=="N":
    		target.close()
    		break
    		print "And finally, we close it."
    
    
    print "And finally, we close it."
    #target.close()

## 出乎意料

比较出乎意料的有两点，第一点是我居然把代码写出来了，而且基本上符合作业的要求，第二点是第一版跟第二版居然完全不一样。


### 我居然把代码写出来了
事情是这样的：在写第二版的时候，我就粗略的看了下其他同学的代码，发现有 def/while/if等模块。嗯，然后我就想我应该怎样把这些模块用起来，然后在睡觉前一直在思考，没有结果。

在今天下午，我没有想去参考别人的代码，就自己一个人在想怎么写。写着写着，发现这段代码重复的比较多，可能需要一个函数去定义它，这样显得比较简洁。

接着发现这里可能需要让用户进行选择，于是去找if的语法。选择之后，发现持续输入是一个循环语句，然后就找到了while true的语法.

我想说的是，这其实是learning by doing的方式，看了别人那么多的代码，还不如自己动手做起来，在实践的过程中发现问题的解决方式。（当然看别人的代码也很重要）


### 前后两个版本完全不一样

第二个版本涉及到更多的函数以及语法，所以从架构上改变非常的大。两者之间的变化是非线性的，这一点很有意思。

问题复杂了，解决的思路应该相应的调整。


## 存在的问题

可以看如下代码
    
    writedairy()
    print "here is what you have written"
    target = open("diary.txt")
    print target.read()

writedairy()是一个函数，让用户进行日记书写。后面三句的功能是把之前用户写的所有内容都打印出来。

能不能把后面三句代码放入到writedairy的函数里面去呢？个人觉得放进去的话，代码会更简洁，但是目前稍微尝试了下，发现不成功。

如果把后面三句放入到writedairy()这个函数里面，print target.read()打印出来的是刚才用户输入的内容，而不是用户输入的所有内容。
