print("TOKOH TOKOH AN")

print("===========PENJUALAN BAJU===========")


print("         ==== MERK DAN UKURAN ====")
print("1. JIN          [M]        @300000")
print("2. JIM          [L]        @350000")
print("3. JING         [XL]       @500000")




x=str(input("ukuran barang :  "))
y=int(input("Harga       :  "))
z=int(input("Jumlah Jual :  "))
v=0
w=0

if (z in range (0,5)):
    v = 0
    print("Tidak ada diskon")
elif (z in range (5,11)):
    v = 5/100
    print("Discount 5%")
elif (z in range ( 11,21)):
    v = 10/100
    print("Discount 10%")
elif (z in range ( 21,31)):
    v = 15/100
    print("Discount 15%")
else:
    v = 20/100
    print("Discount 20%")

w = (y*z)-(y*z*v)

print ("ukuran barang :  ",x)
print ("Harga       :  ",y)
print ("Jumlah Jual :  ",z)
print ("Total Harga :  ",w)
