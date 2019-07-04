def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a

print("Pembuatan kombinasi private key dan public key\nuntuk keperluan enkripsi RSA\n")

p = int(input("Masukkan nilai p: "))
for i in range(p):
    if p%(i+1)==0 and i+1!=p and i+1!=1:
        print("ERROR, P ISNT PRIME NUMBER", i+1)
        exit()

q = int(input("Masukkan nilai q: "))
for i in range(q):
    if q%(i+1)==0 and i+1!=q and i+1!=1:
        print("ERROR, Q ISNT PRIME NUMBER", i+1)
        exit()

n = p*q
o = (p-1)*(q-1)

print("\nNilai nilai penting:\np\t\t=",p,"\nq\t\t=",q,"\nn\t\t=",n,"\n(p-1)(q-1)\t=",o)

e = []
for i in range(2,o):
    if gcd(i,o) == 1:
        e.append(i)

print("\nKombinasi e,d akan ada sekitar:",len(e),"\ntekan apapun untuk melanjutkan...")
input()


print("\n\nKombinasi nilai e dan d yang mungkin: ")

d = []
for i in range(len(e)):
    r = 1
    while (e[i]*r)%o != 1:
        r = r+1
    d.append(r)
    print(str(i+1) + ".\t(" + str(e[i]) + "," + str(d[i]) + ")")

z = input("Masukkan nomor kombinasi yang akan digunakan (1-" + str(len(e)) + "): ")

x = e[int(z)-1]
y = d[int(z)-1]

print("\nPublic key anda\t\t: ",x,"\nPrivate key anda\t: ",y,"\nNilai n\t\t\t: ",n)

input()