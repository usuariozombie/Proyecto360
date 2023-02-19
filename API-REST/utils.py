# -*- coding: utf-8 -*-

import datetime, json, math, os, time

class JSON():
	def Read(path_file):
		with open(f"API/{path_file}", "r", encoding = "utf-8") as jFile: data = json.load(jFile)
		jFile.close()
		return data
	def Write(path_file, data):
		with open(f"API/{path_file}", "w") as jFile: json.dump(data, jFile, indent = "\t")

def now(Mode = None):
	if Mode == None: return math.trunc(time.time())
	else: return datetime.datetime.now().strftime(Mode) # %d/%m/%Y - %H:%M:%S

def PurgeCache():
	CacheFolders = [
		"API/__pycache__",
		"API/endpoints/__pycache__",
	]
	for CacheFolder in CacheFolders: os.system(f"rm -r {CacheFolder}")