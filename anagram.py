def solve(S,T):
	if(sorted(S)== sorted(T)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		

S = str('saiiiiii: ')
T = str('arunnnnn: ')
solve(S , T)
