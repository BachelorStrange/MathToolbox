dennis=245000
jonathan=35
check = 0

while check!=1:
    r=dennis%jonathan
    if r==0:
        print("ggT", jonathan)
        check=1
    else:
        dennis=jonathan
        jonathan=r

print("Algorithmus beendet.")
