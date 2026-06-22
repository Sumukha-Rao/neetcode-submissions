class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def decode():
            nonlocal i
            result = ""
            num = 0

            while i < len(s):
                ch = s[i]

                if ch.isdigit():
                    num = num * 10 + int(ch)

                elif ch == "[":
                    i += 1
                    sub = decode()
                    result += num * sub
                    num = 0

                elif ch == "]":
                    return result

                else:
                    result += ch

                i += 1

            return result

        return decode()