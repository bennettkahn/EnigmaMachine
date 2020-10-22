print("For all three rotor positions please indicate which rotor (I, II, III, IV, or V) you would like to place there. ")


slotOne = raw_input("Which rotor would you like on the right? ")
slotTwo = raw_input("Which rotor would you like in the middle? ")
slotThree = raw_input("Which rotor would you like on the left? ")


#rots_dict = {'A': [slotOne[0], slotTwo[0], slotThree[0]], 'B': [slotOne[1], slotTwo[1], slotThree[1]], 'C': [slotOne[2], slotTwo[2], slotThree[2]], 'D':[slotOne[3], slotTwo[3], slotThree[3]],'E': [slotOne[4], slotTwo[4], slotThree[4]],'F': [slotOne[5], slotTwo[5], slotThree[5]], 'G': [slotOne[6], slotTwo[6], slotThree[6]], 'H': [slotOne[7], slotTwo[7], slotThree[7]], 'I': [slotOne[8], slotTwo[8], slotThree[8]], 'J': [slotOne[9], slotTwo[9], slotThree[9]], 'K': [slotOne[10], slotTwo[10], slotThree[10]], 'L': [slotOne[11], slotTwo[11], slotThree[11]], 'M': [slotOne[12], slotTwo[12], slotThree[12]], 'N': [slotOne[13], slotTwo[13], slotThree[13]], 'O': [slotOne[14], slotTwo[14], slotThree[14]], 'P': [slotOne[15], slotTwo[15], slotThree[15]], 'Q': [slotOne[16], slotTwo[16], slotThree[16]], 'R': [slotOne[17], slotTwo[17], slotThree[17]], 'S': [slotOne[18], slotTwo[18], slotThree[18]], 'T': [slotOne[19], slotTwo[19], slotThree[19]], 'U': [slotOne[20], slotTwo[20], slotThree[20]], 'V': [slotOne[21], slotTwo[21], slotThree[21]], 'W': [slotOne[22], slotTwo[22], slotThree[22]], 'X': [slotOne[23], slotTwo[23], slotThree[23]], 'Y': [slotOne[24], slotTwo[24], slotThree[24]], 'Z': [slotOne[25], slotTwo[25], slotThree[25]]}
reflectorDict = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'} # Z really connected to L; connecting to T for test

# the notch of rotor I is located at letter Y
# when Q is in the window for rotor I and a key is pressed (rotor I moving from Q -> R), the rotor to the left advances
# We are storing the notch/window combos of each rotor in a dictionary
# key = rotor number (Roman Numeral); value = list ([Notch Letter, Window Letter])
notch_windows = {'I': ['Y', 'Q'], 'II': ['M', 'E'], 'III': ['D', 'V'], 'IV': ['R', 'J'], 'V': ['H', 'Z']}

rots_dict = {'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'IV': 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'V': 'VZBRGITYUPSDNHLXAWMJQOFECK'}
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'


right_rotor_start =  raw_input("Which letter would you like the right rotor to start on? ")
middle_rotor_start = raw_input("Which letter would you like the middle rotor to start on? ")
left_rotor_start = raw_input("Which letter would you like the left rotor to start on? ")
print('\n')
right_rotor_ring = 'A' #raw_input("Which letter would you like as the ring setting for the rotor in slot one? ")
middle_rotor_ring = 'A' #raw_input("Which letter would you like as the ring setting for the rotor in slot two? ")
left_rotor_ring = 'A' #raw_input("Which letter would you like as the ring setting for the rotor in slot three? ")


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



		print("Right rotor is at: " + right_rotor)
		print("Middle rotor is at: " + middle_rotor)
		print("Left rotor is at: " + left_rotor)

		right_output_to = rots_dict[right_slot][(((ord(char.upper()) + (ord(right_rotor) - 65)) - 65) % 26)]
		
		print(right_output_to)
		
		middle_output_to = rots_dict[middle_slot][(((ord(right_output_to) - (ord(right_rotor) - 65) + (ord(middle_rotor) - 65)) - 65) % 26)]
		
		print(middle_output_to)

		left_output_to = rots_dict[left_slot][(((ord(middle_output_to) - (ord(middle_rotor) - 65) + (ord(left_rotor) - 65)) - 65) % 26)]

		print(left_output_to)

		r3Input = reflector[((ord(left_output_to) - (ord(left_rotor) - 65)) - 65) % 26]

		print(r3Input)


		left_output_back_dec = rots_dict[left_slot].find(chr((((ord(r3Input) + (ord(left_rotor) - 65)) - 65) % 26) + 65)) + 65
		
		print("left_output_back_dec: " + str(left_output_back_dec))

		if (left_output_back_dec < 65):
			left_output_back = chr(91 - (65 - left_output_back_dec))

		else:
			left_output_back = chr(left_output_back_dec)


		print(left_output_back)

		

		middle_output_back_dec = rots_dict[middle_slot].find(chr((((ord(left_output_back) + (ord(middle_rotor) - 65) - (ord(left_rotor) - 65)) - 65) % 26) + 65)) + 65

		#middle_output_back_dec = rots_dict[middle_slot].find(chr(ord(left_output_back) + (ord(middle_rotor) - 65) - (ord(left_rotor) - 65))) + 65

		


		print("middle_output_back_dec: " + str(middle_output_back_dec))

		# in some scenarios, the line above (final return letter) will return a number LESS THAN 65
		# this is because the ord(encoding done by right rotor) - ord(current setting of the right rotor) is LESS THAN 65
			# this happens when, for example, the right rotor returns an 'F' and is set at 'M'
			# to get our final return letter, we do F = 6 MINUS M = 12 (i.e. move over 12 ticks on rotor one in the reverse direction of the alphabet)
			# arithmatically, this returns -6, but it should really return 26 - (12-6), which account for wrapping back around
		# final note: modular arithmetic could be used in this case, but we envoke the following construction for clarity's sake
		if (middle_output_back_dec < 65):
			middle_output_back = chr(91 - (65 - middle_output_back_dec))

		else:
			middle_output_back = chr(middle_output_back_dec)

		#middle_output_back = rots_dict[middle_slot][(((ord(left_output_back) + (ord(middle_rotor) - 65) - (ord(left_rotor) - 65)) - 65) % 26)]
		print(middle_output_back)

		right_output_back_dec = rots_dict[right_slot].find(chr((((ord(middle_output_back) + (ord(right_rotor) - 65) - (ord(middle_rotor) - 65)) - 65) % 26) + 65)) + 65 - (ord(right_rotor) - 65)

		print('right_output_back_dec: ' + str(right_output_back_dec))

		if (right_output_back_dec < 65):
			right_output_back = chr(91 - (65 - right_output_back_dec))

		else:
			right_output_back = chr(right_output_back_dec)

		#right_output_back = rots_dict[right_slot][(((ord(middle_output_back) + (ord(right_rotor) - 65) - (ord(middle_rotor) - 65)) - 65) % 26)]
		print(right_output_back)
		encrypted += right_output_back

	


	return encrypted



'''
def increment(rotor):
	print("In increment function, rotor is at: " + rotor)
	if rotor == 'Z':
		rotor == 'A'
	else:

		rotor = chr(ord(rotor)+1)
'''

phrase = ''

while (phrase != '-1'):

	phrase = raw_input("Please enter the phrase that you would like to be encrypted: ")

	print(encrypt(phrase, slotOne, slotTwo, slotThree))












