print(5.0 - 4.935) 

# dobiveni rezultat iznosi: 0.06500000000000039 umjesto očekivanih 0.065
# dolazi do pogrešaka jer se brojevi pohranjuju u binarnom formatu, a kako mnogi decimalni brojevi nemaju jednak zapis u binarnom formatu 
# dolazi do malih zaokruživanja ili pogrešaka u preciznosti prilikom računanja
# ti se brojevi prikazuju pomoću 1/2^n, a kako ih se većina ne može tako prikazati moraju se aproksimirati na najbliži 1/2^n
# u ovom slučaju broj 0.065 nema točan binarni zapis

print(0.1 + 0.2 + 0.3) 

# dobiveni rezultat iznosi: 0.6000000000000001 umjesto očekivanih 0.6
# razlog je, ukratko, isti kao i u prvom primjeru
# u ovom slučaju brojevi 0.1, 0.2 i 0.3 nemaju točan binarni prikaz i moraju se aproksimirati. nakon zbrajanje te se male pogreške akumuliraju 
# rezultirajući greškom u rezultatu
# ni samo rješenje 0.6 nije moguće točno prikazati pomoću 1/2^n