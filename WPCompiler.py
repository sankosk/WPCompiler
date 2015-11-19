import os, sys
from Recognizer import Recognizer
from Translater import Translator

class WPCompiler(object):

	def __init__(self):
		self.translated = []
		self.nonTranslated = []

	def fileReader(self, fileName):
		f = open(fileName, 'r')
		content = f.read()
		f.close()

		return content

	def fileWriter(self, outputFileName, toWrite):
		f = open(outputFileName, 'w')
		f.write(toWrite)
		f.close()

	def recognizeCode(self, src):
		begtags = Recognizer(content).getBegTag()
		endtags = Recognizer(content).getEndTag()
		asignations = Recognizer(content).getAssignations()
		macrosumsubs = Recognizer(content).getMathMacro()
		asignations = asignations + macrosumsubs
		succesors =  Recognizer(content).getSucessors()
		predecessors = Recognizer(content).getPredecessors()
		flowcontrols = Recognizer(content).getFlowControlStructures()

		
		for i in begtags:
			self.nonTranslated.append(i)
			self.translated.append(Translator().getTranslatedBegTag(i))

		for i in endtags:
			self.nonTranslated.append(i)
			self.translated.append(Translator().getTranslatedEndTag(i))
		
		for i in asignations:
			self.nonTranslated.append(i)
			self.translated.append(Translator().getTranslatedAssignation(i))
			
		for i in succesors:
			self.nonTranslated.append(i)
			self.translated.append(Translator().getTranslatedSucessor(i).split(";")[0])

		for i in predecessors:
			self.nonTranslated.append(i)
			self.translated.append(Translator().getTranslatedPredecessor(i).split(";")[0])

		for i in flowcontrols:
			self.nonTranslated.append(i)
			self.translated.append(Translator().getTranslatedFlowControlStruct(i))

		"""
		toRecognize = [begtags, endtags, asignations, succesors, flowcontrols]
		for i in toRecognize:
			self.self.nonself.translated.append(i)
			self.translated.append()
		"""

if "__main__":

	wp = WPCompiler()
	content = wp.fileReader(sys.argv[1])

	addToBeg = ""
	variables = Recognizer(content).getVariables()
	variables = list(set(variables)) #eliminamos var repetidas -> O(n)
	for i in variables:
		addToBeg += "%s=0\n" % i
	addToTheEnd = "\nprint x1"

	wp.recognizeCode(content)


	if(len(wp.translated) == len(wp.nonTranslated)):
		for i in range(len(wp.translated)):
			content = content.replace(wp.nonTranslated[i], wp.translated[i])

	content = addToBeg + content + addToTheEnd
	wp.fileWriter(sys.argv[2], content)

	print "Evaluated Code:"
	print "################"
	try:
		os.system("python %s" % sys.argv[2])
	except:
		print "Your .wp program feels wrong wrote, check the syntax again :D\n"
