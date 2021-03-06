import os, re

"""
@Author:		Esteban Montes Morales
@Description: 	Used to recognize reservated words of a while program
"""
#To FIX:
"""
 - Soportar multiples condiciones en los while
 - Anadir los operadores aritmetico-logicos -> {AND, OR, NOT, XOR}
 - Anadir soporte para comentarios
 - Asegurarse de que se respetan las reglas a la hora de anidar funciones
 - Implementar soporte para sentencias de asignacion tales que :  X1 := 0 .. Xn;
 - Implementar soporte para sentencias de asignacio como : Xk+1 := x1; para facilitar el anidado de funciones
"""

#GRAMMAR CONSTANTS
BEGTAG = "BEGIN|begin|Begin"
ENDTAG = "end|End|END"
VARIABLE = "x[0-9]*"
NUMBER = "[0-9]"
COMPARATOR = "==|>=|<=|>|<|!="
SUCESSOR = "succ[(][\s]*%s[\s]*[)];"%(VARIABLE)
PREDECESSOR = "pred[(][\s]*%s[\s]*[)];"%(VARIABLE)
ASSIGNATION = "[\s]*%s[\s]*:=[\s]*x[0-9*]+[\s]*;|[\s]*%s[\s]*:=[\s]*[0-9*]+[\s]*;"%(VARIABLE, VARIABLE)
MATHMACROS = "[\s]*%s[\s]*:=[\s]*%s[\s]*[+-/*][\s]*%s[\s]*;" % (VARIABLE, VARIABLE, VARIABLE)
SENTENCE = "%s|%s|%s" % (ASSIGNATION, SUCESSOR, PREDECESSOR)
FLOWCONTROLSTR = "[\s]*while[(]x[0-9]*[!><=]+x[0-9]*[)][\s]do|[\s]*while[(]x[0-9]*[!><=]+[0-9]*[)][\s]do"
COMMENTS = ""
LOGICALOPERATORS = ""

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
		pattern = re.compile(PREDECESSOR)
		return pattern.findall(self.sourceContent)

	def getFlowControlStructures(self):
		"""
		Get all flow control stuctures of the source code
		@return: List of <<while() do{}>>
		"""
		pattern = re.compile(FLOWCONTROLSTR)
		return pattern.findall(self.sourceContent)
		
	def getMathMacro(self):
		"""
		
		"""
		pattern = re.compile(MATHMACROS)
		return pattern.findall(self.sourceContent)
		
