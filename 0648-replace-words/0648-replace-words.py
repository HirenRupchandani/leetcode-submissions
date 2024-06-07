class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))
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