# %%
class Node:
    """_summary_
    An object for storing a single node of
    a linked list.
    Models two attributes - data and the link
    to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
# %%
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count = count + 1
            current = current.next_node

        return count    

    def add(self, data):
        """ Adds new Node containing data at
        head of the linked list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node 

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:    
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "->".join(nodes)    

    def search(self, key):
        """ 
        Search for the first node containing
        data that matches the key
        Returns the node or None if note found
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current=current.next_node
            
        return None
    
    def insert(self, data, index):
        """ 
        Inserts a new Node containing data at index position
        Insertions takes O(1) time  but finding node at the
        insertion point takes O(n) time.

        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev = current
            next_n = current.next_node

            prev.next_node = new_node
            new_node.next_node = next_n

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position +=1

            return current

    def remove(self, key):
        """
        Removes Node containing data that matches
        the key. Return current or None if key does not exist.
        Takes O(n) time
        """
        current = self.head
        found = False
        previous = None

        while current and not found:

            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current        
# %%
N1 = Node(10)
N1
# %%
N2 = Node(20)
# %%
N1.next_node = N2 
N1.next_node

# %%
l = LinkedList()
# N1 = Node(10)
# l.head = N1
# l.size()
# %%

l.add(3)

# %%
l.add(2)
l.add(1)
# %%
l.add(7)
# %%
n = l.search(2)
print(n)
# %%

# %%
l.insert(2012, 4)
# %%
l
l.remove(3)
# %%
def obter_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i] 
            menor_indice = i      

    return menor_indice   

def ordenar_array(arr):
    novo_array = []
    for i in range(len(arr)):
        menor = obter_menor(arr)
        novo_array.append(arr.pop(menor))        

    return novo_array    

# %%
array = [2,4,0]
# obter_menor(array)
# %%
ordenar_array(array)
# %%
