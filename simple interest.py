def simpleInterest(P, N, R):
    SI = (P * N * R)/100
    return SI
   
P = float(1500 )
 
N = float(5 )
 
R = float(2 )
 
SI = simpleInterest(P, N, R)
 
print("Simple interest : {}".format(SI))
