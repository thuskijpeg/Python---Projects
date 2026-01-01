# File Head Display
# Question 2
# Page 380

def main():
    filename = input("Enter name of file: ")

    try:
        infile = open(filename, 'r')
    except FileNotFoundError as err:
        print("File not found")
        print(f"Error: {err}")
    except IOError as err:
        print("An error occurred when opening the file")
        print(f"Error: {err}")
    else:
        try:
           content = infile.readlines()

           num_lines = len(content)

           if num_lines < 5:
               print("The file has less than 5 lines. Displaying")
               for line in content:
                   print(line.strip())
           else:
               for index in range(5):
                   print(content[index].strip())
                
        except IOError as err:
            print("An error occured when reading file contents")
            print(f"Error: {err}")
    finally:
        try:
            infile.close()
        except Exception as err:
            print("An error occured when closing file")
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
