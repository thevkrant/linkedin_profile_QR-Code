import pyqrcode
link = pyqrcode.create('Paste your linkedin profile url here.')
link.png('code.png', scale=8)
