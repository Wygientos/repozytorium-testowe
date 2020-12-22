n=int(input("Podaj liczbę z końca zakresu: "))

for a in range(0,n+1):
	if(a%2==0 and a%3!=0):
		print(a)