bits = int(input("Enter the number of bits: "))
kilobits = bits / 1000
megabits = bits / (1000 * 1000)
gigabits = bits / (1000 * 1000 * 1000)
print("{} bits is equal to:".format(bits))
print("{:.2f} kilobits".format(kilobits))
print("{:.2f} megabits".format(megabits))
print("{:.2f} gigabits".format(gigabits))
