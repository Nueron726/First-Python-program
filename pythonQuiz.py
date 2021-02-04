# pythonQuiz
# This program is meant to mimic a small quiz, consisting of only 10 questions.
# Author@ Alexis Delgado

#print "Please answer the following questions"
# I decided that it would be best to have the question number and the actual question in the same print line, to reduce the clutter of sequential prints. 
print "Question 1", "\nWhat is the term that describes the magnitude of gene expression?"
print " A. Variable expressivity"
print " B. Incomplete penetrance"
print " C. Codominance"
print " D. Gene supression"



num_correct = 0


Answer = raw_input ("Enter answer: ")


if Answer == "A" or Answer == "a":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is A\n"


print "Question 2", "\nIf a person is diplaying maternal effect, where are they getting their genes from?"
print " A. Extra nuclear genes"
print " B. X linked chromosomes"
print " C. Y linked chromosome"
print " D. Dad linked chromsomes"


Answer = raw_input ("Enter answer: ")


if Answer == "B" or Answer == "b":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is B\n"



print "Question 3", "\nWhich gene is actively transcribed to produce barr bodies?"
print " A. Tsix gene"
print " B. Sixt gene"
print " C. P300 gene"
print " D. P4 gene"


Answer = raw_input ("Enter answer: ")


if Answer == "C" or Answer == "c":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is C\n"


print "Question 4", "\nWho was the geneticist that first observed a double cross over event? "
print " A. Mario Capecchi"
print " B. Gregor Mendel"
print " C. Barbara McClintock"
print " D. Thomas s. Morgan"


Answer = raw_input ("Enter answer: ")


if Answer == "D" or Answer == "d":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is B\n"


print "Question 5", "\nThe theory that describes gene as discrete heritable units is termed"
print " A. The particulate theory of inheritance"
print " B. The blending hypothesis"
print " C. The law of segregation"
print " D. That law of independent assortment"


Answer = raw_input ("Enter answer: ")


if Answer == "B" or Answer == "b":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is B\n"



print "Question 6", " \nWho should be given credit for the discovery of the helical structure of DNA? "
print " A. James Watson"
print " B. Francis Crick"
print " C. Rosalind Franklin"
print " D. Aleis Deglado"


Answer = raw_input ("Enter answer: ")


if Answer == "C" or Answer == "c":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is B\n"


print "Question 7", " \nWhat effect does trysomny have on oocytes during gametogenesis?"
print " A. Nonvaliable"
print " B. Trysomy"
print " C. Abnormalities in individual"
print " D. All of the above"


Answer = raw_input ("Enter answer: ")


if Answer == "D" or Answer == "d":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is B\n"


print "Question 8", " \nTranslocation of metacentric chrosomes into a methylated area can effect the gene expression by:  "
print " A. variable expressivity"
print " B. Gene product"
print " C. Not expressing anyting at all"
print " D. All of the above"


Answer = raw_input ("Enter answer: ")


if Answer == "C" or Answer == "c":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is B\n"


print "Question 9", " \nFind the molarity of a 1 liters 3 Molar solution of HCl, that was diluted with .5 Liters of HF.  "


Answer = int(raw_input ("Enter answer: "))
Answer1 = raw_input ("Units: ")

#This type of input was a bit tricky. It would have been nice to have had both prompt horizontally, rather than vertically. 
if Answer == 6 and Answer1 == "M":
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, the correct answer is: 6 M", "\n"


print "Question 10", "\nHow many micrmedeters are in a milimeters? Include appropiate signifcant figures "


Answer = float(raw_input ("Enter answer: "))



if Answer == 0.001 :
    print "You are correct!\n"
    num_correct = num_correct + 1
else:
    print "Sorry, there are 0.001 milimeters in a micrometer\n"

print "You got", num_correct/ float (10) * 100 , "% on the quiz!", "\nYou got", num_correct, " out of 10."


# I wanted to display messeages that the participant would recieve based on his/her performance on the quiz.
# I wonder if I'll be able to guide the participant through why their given answer was incorrect, much in the same way
# some math programs step you through an equation when you don't get the answer right. 
if num_correct/float (10) *100 < 60:
    print "You're not doing very well, you should come visit me during office hours."
elif num_correct/float (10) *100 > 60 and num_correct/float (10) *100 < 80:
    print "Keep it up, but work a tad harder!"
elif num_correct/float (10) *100 > 80:
    print "Not bad!"




   


