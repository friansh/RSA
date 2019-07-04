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

print("RSA decryptor")
print("v1.0 beta friansh.2k19")
print("working on " + os.getcwd() + "\n")

private_key = int(input("Masukkan private key\t: "))
n = int(input("Masukkan n\t\t: "))
file_name = str(input("\nMasukkan nama berkas enkripsi:\n>> "))

#private_key = 4281
#n = 5359
#file_name = "D:\\tugaz\\ANGGARANEXMA.xlsx.enc"
#file_name = "D:\\tugaz\\to_enc.txt.enc"

print("\nMasukkan path dan filename untuk berkas dekripsi...")
output_filename = input("   Contoh: C:\\encrypted.txt\n>> ")

print("\nDECRYPTING...")

f = open(file_name, "r")
enc = f.readline()
f.close()

enc = enc.split(", ")
desc = []

printProgressBar(0, len(enc), prefix = 'Progress:', suffix = 'Complete', length = 50)

for i in range(len(enc)):
    enc[i] = int(enc[i])
    desc.append(pow(enc[i], private_key)%n)
    printProgressBar(i + 1, len(enc), prefix = 'Progress:', suffix = 'Complete', length = 50)

text_todesc = ''
for i in range(len(desc)):
    text_todesc = text_todesc + chr(desc[i])

f = open(output_filename, "wb")
text_todesc = bytearray(desc)
f.write(text_todesc)
f.close()

print("\nBerkas dekripsi disimpan di:\n\t" + "D:\\tugaz\\ANGGARANEXMA.desc.xlsx")

input("\nSelesai...\ntekan apapun untuk keluar...")