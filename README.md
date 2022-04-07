<div align="center">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/156916372-d8c1bbdd-5fe9-40d1-a250-5a1d4d454832.png">
</div>

<h1 align="center">Linkedin profile QR code using Python</h1>

### Python tip:
There is a simple way to create an interesting way to introduce your LinkedIn profile through a QR code using Python.

### Prerequisites
`Python 3`
`PyQRCode`

### Source Code
```python3

import pyqrcode
link = pyqrcode.create('Paste your linkedin profile url here.')
link.png('code.png', scale=8)

```

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)
