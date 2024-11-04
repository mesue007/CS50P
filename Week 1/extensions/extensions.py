name = input("File name: ").lower()

if name.find(".jpg") >= 0:
    print("image/jpeg")
elif name.find(".jpeg") >= 0:
    print("image/jpeg")
elif name.find(".gif") >= 0:
    print("image/gif")
elif name.find(".png") >= 0:
    print("image/png")
elif name.find(".pdf") >= 0:
    print("application/pdf")
elif name.find(".txt") >= 0:
    print("text/plain")
elif name.find(".zip") >= 0:
    print("application/zip")
else:
    print("application/octet-stream")
