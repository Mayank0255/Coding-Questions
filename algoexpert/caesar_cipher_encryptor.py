def caesarCipherEncryptor(string, key):
	string = [i for i in string]
	i = 0
    while i < len(string):
		if ord(string[i]) + key > 122:
			num = (ord(string[i]) + key - 123) % 26
			string[i] = 'a'
			string[i] = chr(ord(string[i]) + num)
		else:
			string[i] = chr(ord(string[i]) + key)
		i += 1
	return ''.join(string)
