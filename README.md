
# 🔲 QR Code Generator in Python

A beginner-friendly Python script to generate high-quality QR codes for any URL using the `qrcode` and `Pillow` libraries.

---

## 🚀 Features

- Accepts any URL input from the user
- Automatically generates a QR code
- Saves the QR code as a PNG image with a custom filename
- Uses high error correction and large box size for sharp, scannable output

---

## 🛠️ Technologies Used

- Python 3
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)

---

## 💻 Usage

### ⏬ Install Dependencies

```bash
pip install qrcode pillow
```

### ▶️ Run the Script

```bash
python qr_generator.py
```

### 🧾 Sample Output

```
Enter the url of the website for creating qr code: https://example.com
Your qr code has been made.
Tell me the name of file so that i can save it: my_qr
Your file has been made and has been stored to my_qr.png
```

---

## 📂 Output

The generated `.png` file will be saved in the same directory.

---


## 🎯 Future Ideas

- Add GUI using Tkinter
- Support batch QR generation
- Embed logos into the QR

---

## 🤝 Let's Connect

If you're a recruiter or dev looking for someone who enjoys building practical Python tools—I'm open to connect!

---

## 📜 License

MIT License
