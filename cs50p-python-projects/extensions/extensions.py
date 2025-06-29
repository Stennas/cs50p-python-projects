user_input = input("File name: ").lower()

if "gif" in user_input:
    print("image/gif")
elif "jpg" in user_input or "jpeg" in user_input:
    print("image/jpeg" )
elif "png" in user_input:
    print("image/png")
elif "pdf" in user_input:
    print("application/pdf")
elif "text" in user_input:
    print("application/txt")
elif "zip" in user_input:
    print("application/zip")
else:
    print("application/octet-stream")
