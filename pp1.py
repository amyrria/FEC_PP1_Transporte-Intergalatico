import re
btc = 0.00
ltc = 0.00
eth = 0.00
entrada = input()
while entrada != "END":
	autenticacao = entrada.split(",")
	if (len(autenticacao)<8):
		print("False")
		entrada = input()
		break
	tam = len(autenticacao[6])
	count_dig = 0
	count_caract = 0
	count_letMai = 0
	count_letMin = 0

	for i in range(tam):
		if(re.match(r'^(\d)',autenticacao[6][i])!=None):
			count_dig = count_dig + 1
		if(re.match(r'^([\$\@\%\(\*])',autenticacao[6][i])!=None):
			count_caract = count_caract + 1
		if(re.match(r'^([A-Z])',autenticacao[6][i])!=None):
			count_letMai = count_letMai + 1
		if(re.match(r'^([a-z])',autenticacao[6][i])!=None):
			count_letMin = count_letMin + 1

	#print ("tam= ",autenticacao[6][0])
	#print(autenticacao)
	if(re.match(r'[\s]*(via lactea|andromeda|triangulo|redemoinho|sombreiro|girassol|grande nuvem de magalhaes|pequena nuvem de magalhaes|compasso|ana de fenix|messier 87|messier 32|leo i|messier 110)[\s]*',autenticacao[0].lower())!=None):
		if((re.match(r'[\s]*(via lactea|andromeda|triangulo|redemoinho|sombreiro|girassol|grande nuvem de magalhaes|pequena nuvem de magalhaes|compasso|ana de fenix|messier 87|messier 32|leo i|messier 110)[\s]*',autenticacao[1].lower())!=None) and (autenticacao[0].lower()!=autenticacao[1].lower())):
			id_pass = autenticacao[2].split("-")
			if(re.match(r'[\s]*((000)|(078)|(666)|(219)|(9[0-9][0-9])|(111)|(222)|(333)|(444)|(555)|(777)|(888))', id_pass[0])==None):

				if(re.match(r'((00)|(85)|(09)|(11)|(22)|(33)|(44)|(55)|(66)|(77)|(88)|(99))',id_pass[1])==None):

					if(re.match(r'((0000)|(1120)|(9999)|(1111)|(2222)|(3333)|(4444)|(5555)|(6666)|(7777)|(8888))[\s]*',id_pass[2])==None):

						if(re.match(r'[\s]*((0?[1-9]|[12]\d|3[01])[\/](0?[13578]|10|12)[\/](([0-9][0-9]{3}) (([01][0-9]|[2][0-4]):([0-5][0-9]))))[\s]*',autenticacao[3])!=None):

							if(re.match(r'[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*',autenticacao[4].lower())!=None):
								if(re.match(r'[\s]*(BTC) ((0.[0-9]{3})[\s]*|(1.000))[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									btc = btc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(LTC) ([0-9]{2}\.[0-9]{2})[\s]*',autenticacao[5])!=None):

									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									ltc = ltc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(ETH) ([0-9]{3})[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									eth = eth + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")	
								else:
									print("False")
							else:
								print("False")
						elif(re.match(r'[\s]*((0?[1-9]|[12]\d|30)[\/](0?[469]|11)[\/](([0-9][0-9]{3}) (([01][0-9]|[2][0-4]):([0-5][0-9]))))[\s]*',autenticacao[3])!=None):

							if(re.match(r'[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*',autenticacao[4].lower())!=None):
								if(re.match(r'[\s]*(BTC) ((0.[0-9]{3})[\s]*|(1.000))[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									btc = btc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(LTC) ([0-9]{2}\.[0-9]{2})[\s]*',autenticacao[5])!=None):

									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									ltc = ltc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(ETH) ([0-9]{3})[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									eth = eth + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")	
								else:
									print("False")
							else:
								print("False")
						elif(re.match(r'[\s]*((0?[1-9]|1\d|2[0-8])[\/]0?2[\/](([0-9][0-9]{3}) (([01][0-9]|[2][0-4]):([0-5][0-9]))))[\s]*',autenticacao[3])!=None):

							if(re.match(r'[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*',autenticacao[4].lower())!=None):
								if(re.match(r'[\s]*(BTC) ((0.[0-9]{3})[\s]*|(1.000))[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									btc = btc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'[\s]*^[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(LTC) ([0-9]{2}\.[0-9]{2})[\s]*',autenticacao[5])!=None):

									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									ltc = ltc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(ETH) ([0-9]{3})[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									eth = eth + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")	
								else:
									print("False")
							else:
								print("False")
						elif(re.match(r'[\s]*((29[\/]0?2[\/](([0-9][0-9]{3})?(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00)|00)) (([01][0-9]|[2][0-4]):([0-5][0-9])))[\s]*',autenticacao[3])!=None):
							if(re.match(r'[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*|[s]*nebula class a[s]*|[s]*nebula class b[s]*|[s]*intrepid class[s]*|[s]*niagaria class[s]*|[s]*wells class[s]*|[s]*holoship[s]*|[s]*raven[s]*|[s]*peregrine[s]*|[s]*danube class[s]*',autenticacao[4].lower())!=None):
								if(re.match(r'[\s]*(BTC) ((0.[0-9]{3})[\s]*|(1.000))[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									btc = btc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(LTC) ([0-9]{2}\.[0-9]{2})[\s]*',autenticacao[5])!=None):

									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									ltc = ltc + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")
								elif(re.match(r'[\s]*(ETH) ([0-9]{3})[\s]*',autenticacao[5])!=None):
									moeda = autenticacao[5].split(" ")
									flt_moeda = float(moeda[1])
									eth = eth + flt_moeda
									if((count_dig==4) and (count_caract==2) and (count_letMai==3) and (count_letMin==3) and tam ==12):
										if(re.match(r'^[\s]*[a-f0-9]{32}[\s]*$',autenticacao[7])!=None):
											print("True")
										else:
											print("False")
									else:
										print("False")	
								else:
									print("False")
							else:
								print("False")
						else:
							print("False")

					else:
						print("False")
				else:
					print("False")
			else:
				print("False")
		else:
			print("False")
	else:
		print("False")
	entrada = input()
		
print("BTC %.2f" % btc)
print("ETH %.2f" % eth)
print("LTC %.2f" % ltc)
