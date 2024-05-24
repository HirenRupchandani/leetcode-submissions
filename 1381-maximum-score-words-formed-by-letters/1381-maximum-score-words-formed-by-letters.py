class Solution:
    def score_calculator(self,word,count,scores):
        char_count = [0] * 26
        score = 0

        # Calculate word score if letters are in word
        for char in word:
            pos = ord(char) - 97 # ord('a')
            char_count[pos] += 1
            if char_count[pos] <= count[pos]:
                score+=scores[pos]
            else:
                return 0 # Word not found
        return score    
    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = [0] * 26
        for char in letters:
            count[ord(char) - 97]+=1
        return self.max_score_helper(0, words, score, count)
    
    def max_score_helper(self, index, words, score, count):
        if index==len(words):
            return 0    # Base case: reached the end
        
        # Calculate max score without current word
        max_score = self.max_score_helper(index+1,words,score,count)

        # Calculate max score with current word
        include = self.score_calculator(words[index], count, score)
        if include>0:
            temp_count = count[:]
            for char in words[index]:
                temp_count[ord(char) - 97] -= 1
            # Update max score between exclude and include
            # Include will have updated temp_count counter, rest of the recursive call will be same
            max_score = max(max_score, include+self.max_score_helper(index+1, words, score, temp_count))
        return max_score




        