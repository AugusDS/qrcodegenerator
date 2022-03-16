import qrcode

print("QR Code Generator")
print("================")

print("Enter the text to be encoded:")
text = input()

print("Enter the name of the file to save the QR code:")
filename = input()

print("Generating QR code...")

img = qrcode.make(text)

print("Saving QR code...")

type(img)
img.save(filename + ".png")

print("Done!")