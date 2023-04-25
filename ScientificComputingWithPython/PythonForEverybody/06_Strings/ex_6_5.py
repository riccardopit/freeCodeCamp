text = "X-DSPAM-Confidence:    0.8475"
space = text.find(' ')
num = float(text[space:].lstrip())
print(num)