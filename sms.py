class SMS():
	def __init__(self):
		pass	
		
	def convertChar(self, char):
		if ord(char) == ord(' '):
			return '0'
			
		elif ord('A') <= ord(char) < ord('D'):
			number = '2'
			return (ord(char) - ord('A') + 1 ) * number
			
		elif ord(char) < ord('G'):
			number = '3'
			return (ord(char) - ord('D') + 1 ) * number
			
		elif ord(char) < ord('J'):
			number = '4'
			return (ord(char) - ord('G') + 1 ) * number
			
		elif ord(char) < ord('M'):
			number = '5'
			return (ord(char) - ord('J') + 1 ) * number
			
		elif ord(char) < ord('P'):
			number = '6'
			return (ord(char) - ord('M') + 1 ) * number
						
		elif ord(char) < ord('T'):
			number = '7'
			return (ord(char) - ord('P') + 1 ) * number
			
		elif ord(char) < ord('W'):
			number = '8'
			return (ord(char) - ord('T') + 1 ) * number
			
		elif ord(char) <= ord('Z'):
			number = '9'
			return (ord(char) - ord('W') + 1 ) * number
					
	def convertString(self,word):
		result = ""
		previousChar = 'l'
		nextChar = 'l'
		for letter in word:
			nextChar = self.convertChar(letter)
			if nextChar[0] == previousChar[0]:
				nextChar = '_' + nextChar
			result += nextChar
			previousChar = nextChar

			
		return result
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
