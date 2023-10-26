# Декартово дерево (также известное как Treap — от слов "Tree" и "Heap")
# является структурой данных, сочетающей в себе бинарное дерево поиска и бинарную кучу.
# У каждого узла дерева есть два значения:
# - ключ (как в бинарном дереве поиска) и приоритет (как в куче).
# Приоритеты обычно выбираются случайно.
import random


class Node:  # Класс узла дерева
    def __init__(self, key):  # Конструктор
        self.key = key  # Ключ узла
        self.priority = random.random()  # Приоритет узла
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок


class Treap:  # Класс дерева
    def __init__(self):  # Конструктор
        self.root = None  # Корень дерева

    def _split(self, node, key):  # Разбиение дерева по ключу
        if node is None:  # Если дерево пустое
            return None, None  # Возвращаем два пустых дерева
        elif node.key < key:  # Если ключ узла меньше заданного
            l, r = self._split(node.right, key)  # Разбиваем правое поддерево
            node.right = l  # Правое поддерево становится левым поддеревом
            return node, r  # Возвращаем левое поддерево и правое поддерево
        else:
            l, r = self._split(node.left, key)  # Разбиваем левое поддерево
            node.left = r  # Левое поддерево становится правым поддеревом
            return l, node  # Возвращаем левое поддерево и правое поддерево

    def _merge(self, left, right):  # Слияние двух деревьев
        if left is None:  # Если левое дерево пустое
            return right  # Возвращаем правое дерево
        if right is None:  # Если правое дерево пустое
            return left  # Возвращаем левое дерево
        if left.priority > right.priority:  # Если приоритет левого дерева больше приоритета правого
            # Сливаем правое дерево с правым поддеревом левого дерева
            left.right = self._merge(left.right, right)
            return left  # Возвращаем левое дерево
        else:
            # Сливаем левое дерево с левым поддеревом правого дерева
            right.left = self._merge(left, right.left)
            return right  # Возвращаем правое дерево

    def insert(self, key):  # Вставка ключа в дерево
        new_node = Node(key)  # Создаем новый узел
        if self.root is None:  # Если дерево пустое
            self.root = new_node  # Новый узел становится корнем
        else:
            self.root = self._insert(self.root, new_node)  # Вставляем новый узел в дерево

    def _insert(self, node, new_node):  # Вставка ключа в дерево
        if node is None:  # Если дерево пустое
            return new_node  # Возвращаем новый узел
        if new_node.priority > node.priority:  # Если приоритет нового узла больше приоритета текущего узла
            l, r = self._split(node, new_node.key)  # Разбиваем дерево по ключу нового узла
            new_node.left = l  # Левое поддерево нового узла становится левым поддеревом разбиения
            new_node.right = r  # Правое поддерево нового узла становится правым поддеревом разбиения
            return new_node  # Возвращаем новый узел
        elif new_node.key < node.key:  # Если ключ нового узла меньше ключа текущего узла
            node.left = self._insert(node.left, new_node)  # Вставляем новый узел в левое поддерево
        else:
            node.right = self._insert(node.right, new_node)  # Вставляем новый узел в правое поддерево
        return node

    def erase(self, key):  # Удаление ключа из дерева
        self.root = self._erase(self.root, key)  # Удаляем ключ из дерева

    def _erase(self, node: Node, key):  # Удаление ключа из дерева
        assert isinstance(node, Node)
        if node is None:  # Если дерево пустое
            return None  # Возвращаем пустое дерево
        if node.key == key:  # Если ключ текущего узла равен заданному ключу
            return self._merge(node.left, node.right)  # Сливаем левое и правое поддеревья
        if key < node.key:  # Если заданный ключ меньше ключа текущего узла
            node.left = self._erase(node.left, key)  # Удаляем ключ из левого поддерева
        else:
            node.right = self._erase(node.right, key)  # Удаляем ключ из правого поддерева
        return node  # Возвращаем текущий узел

    def find(self, key):  # Поиск ключа в дереве
        return self._find(self.root, key)  # Ищем ключ в дереве

    def _find(self, node: Node, key):  # Поиск ключа в дереве
        if node is None:  # Если дерево пустое
            return False  # То там точно нет ключа
        if node.key == key:  # Если ключ текущего узла равен заданному ключу
            return True  # То ключ найден
        if key < node.key:  # Если заданный ключ меньше ключа текущего узла
            return self._find(node.left, key)  # Ищем ключ в левом поддереве
        return self._find(node.right, key)  # Иначе ищем ключ в правом поддереве


def test_insert():
    t = Treap()
    t.insert(5)
    assert t.root.key == 5
    t.insert(3)
    assert t.find(3)
    t.insert(8)
    assert t.find(8)
    t.insert(3)


def test_erase():
    t = Treap()
    t.insert(5)
    assert t.find(5)
    t.insert(3)
    assert t.find(3)
    t.insert(8)
    assert t.find(8)

    t.erase(3)
    assert not t.find(3)
    t.erase(8)
    assert not t.find(8)
    t.erase(5)
    assert t.root is None


def test_insert_erase():
    t = Treap()
    t.insert(5)
    t.insert(3)
    t.insert(8)
    t.erase(5)
    assert t.root.key == 8 or t.root.key == 3
    t.insert(5)
    assert t.find(5)


def test_large_random_operations():
    t = Treap()  # Создаем дерево
    keys = {}  # Множество вставленных ключей
    min_value = 1
    max_value = 10000
    # Проведем много случайных операций
    for _ in range(100000):
        # Случайным образом выбираем операцию
        op = random.choice(["insert", "erase", "find"])
        if op == "insert":  # Если операция вставки
            key = random.randint(min_value, max_value)  # Выбираем случайный ключ
            t.insert(key)  # Вставляем ключ в дерево
            if key in keys:  # Считаем количество вставок для каждого ключа
                keys[key] += 1  # Если ключ уже есть во множестве, то увеличиваем счетчик
            else:
                keys[key] = 1  # Если ключа нет во множестве, то добавляем его туда
            assert key in keys
            assert t.find(key)  # Убеждаемся, что вставленный ключ действительно присутствует
        elif op == "erase" and keys:  # Если операция удаления и в дереве есть ключи
            key = random.choice(list(keys))
            t.erase(key)  # Удаляем случайный ключ из дерева
            if key in keys:  # Считаем количество удалений для каждого ключа
                keys[key] -= 1  # Уменьшаем счетчик вставок для этого ключа
                if keys[key] == 0:  # Если счетчик вставок стал равен нулю
                    del keys[key]  # Удаляем ключ из множества вставленных ключей
            # Убеждаемся, что ключ присутствует в дереве, если он есть во множестве
            assert t.find(key) == (key in keys)
        elif op == "find":
            key = random.randint(min_value, max_value)  # Выбираем случайный ключ
            # Убеждаемся, что ключ присутствует в дереве, если он есть во множестве
            assert t.find(key) == (key in keys)
