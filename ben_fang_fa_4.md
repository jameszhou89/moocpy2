# 笨方法4

## 1.codeacademy 练习

1）However, it's overwhelmingly common to use self as the first parameter in **init**\(\)；

2）Python will use the first parameter that **init**\(\) receives to refer to the object being created;

3）

```
   class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
```

```
  class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours* 12.00

    def full_time_wage(self,hours):
        self.hours = hours
        return super(PartTimeEmployee,self).calculate_wage(hours)
```

```
   milton = PartTimeEmployee("James")
   print milton.full_time_wage(20)
```

```
 partimeemployee的薪水是 override，但是 full_time_wage是引用其super class的函数的
```

## 2.笨办法学python第41题

![](/assets/2.png)

```
  字典里面的逻辑关系
```



### 3.笨办法学python第42题

![](/assets/import.png)

在这里面第36行，a.number是参数base的具体值，X是TheMultiplier的一个 instance 

x这个instance在第37行业调用了函数do\_it，b.number是这个函数的参数m的值。

