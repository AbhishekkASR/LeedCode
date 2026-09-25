class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def parse_union(i):
            result, i = parse_concat(i)

            while i < n and expression[i] == ',':
                part, i = parse_concat(i + 1)
                result |= part

            return result, i

        def parse_concat(i):
            result = {""}

            while i < n and expression[i] not in '},':
                if expression[i] == '{':
                    part, i = parse_union(i + 1)
                    i += 1
                else:
                    part = {expression[i]}
                    i += 1

                result = {a + b for a in result for b in part}

            return result, i

        result, _ = parse_union(0)
        return sorted(result)