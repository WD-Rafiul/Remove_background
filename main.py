from rembg import remove
in_image = input("Enter a picture: ")
out_image = input("Enter new name of that picture: ")
with open(in_image, "rb") as i:
    with open(out_image, "wb") as o:
        input = i.read()
        output = remove(input)
        o.write(output)

print("Thes image backgraund removed 😊😊");
