import json

def nepaliNumberSpelling():
	f = open('nepalinumber.json', 'r')

	data = f.readline()

	dictData = json.loads(data)

	inData = input("Enter a number: ")

	try:
		rupee, paisa = inData.split('.')
	except:
		rupee = inData
		paisa = None

	length = len(rupee)
	rupee = rupee[::-1]


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

	nepaliString = rupee[0:2][::-1]
	outputString +=	dictData[nepaliString] + " रुपैयाँ "

	if paisa:
		outputString += dictData[paisa] + " पैसा"

	print(outputString)

	return outputString

def main():
	nepaliNumberSpelling()

if __name__ == "__main__":
	main()
