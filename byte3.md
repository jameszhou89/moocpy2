9.参考与拷贝![](/assets/i89mport.png)

10.pickle

Python提供一个标准的模块，称为`pickle`。使用它你可以在一个文件中储存**任何**Python对象，之后你又可以把它完整无缺地取出来。这被称为持久地储存对象。

还有另一个模块称为`cPickle`，它的功能和`pickle`模块完全相同.

```
import cPickle as p
p.dump # dump the object to a file
p.load  # Read back from the storage
```

11.try except

![](/assets/im789port.png)

12. try finally

假如你在读一个文件的时候，希望在无论异常发生与否的情况下都关闭文件，该怎么做呢？这可以使用`finally`块来完成。注意，在一个`try`块下，你可以同时使用`except`从句和`finally`块。如果你要同时使用它们的话，需要把一个嵌入另外一个。

![](/assets/i9import.png)

















