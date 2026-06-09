def main():
    filename = input("Enter file name: ").strip().lower()
    extension = get_extension(filename)
    media_type = get_mime(extension)
    print(media_type)

def get_extension(file):
    i = file.rfind(".")
    return file[i+1:]

def get_mime(file):
    match file:
        case "gif" | "jpeg" | "png":
            return "image"+"/"+file
        case "jpg":
            return "image/jpeg"
        case "pdf" | "zip":
            return "application"+"/"+file
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"

main()
