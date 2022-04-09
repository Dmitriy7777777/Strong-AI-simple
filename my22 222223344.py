txt1="звезда не хотела падать"
ltxt1=len(txt1)
chit="звезда"
lchit=len(chit)
slovo=txt1.split()
nslovo=len(slovo)
ttt=[0]*nslovo
l=0
while l<lchit:
    h=0
    while h<nslovo:
        m=0
        nbyk=len(slovo[h])
        while m<nbyk:
            if slovo[h][m]==chit[l]:
                ttt[h]=4+ttt[h]
                break
            else:
                m=m+1
        for g in range(60):
            if ttt[h]>0:
                if h+g<nslovo:
                    ttt[h+g]=ttt[h+g]+ttt[h]/(g*10+100)
                if h-g>=0:
                    ttt[h-g]=ttt[h-g]+ttt[h]/(g*10+100)
        h=h+1
    l=l+1
print(ttt,slovo,chit,'\n', end='')
   



