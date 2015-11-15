import os,sys

from Recognizer import Recognizer
from Translater import Translator

f = open(str(sys.argv[1]), "r")
content = f.read()
f.close()

translated = []
nontranslated = []

addToBegining = ""
variables = Recognizer(content).getVariables()
for i in variables:
	addToBegining += "%s=0\n" % i

addToTheEnd = "\nprint x1"
begtags = Recognizer(content).getBegTag()
endtags = Recognizer(content).getEndTag()
asignations = Recognizer(content).getAssignations()
succesors =  Recognizer(content).getSucessors()
flowcontrols = Recognizer(content).getFlowControlStructures()


for i in begtags:
	nontranslated.append(i)
	translated.append(Translator().getTranslatedBegTag(i))

for i in endtags:
	nontranslated.append(i)
	translated.append(Translator().getTranslatedEndTag(i))

for i in asignations:
	nontranslated.append(i)
	translated.append(Translator().getTranslatedAssignation(i))

for i in succesors:
	nontranslated.append(i)
	translated.append(Translator().getTranslatedSucessor(i).split(";")[0])

for i in flowcontrols:
	nontranslated.append(i)
	translated.append(Translator().getTranslatedFlowControlStruct(i))


if(len(translated) == len(nontranslated)):

	for i in range(len(translated)):
		content = content.replace(nontranslated[i], translated[i])


content = addToBegining + content + addToTheEnd
f = open(sys.argv[2], "w")
f.write(content)
f.close()


os.system('python %s' % sys.argv[2])

