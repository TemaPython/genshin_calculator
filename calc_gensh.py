from classes import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

"""
Модуль calc_gensh предназзначен для создания приложения и подсчета общих характеристик персонажа. Состоит из блоков:
- Импорт библиотек (необходимы tkinter  локальный модуль classes)
- Константы
- Функция создания персонажа (create_perc)
- Функция назначения оружия (select_weapon)
- Создание окна приложения
- Блок выбора персонажа
- Блок выбора оружия
- Блок артефактов
  - Значения по умолчанию для каждого стата цветка, пера, часов, кубка и шапки
  - Создание интерактивных элементов для каждого стата цветка, пера, часов, кубка и шапки
- Функция подсчета характеристик при нажатии кнопки и вывода их в отдельное окно
- Размещение всех элементов приложения
"""


# Константы
GEOM = '1700x850'
FONT = ('Arial', 14)
WD = 25
TITLE = 'Калькулятор артефактов'
STAT = ['КУ', 'КШ', 'АТК', 'АТК%', 'ХП', 'ХП%', 'МС', 'ЗАЩ', 'ЗАЩ%', 'ВЭ']
STAT_TI = ['АТК% 46.6%', 'ХП% 46.6%', 'МС 187', 'ЗАЩ% 58.3%', 'ВЭ 51.8%']
STAT_GO = ['АТК%', 'ХП%', 'МС', 'ЗАЩ%', 'БОНУС ПИРО', 'БОНУС КРИО', 'БОНУС АНЕМО', 'БОНУС ГЕО', 'БОНУС ЭЛЕКТРО',
           'БОНУС ДЕНДРО', 'БОНУС ГИДРО', 'БОНУС ФИЗ']
STAT_HE = ['КУ', 'КШ', 'АТК%', 'ХП%', 'МС', 'ЗАЩ%', 'БОНУС ЛЕЧ']
PERC = ['Не выбрано', 'Альбедо', 'Итто', 'Горо', 'Путешественник (Гео)', 'Нин Гуан', 'Ноэлль', 'Юнь Цзинь', 'Чжун Ли',
        'Аль-Хайтам', 'Бай Чжу', 'Коллеи', 'Кавех', 'Нахида', 'Тигнари', 'Путешественник (Дендро)', 'Яо Яо',
        'Элой', 'Чун Юнь', 'Диона', 'Эола', 'Гань Юй', 'Кэйа', 'Аяка', 'Лайла', 'Мика', 'Ци Ци', 'Розария', 'Шэнь Хэ',
        'Ху Тао', 'Эмбер', 'Ёимия', 'Беннет', 'Дэхья', 'Дилюк', 'Кли', 'Тома', 'Сян Лин', 'Синь Янь', 'Янь Фэй',
        'Барбара', 'Кандакия', 'Аято', 'Мона', 'Нилу', 'Кокоми', 'Тарталья', 'Син Цю', 'Е Лань',
        'Бэй Доу', 'Сайно', 'Дори', 'Фишль', 'Кэ Цин', 'Сара', 'Синобу', 'Лиза', 'Райдэн', 'Рэйзор',
        'Путешественник (Электро)', 'Яэ Мико',
        'Фарузан', 'Джинн', 'Кадзуха', 'Саю', 'Хэйдхо', 'Сахароза', 'Путешественник (Анемо)', 'Венти', 'Странник',
        'Сяо']
