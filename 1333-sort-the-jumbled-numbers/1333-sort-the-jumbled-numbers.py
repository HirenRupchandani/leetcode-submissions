class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num: int) -> int:
            mapped_num_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_num_str)
        
        # Create a list of tuples where each tuple is (original_num, mapped_value)
        mapped_pairs = [(num, map_number(num)) for num in nums]
        
        # Sort based on the mapped values, while maintaining original order for same mapped values
        mapped_pairs.sort(key=lambda x: x[1])
        
        # Extract the sorted original numbers
        sorted_nums = [num for num, mapped_value in mapped_pairs]
        
        return sorted_nums
        hmap = {i:a for i,a in enumerate(mapping)}

        def split_number(num):
            num_list = []
            while num:
                div = num % 10
                num_list.append(div)
                num = num // 10
            return num_list[::-1]
        
        def combine_number(num_list):
            n = len(num_list)
            num = 0
            for i in range(n):
                print(num_list[i], 10 ** (n-i-1))
                num += num_list[i] * 10 ** (n-i-1)
            return num
        

        return nums
            