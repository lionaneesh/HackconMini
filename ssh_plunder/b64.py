
import base64                                                        

file = open("lipsum.txt")
line = file.read()
line = line.replace("\n" , "##NEWLINE##")
words = line.split()


for word in words:
	print base64.b64encode(word)


