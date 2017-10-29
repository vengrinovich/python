def rgb_hex():
	invalid_msg = "Invalid value added"
	red = int(raw_input("Enter a value for red (R): "))
	if red < 0 or red > 255:
		print invalid_msg

	green = int(raw_input('Enter a value for green (G): '))
	if green < 0 or green > 255:
		print invalid_msg

	blue = int(raw_input('Enter a value for green (G): '))
	if blue < 0 or blue > 255:
		print invalid_msg

	val = (red << 16) + (green << 8) + blue
	print "%s" % (hex(val)[2:]).upper()
