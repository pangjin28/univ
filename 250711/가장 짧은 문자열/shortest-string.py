a = input()
b = input()
c = input()


lengths = [len(a), len(b), len(c)]
diff = max(lengths) - min(lengths)
print(diff)