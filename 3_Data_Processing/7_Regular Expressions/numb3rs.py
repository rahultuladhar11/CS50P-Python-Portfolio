import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if matches:
        octets = matches.groups()
        for octet in octets:
            # Check for out-of-range
            if not 0 <= int(octet) <= 255:
                return False
            # Check for leading 0s
            if len(octet) > 1 and octet.startswith("0"):
                return False
        # If all octets pass
        return True
    else:
        return False


if __name__== "__main__":
    main()
