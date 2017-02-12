import serial
import datetime
import math

ser = serial.Serial('/dev/ttyAMA0', 2400, timeout=0.1, parity=serial.PARITY_EVEN)
rold = ""
count = 1
rawold = 0
while 1:
	s = ser.read(100).encode("hex")
	s = (s[s.find("19"):] + '')
	if (len(s) <= 3):
		continue
	l = s.split("19")
	if (len(l[0]) <= 3):
		l.pop(0)
	for r in l[0:]:
		r = "19" + r
		if (len(r) != 12):
			print "UNKNOWN: " + r
			continue
		r = r[0:8]
		raw = int(r, 16)

		if (r == rold):
			count += 1
		else:
			print "\tLast message repeated " + str(count) + " times.\n"
			count = 1
			rold = r
			rawold = raw;

		decoded = ""
		if (raw & (1<<16)):
			decoded += "BEEP"
		if (raw & (1<<15)):
			decoded += " Stay"
		if (raw & (1<<14)):
			decoded += " Bat"
		if (raw & (1<<12)):
			decoded += "Ready"
		else:
			decoded += "Not Ready"
		if (raw & (1<<7)):
			decoded += " Instant"
		if (raw & (1<<5)):
			decoded += " Chime"
		if (raw & (1<<4)):
			decoded += " Bypass"
		if (raw & (1<<2)):
			decoded += " Away"

		#still unknown
		unknown = [0, 1, 3, 6, 8, 9, 10, 11, 13, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
		for i in unknown:
			if (raw^rawold)&(1<<i):
				print "Unknown bit changed: " + str(i);


		decoded += "\n" + r + "\t" + str(datetime.datetime.now())
		if (count == 1):
			print decoded
