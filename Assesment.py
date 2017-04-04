#This program helps measure how successful a developer would be based on the preset criterias
#
#Oyom Ada - 1/04/2017


def calculate(answer,result): #gets total sum of scores 
	if answer == "c":
		result +=12
		return result

	elif answer == "b": 
		result +=10
		return result

	elif answer == "a":
		result +=7
		return result
	else:
		print "Your Answer has to be either 'a', 'b', or 'c'. Please re-enter your answer choice "
		answer = raw_input()
		calculate(answer,result)


def remark(result): #Gets final remark after result is displayed
	if result <=40:
		text = "Your passion is as cold as Ice, you need urgent help!"

	elif result >= 41 and result <= 60:
		text = "You need to step out of your comfort zone and be a little more proactive"

	elif result >= 61 and result <= 80:
		text = "The fire is definitely burning!"

	elif result >80:
		text ="Defitely C.E.O material!!!"
	return text

#following functions define each question intended for the test
def early_to_work(result):
	print"================================================================="
	print "\n\tHow early do you arrive at work?:  \n"
	print "\nA) African Timer (1hour or more after resumption)\n"
	print "\nB) Average(5 - 30 minutes after resumption)\n"
	print "\nC) I'm the Unofficial gateman(1-2hours before resumption)\n"
	answer = raw_input()
	result = calculate(answer,result)
	return result

def consistency(result): 
	print"================================================================="
	print "\n1) How many hours do you spend at your work station in a day? \n"
	print "\nA) Less Than 6 hours "
	print "\nB) 6-8 hours "
	print "\nC) 8 hours+ "
	answer = raw_input()
	result = calculate(answer,result)
	return result

def social_media_time(result):
	print"================================================================="
	print "\n2) How often do you make use of social media in a day? \n"
	print "\nA) Always Online "
	print "\nB) Half or less than a day "
	print "\nC) Who Social media epp? "
	answer = raw_input()
	result = calculate(answer,result)
	return result

def critical_thinking(result):
	print"================================================================="
	print "\n3) What is your view towards critical thinking? \n"
	print "\nA) Just Solve, think later "
	print "\nB) Solve while thinking "
	print "\nC) Think twice before solving "
	answer = raw_input()
	result = calculate(answer,result)
	return result

def problem_solving(result):
	print"================================================================="
	print "\n4) How eager are you to problem solving? \n"
	print "\nA) Run far away as much as possible "
	print "\nB) Not eager, but never turn down the opportuinity "
	print "\nC) Always eager to solve any"
	answer = raw_input()
	result = calculate(answer,result)
	return result

def collaboration(result):
	print"================================================================="
	print "\n5) How often do you get involved in team collaborations? \n"
	print "\nA) Indifferent, who collaboration epp?  "
	print "\nB) I can\'t tolerate working with other people' "
	print "\nC) Forever in favour of it"
	answer = raw_input()
	result = calculate(answer,result)
	return result

def helping_others(result):
	print"================================================================="
	print "\n6) Do you enjoy rendering solutions to colleagues in need? \n"
	print "\nA) Total loner, i'm cool like that  "
	print "\nB) Detest it, it's time wasting "
	print "\nC) All down for it "
	answer = raw_input()
	result = calculate(answer,result)
	return result

def cheat_codes(result):
	print"================================================================="
	print "\n7) How often do you copy codes from developer sites? \n"
	print "\nA) Google, stackoverflow etc are forever bae  "
	print "\nB) Average user "
	print "\nC) Hardly"
	answer = raw_input()
	result = calculate(answer,result)
	return result

def welcome_note(): 
	print "===============ASSESSMENT TEST=================="
	name = raw_input ("Please input your name: ")
	#profession = (raw_input ("What Is your current profession"))
	print "\n\nHello %s This test is meant to find out your level of dedication and passion to your Job\n" %(name.title())
	print "Just A few questions and you\'re done!"
	print "To answer, type in your answer choice i.e 'a', 'b' or 'c' "
	response  = raw_input("\nExcited to take the test? type 'TAKE', or 'EXIT' TO quit the Test at any time \n:  ")
	response = response.lower()
	result = 0
	if response == "take":
		early = early_to_work(result)
		consistent = consistency(result)
		social = social_media_time(result)
		critical = critical_thinking(result)
		problem = problem_solving(result)
		collabo = collaboration(result)
		helping = helping_others(result)
		cheat = cheat_codes(result)

		score = early + consistent + social + critical + problem + collabo + helping + cheat
		print "You scored ", score 
		comment = remark(score)
		print comment
	if response == "exit":
		print "Goodbye"
		return


welcome_note()