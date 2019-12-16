#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (37.13%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    14.2K
# Total Submissions: 37.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordListSet = set(wordList)
        from collections import defaultdict
        stepMap = defaultdict(list)
        wordMap = defaultdict(list)
        wordListSet.add(beginWord)
        n = len(beginWord)
        for word in wordListSet:
            for j in range(n):
                k = word[:j] + '_' + word[j+1:]
                wordMap[word].append(k)
                stepMap[k].append(word)

        begin_queue = {beginWord}
        end_queue = {endWord}
        wordListSet.remove(endWord)
        step = 0

        def _ladderLength(queue1, queue2):
            tmp_queue = set()
            for word in queue1:
                if word in queue2:
                    return step, None,
                for k in wordMap[word]:
                    for w in stepMap[k]:
                        if w in queue2:
                            return step + 1, None
                        if w not in wordListSet:
                            continue
                        wordListSet.remove(w)
                        tmp_queue.add(w)
            return 0, tmp_queue


        while begin_queue and end_queue:
            step += 1
            if len(begin_queue) >= len(end_queue):
                result, begin_queue = _ladderLength(begin_queue, end_queue)
            else:
                result, end_queue = _ladderLength(end_queue, begin_queue)
            
            if result:
                return result
        return 0



# @lc code=end

