def convert(str):
    new_str = str
    new_str = new_str.replace(":)", "🙂")
    new_str = new_str.replace(":(", "🙁")
    return new_str

def main():
    print(convert(input("Input a string:")))

main()