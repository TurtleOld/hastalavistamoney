"""
Модуль для обработки сообщения от пользователя бота.

От пользователя будет ожидаться картинка с QR-кодом.
"""
import tempfile

from hasta_la_vista_money.bot.qrcode_decode import decode_qrcode
from hasta_la_vista_money.bot.tasks.tasks import (
    async_handle_receipt_text_qrcode,
)


def handle_receipt_text_qrcode(message, bot, user, account):
    """
    Функция по обработке сообщения от пользователя.

    Пользователь отправляет картинку или фотографию с изображением QR-кода.
    В `qr_code_file_id` записывается ID файла.
    Затем Byte код изображения записывается в переменную `byte_code`, который
    декодируется в функции `decode_qrcode`.
    Далее, полученный текст из QR-кода, записывается в переменную `text_qr_code`
    и обрабатывается классом `ReceiptApiReceiver`.
    Получаем JSON текст из базы налоговой и парсим через класс `ReceiptParser`.

    АРГУМЕНТЫ:

    message (telegram.MESSAGE): Объект сообщения, содержащий текст,
    отправленный пользователем.
    """
    if message.photo:
        qr_code_file_id = bot.get_file(message.photo[-1].file_id)
        byte_code = bot.download_file(
            file_path=qr_code_file_id.file_path,
        )
        # Записываем байт-код картинки во вложенный файл и вносим данные
        # в переменную image_file.
        with tempfile.NamedTemporaryFile(
            mode='w+b',
            suffix='.png',
        ) as image_file:
            image_file.write(byte_code)
            # Из image_file с помощью функции decode_qrcode получает
            # текст из QR-кода.
            text_qr_code = decode_qrcode(image_file.name)
            if not text_qr_code:
                return ''

            chat_id = message.chat.id
            user_id = user.id

            async_handle_receipt_text_qrcode.delay(
                chat_id=chat_id,
                user_id=user_id,
                account=account,
                input_user=text_qr_code,
            )
    else:
        bot.send_message(
            message.chat.id,
            'Надо загружать только фото или картинку с QR-кодом!',
        )
        return ''