PERC_DICT = {'Альбедо': Albedo(), 'Итто': AratakiItto(), 'Горо': Gorou(), 'Путешественник (Гео)': TravelerGeo(),
             'Нин Гуан': Ningguang(), 'Ноэлль': Noelle(), 'Юнь Цзинь': YunJin(), 'Чжун Ли': Zhongli(),
             'Аль-Хайтам': Alhaitham(), 'Бай Чжу': Baizhu(), 'Коллеи': Collei(), 'Кавех': Kaveh(), 'Нахида': Nahida(),
             'Тигнари': Tighnari(), 'Путешественник (Дендро)': TravelerDendro(), 'Яо Яо': Yaoyao(),
             'Элой': Aloy(), 'Чуе Юнь': Chongyun(), 'Диона': Diona(), 'Эола': Eula(),
             'Гань Юй': Ganyu(), 'Кэйа': Kaeya(), 'Аяка': KamisatoAyaka(), 'Лайла': Layla(),
             'Мика': Mika(), 'Ци Ци': Qiqi(), 'Розария': Rosaria(), 'Шэнь Хэ': Shenhe(),
             'Эмбер': Amber(), 'Ёимия': Yoimiya(), 'Беннет': Bennett(), 'Дэхья': Dehya(), 'Дилюк': Diluc(),
             'Кли': Klee(), 'Ху Тао': HuTao(), 'Тома': Thoma(), 'Сян Лин': Xiangling(), 'Синь Янь': Xinyan(),
             'Янь Фэй': Yanfei(),
             'Барбара': Barbara(), 'Кандакия': Candace(), 'Аято': KamisatoAyato(), 'Мона': Mona(), 'Нилу': Nilou(),
             'Кокоми': SangonomiyaKokomi(), 'Тарталья': Tartaglia(), 'Син Цю': Xingqiu(), 'Е Лань': Yelan(),
             'Бэй Доу': Beidou(), 'Сайно': Cyno(), 'Дори': Dori(), 'Фишль': Fischl(), 'Кэ Цин': Keqing(),
             'Сара': KujouSara(), 'Синобу': KukiShinobu(), 'Лиза': Lisa(), 'Райдэн': RaidenShogun(), 'Рэйзор': Razor(),
             'Путешественник (Электро)': TravelerElectro(), 'Яэ Мико': YaeMiko(),
             'Фарузан': Faruzan(), 'Джинн': Jean(), 'Кадзуха': KaedeharaKazuha(), 'Саю': Sayu(),
             'Хэйдхо': ShikanoinHeizou(), 'Сахароза': Sucrose(), 'Путешественник (Анемо)': TravelerAnemo(),
             'Венти': Venti(), 'Странник': Wanderer(), 'Сяо': Xiao()}
WEAP_DICT = {"Коршун": Korshun, "Хома": Homa}
WEAPON_SWORD = ['Меч']
WEAPON_CLAYMORE = ['Двурук']
WEAPON_POLEARM = ['Коршун', 'Хома']
WEAPON_CATALYST = ['Песнь странника']
WEAPON_BOW = ['Лук']

# Функция создания нового персонажа и подбор списка оружия для него


def create_perc(*args):

    """Функция переназначает класс выбранного персонажа и меняет значения списка оружия подходящего
    под этого персонажа"""

    selected_perc = PERC_DICT[percbox.get()]
    if selected_perc.weapon_type == 'sword':
        weapbox.config(values=WEAPON_SWORD)
    elif selected_perc.weapon_type == 'claymore':
        weapbox.config(values=WEAPON_CLAYMORE)
    elif selected_perc.weapon_type == 'polearm':
        weapbox.config(values=WEAPON_POLEARM)
    elif selected_perc.weapon_type == 'catalyst':
        weapbox.config(values=WEAPON_CATALYST)
    elif selected_perc.weapon_type == 'bow':
        weapbox.config(values=WEAPON_BOW)
    return

# Функция выбора оружия


def select_weapon(*args):
    """
    Функция переназначает выбранное оружие
    """
    selected_weapon = WEAP_DICT[weapbox.get()]
    print(selected_weapon)
    return


window = tk.Tk()  # порождаем окно как экземпляр класса Tk
window.geometry(GEOM)
window.title(TITLE)

# Блок выбора персонажа
selected_perc = tk.StringVar(value='Не выбрано')
perctext = ttk.Label(window, font=FONT, text='Выберите персонажа')
percbox = ttk.Combobox(window, values=PERC, font=FONT, textvariable=selected_perc, width=WD)
# Блок выбора оружия
selected_weapon = tk.StringVar(value='Не выбрано')
weaptext = ttk.Label(window, font=FONT, text='Выберите оружие')
weapbox = ttk.Combobox(window, values=WEAPON_POLEARM, font=FONT, textvariable=selected_weapon, width=WD)

# Блок артефактов
arttext = ttk.Label(window, font=FONT, text='Выберете и заполните характеристики артефактов')

# Значения по умолчанию (Каждому combobox нужен свой StringVar, иначе при смене значения, оно будет меняться везде)
# Цветок
selectstatfl1 = tk.StringVar(value=STAT[0])
selectstatfl2 = tk.StringVar(value=STAT[1])
selectstatfl3 = tk.StringVar(value=STAT[5])
selectstatfl4 = tk.StringVar(value=STAT[8])

# Перо
selectstatfe1 = tk.StringVar(value=STAT[0])
selectstatfe2 = tk.StringVar(value=STAT[1])
selectstatfe3 = tk.StringVar(value=STAT[5])
selectstatfe4 = tk.StringVar(value=STAT[8])

# Перо
selectmainstatti = tk.StringVar(value=STAT_TI[0])
selectstatti1 = tk.StringVar(value=STAT[0])
selectstatti2 = tk.StringVar(value=STAT[1])
selectstatti3 = tk.StringVar(value=STAT[6])
selectstatti4 = tk.StringVar(value=STAT[9])

