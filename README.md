# Traverse a tree

**Содержание:**
- [Pre-order traversal](#Pre-order)
   - [Итеративная реализация](#Pre-iterative)
   - [Рекурсивная реализация](#Pre-recursive)
   

## Алгоритмы. Обход Дерева
Обход дерева может быть реализован двумя методами:
1. в глубину (Depth-first) **DFS**  
2. в ширину (Breadth-first) **BFS**


## Depth-first search 
Поиск в глубину имеет 3 типа обходов: 
- **Pre-order** (Прямой обход)
- **In-order** 
- **Post-order**

### Pre-order traversal <a name="Pre-order"></a>

[Здесь](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/Pre-order_traversal_iterative.py) можно увидеть итеративную реализацию прямого обхода. 

#### Как это работает?

Мы посещаем каждый узел дерева до того, как посетить его потомков. То есть следуем такой процедуре:
- Посетить корень
- Посетить левый потомок
- Посетить правый потомок

Вершина - левое поддерево - правое поддерево

#### Рассмотрим итеративную реализацию <a name="Pre-iterative"></a>

Мы создадим список-стек, который будем наполнять значениями ячеек дерева. А потом по очередности их возвращать. 

На словах идея может быть не понятна, но ее легко понять увидев в действии.

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/tree.png)

Вывод значения ячеек этого дерева будет виглядеть так: **[ A B D E G C F H I ]**

Если отслеживать значения в бинарном дереве по порядку, который у нас получился на выходе, можно понять идею алгоритма.

##### Реализация и стек

Как и говорилось выше,  мы создадим список-стек. Кроме того, создадим список tree, который будет хранить значения ячеек дерево в правильной последовательности. Это будет работать так: 

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/tree_stack.png)

1. Добавляем значения узла в стек
2. Удаляем это значение и перемещаем в tree
3. Добавляем в стек его потомков (сначала правый, потом левый)
4. Удаляем и перемещаем левый узел и ложим в стек его потомков

Так будет  продолжаться до тех пор, пока мы не обойдем полностью левое поддерево. После этого аналогично обойдем и правое поддерво.

А теперь код: 

```python
       stack = []
       tree = []
       stack.append(root) # Добавляем в стек значение вершины дерева
```
Метод стоки **pop()** тут очень даже кстати. Он позволяет удалить значение из стека, при этом его не потеряв.

```python
 while len(stack) > 0:
        
     node = stack.pop()
     tree.append(node.val)                           # Добавляем в список значения узла
     
     if node.right is not None:                      # Если этот узел не лист - добавляем в стек
           stack.append(node.right)
     
     if node.left is not None:
           stack.append(node.left)
            
            
```

#### Рассмотрим рекурсивную реалиацию <a name="Pre-recursive"></a>

[Здесь](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/Pre-order_traversal.py) можно увидеть код.

#### Как это работает 

Рассмотрим тоже самое дерево:

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/tree.png)

И код:

```python
 def PreorderTraversal(self, root):
        arr = []
        if root is not None:
            arr.append(root.data)
            arr += self.PreorderTraversal(root.left)
            arr += self.PreorderTraversal(root.right)
        return arr
```

Если описывать этот алгоритм словами, понять с первого раза довольно сложно. По-этому будем рассматривать алгоритм на примере этого дерева. 

Сначала мы вызываем функцию **PreorderTraversal** и передаем ей корень дерева (экземпляр класса Node).

Здесь инициализируем пустой список **arr**.

Проходим проверку: 

```python
if root is not None:
```
Поскольку наш корень не имеет значение **None**, это условие выполнится, и в список **arr** добавится значение корня - **A**.

Дальше следует эта строчка: 

```python
arr += self.PreorderTraversal(root.left)
```
Тут мы вызываем функцию **PreorderTraversal**, передавая ей левого потомка, который принадлежит корню дерева. Эта функция возварщает список, по-этому список который она вернет мы прибавим к **arr**.

Он пройдет тот самый маршрут, что его родитель, и будет вызвана функция **PreorderTraversal** с переданным  ей левым потомком, который имеет значение **D**.

Этот узел левого потомка не имеет, сообственно он проверку не прошел и будет выполнена следующая строка:
```python
return arr
```

Функция возвращает список **arr** со значением **D** 

```python
arr += self.PreorderTraversal(root.left)
```
И список **arr** теперь имеет значения [B,D].

Можно подумать, что стек будет освободится, и будет возращен список [B,D], который прибавится к списку [A]. **Но это не так!**




##### INPUT/OUTPUT

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/input_output.PNG)

##### СКОРОСТЬ АЛГОРИТМОВ

Это скорость итеративной версии: 

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/complexity.PNG)

Это скорость рекурсивной версии:

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/complexity_rec.PNG)
