import matplotlib.pyplot as plt

# function to find primal numbers
def isPrime(num):
    isP = True
    for i in range(2, int(num/2)+1):
        if (num % i == 0): isP = False
    return isP


# creating the array with primal numbers from 2 to 256
limit = pow(2, 8)
primes = []
for i in range(2, limit+1):
    primFreq = dict(number=i, freq=0)
    if isPrime(i):
        primes.append(primFreq)

# calculatig frequences of primal numbers in range(2,2^16)
max = pow(2, 16)
def frequence(prime):
    for i in range(2, max+1):
        if i % prime["number"] == 0:
            prime["freq"] += 1

for i in primes:
    frequence(i)

for i in primes:
    i["freq"]/=max

for i in primes:
    print(i)

#calculating the average frequence of a prime number
sum = 0
for i in primes:
    sum += i["freq"]

print(str(sum/len(primes)*100)+"%")

#creating the graph of primes frequences
x = []
y = []

for i in primes:
    x.append(i["number"])
for i in primes:
    y.append(i["freq"])

plt.bar(x, y)
plt.xlabel("number")
plt.ylabel("frequence")
plt.show()




