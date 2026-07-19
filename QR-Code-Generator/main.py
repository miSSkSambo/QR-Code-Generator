import qrcode

print("=" * 40)
print("        QR Code Generator")
print("=" * 40)

data = input("Enter text or URL: ").strip()

if not data:
    print("No data entered.")
    exit()

filename = input("Enter filename (without .png): ").strip()

if not filename:
    filename = "QRCode"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save(f"{filename}.png")

print(f"\n✅ QR Code saved as {filename}.png")