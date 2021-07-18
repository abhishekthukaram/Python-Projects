"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
You can assume that K is less than or equal to the length of the given string.
"""

def longest_substring_with_k_distinct(str, k):
    start_position = 0
    max_length = 0
    result = {}
    for window_start in range(len(str)):
        print("This is",window_start)
        if str[window_start] not in result:
            result[str[window_start]] =0
            print("Initial",result)
        print("WindowSTart", window_start)
        result[str[window_start]]+=1
        print("After adding", result)
        while len(result) > k:
            removed_character = str[start_position]
            result[removed_character]-=1
            if result[removed_character] ==0:
                del result[removed_character]
            print("After",result)
            start_position+=1
            max_length = max(max_length, window_start-start_position+1)
            print(max_length)
    return max_length


print(longest_substring_with_k_distinct("araaci", 2))
