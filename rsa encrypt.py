def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

import os
print("RSA encryptor")
print("v1.0 beta friansh.2k19")
print("working on " + os.getcwd() + "\n")

public_key = int(input("Masukkan public key\t: "))
n = int(input("Masukkan n\t\t: "))
file_name = input("\nMasukkan nama berkas yang akan dienkripsi:\n>> ")

print("\nENCRYPTING...")

#public_key = 2921
#n = 5359
#file_name = "D:\\tugaz\\ANGGARANEXMA.xlsx"
#file_name = "D:\\tugaz\\to_enc.txt"

f = open(file_name, "rb")
text_toenc = f.read()

#text_toenc = ''
#for line in f:
#    text_toenc = text_toenc + str(line)
#print("\n\n",text_toenc,"\n\n")

toenc = []
enc = []

printProgressBar(0, len(text_toenc), prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(len(text_toenc)):
    toenc.append(text_toenc[i])
    enc.append(pow(toenc[i], public_key)%n)
    printProgressBar(i + 1, len(text_toenc), prefix = 'Progress:', suffix = 'Complete', length = 50)

#print("\n\n",toenc,"\n\n")
##print("Masukkan path dan filename untuk berkas enkripsi...")
##output_filename = input("   Contoh: C:\\encrypted.txt\n>> ")

print("\nBerkas enkripsi disimpan di:\n\t" + file_name + ".enc")

enc = str(enc)

f = open(file_name + ".enc", "w")
f.write(enc[1:len(enc)-1])
f.close()

input("\ntekan apapun untuk keluar...")