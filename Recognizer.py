import os, re

"""
@Author:		Esteban Montes Morales
@Description: 	Used to recognize reservated words of a while program
"""

#GRAMMAR CONSTANTS
BEGTAG = "BEGIN|begin|Begin"
ENDTAG = "end|End|END"
VARIABLE = "x[0-9]*"
NUMBER = "[0-9]"
COMPARATOR = "==|>=|<=|>|<|!="
SUCESSOR = "succ[(][\s]*%s[\s]*[)];"%(VARIABLE)
ASSIGNATION = "[\s]*%s[\s]*:=[\s]*x[0-9*]+[\s]*;|[\s]*%s[\s]*:=[\s]*[0-9*]+[\s]*;"%(VARIABLE, VARIABLE)
SENTENCE = "%s|%s" % (ASSIGNATION, SUCESSOR)
FLOWCONTROLSTR = "[\s]*while[(]x[0-9]*[><=]+x[0-9]*[)][\s]do"

class Recognizer(object):
	
	def __init__(self, sourceCode):
		self.sourceContent = sourceCode
		self.availableWords = [SENTENCE, FLOWCONTROLSTR]

	def getAllReservedWords(self):
		"""
		Get all reserved words found in the wp source code
		@return: List of reserved words
		"""

		res = []
		for w in self.availableWords:
			pattern = re.compile(w)
			for x in pattern.findall(self.sourceContent):
				res.append(x)

		return res


	def getBegTag(self):
		patter = re.compile(BEGTAG)
		return patter.findall(self.sourceContent)

	def getEndTag(self):
		patter = re.compile(ENDTAG)
		return patter.findall(self.sourceContent)

	def getVariables(self):
		"""
		Get all variables of the source code
		@return: List of variables
		"""
		pattern = re.compile(VARIABLE)
		return pattern.findall(self.sourceContent)

	def getAssignations(self):
		"""
		Get all assignations of the source code
		@return: List of assignations
		"""
		pattern = re.compile(ASSIGNATION)
		return pattern.findall(self.sourceContent)

	def getSentences(self):
		"""
		Get all sentences of the source code
		@return: List of sentences
		"""
		pattern = re.compile(SENTENCE)
		return pattern.findall(self.sourceContent)

	def getComparators(self):
		"""
		Get all comparators of the source code
		@return: List of comparators
		"""
		pattern = re.compile(COMPARATOR)
		return pattern.findall(self.sourceContent)

	def getSucessors(self):
		"""
		Get all sucessor sentences of the source code
		@return: List of sucessors sentences
		"""
		pattern = re.compile(SUCESSOR)
		return pattern.findall(self.sourceContent)

	def getPredecessors(self):
		"""
		Get all predecessors sentences of the source code
		@return: List of predecessors sentences
		"""
		return ""

	def getFlowControlStructures(self):
		"""
		Get all flow control stuctures of the source code
		@return: List of <<while() do{}>>
		"""
		pattern = re.compile(FLOWCONTROLSTR)
		return pattern.findall(self.sourceContent)