def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    time = time.split(sep = ":")
    minutes = time.pop()
    minutes = int(minutes) / 60
    time = int(time[0]) + minutes
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print ("dinner time")


if __name__ == "__main__":
    main()