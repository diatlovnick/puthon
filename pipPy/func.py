#1) написать функцию add, которая примет 2 числа и сложит их

def add(update, context):
    arg = context.args
    print(arg)
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Вы ничего не ввели, введите числа через пробел после названия команды")
        return
    try:
        arg = list(map(int,arg))
    except ValueError:
        context.bot.send_message(update.effective_chat.id, "Вы ввели не число")
    res = sum(arg)
    arg = "+".join(list(map(str,arg)))
    context.bot.send_message(update.effective_chat.id, f"{arg} = {res}")

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "I'm Batman")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')

