def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0:2].isalpha() == False:
        return False
    elif s[-1].isalpha() and s[2:-1].isalnum():
        return False
    elif s.isalnum() == False:
        return False
    nums = []
    for chars in s:
        if chars.isdigit():
            nums.append(chars)
            if nums[0] == "0" or chars.index(nums[len(nums)-1]) != chars.index(chars[len(chars)-1]):
                return False
    else:
        return True


if __name__ == "__main__":
    main()