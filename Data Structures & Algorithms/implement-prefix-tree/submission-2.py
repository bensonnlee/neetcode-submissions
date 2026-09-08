class Node:
    def __init__(self, char: str):
        self.children = []
        self.val = char
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = Node('')

    def insert(self, word: str) -> None:
        node = self.root
        for idx, char in enumerate(word):
            child = self._get_child(node, char)
            if child:
                node = child              
            else:
                node.children.append(Node(char))
                node = self._get_child(node, char)
                
            if idx == len(word) - 1:
                node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            child = self._get_child(node, char)
            if child:
                node = child
            else:
                return False
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            child = self._get_child(node, char)
            if child:
                node = child
            else:
                return False
        return True


    def _get_child(self, node, target) -> Optional[Node]:
        for child in node.children:
            if child.val == target:
                return child
        return None