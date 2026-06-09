import re

def main():
    print(parse(input("HTML: ")))

def parse(html):
    long_url = re.search(r'^<iframe.+src=(".+youtube.+")(?: title.+)?></iframe>$', html)

    if long_url:

        short_url = re.search(r'^"https?://(?:www\.)?(youtube)\.com/embed(.+)"$', long_url.group(1))

        if short_url:
            webname = re.sub(r"^(.{5})(.*)$", r"\1.\2", short_url.group(1))

            return f"https://{webname}{short_url.group(2)}"


if __name__ == "__main__":
    main()
