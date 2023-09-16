class Solution(object):
    def reverseStr(self, s, k = int):
        s_list = list(s)
        n = len(s)
        i = 0
        while i < n:
            if i + k <= n:
                s_list[i:i+k] = s_list[i:i+k][::-1]
            else:
                s_list[i:] = s_list[i:][::-1]
            i += 2 * k
        return ''.join(s_list)