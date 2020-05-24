# Name : TEST语言编译器
# Time : 2018.11.20 ~ 2018.
# Developer : wngg
# Coding : utf-8

from lexicalAnalysis import LexicalAnalysis
from otherClass import StringOut
from otherClass import InputCommands
from grammaticalAnalysis import GrammaticalAnalysis

# --------------------GLOBAL------------------- #



# --------------------CLASS-------------------- #



# --------------------FUNCT-------------------- #

def main():

	#提示字符串输出
	stringOut = StringOut()
	stringOut.version()
	stringOut.commands_list()

	while True :

		#用户输入命令
		print()
		inputCommands = InputCommands(input(">>> "))

		#-h命令
		if inputCommands.is_help == 1 :
			stringOut._help()

		#-l命令
		if inputCommands.is_lexical == 1 :
			lexicalAnalysis = LexicalAnalysis(inputCommands.filePath)
			lexicalAnalysis.LA_analysis()
			
		#-g命令
		if inputCommands.is_grammatical == 1 :
			if inputCommands.is_lexical == 0 :
				print ("[--grammatical] error : Lexical analysis is needed before grammatical analysis !")
			else :
				grammaticalAnalysis = GrammaticalAnalysis(inputCommands.filePath[:inPath.rfind("\\") + 1] + "Lexical_out.txt")
		print

# --------------------ENTRY-------------------- #

if __name__ == '__main__':
	
	main()






























'''
 
    █████▒█    ██  ▄████▄   ██ ▄█▀       ██████╗ ██╗   ██╗ ██████╗
  ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒        ██╔══██╗██║   ██║██╔════╝
  ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░        ██████╔╝██║   ██║██║  ███╗
  ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄        ██╔══██╗██║   ██║██║   ██║
  ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄       ██████╔╝╚██████╔╝╚██████╔╝
   ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒       ╚═════╝  ╚═════╝  ╚═════╝
   ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
   ░ ░    ░░░ ░ ░ ░        ░ ░░ ░
            ░     ░ ░      ░  ░
'''


