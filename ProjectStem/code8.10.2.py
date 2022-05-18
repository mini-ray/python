vocab = ["Libraries", "Bandwidth", "Hierarchy", "Software", "Firewall", "Cybersecurity","Phishing", "Logic", "Productivity"]
print(vocab)


for i in range(len(vocab)):
    for j in range(len(vocab)):
        if vocab[i] < vocab[j]:
            vocab[j],vocab[i] = vocab[i],vocab[j]


print(vocab)