class Translator(object):

	def getTranslatedVariable(self, code):
		"""
		Method to tranlate <<variables>> program while sintax to python
		@param: a string that contains the program while code to replace
		"""
		return ""

	def getTranslatedAssignation(self, code):
		"""
		Method to tranlate <<variables>> program while sintax to python
		@param: a string that contains the program while code to replace
		"""
		return "".join("".join(code).split(":")).split(";")[0]

	def getTranslatedComparator(self, code):
		"""
		Method to tranlate <<variables>> program while sintax to python
		@param: a string that contains the program while code to replace
		"""
		return ""

	def getTranslatedSucessor(self, code):
		"""
		Method to tranlate <<sucessor>> program while sintax to python
		@param: a string that contains the program while code to replace
		"""
		return "".join("".join("".join(code).split("succ(")).split(")")[0] + "+=1")

	def getTranslatedPredecessor(self, code):
		"""
		Method to tranlate <<variables>> program while sintax to python
		@param: a string that contains the program while code to replace
		"""
		return "".join("".join("".join(code).split("pred(")).split(")")[0] + "-=1")


	def getTranslatedFlowControlStruct(self, code):
		"""
		Method to tranlate <<variables>> program while sintax to python
		@param: a string that contains the program while code to replace
		"""
		return "".join(code).split(" do")[0] + ":"
		
	def getTranslatedBegTag(self, code):
		return ""

	def getTranslatedEndTag(self, code):
		return ""
		
	def getTranslatedMathMacro(self,code):
		return code.split(";")[0].replace(":=", "=")
		
