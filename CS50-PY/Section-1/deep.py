answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

answer = answer.lower().replace("-", " ").strip()

if answer == "forty two" or answer == "42":
    print("Yes")
else:
    print("No")