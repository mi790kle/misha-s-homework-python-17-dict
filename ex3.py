def merging_dicts(dict1, dict2) -> dict:
    dict3 = {}
    for key, value in dict1.items():
        if key in dict2:
            if len(value) > len(dict2[key]):
                dict3[key] = value
            elif len(value) == len(dict2[key]):
                dict3[key] = value
            else:
                dict3[key] = dict2[key]
        else:
            dict3[key] = value
    for key, value in dict2.items():
        if key in dict3:
            continue
        else:
            dict3[key] = value
    return dict3

dict1 = {"misha": "gamer", "lena": "gym_rat", "grisha": "hiker"}
dict2 = {"misha": "coder", "zorik": "madrich", "daniel": "alcoholic", "lena": "singer", "grisha": "cook"}
print(merging_dicts(dict1, dict2))