class MapSum:

    def __init__(self):
        self.trie = {}
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        old = self.values.get(key, 0)
        diff = val - old
        self.values[key] = val

        node = self.trie

        for ch in key:
            if ch not in node:
                node[ch] = {'#': 0}
            node = node[ch]
            node['#'] += diff

    def sum(self, prefix: str) -> int:
        node = self.trie

        for ch in prefix:
            if ch not in node:
                return 0
            node = node[ch]

        return node['#']