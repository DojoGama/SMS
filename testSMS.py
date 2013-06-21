import unittest
from sms import *

class TestSMS(unittest.TestCase):
	def setUp(self):
		self.sms = SMS()
		
	def testKey2(self):
		self.assertEqual('2', self.sms.convertChar('A'))
		self.assertEqual('22', self.sms.convertChar('B'))
		self.assertEqual('222', self.sms.convertChar('C'))
		
	def testKey3(self):
		self.assertEqual('3', self.sms.convertChar('D'))
		self.assertEqual('33', self.sms.convertChar('E'))
		self.assertEqual('333', self.sms.convertChar('F'))
	
	def testKey0(self):
		self.assertEqual('0', self.sms.convertChar(' '))
		
	def testKey7(self):
		self.assertEqual('7', self.sms.convertChar('P'))
		self.assertEqual('77', self.sms.convertChar('Q'))
		self.assertEqual('777', self.sms.convertChar('R'))
		self.assertEqual('7777', self.sms.convertChar('S'))
		
	def testConvertString(self):
		self.assertEqual('3232', self.sms.convertString('DADA'))
		self.assertEqual('22332233', self.sms.convertString('BEBE'))
		self.assertEqual('2233223303232', self.sms.convertString('BEBE DADA'))
	
	def testConvertStringWithUnderline(self):
		self.assertEqual('2_2',self.sms.convertString('AA'))
		
if __name__ == "__main__":
	unittest.main()

		
