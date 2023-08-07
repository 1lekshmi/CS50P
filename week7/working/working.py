import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if re.match(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s):
        start, finish = s.split("to")
        s_time = convert_time(start)
        e_time = convert_time(finish)
        return f"{s_time} to {e_time}"
    else:
        raise ValueError("Invalid Arguments")

def convert_time(a):
    time,ref = a.strip().split(" ")

    if ref == "AM":
        if re.match(r"(\d{1,2}):?(\d{2})",time):
            return convert_hour_mins_am(time)
        else:
            return convert_hour_am(time)
    else:
        if re.match(r"(\d{1,2}):?(\d{2})",time):
            return convert_hour_mins_pm(time)
        else:
            return convert_hour_pm(time)

def convert_hour_mins_am(time):
    hour, min = time.split(":")
    if int(min) < 0 or int(min) > 59:
        raise ValueError("Invalid Arguments")
    if hour == "12":
        hour = "0"
    return f"{int(hour):02d}:{int(min):02d}"

def convert_hour_am(time):
    if time == "12":
        time = "0"

    min = "0"
    return f"{int(time):02d}:{int(min):02d}"

def convert_hour_mins_pm(time):
    hour, min = time.split(":")
    if int(min) < 0 or int(min) > 59:
        raise ValueError("Invalid Arguments")
    if hour != "12":
        hour = int(hour) + 12
    return f"{int(hour):02d}:{int(min):02d}"

def convert_hour_pm(time):
    if time != "12":
        time = int(time) + 12

    min = "0"
    return f"{int(time):02d}:{int(min):02d}"

if __name__ == "__main__":
    main()