# Кубок
selectmainstatgo = tk.StringVar(value=STAT_TI[0])
selectstatgo1 = tk.StringVar(value=STAT[0])
selectstatgo2 = tk.StringVar(value=STAT[1])
selectstatgo3 = tk.StringVar(value=STAT[6])
selectstatgo4 = tk.StringVar(value=STAT[9])

# Шапка
selectmainstathe = tk.StringVar(value=STAT_HE[0])
selectstathe1 = tk.StringVar(value=STAT[0])
selectstathe2 = tk.StringVar(value=STAT[1])
selectstathe3 = tk.StringVar(value=STAT[6])
selectstathe4 = tk.StringVar(value=STAT[9])

# Создание интерактивных элементов цветка
flowertext1 = ttk.Label(window, text='Цветок', font=FONT)
flowertext2 = ttk.Label(window, text='Основной стат ХП', font=FONT)
flowertext3 = ttk.Label(window, text='ХП 4780', font=FONT)
flowerbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl1, font=FONT)
flower1 = ttk.Entry(window, font=FONT)
flowerbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl2, font=FONT)
flower2 = ttk.Entry(window, font=FONT)
flowerbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl3, font=FONT)
flower3 = ttk.Entry(window, font=FONT)
flowerbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl4, font=FONT)
flower4 = ttk.Entry(window, font=FONT)

# Создание интерактивных элементов пера
feathertext1 = ttk.Label(window, text='Перо', font=FONT)
feathertext2 = ttk.Label(window, text='Основной стат АТК', font=FONT)
feathertext3 = ttk.Label(window, text='АТК 311', font=FONT)
featherbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe1, font=FONT)
feather1 = ttk.Entry(window, font=FONT)
featherbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe2, font=FONT)
feather2 = ttk.Entry(window, font=FONT)
featherbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe3, font=FONT)
feather3 = ttk.Entry(window, font=FONT)
featherbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe4, font=FONT)
feather4 = ttk.Entry(window, font=FONT)

# Создание интерактивных элементов часов
timepiecetext1 = ttk.Label(window, text='Часы', font=FONT)
timepiecetext2 = ttk.Label(window, text='Основной стат', font=FONT)
timepiecemain = ttk.Combobox(window, values=STAT_TI, textvariable=selectmainstatti, justify='center', font=FONT)
timepiecebox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatti1, font=FONT)
timepiece1 = ttk.Entry(window, font=FONT)
timepiecebox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatti2, font=FONT)
timepiece2 = ttk.Entry(window, font=FONT)
timepiecebox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatti3, font=FONT)
timepiece3 = ttk.Entry(window, font=FONT)
timepiecebox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatti4, font=FONT)
timepiece4 = ttk.Entry(window, font=FONT)

# Создание интерактивных элементов часов
goblettext1 = ttk.Label(window, text='Кубок', font=FONT)
goblettext2 = ttk.Label(window, text='Основной стат', font=FONT)
gobletmain = ttk.Combobox(window, values=STAT_GO, textvariable=selectmainstatgo, justify='center', font=FONT)
gobletbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo1, font=FONT)
goblet1 = ttk.Entry(window, font=FONT)
gobletbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo2, font=FONT)
goblet2 = ttk.Entry(window, font=FONT)
gobletbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo3, font=FONT)
goblet3 = ttk.Entry(window, font=FONT)
gobletbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo4, font=FONT)
goblet4 = ttk.Entry(window, font=FONT)

# Создание интерактивных элементов кубка
headgeartext1 = ttk.Label(window, text='Кубок', font=FONT)
headgeartext2 = ttk.Label(window, text='Основной стат', font=FONT)
headgearmain = ttk.Combobox(window, values=STAT_HE, textvariable=selectmainstathe, justify='center', font=FONT)
headgearbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstathe1, font=FONT)
headgear1 = ttk.Entry(window, font=FONT)
headgearbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstathe2, font=FONT)
headgear2 = ttk.Entry(window, font=FONT)
headgearbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstathe3, font=FONT)
headgear3 = ttk.Entry(window, font=FONT)
headgearbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstathe4, font=FONT)
headgear4 = ttk.Entry(window, font=FONT)

# Функция подсчёта характеристик


def clicked():
    messagebox.showinfo("Проверка", f'Ваша сборка оптимальна на  {None} %')


button = ttk.Button(window, text='Подсчитать значения', command=clicked)


