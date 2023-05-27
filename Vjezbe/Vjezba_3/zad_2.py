def iteracije(N):
    
    zbroj=5
    
    for i in range(N):
        zbroj += 1/3
        
    for i in range(N):
        zbroj -= 1/3
    
    print ("{} iteracija daje rješenje: {}".format(N, zbroj))  

iteracije(200)
iteracije(2000)
iteracije(20000)


#a=int(input("Unesi broj iteracija: "))

#for i in range(a):

    #iteracije(i+1)

# kako smo dodavali i oduzimali broj 1/3 koji se ne može zapisati u binarnom formatu (1/2^n) za različiti broj iteracija smo dobili 
# različite aproksimacije broja 5, ali ne i 5.0
# testom sam došao do broja N od 176 iteracija pri kojem još dobivamo rješenje 5.0 što znači da nakon toga se akumulira dovoljno
# malih pogrešaka da aproksimirano rješenje više ne iznosi 5.0