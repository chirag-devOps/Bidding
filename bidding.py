# program to bid for a product
import random

print("Market opens !")
print("Enter a bid between 50-100 to purchase a product X")
base = random.randint(50,100)
# print(base)

print("Enter your bid")
bid=int(input())

if bid > base:
    print("You are a qualified bidder.")
else:
    print("Sorry ! Your bid {} was very less. The base was {}".format(bid,base))

print("Market closed")
