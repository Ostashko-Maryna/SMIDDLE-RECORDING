from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



btn_functional = InlineKeyboardButton('Функціонал SMIDDLE RECORDING', callback_data='functional')
kb_functional = InlineKeyboardMarkup().add(btn_functional)


kb_all_abilities = InlineKeyboardMarkup()
kb_all_abilities.add(InlineKeyboardButton('Розпізнавання мовлення', callback_data='func_speech'))
kb_all_abilities.add(InlineKeyboardButton('Пошук за параметрами', callback_data='func_search'))
kb_all_abilities.add(InlineKeyboardButton('Прискорене прослуховування записів', callback_data='func_listen'))
kb_all_abilities.add(InlineKeyboardButton('Зберігання записів', callback_data='func_keep'))
kb_all_abilities.add(InlineKeyboardButton('Багатомовний веб-інтерфейс', callback_data='func_multilingualism'))
kb_all_abilities.add(InlineKeyboardButton('Безпека', callback_data='func_safety'))
kb_all_abilities.add(InlineKeyboardButton('Запис єкрану оператора', callback_data='func_screen'))
kb_all_abilities.add(InlineKeyboardButton('API для інтеграції з сторонніми системами', callback_data='func_API'))



kb_help = InlineKeyboardMarkup()
kb_help.add(InlineKeyboardButton('Перейти на сайт SMIDDLE RECORDING', url='https://smiddle.com/uk/solutions/rishennia-dlia-kontakt-tsentru/smiddle-recording'))
kb_help.add(InlineKeyboardButton('Переглянути відео про SMIDDLE RECORDING', callback_data='video'))
kb_help.add(btn_functional)
kb_help.add(InlineKeyboardButton('Наші контакти', callback_data='contact'))
kb_help.add(InlineKeyboardButton('Замовити демо', callback_data='demo'))
# kb_help.add(InlineKeyboardButton("Зв'язатися з розробником",  switch_inline_query_current_chat='@Maro_Sulima'))

