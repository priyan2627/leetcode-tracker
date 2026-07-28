# Last updated: 7/28/2026, 1:10:52 PM
1from collections import Counter
2
3class Solution:
4    def findSubstring(self, s, words):
5        if not s or not words:
6            return []
7
8        word_len = len(words[0])
9        num_words = len(words)
10        total_len = word_len * num_words
11
12        word_count = Counter(words)
13        result = []
14
15        for i in range(word_len):
16            left = i
17            current_count = Counter()
18            count = 0
19
20            for right in range(i, len(s) - word_len + 1, word_len):
21                word = s[right:right + word_len]
22
23                if word in word_count:
24                    current_count[word] += 1
25                    count += 1
26
27                    while current_count[word] > word_count[word]:
28                        left_word = s[left:left + word_len]
29                        current_count[left_word] -= 1
30                        left += word_len
31                        count -= 1
32
33                    if count == num_words:
34                        result.append(left)
35
36                        left_word = s[left:left + word_len]
37                        current_count[left_word] -= 1
38                        left += word_len
39                        count -= 1
40
41                else:
42                    current_count.clear()
43                    count = 0
44                    left = right + word_len
45
46        return result