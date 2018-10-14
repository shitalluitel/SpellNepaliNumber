
def convert(data):
	numberMap = {
		".":".",
		"0":"०",
		"1":"१",
		"2":"२",
		"3":"३",
		"4":"४",
		"5":"५",
		"6":"६",
		"7":"७",
		"8":"८",
		"9":"९",
	}

	length = len(data)
	nepaliNumber = ""

	for i in range(0,length):
		nepaliNumber += numberMap[data[i]]

	return nepaliNumber


def run():

	dictData = {
		"०१":"एक","०२":"दुई","०३": "तिन", "०४": "चार", "०५": "पाँच", "०६": "छ", "०७": "सात", "०८": "आठ", "०९": "नौ", 
		"०": "सुन्ना", "१": "एक", 	"२": "दुई", "३": "तिन", "४": "चार", "५": "पाँच", "६": "छ", "७": "सात", "८": "आठ", "९": "नौ", 
		"१०": "दस", "११": "एघार", "१२": "बाह्र", "१३": "तेह्र", "१४": "चौध", "१५": "पन्ध्र", "१६": "सोह्र", "१७": "सत्र", "१८": "अठार", "१९": "उन्नाइस", 
		"२०": "बिस", "२१": "एक्काइस", "२२": "बाइस", "२३": "तेइस", "२४": "चौबिस", "२५": "पच्चिस", "२६": "छब्बिस", "२७": "सत्ताइस", "२८": "अट्ठाइस", "२९": "उनन्तिस", 
		"३०": "तिस", "३१": "एकतिस", "३२": "बत्तिस", "३३": "तेत्तिस", "३४": "चौँतिस", "३५": "पैँतिस", "३६": "छत्तिस", "३७": "सैँतिस", "३८": "अठतिस", "३९": "उनन्चालिस",
		"४०": "चालिस", "४१": "एकचालिस", "४२": "बयालिस", "४३": "त्रिचालिस", "४४": "चवालिस", "४५": "पैँतालिस", "४६": "छयालिस", "४७": "सतचालिस", "४८": "अठचालिस", "४९": "उनन्चास", 
		"५०": "पचास", "५१": "एकाउन्न", "५२": "बाउन्न", "५३": "त्रिपन्न", "५४": "चवन्न", "५५": "पचपन्न", "५६": "छपन्न", "५७": "सन्ताउन्न", "५८": "अन्ठाउन्न", "५९": "उनन्साठी", 
		"६०": "साठी", "६१": "एकसट्ठी", "६२": "बयसट्ठी", "६३": "त्रिसट्ठी", "६४": "चौसट्ठी", "६५": "पैँसट्ठी", "६६": "छयसट्ठी", "६७": "सतसट्ठी", "६८": "अठसट्ठी", "६९": "उनन्सत्तरी", 
		"७०": "सत्तरी", "७१": "एकहत्तर", "७२": "बहत्तर", "७३": "त्रिहत्तर", "७४": "चौहत्तर", "७५": "पचहत्तर", "७६": "छयहत्तर", "७७": "सतहत्तर", "७८": "अठहत्तर", "७९": "उनासी",
		"८०": "असी", "८१": "एकासी", "८२": "बयासी", "८३": "त्रियासी", "८४": "चौरासी", "८५": "पचासी", "८६": "छयासी", "८७": "सतासी", "८८": "अठासी", "८९": "उनान्नब्बे", 
		"९०": "नब्बे", "९१": "एकानब्बे", "९२": "बयानब्बे", "९३": "त्रियानब्बे", "९४": "चौरानब्बे", "९५": "पन्चानब्बे", "९६": "छयानब्बे", "९७": "सन्तानब्बे","९८": "अन्ठानब्बे", "९९": "उनान्सय"		
	}

	inData = input("Enter a number: ")

	try:
		if int(inData[0]) in range(0,10):
			inData = convert(inData)	
	except:
		inData = inData

	try:
		rupee, paisa = inData.split('.')
	except:
		rupee = inData
		paisa = ""

	length = len(rupee)
	rupee = rupee[::-1]

	if len(paisa) > 2:
		print("Only 2 digits accepted after decimal.")

	outputString = ""

	dictmap = {
		"3": "सय",
		"4": "हजार",
		"5": "हजार",
		"6": "लाख",
		"7": "लाख",
		"8": "करोड",
		"9": "करोड",	
		"10": "अरब",
		"11": "अरब",
		"12": "खरब",
		"13": "खरब",
	}

	try:
		if length > 3:
			if length % 2 == 0:
				old_length = length	
				length = length - 1
				nepaliString = rupee[length]
				outputString += dictData[nepaliString] + " " + dictmap[str(old_length)] + " "

			for i in range(length,3, -2):
				nepaliString = rupee[i-2:i][::-1]
				outputString += dictData[nepaliString] + " " + dictmap[str(i)] + " "
			length = 3

		if length == 3:
			nepaliString = rupee[2]
			outputString += dictData[nepaliString] + " " + dictmap[str(3)] + " "	

		if length == 2:
			nepaliString = rupee[0:2][::-1]
			if not nepaliString == '००':
				outputString +=	dictData[nepaliString] + " रुपैयाँ "
		else:
			nepaliString = rupee[0]
			if not nepaliString == '०':
				outputString += dictData[nepaliString] + " रुपैयाँ "	

		if len(paisa) > 0:
			if not paisa == '००' and not paisa == '०':
				outputString += dictData[paisa] + " पैसा "

		print("%s= %s" % 	(inData,outputString))
		return outputString
	except :
		print("Unable to convert.")
	

def main():
	run()

if __name__ == "__main__":
	main()
