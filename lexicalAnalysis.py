# Name : TEST语言编译器
# Time : 2018.11.20 ~ 2018.
# Developer : wngg
# Coding : utf-8

import operator

# --------------------GLOBAL------------------- #

#保留字
KEYWORD = ( "call", "do", "else", "for", "function", "if", "int", "read", "while", "write" )
#单分界符
SINGLEWORD = ( "+", "-", "*", "(", ")", "{", "}", ";", ",", ":", "%" )
#双分界符
DOUBLEWORD = ( ">", "<", "=", "!", "&", "|" )

# --------------------CLASS-------------------- #

#词法分析器
#作用：进行词法分析
#输入：文件路径
class LexicalAnalysis:

	def __init__(self,inPath):

		self.outPath = inPath[:inPath.rfind("\\") + 1] + "Lexical_out.txt"			#输出结果文件路径
		self.inFile = open(inPath,"r")												#打开输入文件
		self.outFile = open(self.outPath,"w")										#打开输出文件

		self.ch = self.inFile.read(1)												#当前分析的字符
		self.lines = 1																#当前分析第几行
		self.errorCode = 0
		self.errorLines = []

		
	def LA_analysis(self):															#词法分析函数

		while True :

			if not self.ch :														#如果在文件尾就结束分析
				break
			while self.ch == " " or self.ch == "\n" or self.ch == "\t" :			#跳过空格、\t和\n
				if self.ch == "\n" :
					self.lines += 1 												#记录行数
				self.ch = self.inFile.read(1)

			if self.ch.isalpha() :

				self.LA_isAlphabet()

			elif self.ch.isdigit() :

				self.LA_isDigit()

			elif SINGLEWORD.count(self.ch) == 1 :

				self.LA_isSingleWord()

			elif DOUBLEWORD.count(self.ch) == 1 :

				self.LA_isDoubleWord()

			elif self.ch == "/" :

				self.LA_isAnnotation()

			else :

				self.LA_isError()


		if self.errorCode >0 :
			print ("[--lexical] Error : errors in lexical analysis , the error code is as follows :")
			if self.errorCode == 1 :
				print ("----[error:001] 打开词法分析输入文件出错！")
			if self.errorCode == 2 :
				print ("----[error:002] 创建词法分析输出文件出错！")
			if self.errorCode == 3 :
				for i in self.errorLines :
					print ("----[error:003] 第" + str(i) + "行有未定义符号！请检查输出文件！")
		else :
			print ("[--lexical] Lexical analysis succeed !")

		self.inFile.close()
		self.outFile.close()


	#标识符处理
	def LA_isAlphabet(self) :

		token = self.ch
		self.ch = self.inFile.read(1)

		while self.ch.isalnum() :													#如果是数字或者字母则一直查找
			token = token + self.ch
			self.ch = self.inFile.read(1)

		#折半法查保留字
		low = 0
		high = len(KEYWORD) - 1
		mid = -1
		isKeyword = 0																#如果token在标识符元组中则赋值1
		while low <= high :
			mid = (low + high) // 2;
			if operator.eq(KEYWORD[mid], token) :
				isKeyword = 1
				break																#查找成功
			elif operator.gt(KEYWORD[mid], token) :									#待查记录在低半区间
				high = mid - 1
			else :																	#待查记录在高半区间
				low = mid + 1
		if isKeyword == 0 :															#是标识符
			self.outFile.write("[{0}]\t{1}\t\t{2}\n".format(self.lines,"ID",token))
		else :																		#是保留字
			if token == "function" :												#function太长,只用一个\t对齐
				self.outFile.write("[{0}]\t{1}\t{2}\n".format(self.lines,token,token))
			else :
				self.outFile.write("[{0}]\t{1}\t\t{2}\n".format(self.lines,token,token))

	#如果是字符是数字则组合数字
	def LA_isDigit(self) :

		token = self.ch
		self.ch = self.inFile.read(1)
		while self.ch.isdigit() :													#整合数字
			token = token + self.ch
			self.ch = self.inFile.read(1)

		self.outFile.write("[{0}]\t{1}\t\t{2}\n".format(self.lines,"NUM",token))

	#单字符
	def LA_isSingleWord(self) :

		if SINGLEWORD.count(self.ch) == 1 :
			token = self.ch
			self.ch = self.inFile.read(1)
		self.outFile.write("[{0}]\t{1}\t\t{2}\n".format(self.lines,token,token))

	#双字符
	def LA_isDoubleWord(self) :

		if DOUBLEWORD.count(self.ch) == 1 :
			token = self.ch
			self.ch = self.inFile.read(1)
		if token == "&" :
			if self.ch == "&" :														#如果第二个还是&则识别为双分界符&&否则为单分界符&
				token = token + self.ch
				self.ch = self.inFile.read(1)
		elif token == "|" :
			if self.ch == "|" :
				token = token + self.ch
				self.ch = self.inFile.read(1)
		elif self.ch == "="	:														#第一个字符为其他的情况且第二个字符为=则组合双分界，否则为单分界符
			token = token + self.ch
			self.ch = self.inFile.read(1)

		self.outFile.write("[{0}]\t{1}\t\t{2}\n".format(self.lines,token,token))

	#注释处理
	def LA_isAnnotation(self) :

		if self.ch == "/" :
			self.ch = self.inFile.read(1)
			if self.ch == "*" :
				self.ch = self.inFile.read(1)
				ch1 = self.inFile.read(1)
				if self.ch == "\n" :
					self.lines += 1
				if ch1 == "\n" :
					self.lines += 1
				while (self.ch != '*' or ch1 != '/') and ch1 :						#跳过注释
					self.ch = ch1
					ch1 = self.inFile.read(1)
					if ch1 == '\n' :
						self.lines += 1
				self.ch = self.inFile.read(1)
			else :
				token = "/"
				self.outFile.write("[{0}]\t{1}\t\t{2}\n".format(self.lines,token,token))


	#错误处理
	def LA_isError(self) :

		token = self.ch
		self.ch = self.inFile.read(1)
		self.errorCode = 3															#未定义符号,错误代码3
		self.errorLines.append(self.lines)											#记录错误行号
		self.outFile.write("[{0}]\t{1}\t\t{2}\n".format(self.lines,"ERROR",token))