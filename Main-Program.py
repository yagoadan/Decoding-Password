
#IMPORTING LIBRARIES
import serial
import time
import re

#Telling user to wait
print('Wait for the software to find your student id and give you a password')
time.sleep(2)

#Serial Set Up
arduino = serial.Serial('/dev/ttyACM1', 9600, timeout=2)
time.sleep(2)

#Sending data to the rasberry
arduino.write('M00717681')
print('Data collected. Please wait...')


hidp = arduino.readline()       #This is the password coded, I need to decoded
time.sleep(2)
print('This is your coded password')
print(hidp)                      #Showing the user the coded password and closing the port
arduino.close()

#Decoding using Base64
hidp = hidp.encode('base64', 'strict')
pw = 'This is your password: ' + hidp.decode('base64', 'strict')
password = int(filter(str.isdigit, pw))

part = pw[42:]

s = list(part)
#Converting the coded password from ASCII to decimal
pr = ord(s[8])
pr1 = ord(s[9])
pr2 = ord(s[10])
pr3 = ord(s[11])
pr4 = ord(s[12])
pr5 = ord(s[13])
pr6 = ord(s[14])
pr7 = ord(s[15])
pr8 = ord(s[16])

print ('Password in decimal')
print pr, pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8
time.sleep(2)


letter = pr + password
letter1 = pr1 + password
letter2= pr2 + password
letter3= pr3 + password
letter4= pr4 + password
letter5= pr5 + password
letter6= pr6 + password
letter7= pr7 + password
letter8 = pr8 + password


#Storing the decimal
r = chr(letter)
r1 = chr(letter1)
r2 = chr(letter2)
r3 = chr(letter3)
r4 = chr(letter4)
r5 = chr(letter5)
r6 = chr(letter6)
r7 = chr(letter7)
r8 = chr(letter8)

finalp = (r + r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8)
print "Your password is: "
print(finalp)