# Блок размещения элементов
# Персонаж
perctext.grid(column=2, row=0, padx=20, pady=10)
percbox.grid(column=2, row=1, padx=20, pady=10)
selected_perc.trace_add('write', create_perc)

# Оружие
weaptext.grid(column=2, row=2, padx=20, pady=10)
weapbox.grid(column=2, row=3, padx=20, pady=10)
selected_weapon.trace_add('write', select_weapon)

# Артефакты
arttext.grid(column=2, row=4, padx=20, pady=10)

# Подблок Цветок
flowertext1.grid(column=0, row=5, padx=20, pady=10)
flowertext2.grid(column=0, row=6, padx=20, pady=10)
flowertext3.grid(column=0, row=7, padx=20, pady=10)
flowerbox1.grid(column=0, row=8, padx=20, pady=10)
flower1.grid(column=0, row=9, padx=20, pady=10)
flowerbox2.grid(column=0, row=10, padx=20, pady=10)
flower2.grid(column=0, row=11, padx=20, pady=10)
flowerbox3.grid(column=0, row=12, padx=20, pady=10)
flower3.grid(column=0, row=13, padx=20, pady=10)
flowerbox4.grid(column=0, row=14, padx=20, pady=10)
flower4.grid(column=0, row=15, padx=20, pady=10)

# Подблок Перо
feathertext1.grid(column=1, row=5, padx=20, pady=10)
feathertext2.grid(column=1, row=6, padx=20, pady=10)
feathertext3.grid(column=1, row=7, padx=20, pady=10)
featherbox1.grid(column=1, row=8, padx=20, pady=10)
feather1.grid(column=1, row=9, padx=20, pady=10)
featherbox2.grid(column=1, row=10, padx=20, pady=10)
feather2.grid(column=1, row=11, padx=20, pady=10)
featherbox3.grid(column=1, row=12, padx=20, pady=10)
feather3.grid(column=1, row=13, padx=20, pady=10)
featherbox4.grid(column=1, row=14, padx=20, pady=10)
feather4.grid(column=1, row=15, padx=20, pady=10)

# Подблок Часы
timepiecetext1.grid(column=2, row=5, padx=20, pady=10)
timepiecetext2.grid(column=2, row=6, padx=20, pady=10)
timepiecemain.grid(column=2, row=7, padx=20, pady=10)
timepiecebox1.grid(column=2, row=8, padx=20, pady=10)
timepiece1.grid(column=2, row=9, padx=20, pady=10)
timepiecebox2.grid(column=2, row=10, padx=20, pady=10)
timepiece2.grid(column=2, row=11, padx=20, pady=10)
timepiecebox3.grid(column=2, row=12, padx=20, pady=10)
timepiece3.grid(column=2, row=13, padx=20, pady=10)
timepiecebox4.grid(column=2, row=14, padx=20, pady=10)
timepiece4.grid(column=2, row=15, padx=20, pady=10)

# Подблок Кубок
goblettext1.grid(column=3, row=5, padx=20, pady=10)
goblettext2.grid(column=3, row=6, padx=20, pady=10)
gobletmain.grid(column=3, row=7, padx=20, pady=10)
gobletbox1.grid(column=3, row=8, padx=20, pady=10)
goblet1.grid(column=3, row=9, padx=20, pady=10)
gobletbox2.grid(column=3, row=10, padx=20, pady=10)
goblet2.grid(column=3, row=11, padx=20, pady=10)
gobletbox3.grid(column=3, row=12, padx=20, pady=10)
goblet3.grid(column=3, row=13, padx=20, pady=10)
gobletbox4.grid(column=3, row=14, padx=20, pady=10)
goblet4.grid(column=3, row=15, padx=20, pady=10)

# Подблок Шапка
headgeartext1.grid(column=4, row=5, padx=20, pady=10)
headgeartext2.grid(column=4, row=6, padx=20, pady=10)
headgearmain.grid(column=4, row=7, padx=20, pady=10)
headgearbox1.grid(column=4, row=8, padx=20, pady=10)
headgear1.grid(column=4, row=9, padx=20, pady=10)
headgearbox2.grid(column=4, row=10, padx=20, pady=10)
headgear2.grid(column=4, row=11, padx=20, pady=10)
headgearbox3.grid(column=4, row=12, padx=20, pady=10)
headgear3.grid(column=4, row=13, padx=20, pady=10)
headgearbox4.grid(column=4, row=14, padx=20, pady=10)
headgear4.grid(column=4, row=15, padx=20, pady=10)

# Кнопки
button.grid(column=2, row=16, padx=20, pady=10)  # Кнопка вызова функции подсчета общих характеристик


window.mainloop()  # бесконечный цикл ожидания
