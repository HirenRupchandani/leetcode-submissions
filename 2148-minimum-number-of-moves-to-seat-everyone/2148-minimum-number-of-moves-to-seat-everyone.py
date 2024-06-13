class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort the arrays
        seats.sort()
        students.sort()
        # The elements are sorted so for example: seats = [2,2,6,6], students = [1,3,2,6], 
        # we get -> seats = [2,2,6,6], students = [1,2,3,6]
        # The seat closest to the corresponding student is assigned
        # Think of it like getting seated in ith row because you have jth height.
        # Taller student gets seated at the later rows.
        res = 0
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res