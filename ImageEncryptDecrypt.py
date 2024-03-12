import random
from PIL import Image

def encrypt(image_data, key, operation="swap"):

    width, height = image_data.size
    encrypted_data = image_data.copy()
    pixels = encrypted_data.load()

    if operation == "swap":
        for i in range(width):
            for j in range(height):

                neighbor_i = (i + random.randint(-2, 2)) % width
                neighbor_j = (j + random.randint(-2, 2)) % height

                pixels[i, j], pixels[neighbor_i, neighbor_j] = pixels[neighbor_i, neighbor_j], pixels[i, j]
    elif operation == "xor":

        key_bytes = key.to_bytes(len(image_data.getdata()), byteorder='big')
        for i, pixel in enumerate(image_data.getdata()):
            encrypted_data.putpixel((i % width, i // width), tuple(a ^ b for a, b in zip(pixel, key_bytes[i % len(key_bytes)])))

    return encrypted_data

def decrypt(encrypted_data, key, operation):
    return encrypt(encrypted_data, key, operation)

def main():
    image = Image.open("download.jpeg")

    key = "your_strong_secret_key"

    try:
        encrypted_image = encrypt(image.copy(), key, operation="swap")
        encrypted_image.save("encrypted.jpg")

        decrypted_image = decrypt(encrypted_image, key, operation="swap")
        decrypted_image.save("decrypted.jpg")
        print("Image encryption and decryption completed (for educational purposes only).")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
