
def encrypt(plain_text,x):
	ans = ""

	# traverse text
	for i in range(len(plain_text)):
		char = plain_text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			ans = ans + (chr((ord(char) + x-65) % 26 + 65))

		# Encrypt lowercase characters
		else:
			ans = ans + (chr((ord(char) + x - 97) % 26 + 97))

	return ans

#check the above function
plain_text = "Thisisceasercipher"
x = 6
print ("Text : " + plain_text)
print ("Shift : " + str(x))
print ("Cipher: " + encrypt(plain_text,x))
