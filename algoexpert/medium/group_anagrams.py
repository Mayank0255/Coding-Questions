from collections import Counter

def groupAnagrams(words):
    res = []
	for i in range(len(words)):
		sec = []
		for j in range(1, len(words)):
			checker = words[i]
			sec.append(checker)
			if checkAnagram(checker, words[j]):
				sec.append(words[j])
				# words.pop(j)
		res.append(sec)
	return res

def checkAnagram(str1, str2):
	return Counter(str1) == Counter(str2)
