class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = ""
        dictionary.sort()
        sentence = [word for word in sentence.split()]
        for word in sentence:
            new_root = word
            temp = len(sentence)
            flag = True
            for root in dictionary:

                # print('word:', word, 'root:', root)
                if len(root)>len(word):
                    continue
                for i in range(len(root)):
                    if root[i] != word[i]:
                        flag = False
                        break
                    flag = True
                # print(len(root), temp)
                if len(root) < temp and flag:
                    # print('True', len(root), len(new_root))
                    new_root = root
                    temp = len(new_root)
                    
                
            res += new_root + " "
        
        return res.strip()