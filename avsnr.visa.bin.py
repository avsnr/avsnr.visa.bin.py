# avsnr.visa.bin.py
( ™ ) extraction tool, VisaVisa Private and Spam. ( ™ ) works without any error .➖➖➖➖. ( ™ ) Visa extraction tool - Bin. ( ™ ) to collect information. ( ™ ) works without any error. ( ™ ) The tool is not encrypted. .➖➖➖➖ ( ™ ) - Pip ™ random ™ Requests ™ system ™ pyfiglet ™ Web browser ™ operating system  ™ Channel: @avsnr
import random
import requests
import os
import pyfiglet
import webbrowser
Ba = 0
A = '\033[2;34m'#ازرق
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ا
G = '0123456789'
print(f"""{B}' .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................ 
""")
bw = input("""
\033[1;31m [\033[2;32m 1 \033[1;31m] \033[2;36m Do You Want To Hack Bin Visa
\033[1;31m [\033[2;32m 2 \033[1;31m] \033[2;36m Bin Info
\033[1;31m [\033[2;32m 3 \033[1;31m] \033[2;36m Want To Make Visas 
\033[2;31m----------------------------------------------
\033[1;31m [\033[2;32m ≈ \033[1;31m] \x1b[1;33m  Choose : \x1b[2;32m""")
print(Z+'-'*58)
if bw == '1':
	os.system('clear')
	print(f"""{B}' .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................ 
 """)
	token = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER TOKEN BOT"+Z+" ==>"+B)
	ID = input(Z+"["+F+"⌯"+Z+"]"+X+ "ENTER ID "+Z+" ==>"+B)
	
	while True:
		ml = '3'+str(''.join((random.choice(G) for i in range(5))))
		xc = '4'+str(''.join((random.choice(G) for i in range(5))))
		za = [ml,xc]
		v = (random.choice(za))
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		response = reg.text
		if '"country"' in response:
		  	f = requests.get(api)
		  	res = f.json()
		  	z = res['country']['emoji']
		  	m = res['scheme']
		  	k = res['country']['name']
		  	g = res['country']['currency']
		  	u = v
		  	p = k +' '+z
		  	tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=™
 HI NEW BIN FROM AVSNR
*---------------------------------------*
- ʙɪɴ ⇨  {u}
- country ⇨  {p}
- ᴄᴀʀᴅ ᴛʏᴘᴇ ⇨ {m}
- currency ⇨ {g}
*---------------------------------------*
- channel ⇨ @avsnr 👾💀''')
		  	i = requests.post(tlg)
		  	print(F+'Available =>  '+v)
		  	print(k+' '+z)
		  	print(g)
		  	print(m)
		else:
			print(Z+'Not Available =>  '+v)
if bw == '2':
	tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER TOKEN BOT"+Z+" ==>"+B)
	id = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER ID"+Z+" ==>"+B)
	while True:
		v = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER YUOR BIN"+Z+" ==>"+B)
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		res = reg.json()
		z = res['country']['emoji']
		m = res['scheme']
		k = res['country']['name']
		g = res['country']['currency']
		print(B+k+z)
		print(B+m)
		print(B+g)
		u = v
		p = k +' '+z
		print('Done Send Your Bot ! ')
		print(Z+'='*58)
		tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=®
 HI NEW BIN FROM AVSNR
*---------------------------------------*
- ʙɪɴ ⇨  {u}
- country ⇨  {p}
- ᴄᴀʀᴅ ᴛʏᴘᴇ ⇨ {m}
- currency ⇨ {g}
*---------------------------------------*
- channel ⇨ @avsnr 👾💀''')
		i = requests.post(tlg)
if bw == '3':
	os.system('clear')
	print(f"""{B}' .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................ 
      """)
	tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER TOKEN BOT"+Z+" ==>"+B)
	id = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER ID"+Z+" ==>"+B)
	os.system(f'rm -rf basha.txt')
	B = input("""
\033[1;31m [ \033[2;32m 1 \033[1;31m ] \033[2;36m Visa
\033[1;31m [ \033[2;32m 2 \033[1;31m ] \033[2;36m From Visa Bin
\033[2;31m----------------------------------------------
\033[1;31m [ \033[2;32m + \033[1;31m ] \x1b[1;33m  Choose : \x1b[2;32m""")	
def bae():
	print(A+'='*58)
	if B == '2':
		ba = input(Z+"["+F+"⌯"+Z+"]"+X+ " Your Bin 5 / 6"+Z+" ==>"+B)
		if ba == '6':
			bi = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER YUOR BIN"+Z+" ==>"+B)
		if ba == '5':
			bi = input(Z+"["+F+"⌯"+Z+"]"+X+ " ENTER YUOR BIN"+Z+" ==>"+B)
	G = '0123456789'
	Z = ['2023','2024','2025','2026','2027']
	Ba = 0
	while Ba < 20:
	   		if B == '1':
    				v = str(''.join((random.choice(G) for i in range(16))))
    				b = str(''.join((random.choice(TY) for i in range(2))))
    				a = str(''.join((random.choice(G) for i in range(3))))
    				p = str(random.choice(Z))
    				h = v+'|'+'0'+b+'|'+p+'|'+a
    				print(X+'Visa ==> '+'\033[2;36m'+h)
    				g = open('basha.txt', 'a')
    				g.write(h+ '\n')
    				tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
    				i = requests.post(tlg)
    				Ba = Ba + 1
	   		if B == '2':
	   			if ba == '5':
    					v = str(''.join((random.choice(G) for i in range(11))))
    					b = str(''.join((random.choice(TY) for i in range(2))))
    					a = str(''.join((random.choice(G) for i in range(3))))
    					p = str(random.choice(Z))
    					h = bi+v+'|'+'0'+b+'|'+p+'|'+a
    					print(X+'Visa ==> '+'\033[2;36m'+h)
    					g = open('basha.txt', 'a')
    					g.write(h+ '\n')
    					Ba = Ba + 1
    					tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
    					i = requests.post(tlg)
	   			if ba == '6':
	   				v = str(''.join((random.choice(G) for i in range(10))))
	   				b = str(''.join((random.choice(TY) for i in range(1))))
	   				a = str(''.join((random.choice(G) for i in range(3))))
	   				p = str(random.choice(Z))
	   				h = bi+v+'|'+'0'+b+'|'+p+'|'+a
	   				print(X+'VISA ==> '+'\033[2;36m'+h)
	   				g = open('basha.txt', 'a')
	   				g.write(h+ '\n')
	   				Ba = Ba + 1
	   				tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
	   				i = requests.post(tlg)
	   		

bae()  				
