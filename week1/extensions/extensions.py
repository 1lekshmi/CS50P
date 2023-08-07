def main():
    name = input ("File name: ")
    extension(name)

def extension(n):
    n = n.strip().lower().split(sep = ".")
    n = n.pop()
    if n == "gif" or  n == "png" or n == "jpg" or n == "jpeg":
        if n == "jpg" or n == "jpeg":
            print ("image/jpeg")
        else:
            print ("image/" + n)
    elif n == "pdf" or n == "zip":
        print ("application/" + n)
    elif n == "txt":
        print ("text/plain")
    else:
        print ("application/octet-stream")

main()