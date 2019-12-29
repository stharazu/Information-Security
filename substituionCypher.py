englishLetterFrequency = {
    'e' : 12.70,
    't' : 9.06,
    'a' : 8.17,
    'o' : 7.51,
    'i' : 6.97,
    'n' : 6.75,
    's' : 6.33,
    'h' : 6.09,
    'r' : 5.99,
    'd' : 4.25,
    'l' : 4.03,
    'c' : 2.78,
    'u' : 2.76,
    'm' : 2.41,
    'w' : 2.36,
    'f' : 2.23,
    'g' : 2.02,
    'y' : 1.97,
    'p' : 1.93,
    'b' : 1.29,
    'v' : 0.98,
    'k' : 0.77,
    'j' : 0.15,
    'x' : 0.15,
    'q' : 0.10,
    'z' : 0.07,
}
f = open('cipher1.txt','r')       
text = f.read()
print(text)
stored_letter = {}
for char in text:
    if char not in stored_letter:
        stored_letter[char] = 1
    else:
        stored_letter[char] += 1
print(stored_letter)
key=dict()
attempt=text.replace("w", "E")
key.update({"w": "E",})
attempt=attempt.replace("r", "M")
key.update({"r": "M",})
attempt=attempt.replace("d", "I")
key.update({"d": "I",})
attempt=attempt.replace("o", "A")
key.update({"o": "A",})
attempt=attempt.replace("q", "C")
key.update({"q": "C",})
attempt=attempt.replace("b", "F")
key.update({"b": "F",})
attempt=attempt.replace("e", "R")
key.update({"e": "R",})
attempt=attempt.replace("h", "D")
key.update({"h": "D",})
attempt=attempt.replace("x", "O")
key.update({"x": "O",})
attempt=attempt.replace("a", "N")
key.update({"a": "N",})
attempt=attempt.replace("s", "P")
key.update({"s": "P",})
attempt=attempt.replace("c", "L")
key.update({"c": "L",})
attempt=attempt.replace("j", "T")
key.update({"j": "T",})
attempt=attempt.replace("v", "H")
key.update({"v": "H",})
attempt=attempt.replace("n", "Y")
key.update({"n": "Y",})
attempt=attempt.replace("t", "W")
key.update({"t": "W",})
attempt=attempt.replace("f", "S")
key.update({"f": "S",})
attempt=attempt.replace("i", "V")
key.update({"u": "G",})
attempt=attempt.replace("u", "G")
key.update({"u": "G",})
attempt=attempt.replace("l", "J")
key.update({"l": "J",})
attempt=attempt.replace("g", "B")
key.update({"g": "B",})
attempt=attempt.replace("y", "Z")
key.update({"y": "Z",})
attempt=attempt.replace("m", "U")
key.update({"m": "U",})
attempt=attempt.replace("k", "K")
key.update({"k": "K",})
print(attempt)
encryption_key=str(key.values())
print(encryption_key)
fw = open('decrypt.txt','w')
fw.write(attempt)
decryptkey = ['E', 'M', 'I', 'A', 'C', 'F', 'R', 'D', 'O', 'N', 'P', 'L', 'T', 'H', 'Y', 'W', 'S', 'G', 'J', 'B', 'Z', 'U', 'K']
exit()

