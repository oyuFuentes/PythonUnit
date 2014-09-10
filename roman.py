roman_numeral_map = (('M',  1000),
					('CM', 900),
					('D',  500),
					('CD', 400),
					('C',  100),
					('XC', 90),
					('L',  50),
					('XL', 40),
					('X',  10),
					('IX', 9),
					('V',  5),
					('IV', 4),
					('I',  1)) 

def to_roman(numero_entero):
	"""
	TDD
	"""
	if not (0 < numero_entero < 4000):
		raise OutOfRangeError('number out of range (must be less than 1...3999)') 

	if not isinstance(numero_entero, int):                                          
		raise NotIntegerError('non-integers can not be converted')

	result = ''
	for numeral, integer in roman_numeral_map:
		while numero_entero >= integer:                     
			result += numeral
			numero_entero -= integer
	return result

def from_roman(numero_romano):
	'''convert Roman numeral to integer'''
	result = 0
	index = 0
	for numeral, integer in roman_numeral_map:
		while numero_romano[index:index+len(numeral)] == numeral:  
			result += integer
			index += len(numeral)
	return result

class OutOfRangeError(ValueError): pass

class NotIntegerError(ValueError): pass

class InvalidRomanNumeralError(ValueError): pass