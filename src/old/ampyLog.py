import logging
import datetime
import os


class ampylog:
	logfilename = ""
	prevdir = ""

	def __init__(self):
		prevdir = os.curdir
		if not os.path.isdir("../logs/"):
			os.mkdir("../logs/")
		os.chdir("../logs/")
		logfilename = str(datetime.datetime.now()) + ".log"
		logging.basicconfig(filename=logfilename, level=logging.debug)
		logging.debug("starting ampy!")

	def write(self, string):
		logging.debug(string)


