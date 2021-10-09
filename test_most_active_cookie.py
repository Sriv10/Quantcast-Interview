from most_active_cookie import *
import unittest

class TestMostActiveCookie(unittest.TestCase):
	def testProcessFileFail(self):
		self.assertRaises(ValueError, processFile, "")
		self.assertRaises(ValueError, processFile, "cookie_log.excel")
		self.assertRaises(FileNotFoundError, processFile, "empty.csv")

	def testProcessArgs(self):
		#Fails
		args = ["1", "2", "3"]
		self.assertRaises(ValueError, processArgs, args)

		args = ["1", "file.csv", "-a", "2010-04-12"]
		self.assertRaises(ValueError, processArgs, args)

		args = ["1", "file.csv", "-d", "2010-04-222"]
		self.assertRaises(ValueError, processArgs, args)

		args = ["1", "file.csv", "-d", "2010-04-33"]
		self.assertRaises(ValueError, processArgs, args)

		#Passes
		args = ["1", "file.csv", "-d", "2010-04-12"]
		processArgs(args)



if __name__ == '__main__':
	unittest.main()
