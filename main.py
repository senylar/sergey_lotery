from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from datetime import datetime as dt

bot = Bot(token='6177906462:AAE4QbSASTkNdDM_BdcI1CfG_E0up4OSjQs')
dp = Dispatcher(bot)

#балланс пользователей: id: балланс
us_ball = {}
#ставка пользователя: id: ставка
us_bet = {}
#событие на которое ставка: id: true/false
us_bet_var = {}
us_stat = {}
#вводиться ли сейчас ставка?
bet = False

#проводиться ли сейчас регистрация?
req = False

fuc = False
#словарь с никами пользователями id: ник
name_dict = {}

fu_list = {}


coef = 0.5
set_c =  False

ser_to_vuz = ""

admin_list = [149378045]

print(bet)

button_hi = KeyboardButton('Сделать ставку')
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

button_true = KeyboardButton('Придёт')
button_false = KeyboardButton('Не придёт')


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    global req
    await bot.send_message(msg.chat.id,"Привет \nЗдесь ты сможешь поставить ставку на посещаемость серёги\nСейчас я тебя зарегестрирую")
    await bot.send_sticker(msg.chat.id,sticker='CAACAgIAAxkBAAEG3gVjnf9piTtC2JvvVw9Uk0KEWfadbwACYhIAArQxyEs8A3YD_xAHOiwE')
    print(msg.from_user.first_name , msg.from_user.last_name)
    if msg.chat.id in us_ball.keys():
        await bot.send_message(msg.chat.id,"Вы уже зарегестрированны")
    else:
        us_ball[msg.chat.id] = 1000
        await bot.send_message(msg.chat.id,"Ваш балланс - 1000 кредитов",reply_markup=greet_kb1)

        await bot.send_message(msg.chat.id,"Введите ник для статистики")
        req = True

# @dp.message_handler(commands=['req'])

# async def process_start_command(msg: types.Message):
#     if msg.chat.id in us_ball.keys():
#         await bot.send_message(msg.chat.id,"Вы уже зарегестрированны")
#     else:
#         us_ball[msg.chat.id] = 1000
#         await bot.send_message(msg.chat.id,"Ваш балланс - 1000 кредитов",reply_markup=greet_kb1)





def chek_bet(bet,bal):
    if bal < bet * 2:
        return "Недостаточно средств"
    else:
        return True

async def results(win):
    global us_bet
    global us_ball
    global us_bet_var

    for id in us_bet_var.keys():
        if win == us_bet_var[id]:
            bet = us_bet[id]

            us_ball[id] = us_ball[id] + (bet * 2)
            await bot.send_message(id, "Поздравляю, Сергей пришёл, ты был прав!")
            await bot.send_message(id,f"Ты выиграл, твой балланс: {us_ball[id]} \nВыигрыш составил: {bet * 2}")
            us_stat[id][0] += 1
            print(us_stat)
        else:

            bet = us_bet[id]
            us_ball[id] = us_ball[id] - (bet)
            await bot.send_message(id, "К сожалению Сергей решил проспать (((")
            await bot.send_message(id, f"Ты проиграл, твой балланс: {us_ball[id]} \nПроигрыш составил: {bet * 2}")
            us_stat[id][1] += 1
            print(us_stat)

    us_bet_var.clear()
    print(us_bet_var)



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")

@dp.message_handler(commands=['set_coef'])
async def sc(msg):
    global set_c
    await bot.send_message(msg.chat.id,"lol")
    set_c = True
    print(set_c)

@dp.message_handler(commands=['chek_coef'])
async def sc(msg):
    global coef
    await bot.send_message(msg.chat.id,f"Актуальный коеффициент {coef}")




@dp.message_handler(commands=['c'])
async def admin(msg):
    global ser_to_vuz
    if msg.chat.id in admin_list:
        await bot.send_message(msg.chat.id,f"/set_coef /chek_coef /set_event_True /set_event_False /ballance_pep ")

@dp.message_handler(commands=['set_event_True'])
async def admin(msg):
    global ser_to_vuz
    if msg.chat.id in admin_list:
        ser_to_vuz = True
        print(ser_to_vuz)
        await results(ser_to_vuz)


@dp.message_handler(commands=['set_event_False'])
async def admin(msg):
    global ser_to_vuz
    if msg.chat.id in admin_list:
        ser_to_vuz = False
        print(ser_to_vuz)
        await results(ser_to_vuz)



@dp.message_handler(commands=["ballance_pep"])
async def ball(msg):
    for id in us_ball.keys():
        print(us_ball[id])
        await bot.send_message(msg.chat.id,us_ball[id])

@dp.message_handler(commands=["fuck_u"])
async def fuck(msg):
    global fuc
    await bot.send_message(msg.chat.id,"Кого ты хочешь послать?")
    fuc = True

