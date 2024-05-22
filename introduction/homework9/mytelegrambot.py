# !pip install pyTelegramBotAPI
# !pip install khayyam
# !pip install gtts
# !pip install qrcode
import random
import io
import telebot
import khayyam
import qrcode
from gtts import gTTS

from telebot import types

my_keyboard= types.ReplyKeyboardMarkup (row_width = 3)
key1= types.KeyboardButton("Start")
key2= types.KeyboardButton("Guess number game")
key3= types.KeyboardButton("Max")
key4= types.KeyboardButton("Argmax")
key5= types.KeyboardButton("QR_Code")
key6= types.KeyboardButton("Age")
key7= types.KeyboardButton("Voice")
key8= types.KeyboardButton("Help")

my_keyboard.add (key1,key2,key3,key4,key5,key6,key7,key8)

user_states = {}


bot =  telebot.TeleBot ("7090310909:AAGNkDIzxNlCMPb_ubURrZRXDHI50XXDhQc",parse_mode=None)


@bot.message_handler (commands=['start'])
def send_welcome (message) :
  text_message = "Hello," + message.from_user.first_name + ". 😍\n ❣WELCOME TO MY BOT❣" +"\nPlease select your request from the menu" 
  bot.reply_to (message, text_message,reply_markup=my_keyboard)

@bot.message_handler(func=lambda message: message.text == "Start")
def start_message(message):
  bot.send_message(message.chat.id, f"Hi {message.from_user.first_name}😎, Please select your request from the menu", reply_markup=my_keyboard)



@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == "Help")
def send_help(message):
  help_text = "🧐In my bot, the following commands are available: \n"
  help_text += "/start : Welcome.\n"
  help_text += "/game : Guess number game.\n"
  help_text += "/age : Calculate your age.\n"
  help_text += "/voice : Convert a text to audio file.\n"
  help_text += "/max : Find the maximum number.\n"
  help_text += "/argmax : Find the index of the max number.\n"
  help_text += "/qrcode : Make a QR code from the input text."
  bot.reply_to ( message , help_text )


def start_game(chat_id):
  selected_number = random.randint (1,100)
  guess_itr = 0
  user_states[chat_id] = {"game": {"playing": True, "number": selected_number, "guesses": guess_itr}}
  game_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  game_keyboard.add(types.KeyboardButton("New Game"))
  bot.send_message(chat_id, "Welcome to my Guess number Game! Guess a number between 1 and 100. I can help you to find the correct number.", reply_markup=game_keyboard)

@bot.message_handler(commands=['game'])
@bot.message_handler(func=lambda message: message.text == "Guess number game" or message.text == "New Game")
def handle_game_start(message):
    start_game(message.chat.id)

@bot.message_handler(func=lambda message: message.chat.id in user_states and "game" in user_states[message.chat.id] and user_states[message.chat.id]['game']['playing'])
def handle_guess(message):
  chat_id = message.chat.id
  game_state = user_states[chat_id]["game"]
  guess_number = int (message.text)
  if guess_number < 1 or guess_number > 100:
    bot.send_message (chat_id , "Invalid number, type a number between 1 and 100")
  elif guess_number == game_state['number'] :
    bot.send_message (chat_id , "🍀🍀CONGRATULATION🍀🍀")
    bot.send_message (chat_id , "YOU WIN")
    text = "number of incorrect guess :"
    text += str (game_state['guesses'])
    bot.send_message (chat_id , text)
    game_state['playing'] = False
    bot.send_message(chat_id, "Select an option from the menu or start a new game.", reply_markup=my_keyboard)
  elif guess_number > game_state['number'] :
    bot.send_message (chat_id , "GO DOWN 🔽🔽")
    game_state['guesses'] += 1
  elif guess_number < game_state['number'] :
    bot.send_message (chat_id , "GO UP 🔼🔼")
    game_state['guesses'] += 1
  elif message.text == "New Game":
    game_state['playing'] = False
     

 


@bot.message_handler(commands=['age'])
@bot.message_handler(func=lambda message: message.text == "Age")
def Type_Birthday_Date (message):
  bot.send_message(message.chat.id, "Please enter your birthdate in Shamsi (Hijri Shamsi) format as: (YYYY-MM-DD).")
  
@bot.message_handler(func=lambda  message: "-" in message.text and len(message.text.split("-")) == 3)
def calculate_age(message):
  birthdate = message.text.split("-")
  today = khayyam.JalaliDate.today()
  age = today - khayyam.JalaliDatetime (int (birthdate[0]),int(birthdate[1]),int(birthdate[2])) 
  age_in_day = str(age).split (" ")
  age_in_year = int (int(age_in_day[0]) / 365)
  bot.send_message(message.chat.id, f"You are {age_in_year} years old.")

@bot.message_handler(commands=['voice'])
@bot.message_handler(func=lambda message: message.text == "Voice")
def Type_Birthday_Date (message):
  bot.send_message(message.chat.id, "Please enter your text to convert it to audio file, format as: (v: My text).")

@bot.message_handler(func=lambda message: "v:" in message.text)
def text_to_voice(message):
    text_to_convert = message.text.replace('v:', '').strip()
    tts = gTTS(text_to_convert, lang='en')
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    bot.send_voice(message.chat.id, voice)


@bot.message_handler(commands=['qrcode'])
@bot.message_handler(func=lambda message: message.text == "QR_Code")
def ask_for_qr_data(message):
    bot.send_message(message.chat.id, "Please send me the data you want to encode in a QR code, format as: (qr: My request).")

@bot.message_handler(func=lambda message: "qr:" in message.text)
def generate_qr_code(message):
    data_for_qr = message.text.replace('qr:', '').strip()
    qr = qrcode.make(data_for_qr)
    img = io.BytesIO()
    qr.save(img, 'PNG')
    img.seek(0)
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['max','argmax'])
@bot.message_handler(func=lambda message: message.text == "Max" or message.text == "Argmax")
def ask_for_array(message):
  user_states[message.chat.id] = {"command": message.text}
  bot.send_message(message.chat.id, "Please send me a list of numbers separated by commas, format as: (1,2,3,...).")

@bot.message_handler(func=lambda message: "," in message.text and message.chat.id in user_states)
def max_argmax (message):
    command = user_states[message.chat.id].get("command")
    array = message.text.split (",")
    for i in range (len (array)):
      array [i] =int (array [i])

    if command == "/max" or command == "Max" :
      max_value = max (array)
      bot.send_message(message.chat.id, f"The maximum number is: {max_value}")
    elif command == "/argmax" or command == "Argmax":
      max_index = array.index(max(array))
      bot.send_message(message.chat.id, f"The index of the maximum number is: {max_index+1}")
    if message.chat.id in user_states:
        del user_states[message.chat.id]


    
   
    
bot.infinity_polling()

