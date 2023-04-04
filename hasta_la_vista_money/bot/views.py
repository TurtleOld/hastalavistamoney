import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .config_bot import bot_admin
from .config_bot import bot_type
from .log_config import logger
from .receipt_parser_json import handle_receipt_json
from .receipt_parser_text import handle_receipt_text


@csrf_exempt
def webhooks(request):
    if request.method == 'POST':
        try:
            json_request = request.body.decode('utf8')
            json_data = json.loads(json_request)

            update = bot_type.Update.de_json(json_data)
            bot_admin.process_new_updates([update])
            if update.message and update.message.text:
                handle_receipt_text(update.message.text)
                handle_receipt_json(update.message.text)
        except Exception as error:
            logger.error(error)
        return HttpResponse('')
