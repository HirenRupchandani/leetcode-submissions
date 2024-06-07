class TrieTree:
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        p = self.root
        for char in word:
            if char not in p:
                p[char] = {}
            p = p[char]
        p['#'] = True
    
    def search(self, word):
        p = self.root
        res = ''
        for char in word:
            if char in p:
                res += char
                p = p[char]
                if '#' in p:
                    break
            else:
                break
        return res if '#' in p else word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    # Trie Tree:
        tree = TrieTree()
        for root in dictionary:
            tree.insert(root)
        return ' '.join(map(tree.search, sentence.split()))

    # Solution: A bit optimized
    # def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    #     rootset = set(dictionary)

    #     def replace(word):
    #         for i in range(1, len(word)):
    #             if word[:i] in rootset:
    #                 return word[:i]
    #         return word

    #     return " ".join(map(replace, sentence.split()))

        # Brute Force
        # res = ""
        # dictionary.sort()
        # sentence = [word for word in sentence.split()]
        # for word in sentence:
        #     new_root = word
        #     temp = len(sentence)
        #     flag = True
        #     for root in dictionary:
        #         if len(root)>len(word):
        #             continue
        #         for i in range(len(root)):
        #             if root[i] != word[i]:
        #                 flag = False
        #                 break
        #             flag = True
        #         if len(root) < temp and flag:
        #             new_root = root
        #             temp = len(new_root)
        #     res += new_root + " "
        # return res.strip()