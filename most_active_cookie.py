#!/usr/bin/python

import sys
import csv
import os
from datetime import datetime

def processArgs(args):
	if (len(args) != 4):
		raise ValueError("Invalid number of arguments: ", args)
	if (args[2] != "-d"):
		raise ValueError
	try:
		datetime.strptime(args[3], '%Y-%m-%d')
	except:
		raise ValueError

	fileName = args[1]
	searchDate = args[3]
	return fileName, searchDate

def processFile(fileName):
	if (not fileName.endswith(".csv")):
			raise ValueError("Improper file type")
	elif not os.path.isfile(fileName):
		raise FileNotFoundError
	else:
		file = open(fileName)
		return file

def findMostActiveCookies(file, searchDate):
	foundDate = False
	frequency = {}
	activeCookies = []
	activeMax = 0

	with file as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			 data = ','.join(row).split(",")
			 cookieName = data[0]
			 date = data[1].split('T')[0]
			 if (date == searchDate):
				 foundDate = True
				 count = frequency.get(cookieName, 0) + 1
				 if (count > activeMax):
					 activeMax = count
					 activeCookies = [cookieName]
				 elif (count == activeMax):
					 activeCookies.append(cookieName)
				 frequency[cookieName] = count
			 elif(foundDate == True):
				 printMostActiveCookies(activeCookies)
				 quit()

def printMostActiveCookies(mostActiveCookies):
	for cookie in mostActiveCookies:
		print(cookie)

def main():
	fileName, searchDate = processArgs(sys.argv)
	file = processFile(fileName)
	findMostActiveCookies(file, searchDate)




if __name__ == "__main__":
	main()
