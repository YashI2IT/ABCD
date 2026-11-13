# Huffman Encoding (Greedy)

mode = input("1) Enter a text   2) Enter symbols with frequencies: ")

freq = {}
text = None

if mode == "1":
    text = input("Enter text: ")
    for c in text:
        freq[c] = freq.get(c, 0) + 1
else:
    for _ in range(int(input("Number of symbols: "))):
        c = input("Symbol: ")
        freq[c] = int(input("Frequency of %s: " % c))

heap = [[f, i, c] for i, (c, f) in enumerate(freq.items())]
codes, k = {}, len(heap)

while len(heap) > 1:
    heap.sort()
    f1, _, a = heap.pop(0)
    f2, _, b = heap.pop(0)
    heap.append([f1 + f2, k, (a, b)])
    k += 1

def walk(node, code):
    if isinstance(node, tuple):
        walk(node[0], code + "0")
        walk(node[1], code + "1")
    else:
        codes[node] = code or "0"

walk(heap[0][2], "")

print("\nSymbol  Freq  Code")
for c in codes:
    print("%-7r %-5d %s" % (c, freq[c], codes[c]))

h = sum(freq[c] * len(codes[c]) for c in freq)
f = sum(freq.values()) * max(1, (len(freq)-1).bit_length())

print("\nHuffman bits =", h, "| Fixed-length bits =", f)

if text is not None:
    encoded = "".join(codes[c] for c in text)
    decoded = ""
    temp = ""

    for b in encoded:
        temp += b
        if temp in codes.values():
            decoded += list(codes.keys())[list(codes.values()).index(temp)]
            temp = ""

    print("Encoded :", encoded)
    print("Decoded :", decoded, "| matches original:", decoded == text)