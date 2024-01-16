import os
import qrcode
from pyrogram import Client, filters
from pyrogram.types import Message

async def create():
    mes = await client.listen(message.from_user.id)
    photo_path = await message.download()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(photo_path)
    qr.make(fit=True)
    
    # Save the QR code image
    qr_image_path = os.path.join(photo_path, f'qr_{message.id}.png')
    qr.make_image(fill_color="black", back_color="white").save(qr_image_path)

    # Send the generated QR code
    await client.send_photo(message.chat.id, qr_image_path)


await create()
