help_message = '''
Отправьте команду /start, чтобы перейти к покупке.
Узнать правила можно воспользовавшись командой /terms.
'''

start_message = 'Здравствуйте, вас привествует магазин "JetStreetSam".Желаете приобрести игровую приставку Playstation 4?"!\n' + help_message

terms = '''\
Информацию по достваке вам вышлют на почту после плотежа!
'''

item_title = 'PS 4'
item_description = '''\
Купить PS4 
'''
item_title_1 = 'PS 5'
item_description_1 = '''\
Купить PS5
'''
item_title_2 = 'PS 4 pro'
item_description_2 = '''\
Купить PS4 pro
'''

AU_error = '''\
В данную страну доставка не оформляется.
'''


successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!  
Данные вашей доставки вышлены вам на почту'''



MESSAGES = {
    'start': start_message,
    'help': help_message,
    'terms': terms,
    'item_title': item_title,
    'item_description': item_description,
    'item_title_1': item_title_1,
    'item_description_1': item_description_1,
    'item_title_2': item_title_2,
    'item_description_2': item_description_2,
    'AU_error': AU_error,
    'successful_payment': successful_payment,
}
