class SMS():
	def __init__(self):
		pass	
		
	def convertChar(self, char):
		if ord(char) == ord(' '):
			return '0'
			
		elif ord('a') <= ord(char) < ord('d'):
			number = '2'
			return (ord(char) - ord('a') + 1 ) * number
			
		elif ord(char) < ord('g'):
			number = '3'
			return (ord(char) - ord('d') + 1 ) * number
			
		elif ord(char) < ord('j'):
			number = '4'
			return (ord(char) - ord('g') + 1 ) * number
			
		elif ord(char) < ord('m'):
			number = '5'
			return (ord(char) - ord('j') + 1 ) * number
			
		elif ord(char) < ord('p'):
			number = '6'
			return (ord(char) - ord('m') + 1 ) * number
						
		elif ord(char) < ord('t'):
			number = '7'
			return (ord(char) - ord('p') + 1 ) * number
			
		elif ord(char) < ord('w'):
			number = '8'
			return (ord(char) - ord('t') + 1 ) * number
			
		elif ord(char) <= ord('z'):
			number = '9'
			return (ord(char) - ord('w') + 1 ) * number
					
	def convertString(self,word):
	
		if len(word) > 255:
			word = word[:255]
		result = ""
		previousChar = 'l'
		nextChar = 'l'

		for letter in word:
			nextChar = self.convertChar(letter.lower())
			if letter == letter.upper() and letter != ' ':
				nextChar = '#' + nextChar
			elif nextChar[0] == previousChar[0]:
				nextChar = '_' + nextChar
			result += nextChar
			previousChar = nextChar



			
		return result
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
