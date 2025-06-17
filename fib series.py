def fib_series(nterms):
    n1,n2=0,1
    count=0
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

nterms=int(input("how many terms?"))
if nterms<=0:
    print("please enter a positive number")
elif nterms==1:
    print("Febonecci Sequence upto",nterms,":")
    fib_series(nterms)
else:
    print("Febonecci Sequence:")
    fib_series(nterms)