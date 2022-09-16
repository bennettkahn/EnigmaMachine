# USUALLY 10 OUT OF 13 WIRES ON PLUGBOARD WERE USUALLY WIRED UP!!!!!!

'''
This dictionary stores the key for rotors one, two, and three
The keys are the English alphabet (in order)
The value of each entry is a list, 
with index 0 being what rotor one converts the key letter to,
index 1 being what rotor two converts the key letter to,
and index 2 being what rotor three converts the key letter to.
'''

def encrypt(phrase, right_slot, middle_slot, left_slot):
	# assign the right rotor to the user-specified start
	right_rotor = right_rotor_start

	# assign the middle rotor to the user-specified start
	middle_rotor = middle_rotor_start

	# assign the left rotor to the user-specified start
	left_rotor = left_rotor_start
	right_rotorTicks = 0
	middle_rotorTicks = 0
	encrypted = ''
	for char in phrase:

		# rotors are incremented BEFORE electrical signal passes through

		# if the middle rotor is at its notch, we increment the left rotor (regardless of whether or not right rotor is at ITS notch)
		if (middle_rotor == notch_windows[middle_slot][1]):
			if (left_rotor) == 'Z':
				left_rotor = 'A'
			else:
				left_rotor = chr(ord(left_rotor) + 1)

		# if the right rotor is at its notch OR the middle rotor is at ITS notch we increment the middle rotor
		if (right_rotor == notch_windows[right_slot][1]) or (middle_rotor == notch_windows[middle_slot][1]):
			if (middle_rotor) == 'Z':
				middle_rotor = 'A'
			else:
				middle_rotor = chr(ord(middle_rotor) + 1)

		# the right rotor increments on every key press
		# if the right_rotor is at Z, we loop back around to A
		if (right_rotor == 'Z'):
			right_rotor = 'A'
		# otherwise, we increment right_rotor by one
		else:
			right_rotor = chr(ord(right_rotor) + 1)



		right_output_to = rots_dict[right_slot][(((ord(char.upper()) + (ord(right_rotor) - 65)) - 65) % 26)]
	
		
		middle_output_to = rots_dict[middle_slot][(((ord(right_output_to) - (ord(right_rotor) - 65) + (ord(middle_rotor) - 65)) - 65) % 26)]
		

		left_output_to = rots_dict[left_slot][(((ord(middle_output_to) - (ord(middle_rotor) - 65) + (ord(left_rotor) - 65)) - 65) % 26)]

	
		r3Input = reflector[((ord(left_output_to) - (ord(left_rotor) - 65)) - 65) % 26]

	
		left_output_back_dec = rots_dict[left_slot].find(chr((((ord(r3Input) + (ord(left_rotor) - 65)) - 65) % 26) + 65)) + 65
		

		if (left_output_back_dec < 65):
			left_output_back = chr(91 - (65 - left_output_back_dec))

		else:
			left_output_back = chr(left_output_back_dec)
		

		middle_output_back_dec = rots_dict[middle_slot].find(chr((((ord(left_output_back) + (ord(middle_rotor) - 65) - (ord(left_rotor) - 65)) - 65) % 26) + 65)) + 65

		# in some scenarios, the line above (final return letter) will return a number LESS THAN 65
		# this is because the ord(encoding done by right rotor) - ord(current setting of the right rotor) is LESS THAN 65
			# this happens when, for example, the right rotor returns an 'F' and is set at 'M'
			# to get our final return letter, we do F = 6 MINUS M = 12 (i.e. move over 12 ticks on rotor one in the reverse direction of the alphabet)
			# arithmatically, this returns -6, but it should really return 26 - (12-6), which account for wrapping back around
		# final note: modular arithmetic could be used in this case, but we invoke the following construction for clarity's sake
		if (middle_output_back_dec < 65):
			middle_output_back = chr(91 - (65 - middle_output_back_dec))

		else:
			middle_output_back = chr(middle_output_back_dec)
		

		right_output_back_dec = rots_dict[right_slot].find(chr((((ord(middle_output_back) + (ord(right_rotor) - 65) - (ord(middle_rotor) - 65)) - 65) % 26) + 65)) + 65 - (ord(right_rotor) - 65)


		if (right_output_back_dec < 65):
			right_output_back = chr(91 - (65 - right_output_back_dec))

		else:
			right_output_back = chr(right_output_back_dec)
		
		encrypted += right_output_back

	


	return encrypted


print("For all three rotor positions please indicate which rotor (I, II, III, IV, or V) you would like to place there. ")

valid_rotors = ['I', 'II', 'III', 'IV', 'V']

# validate input
while True:
	slotOne = input("Which rotor would you like on the right? ")
	slotTwo = input("Which rotor would you like in the middle? ")
	slotThree = input("Which rotor would you like on the left? ")
	if (slotOne in valid_rotors) and (slotTwo in valid_rotors) and (slotThree in valid_rotors):
		break
	else:
		print("Please enter 'I', 'II', 'III', 'IV', or 'V' for each rotor")
		

print()

# the notch of rotor I is located at letter Y
# when Q is in the window for rotor I and a key is pressed (rotor I moving from Q -> R), the rotor to the left advances
# We are storing the notch/window combos of each rotor in a dictionary
# key = rotor number (Roman Numeral); value = list ([Notch Letter, Window Letter])
notch_windows = {'I': ['Y', 'Q'], 'II': ['M', 'E'], 'III': ['D', 'V'], 'IV': ['R', 'J'], 'V': ['H', 'Z']}

rots_dict = {'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'IV': 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'V': 'VZBRGITYUPSDNHLXAWMJQOFECK'}
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

r = range(ord('A'), ord('Z') + 1) # range of ASCII values for all uppercase letters

# validate input
while True:
	
	try:
		right_rotor_start =  input("Which letter would you like the right rotor to start on? (A-Z) ").upper()
		middle_rotor_start = input("Which letter would you like the middle rotor to start on? (A-Z) ").upper()
		left_rotor_start = input("Which letter would you like the left rotor to start on? (A-Z) ").upper()

		if (ord(right_rotor_start) in r) and (ord(middle_rotor_start) in r) and (ord(left_rotor_start) in r):
			break
		else:
			print("Please enter (A-Z) for each rotor start")
	
	except:
		print("Please be sure to enter a character (A-Z) for each rotor\n")
		continue
	
	
		
	
print('\n')

phrase = ''
print("You are using a Enigma Machine with the following configuration: ")
print("\tRight Rotor: {}, beginning at {}".format(slotOne, right_rotor_start))
print("\tMiddle Rotor: {}, beginning at {}".format(slotTwo, middle_rotor_start))
print("\tLeft Rotor: {}, beginning at {}".format(slotThree, left_rotor_start))
print()
while (phrase != 'q'):

	phrase = raw_input("Please enter the phrase that you would like to be encrypted ('q' to quit/reset rotors): ")
	
	print("\'{}\' encrypts to: ".format(phrase))

	print(encrypt(phrase.upper(), slotOne, slotTwo, slotThree))
	print()

	
print("Thanks for playing!")
	


