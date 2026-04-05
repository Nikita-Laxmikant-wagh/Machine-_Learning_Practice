import matplotlib.pyplot as plt

spam_words = [20, 32, 18, 30, 46, 30, 50]
real_words = [50, 39, 28, 48, 70, 65, 58]

plt.hist(spam_words, bins=5, alpha=0.5, label="Spam Email")
plt.hist(real_words, bins=5, alpha=0.5, label="Real Email")

plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.title("Spam vs Real Email Histogram")
plt.legend()
plt.show()
