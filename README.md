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
### Output
<p align="center">
  <a href="Output/code.png"><img height="600" src="https://user-images.githubusercontent.com/85709371/162178619-7a4310a4-e23d-4634-baf0-c242603d6487.png" alt="output"></a>
</p>

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)
