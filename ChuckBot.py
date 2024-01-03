import constants as consts
from telegram.ext import *
from AzureTranslator import *
from ChuckNorrisScraper import *


class ChuckBot:
    def __init__(self):
        self.translator = AzureTranslator(consts.endpoint, consts.subscription_key, consts.region)
        self.scraper = ChuckNorrisScraper(consts.scrape_API_KEY)
        self.cur_language = None

    def process_input(self, input_text):
        if "set language" in input_text:
            input_text_ls = list(input_text.split())
            lang = input_text_ls[len(input_text_ls) - 1]
            if lang in self.translator.lang_dic:
                self.cur_language = lang
                return consts.SET_REQUEST
            else:
                return consts.UNDEFINED_MSG
        elif input_text.isdigit():
            if consts.MIN_JOKE_NUM <= int(input_text) <= consts.MAX_JOKE_NUM:
                return consts.JOKE_NUM
            else:
                return consts.UNDEFINED_MSG
        return consts.UNDEFINED_MSG

    def handle_response(self, input_text):
        msg_type = self.process_input(input_text)
        if msg_type == consts.SET_REQUEST:
            return self.translator.translate_text("No problem", self.cur_language)
        if msg_type == consts.JOKE_NUM:
            joke = self.scraper.jokes_ls[int(input_text) - 1]
            if not self.cur_language:
                return consts.SET_LANG_MSG
            else:
                translated_joke = self.translator.translate_text(joke, self.cur_language)
                return translated_joke
        else:
            return consts.DONT_UNDERSTAND_MSG

    async def start_command(self, update, context):
        await update.message.reply_text(consts.CHOOSE_LANG_MSG)

    async def handle_message(self, update, context):
        text = str(update.message.text).lower()
        response = self.handle_response(text)
        await update.message.reply_text(response)

    def error(self, update, context):
        print(f"Update {update} caused error {context.error}")

    def main(self):
        self.scraper.set_jokes_list()
        print("start bot..")
        # initialize app
        app = Application.builder().token(consts.telegram_api_key).build()
        app.add_handler(CommandHandler('start', self.start_command))
        app.add_handler(MessageHandler(filters.TEXT, self.handle_message))
        app.add_error_handler(self.error)
        # check very 3 sec for updates
        print("start polling..")
        app.run_polling(poll_interval=3)


if __name__ == '__main__':
    bot = ChuckBot()
    bot.main()