@dp.message_handler(commands=["hu_fucked"])
async def fuck(msg):
    global fu_list

    out = "Вот топ тех кого послали:\n"
    fu_list_st = sorted(fu_list, key=fu_list.get)
    fu_list_st.reverse()
    print(fu_list_st)
    le = 0
    for m_key in fu_list_st:
        if le == 5:
            break

        x = fu_list_st.index(m_key)
        out += f"{x + 1}. {m_key} послали {fu_list[m_key]} раз(а)\n"
        le += 1


    await bot.send_message(msg.chat.id, out)




@dp.message_handler(commands=["statistics"])
async def ball(msg):
    out = "Топ по баллансу:\n"


    us_ball_st = sorted(us_ball,key=us_ball.get)
    us_ball_st.reverse()
    print(us_ball_st)

    for m_key in us_ball_st:
        x = us_ball_st.index(m_key)
        out += f"{x+1}. {name_dict[m_key]}: {us_ball[m_key]}. {us_stat[m_key][0]} побед, и {us_stat[m_key][1]} поражений\n"

    out += ".............................\n"

    out += f"Твоё место: {us_ball_st.index(msg.chat.id)+1} {name_dict[msg.chat.id]}: {us_ball[msg.chat.id]}. {us_stat[msg.chat.id][0]} побед, и {us_stat[msg.chat.id][1]} поражений\n"
    #
    # for i in range(4):
    #     out += out_l[i]
    #
    await bot.send_message(msg.chat.id,out)






inline_btn_1 = InlineKeyboardButton('Серый придёт', callback_data='button1')
IN_B_2 = InlineKeyboardButton('Серого не будет', callback_data='btn2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1,IN_B_2)



@dp.callback_query_handler()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    user_id = callback_query.message.chat.id
    print(user_id)

    if user_id in us_bet_var.keys():

        await bot.send_message(user_id,"Переобуваться нельзя)")

    else:
        if code == "1":
            us_bet_var[user_id] = True
            await bot.send_message(user_id,f"Ставка принята, вы очень оптимистичны.\n\nВыигрыш\Проигрыш составит: {us_bet[user_id] * coef}")

        if code == "2":
            us_bet_var[user_id] = False
            await bot.send_message(user_id,f"Ставка принята, вы весьма прогматичны, и это правильно.\n\nВыигрыш\Проигрыш составит: {us_bet[user_id] * coef}")

    print(us_bet_var)



@dp.message_handler()
async def echo_message(msg):
    global bet
    global set_c
    global coef
    global fuc


    if msg.text == "Сделать ставку":


        bet = True
        global req
        global name_dict

        await bot.send_message(msg.chat.id,f"Актуальный коэффициент: {coef}\n\n Введите ставку:")
    elif set_c:

        if msg.chat.id in admin_list:
            try:
                coef = float(msg.text)
                print(msg.text)
                await bot.send_message(msg.chat.id, f"коеффициент изменён на: {coef}")
                print(coef)
                set_c = False
            except:
                await bot.send_message(msg.chat.id,"Неверно сука блять")

    elif req:
        name_dict[msg.chat.id] = msg.text
        us_stat[msg.chat.id] = [0,0]
        print(name_dict)
        req = False
        await bot.send_message(msg.chat.id, f"Очень приятно, {msg.text}")


    elif bet == True:

        print(us_bet.get(msg.chat.id))
        user_id = msg.chat.id
        try:
            bet = int(msg.text)
        except:
            Bot.send_message(msg.chat.id,"Неверное значение, попробуйте снова")

        chek_bet(bet, us_ball[user_id])
        if chek_bet(bet,us_ball[user_id]):


            if us_ball[user_id] >= bet:
                if user_id in us_bet.keys():

                    us_bet[user_id] = us_bet[user_id] + bet
                    us_ball[user_id] = us_ball[user_id] - bet
                    print(us_bet)
                    print(us_ball)
                    await bot.send_message(msg.chat.id, f"Ваша ставка {us_bet[user_id]}\nВаш балланс - {us_ball[user_id]}",reply_markup=inline_kb1)
                else:
                    us_bet[user_id] = int(bet)
                    us_ball[user_id] = us_ball[user_id] - bet
                    await bot.send_message(msg.chat.id, f"Ваша ставка {us_bet[user_id]}\nВаш балланс - {us_ball[user_id]}",reply_markup=inline_kb1)
                    print(us_bet)
                    print(us_ball)
            else:
                await bot.send_message(msg.chat.id,"Недостаточно средств(((")
        else:
            await bot.send_message(msg.chat.id, "Недостаточно средств(((")
    elif fuc:
        us_name = msg.text.lower()

        if us_name in fu_list.keys():

            fu_list[us_name] += 1

            await bot.send_message(msg.chat.id, f"Отлично, его послали нахуй вот столько раз: {fu_list[us_name]}")

        else:
            fu_list[us_name] = 1

            await bot.send_message(msg.chat.id, f"Отлично, ты первый кто послал его нахуй")

        fuc = False









if __name__ == '__main__':
    executor.start_polling(dp)