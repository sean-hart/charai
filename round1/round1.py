
# """Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# """
# in_string = "CODEBANC", t = "ABC"
# out_string = "BANC"

# CODEBA
# BANC
# ODEBANC


# def get_substring(input, substring):
# 	substr_length = len(substring)
# 	if not compare_strings(input,substring):
#   	    return ""
#     window = len(substring)
#     start_index = 0
#     end_index = 0 + window -1
#   while len(window) < len(input): 
#     while end_index < len(input) - 1:
#       my_slice = input{start_index:end_index}

#       if compare_strings(my_slice, substring):
#         return my_slice
#       start_index += 1
#       end_index += 1
#     start_index = 0
#     end_index += 1
#   return ""
    
    
# def compare_strings(string1, string2):
#     for i in string2:
#     	if i in string1:
#       	    string1.delete(string1.index(i))
#         else:
#       	    return false
#     return true

from itertools import product

def compare_strings(string1, string2):
    index = {}
    all_indicies = []
    ## build index
    i = 0
    for letter in string2:
        index[f'{letter}-{i}'] = [ i for i in range(len(string1)) if string1[i] == letter ]
        i += 1
    max = 0
    min = 0
    

    min_distance = len(string1)
    indexes = []
    all_combinations = product(*index.values())
    for combination in all_combinations:
        # Don't use the same index twice
        if len(set(combination)) < len(combination):
            continue
        distance = calculate_distance(list(combination))
        if distance < min_distance:
            min_distance = distance
            indexes = list(combination)
    indexes.sort()

    # If it's not found, return empty string
    if indexes == []:
        return ""
    #Slices are non-inclusive, so if we want the last character of string 1, set end of slice to None
    if indexes[-1] == len(string1) - 1:
        indexes[-1] = None
    # Otherwise, bump up by 1
    else:
        indexes[-1] += 1
    return f"{string1[indexes[0]:indexes[-1]]}"



def calculate_distance(item_list):
    item_list.sort()
    return item_list[-1] - item_list[0]


        


