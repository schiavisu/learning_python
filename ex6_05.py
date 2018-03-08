text = "X-DSPAM-Confidence:    0.8475";
pos=text.find(" ")
num = text[pos:]
num.strip()
num = float(num)
print(num)
