class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = ("(", "{", "[")
        close_bracket = (")", "}", "]")
        stack = []
        for char in s:
            if char in open_bracket:
                stack.append(char)
            elif char in close_bracket:
                if len(stack) == 0:
                    return False
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                    continue
                if char == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
                if char == "]" and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
        return len(stack) == 0