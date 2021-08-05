def main():
    #write your code below this line
    file_name = input("Name of the file:")
    word = input("Search for:")

    try:
        with open(file_name, 'r') as f:
            words = f.read().splitlines()

        if word in words:
            print("Found!")
        else:
            print("Not found.")
    except:
        print("Reading the file {} failed.".format(file_name))


if __name__ == '__main__':
    main()
