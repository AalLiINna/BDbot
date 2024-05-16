from dbconnector import *
import telebot
from telebot import types
#your TOKEN
TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def button_message(message):
    global button01, button02, button03, button04
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button01 = types.KeyboardButton("Employee")
    button02 = types.KeyboardButton("Customer")
    button03 = types.KeyboardButton("Orders")
    button04 = types.KeyboardButton("Fails")
    markup.add(button01, button02, button03, button04)
    msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
    bot.register_next_step_handler(msg, first_answer)


def first_answer(message):
    button_start = types.KeyboardButton("Back to start")


    if message.text == "Employee":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Add Employee")
        button2 = types.KeyboardButton("Remove Employee")
        button3 = types.KeyboardButton("Get Employee")
        markup.add(button1, button2, button3, button_start)
        msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
        bot.register_next_step_handler(msg, emp_answer)

    elif message.text == "Customer":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Add Customer")
        button2 = types.KeyboardButton("Remove Customer")
        button3 = types.KeyboardButton("Get Customer")
        markup.add(button1, button2, button3, button_start)
        msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
        bot.register_next_step_handler(msg, cust_answer)

    elif message.text == "Orders":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Add Orders")
        button2 = types.KeyboardButton("Remove Orders")
        button3 = types.KeyboardButton("Get Orders")
        markup.add(button1, button2, button3, button_start)
        msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
        bot.register_next_step_handler(msg, orders_answer)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Add Fails")
        button2 = types.KeyboardButton("Remove Fails")
        button3 = types.KeyboardButton("Get Fails")
        markup.add(button1, button2, button3, button_start)
        msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
        bot.register_next_step_handler(msg, fails_answer)

def add_employee(text: types.Message):
    t = text.text.split(", ")
    connector = DbConnector()
    connector.add_employee(*t)
    bot.register_next_step_handler('Choose action', emp_answer)

def add_customer(text: types.Message):
    t = text.text.split(", ")
    connector = DbConnector()
    connector.add_customer(*t)
    bot.register_next_step_handler('Choose action', cust_answer)

def add_order(text: types.Message):
    t = text.text.split(", ")
    connector = DbConnector()
    connector.add_order(*t)
    bot.register_next_step_handler('Choose action', orders_answer)

def add_fail(text: types.Message):
    t = text.text.split(", ")
    connector = DbConnector()
    connector.add_fail(*t)
    bot.register_next_step_handler('Choose action', fails_answer)

def remove_customer(text: types.Message):
    connector = DbConnector()
    connector.remove_customer(text.text)
    bot.register_next_step_handler('Choose action', cust_answer)

def remove_fail(text: types.Message):
    connector = DbConnector()
    connector.remove_fail(text.text)
    bot.register_next_step_handler('Choose action', fails_answer)

def remove_employee(text: types.Message):
    connector = DbConnector()
    connector.remove_employee(text.text)
    bot.register_next_step_handler('Choose action', emp_answer)

def remove_orders(text: types.Message):
    connector = DbConnector()
    connector.remove_orders(text.text)
    bot.register_next_step_handler('Choose action', orders_answer)
def emp_answer(message):
    if message.text == "Add Employee":
        msg = bot.send_message(message.chat.id, "Write the data separated by ', + space'\nId\nName\nSpecialisation\nDate of employement")
        bot.register_next_step_handler(msg, add_employee)

    elif message.text == "Remove Employee":
        msg = bot.send_message(message.chat.id, "Remove Employee with Name:")
        bot.register_next_step_handler(msg, remove_employee)

    elif message.text == "Get Employee":
        get_emp = a.get_employees()
        employees = []
        for emp in get_emp:
            employees.append(f"id{emp[0]}\nName: {emp[1]}\nSpec: {emp[2]}\nDate of emp.: {emp[3]}\n")
        msg = bot.send_message(message.chat.id,'\n'.join(employees))
        bot.register_next_step_handler(msg, emp_answer)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(button01, button02, button03, button04)
        msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
        bot.register_next_step_handler(msg, first_answer)



def cust_answer(message):
    if message.text == "Add Customer":
        msg = bot.send_message(message.chat.id,"Write the data separated by ', + space'\nPhone Number\nCustomer's Name")
        bot.register_next_step_handler(msg, add_customer)

    elif message.text == "Remove Customer":
        msg = bot.send_message(message.chat.id, "Remove Customer with Name:")
        bot.register_next_step_handler(msg, remove_customer)

    elif message.text == "Get Customer":
        get_cust = a.get_customers()
        customers = []
        for cs in get_cust:
            # phone_number}','{cust_name
            customers.append(f"Name: {cs[0]}\nPhone number: {cs[1]}\n")
        msg = bot.send_message(message.chat.id, '\n'.join(customers))
        bot.register_next_step_handler(msg, cust_answer)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(button01, button02, button03, button04)
        msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
        bot.register_next_step_handler(msg, first_answer)


def orders_answer(message):
    if message.text == "Add Orders":
        msg = bot.send_message(message.chat.id,"Write the data separated by ', + space'\nID\nOrder Code\nPC Code"
                                               "\nMaster ID\nRepair begin\nRepair end\nCost\nFailure\nCustomer's Name")
        bot.register_next_step_handler(msg, add_order)

    elif message.text == "Remove Orders":
        msg = bot.send_message(message.chat.id, "Remove Order with 'Order Code':")
        bot.register_next_step_handler(msg, remove_orders)

    elif message.text == "Get Orders":
        get_o = a.get_orders()
        orders = []
        for o in get_o:
            orders.append(f"ID: {o[0]}\nOrder Code: {o[1]}\nPC Code: {o[2]}\nMaster ID: {o[3]}\nRepair begin: {o[4]}\nRepair end: {o[5]}\n"
                          f"Cost: {o[6]}\nFailure: {o[7]}\nCustomer's Name: {o[8]}\n")
        msg = bot.send_message(message.chat.id, '\n'.join(orders))
        bot.register_next_step_handler(msg, orders_answer)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(button01, button02, button03, button04)
        msg = bot.send_message(message.chat.id, "Choose answer", reply_markup=markup)
        bot.register_next_step_handler(msg, first_answer)

def fails_answer(message):
    if message.text == "Add Fails":
        msg = bot.send_message(message.chat.id,"Write the data separated by ', + space'\nID\nOrder ID"
                                               "\nMaster ID\nFail cause\nFailure Description")
        bot.register_next_step_handler(msg, add_fail)

    elif message.text == "Remove Fails":
        msg = bot.send_message(message.chat.id, "Remove Failure with 'ID':")
        bot.register_next_step_handler(msg, remove_fail)

    elif message.text == "Get Fails":
        get_cust = a.get_fail()
        fail = []
        for f in get_cust:
            fail.append(f"ID: {f[0]}\nOrder ID: {f[1]}\nMaster ID: {f[2]}\nFail cause: {f[3]}\nDescription: {f[4]}\n")
        msg = bot.send_message(message.chat.id, '\n'.join(fail))
        bot.register_next_step_handler(msg, cust_answer)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(button01, button02, button03, button04)
        msg = bot.send_message(message.chat.id, "Choose action", reply_markup=markup)
        bot.register_next_step_handler(msg, first_answer)




bot.infinity_polling()
