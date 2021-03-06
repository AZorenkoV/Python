morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--.."
}

def encode_morze_sym(symbol):
    symbolEnc = ""
    for x in morse_code.get(symbol):
        if x == ".":
            symbolEnc += "^_"
        elif x == "-":
            symbolEnc += "^^^_"
    return symbolEnc[:-1]

def encode_morze(text):
    text = text.upper()
    new_text = ""
    for x in text:
        if x in morse_code.keys():
            new_text += encode_morze_sym(x) + "___"
        elif x == " ":
            new_text = new_text[:-3]
            new_text += "_______"
    return new_text[:-3]



#print encode_morze_sym("S")
#print encode_morze_sym("O")

print encode_morze("SOS")
print encode_morze('Prometheus')
print encode_morze('Morze')
print encode_morze('code')
print encode_morze('Morze code')
#print encode_morze("boo 123 boo")
#print encode_morze("123")
