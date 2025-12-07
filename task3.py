import matplotlib.pyplot as plt
filename = "text.txt"
vowels = "aeiou"
with open(filename, 'r') as file:
    text = file.read()
vowel_count= {}
for v in vowels:
    vowel_count[v]=0
for c in text:
    if c in vowel_count:
        vowel_count[c] = vowel_count[c] + 1
letters = []
counts = []
for v in vowel_count:
    letters.append(v)
    counts.append(vowel_count[v])
plt.figure(figsize=(8, 6))
plt.bar(letters, counts, color='pink')
plt.xlabel("Vowels")
plt.ylabel("Frequency")
plt.title("histogram")
plt.savefig("vowel_histogram.png")
plt.show()