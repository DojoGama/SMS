import unittest
from sms import *

class TestSMS(unittest.TestCase):
	def setUp(self):
		self.sms = SMS()
		
	def testKey2(self):
		self.assertEqual('2', self.sms.convertChar('a'))
		self.assertEqual('22', self.sms.convertChar('b'))
		self.assertEqual('222', self.sms.convertChar('c'))
		
	def testKey3(self):
		self.assertEqual('3', self.sms.convertChar('d'))
		self.assertEqual('33', self.sms.convertChar('e'))
		self.assertEqual('333', self.sms.convertChar('f'))
	
	def testKey0(self):
		self.assertEqual('0', self.sms.convertChar(' '))
		
	def testKey7(self):
		self.assertEqual('7', self.sms.convertChar('p'))
		self.assertEqual('77', self.sms.convertChar('q'))
		self.assertEqual('777', self.sms.convertChar('r'))
		self.assertEqual('7777', self.sms.convertChar('s'))
		
	def testConvertString(self):
		self.assertEqual('3232', self.sms.convertString('dada'))
		self.assertEqual('22332233', self.sms.convertString('bebe'))
		self.assertEqual('2233223303232', self.sms.convertString('bebe dada'))
	
	def testConvertStringWithUnderline(self):
		self.assertEqual('2_2',self.sms.convertString('aa'))
		self.assertEqual('2_22',self.sms.convertString('ab'))

	def testConvertWord(self):
		self.assertEqual("277727772",self.sms.convertString("arara"))
		self.assertEqual("222_2777_777666",self.sms.convertString("carro"))


	def testGSMLengthLimit(self):
		self.assertEqual(self.sms.convertString(" "*255),
			self.sms.convertString(" "*400))

	def testCapitalLetters(self):
		self.assertEqual("#2",self.sms.convertString("A"))	
		self.assertEqual("#2#2", self.sms.convertString("AA"));

	def testFimdesteDojo(self):
		self.assertEqual("#333444603_3377778330#3#666#5#6660#42#62",self.sms.convertString("Fim deste DOJO GaMa"))

if __name__ == "__main__":
	unittest.main()

		
