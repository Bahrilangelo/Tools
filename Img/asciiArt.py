import PIL.Image
import PIL.ImageOps

def ascii_art(image_path, width=80):
    image = PIL.Image.open(image_path)
    image = PIL.ImageOps.grayscale(image)
    image = image.resize((width, int(image.size[1] * width / image.size[0])))

    ascii_chars = [" ", ".", ",", ":", ";", "=", "+", "*", "#", "@"]

    ascii_art = ""
    for row in image.getdata():
        ascii_art += "".join([ascii_chars[int(i)] for i in row]) + "\n"

    return ascii_art

if __name__ == "__main__":
    image_path = input("Resim yolunu girin: ")
    ascii_art = ascii_art(image_path)
    print(ascii_art)