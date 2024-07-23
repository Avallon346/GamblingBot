import telebot




Bot_From_Deploy = telebot.TeleBot( "7492196207:AAHO80rrFy1JPgB01V1M0D6OiBvRC5c6wfk" )

from telebot import types

@Bot_From_Deploy.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name} </b>, Привет! Хочешь поучаствовать в розыгрыше?"
    markup = types.ReplyKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
    markup.add(button_yes)
    Bot_From_Deploy.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@Bot_From_Deploy.message_handler(func=lambda call:True)
def respond(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = "Большое спасибо за ваше участие в нашем розыгрыше!"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Посмотреть другие розыгрыши:", url= '@pitersmoke_vilkitsky' )) #Не забудь добавить ссылку на группу!
            button_continie = types.InlineKeyboardButton(text = "Продолжить", callback_data='continie')
            markup.add(button_continie)
            Bot_From_Deploy.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            Bot_From_Deploy.answer_callback_query(function_call.id)
Bot_From_Deploy.infinity_polling()