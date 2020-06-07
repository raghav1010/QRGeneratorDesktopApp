import io
import pyqrcode
from base64 import b64encode
import eel

eel.init('web')

@eel.expose
def generate_qr(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR code generation successful.")
    return "data:image/png;base64, " + encoded


eel.start('index.html', size=(600, 600))
