us_ball = {
           149378046: 20,
           149378047: 100,
           149378048: 400,
           149378049: 800}
#ставка пользователя: id: ставка
us_bet = {}
#событие на которое ставка: id: true/false
us_bet_var = {}
us_stat = {149378045: [11,0],
           149378046: [1,4],
           149378047: [1,5],
           149378048: [5,5],
           149378049: [1,6]}
#вводиться ли сейчас ставка?
bet = False

#проводиться ли сейчас регистрация?
req = False

#словарь с никами пользователями id: ник
name_dict = {
           149378046: "чсо",
           149378047: "lol",
           149378048: "kek",
           149378049: "hu"}


fu_list = {"1": 4,
           "2": 2,
           "3":1}
def fuck():
    global fu_list

    out = "Топ по баллансу:\n"

    fu_list_st = sorted(us_ball, key=us_ball.get)
    fu_list_st.reverse()
    print(fu_list)

    for m_key in fu_list_st:
        x = fu_list_st.index(m_key)
        out += f"{x + 1}. {name_dict[m_key]}: {us_ball[m_key]}. {us_stat[m_key][0]} побед, и {us_stat[m_key][1]} поражений\n"

    out += ".............................\n"

    out += f"Твоё место: {fu_list_st.index(n) + 1} {name_dict[n]}: {us_ball[msg.chat.id]}. {us_stat[msg.chat.id][0]} побед, и {us_stat[msg.chat.id][1]} поражений\n"
    #
    # for i in range(4):
    #     out += out_l[i]