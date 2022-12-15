from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


file_enc = open("C:/Users/User/Downloads/file_txt.txt", "r")
print('====================================')
print('Enkripsi File_Sistem Keamanan Data')
print('====================================')

read = file_enc.readlines() # digunakan untuk membaca isi file
print (read[0])

# digunakan untuk membaca string kalimat
teks = str(read[0])
# digunakan untuk mengkorversi dari teks ke kode binary
teks_binary = teks.encode() 
# digunakan untuk menampilkan output kode binary
print(teks_binary)

# kunci RSA generate
keyPair = RSA.generate(3072)

# digunakan untuk menampilkan publickey
pubKey = keyPair.publickey() 
pubKeyPEM = pubKey.exportKey()
key2 = pubKeyPEM.decode('ascii')
# digunakan untuk menampilkan output(pubKeyPEM.decode('ascii'))


privKeyPEM = keyPair.exportKey()

# PROSES ENKRIPSI
encryptor = PKCS1_OAEP.new(pubKey)
# digunakan untuk mengkonversi ke kode binary
encrypted = encryptor.encrypt(teks_binary)
print("Encrypted:", binascii.hexlify(encrypted))
cipher_ascii = binascii.hexlify(encrypted)
cipherteks = cipher_ascii.decode()

# PROSES DEKRIPSI
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
plainteks = decrypted.decode()
# digunakan untuk menampilkan output plainteks deksripsi
print('Decrypted:', plainteks)

file_dec = open("pkey.txt", "a")
file_dec.write(key2)
