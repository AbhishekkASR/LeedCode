class Solution:
    def findMode(self, root):
        count = {}
        max_count = 0

        def dfs(node):
            nonlocal max_count

            if not node:
                return

            count[node.val] = count.get(node.val, 0) + 1
            max_count = max(max_count, count[node.val])

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return [val for val, freq in count.items() if freq == max_count]