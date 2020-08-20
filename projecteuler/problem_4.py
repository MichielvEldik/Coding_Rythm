"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""


class FindLargestPalindrome:
    def __init__(self, no_1, no_2):
        self.number_1 = no_1
        self.number_2 = no_2
        all_combs = self.list_all_combinations(no_1, no_2)
        str_combs =  self.turn_int_to_string(all_combs)
        palindromes_found = self.list_all_palindromes(str_combs)
        palindromes_to_int = self.turn_str_to_int(palindromes_found)
        print(max(palindromes_to_int))

    def list_all_combinations(self, one_number, two_number):
        list_combinations = []
        for i in range(one_number + 1):
            for n in range (two_number + 1):
                list_combinations.append(i * n)
        return list_combinations
    
    def turn_int_to_string(self, int_list):
        string_list = []
        for a in int_list:
            string_list.append(str(a))
        return string_list

    def list_all_palindromes(self, string_list):
        palindromes = []
        for b in string_list:
            try:
                if b[0] == b[-1]:
                    if b[1] == b[4] and b[2] == b[3]:
                        palindromes.append(b)
            except IndexError:
                pass
        return palindromes

    def turn_str_to_int(self, palindromes_str):
        palindromes_int = []
        for p in palindromes_str:
            palindromes_int.append(int(p))
        return palindromes_int
    

if __name__ == '__main__':
    FindLargestPalindrome(999, 999)

