# Name : TEST语言编译器
# Time : 2018.11.20 ~ 2018.
# Developer : wngg
# Coding : utf-8


# --------------------CLASS-------------------- #

#语法分析器
#作用：进行语法分析
#输入：文件路径
class GrammaticalAnalysis :

	def __init__(self,inPath) :

		self.outPath = inPath[:inPath.rfind("\\") + 1] + "Grammatical_out.txt"		#输出结果文件路径
		self.inFile = open(inPath,"r")												#打开输入文件
		self.outFile = open(self.outPath,"w")										#打开输出文件