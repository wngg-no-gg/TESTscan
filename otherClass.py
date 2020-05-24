# Name : TEST语言编译器
# Time : 2018.11.20 ~ 2018.
# Developer : wngg
# Coding : utf-8


# --------------------CLASS-------------------- #

#字符串输出类
#用于输出程序提示等字符串
class StringOut:

	def version(self):
		print ()
		print ()
		print ("-------------------------------------------------------------------------")
		print ()
		print ("    ██████    ▄████▄  ▄████▄  ██████  ")
		print ("        ██      ██            ██              ██    ")
		print ("        ██      █████        ████▄      ██    ")
		print ("        ██      ██                    ██      ██    ")
		print ("        ██        █████    █████        ██     compiler")
		print ()
		print ("-------------------------------------------------------------------------")
		print ()
		print ("TEST Languague Compiler -Version : 1.0 -181120")
		print ()
		print ("Welcome and there are commands :")

	def commands_list(self):
		print ("\t-h [--help]\t\t: direction for use")
		print ("\t-l [--lexical]\t\t: lexical analysis")
		print ("\t-g [--grammatical]\t: grammatical analysis")

	def _help(self):
		print ("[--help] The command format is :\n"+"----[e.g.] d:\\path\\file.txt -hl")

#输入命令类
#作用：处理用户输入的命令
#输入：用户输入的命令
class InputCommands:

	def __init__(self,inputString):

		self.is_help = 0															#is_help为是否输入了-h
		self.is_lexical = 0													 		#is_lexical为是否输入了-l
		self.is_grammatical = 0														#is_grammatical为是否输入了-g
		self.filePath = inputString[:inputString.find(" ")]
		self.inputString = inputString[inputString.find("-"):]

		if self.inputString.find("h") >= 0 :
			self.is_help = 1
		if self.inputString.find("l") >= 0 :
			self.is_lexical = 1
		if self.inputString.find("g") >= 0 :
			self.is_grammatical = 1