def is_anagram(s: str, t: str) -> bool:
    character_dic = {}
    character_dic_keys = set()
    for character in s:
        if character in character_dic:
            character_dic[character] += 1
        else:
            character_dic_keys.add(character)
            character_dic[character] = 1
    for character in t:
        if character in character_dic:
            character_dic[character] -= 1
        else:
            return False
    for key in character_dic_keys:
        if character_dic[key] != 0:
            return False
    return True


assert is_anagram("anagram", "nagaram") == True
assert is_anagram("rat", "car") == False
