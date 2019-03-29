otazky = ["Kdo?", "Kdy?"]

val=[]
key=[]

for a in range(2):
    for i in otazky:
        odpoved =  input(i)
        val.append(odpoved)
        key.append(i)

ntice=[]
for key, val in zip(key, val):
    ntice.append('{} = {}'.format(key, val)) #vytvoří n-tice

print(ntice)

ntice_podlis = [v.split('=',1) for v in ntice if '=' in v]    #rozeká seznam na podsenamy
print(ntice_podlis)

slovník = dict(ntice_podlis)
print(slovník)
