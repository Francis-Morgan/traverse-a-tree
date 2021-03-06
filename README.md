# Traverse a tree

**Содержание:**
- [Pre-order traversal](#Pre-order)
   - [Итеративная реализация](#Pre-iterative)
   - [Рекурсивная реализация](#Pre-recursive)
- [In-order traversal](#In-order)
   

## Алгоритмы. Обход Дерева
Обход дерева может быть реализован двумя методами:
1. в глубину (Depth-first) **DFS**  
2. в ширину (Breadth-first) **BFS**

Первое время тут будут рассмотрены обходы деревьев в глубину

Поиск в глубину имеет 3 типа обходов: 
- **Pre-order** (Прямой обход)
- **In-order**  (Симметричный обход)
- **Post-order** (Обратный обход)

## Pre-order traversal <a name="Pre-order"></a>
 

### Как это работает?

Мы посещаем каждый узел дерева до того, как посетить его потомков. То есть следуем такой процедуре:
- Посетить корень
- Посетить левый потомок
- Посетить правый потомок

Вершина - левое поддерево - правое поддерево

Припустим, у нас есть дерево:

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/tree.png)

Вывод значения ячеек этого дерева будет виглядеть так: **[ A B D E G C F H I ]**

Если отслеживать значения в бинарном дереве по порядку, который у нас получился на выходе, можно понять идею алгоритма.

### Итеративная реализация <a name="Pre-iterative"></a>

[Здесь](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/Pre-order_traversal_iterative.py) можно увидеть итеративную реализацию прямого обхода.

Мы создадим список-стек, который будем наполнять значениями ячеек дерева. А потом по очередности их возвращать. Кроме того, создадим список tree, который будет хранить значения ячеек дерево в правильной последовательности. 

На словах идея может быть не понятна, но ее легко понять увидев в действии.

Это будет работать так: 

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/tree_stack.png)

1. Добавляем значения узла в стек
2. Удаляем это значение и перемещаем в tree
3. Добавляем в стек его потомков (сначала правый, потом левый)
4. Удаляем и перемещаем в список tree левый узел (последний элемент стека) и ложим в стек его потомков

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

## Рекурсивная реалиация <a name="Pre-recursive"></a>

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

Если описывать этот алгоритм словами, понять с первого раза довольно сложно. К тому же, нужно четко знать как работает рекурсия. По-этому будем рассматривать алгоритм на примере этого дерева. 

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

Левый потомок пройдет тот самый маршрут, что его родитель, и будет вызвана функция **PreorderTraversal** с переданным  ей левым потомком, который имеет значение **D**.

Этот узел левого потомка не имеет, сообственно он проверку не прошел и будет выполнена следующая строка:
```python
return arr
```

Функция возвращает список **arr** со значением **D** 

```python
arr += self.PreorderTraversal(root.left)
```
И список **arr** теперь имеет значения [B,D].

Можно подумать, что стек будет освобождаться дальше, и будет возращен список [B,D], который прибавится к списку [A]. **Но это не так!** Мы все еще остаемся в стеке (это значит что мы вернулись к узлу-родителю, а не к вершине дерева).

Список будет имеет значения: [B,D], и будет выполнена следующая строчка: 

```python
arr += self.PreorderTraversal(root.right)
```

**Сейчас root - это узел со значением B!**

Вызываем функцию, передавая ей правого потомка этого узла. 

Создается список с его значением - [E]. И программа опять вызывает себя, передавая значение левого потомка. Этот вызов вернет [G].
Список будет иметь значения [E,G].

Я подозреваю, что в моем объяснении может быть что-то непонятно, или можно запутаться.

По-этому я попытался это нарисовать (что-то наподобии блок-схемы). На рисунке изображен обход левого поддерева. Pre-Travel это наша функция PreorderTraversal

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/rec_explanation.png)



##### INPUT/OUTPUT

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/input_output.PNG)

##### СКОРОСТЬ АЛГОРИТМОВ

Это скорость итеративной версии: 

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/complexity.PNG)

Это скорость рекурсивной версии:

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/complexity_rec.PNG)

## In-order traversal <a name="In-order"></a>

### Как это работает?

Сначала мы проверяем детей и только потом подымаемся к к родительским узлам.

![](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/TREE%20TRAVERSE/tree.png)

Вывод этого дерева будет выглядеть так: **[D,B,G,E,A,C,H,F,I]**

## Рекурсивная реализация 

[Здесь](https://github.com/Francis-Morgan/traverse-a-tree/blob/master/In-order_traversal.py) можно увидеть код.

Рекурсивные алгоритмы довольно сложно пояснить на словах, и не запутаться. По-этому, мы будем рассматривать работу этого лгоритма на конкретном дереве, которое було представлено выше.

Эта функция - реализация алгоритма.
```python
def in_order(self, root):
        tree = []
        if root:
            tree += self.in_order(root.left)
            tree.append(root.val)
            tree += self.in_order(root.right)
        return tree
```

