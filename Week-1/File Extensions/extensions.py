extension = input("File name: ").strip().lower().split(".")[-1]

match extension:
    case "png" | "gif":
        print(f"image/{extension}")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case  "zip" | "pdf":
        print(f"application/{extension}")
    case _:
        print("application/octet-stream")
