from classes import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

"""
Модуль calc_gensh предназзначен для создания приложения и подсчета общих
 характеристик персонажа. Состоит из блоков:
- Импорт библиотек (необходимы tkinter  локальный модуль classes)
- Константы
- Функция создания персонажа (create_perc)
- Функция назначения оружия (select_weapon)
- Создание окна приложения
- Блок выбора персонажа
- Блок выбора оружия
- Блок артефактов
  - Значения по умолчанию для каждого стата цветка, пера, часов, кубка и шапки
  - Создание интерактивных элементов для каждого стата цветка, пера, часов,
   кубка и шапки
- Функция подсчета характеристик при нажатии кнопки и вывода их в отдельное окно
- Размещение всех элементов приложения
"""


# Константы
GEOM = '1700x850'
FONT = ('Arial', 14)
WD = 25
TITLE = 'Калькулятор артефактов'
STAT = ['КУ', 'КШ', 'АТК', 'АТК%', 'ХП', 'ХП%', 'МС', 'ЗАЩ', 'ЗАЩ%', 'ВЭ']
STAT_TI = ['АТК% 46.6', 'ХП% 46.6', 'МС 187', 'ЗАЩ% 58.3', 'ВЭ 51.8']
STAT_GO = ['АТК% 46.6', 'ХП% 46.6', 'МС 187', 'ЗАЩ% 58.3', 'БОНУСПИРО 46.6',
           'БОНУСКРИО  46.6', 'БОНУСАНЕМО  46.6', 'БОНУСГЕО  46.6',
           'БОНУСЭЛЕКТРО  46.6', 'БОНУСДЕНДРО  46.6', 'БОНУСГИДРО  46.6',
           'БОНУСФИЗ 58.3']
STAT_HE = ['КУ 62.2', 'КШ 31.1', 'АТК% 46.6', 'ХП% 46.6', 'МС 187', 'ЗАЩ% 58.3',
           'БОНУСЛЕЧ 35.9']
PERC = [
        #'Не выбрано', 'Альбедо', 'Итто', 'Горо', 'Путешественник (Гео)',
        #'Нин Гуан', 'Ноэлль', 'Юнь Цзинь', 'Чжун Ли', 'Аль-Хайтам', 'Бай Чжу',
        #'Коллеи', 'Кавех', 'Нахида', 'Тигнари', 'Путешественник (Дендро)',
        #'Яо Яо', 'Элой', 'Чун Юнь', 'Диона', 'Эола', 'Гань Юй', 'Кэйа', 'Аяка',
        #'Лайла', 'Мика', 'Ци Ци', 'Розария', 'Шэнь Хэ',
        'Ху Тао',
        #'Эмбер',
        #'Ёимия', 'Беннет', 'Дэхья', 'Дилюк', 'Кли', 'Тома', 'Сян Лин',
        #'Синь Янь', 'Янь Фэй', 'Барбара', 'Кандакия', 'Аято', 'Мона', 'Нилу',
        #'Кокоми', 'Тарталья', 'Син Цю', 'Е Лань', 'Бэй Доу', 'Сайно', 'Дори',
        #'Фишль', 'Кэ Цин', 'Сара', 'Синобу', 'Лиза', 'Райдэн', 'Рэйзор',
        #'Путешественник (Электро)', 'Яэ Мико', 'Фарузан', 'Джинн', 'Кадзуха',
       # 'Саю', 'Хэйдхо', 'Сахароза', 'Путешественник (Анемо)', 'Венти',
        #'Странник', 'Сяо'
        ]
PERC_DICT = {'Альбедо': Albedo(), 'Итто': AratakiItto(), 'Горо': Gorou(),
             'Путешественник (Гео)': TravelerGeo(), 'Нин Гуан': Ningguang(),
             'Ноэлль': Noelle(), 'Юнь Цзинь': YunJin(), 'Чжун Ли': Zhongli(),
             'Аль-Хайтам': Alhaitham(), 'Бай Чжу': Baizhu(), 'Коллеи': Collei(),
             'Кавех': Kaveh(), 'Нахида': Nahida(), 'Тигнари': Tighnari(),
             'Путешественник (Дендро)': TravelerDendro(), 'Яо Яо': Yaoyao(),
             'Элой': Aloy(), 'Чуе Юнь': Chongyun(), 'Диона': Diona(),
             'Эола': Eula(), 'Гань Юй': Ganyu(), 'Кэйа': Kaeya(),
             'Аяка': KamisatoAyaka(), 'Лайла': Layla(), 'Мика': Mika(),
             'Ци Ци': Qiqi(), 'Розария': Rosaria(), 'Шэнь Хэ': Shenhe(),
             'Эмбер': Amber(), 'Ёимия': Yoimiya(), 'Беннет': Bennett(),
             'Дэхья': Dehya(), 'Дилюк': Diluc(), 'Кли': Klee(),
             'Ху Тао': HuTao(), 'Тома': Thoma(), 'Сян Лин': Xiangling(),
             'Синь Янь': Xinyan(), 'Янь Фэй': Yanfei(), 'Барбара': Barbara(),
             'Кандакия': Candace(), 'Аято': KamisatoAyato(), 'Мона': Mona(),
             'Нилу': Nilou(), 'Кокоми': SangonomiyaKokomi(),
             'Тарталья': Tartaglia(), 'Син Цю': Xingqiu(), 'Е Лань': Yelan(),
             'Бэй Доу': Beidou(), 'Сайно': Cyno(), 'Дори': Dori(),
             'Фишль': Fischl(), 'Кэ Цин': Keqing(), 'Сара': KujouSara(),
             'Синобу': KukiShinobu(), 'Лиза': Lisa(), 'Райдэн': RaidenShogun(),
             'Рэйзор': Razor(), 'Путешественник (Электро)': TravelerElectro(),
             'Яэ Мико': YaeMiko(), 'Фарузан': Faruzan(), 'Джинн': Jean(),
             'Кадзуха': KaedeharaKazuha(), 'Саю': Sayu(),
             'Хэйдхо': ShikanoinHeizou(), 'Сахароза': Sucrose(),
             'Путешественник (Анемо)': TravelerAnemo(), 'Венти': Venti(),
             'Странник': Wanderer(), 'Сяо': Xiao()}
IMG_DICT = {'Ху Тао': 'AvatarIcon_Hutao.png'}
WEAP_DICT = {'Меч Сокола': AquilaFavonia,
             'Маяк тростникового моря':  BeaconOfTheReedSea,
             'Коршун': Korshun, 'Хома': Homa,
             'Сновидения тысячи ночей': AThousandFloatingDreams,
             'Лук Амоса': AmosBow}
WEAPON_SWORD = ['Меч Сокола']
WEAPON_CLAYMORE = ['Маяк тростникового моря']
WEAPON_POLEARM = ['Коршун', 'Хома']
WEAPON_CATALYST = ['Сновидения тысячи ночей']
WEAPON_BOW = ['Лук Амоса']

# Функция создания нового персонажа и подбор списка оружия для него


def create_perc(*args):

    """Функция переназначает класс выбранного персонажа и меняет значения
    списка оружия подходящего
    под этого персонажа"""
    global selected_perc
    selected_perc = PERC_DICT[percbox.get()]
    # Блок изменение картинки персонажа
    img = Image.open(IMG_DICT[percbox.get()])
    img = ImageTk.PhotoImage(img.resize((150, 150)))
    panel.configure(image=img)
    panel.image = img

    # Блок изменения списка оружия
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
    if percbox.get() == 'Не выбрано':
        messagebox.showerror("Ошибка", "Сначала выберите персонажа")
        return
    selected_weapon = WEAP_DICT[weapbox.get()]
    selected_perc.give_weapon(selected_weapon)
    return


window = tk.Tk()  # порождаем окно как экземпляр класса Tk
window.geometry(GEOM)
window.title(TITLE)

# Блок выбора персонажа
selected_perc = tk.StringVar(value='Не выбрано')
perctext = ttk.Label(window, font=FONT, text='Выберите персонажа')
percbox = ttk.Combobox(window, values=PERC, font=FONT,
                       textvariable=selected_perc, width=WD, state='readonly')
# Блок выбора оружия
selected_weapon = tk.StringVar(value='Не выбрано')
weaptext = ttk.Label(window, font=FONT, text='Выберите оружие')
weapbox = ttk.Combobox(window, values=WEAPON_POLEARM, font=FONT,
                       textvariable=selected_weapon, width=WD, state='readonly')

# Блок артефактов
arttext = ttk.Label(window, font=FONT,
                    text='Выберите и заполните характеристики артефактов')

# Значения по умолчанию (Каждому combobox нужен свой StringVar,
# иначе при смене значения, оно будет меняться везде)
# Цветок
selectstatfl1 = tk.StringVar(value=STAT[0])
selectstatfl2 = tk.StringVar(value=STAT[1])
selectstatfl3 = tk.StringVar(value=STAT[5])
selectstatfl4 = tk.StringVar(value=STAT[8])
statfl1 = tk.StringVar(value='0')
statfl2 = tk.StringVar(value='0')
statfl3 = tk.StringVar(value='0')
statfl4 = tk.StringVar(value='0')

# Перо
selectstatfe1 = tk.StringVar(value=STAT[0])
selectstatfe2 = tk.StringVar(value=STAT[1])
selectstatfe3 = tk.StringVar(value=STAT[5])
selectstatfe4 = tk.StringVar(value=STAT[8])
statfe1 = tk.StringVar(value='0')
statfe2 = tk.StringVar(value='0')
statfe3 = tk.StringVar(value='0')
statfe4 = tk.StringVar(value='0')

# Перо
selectmainstatti = tk.StringVar(value=STAT_TI[0])
selectstatti1 = tk.StringVar(value=STAT[0])
selectstatti2 = tk.StringVar(value=STAT[1])
selectstatti3 = tk.StringVar(value=STAT[6])
selectstatti4 = tk.StringVar(value=STAT[9])
statti1 = tk.StringVar(value='0')
statti2 = tk.StringVar(value='0')
statti3 = tk.StringVar(value='0')
statti4 = tk.StringVar(value='0')

# Кубок
selectmainstatgo = tk.StringVar(value=STAT_GO[0])
selectstatgo1 = tk.StringVar(value=STAT[0])
selectstatgo2 = tk.StringVar(value=STAT[1])
selectstatgo3 = tk.StringVar(value=STAT[6])
selectstatgo4 = tk.StringVar(value=STAT[9])
statgo1 = tk.StringVar(value='0')
statgo2 = tk.StringVar(value='0')
statgo3 = tk.StringVar(value='0')
statgo4 = tk.StringVar(value='0')

# Шапка
selectmainstathe = tk.StringVar(value=STAT_HE[0])
selectstathe1 = tk.StringVar(value=STAT[3])
selectstathe2 = tk.StringVar(value=STAT[1])
selectstathe3 = tk.StringVar(value=STAT[6])
selectstathe4 = tk.StringVar(value=STAT[9])
stathe1 = tk.StringVar(value='0')
stathe2 = tk.StringVar(value='0')
stathe3 = tk.StringVar(value='0')
stathe4 = tk.StringVar(value='0')

# Создание интерактивных элементов цветка
flowertext1 = ttk.Label(window, text='Цветок', font=FONT)
flowertext2 = ttk.Label(window, text='Основной стат ХП', font=FONT)
flowertext3 = ttk.Label(window, text='ХП 4780', font=FONT)
flowerbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl1,
                          font=FONT)
flower1 = ttk.Entry(window, font=FONT, textvariable=statfl1)
flowerbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl2,
                          font=FONT)
flower2 = ttk.Entry(window, font=FONT, textvariable=statfl2)
flowerbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl3,
                          font=FONT)
flower3 = ttk.Entry(window, font=FONT, textvariable=statfl3)
flowerbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatfl4,
                          font=FONT)
flower4 = ttk.Entry(window, font=FONT, textvariable=statfl4)

# Создание интерактивных элементов пера
feathertext1 = ttk.Label(window, text='Перо', font=FONT)
feathertext2 = ttk.Label(window, text='Основной стат АТК', font=FONT)
feathertext3 = ttk.Label(window, text='АТК 311', font=FONT)
featherbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe1,
                           font=FONT)
feather1 = ttk.Entry(window, font=FONT, textvariable=statfe1)
featherbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe2,
                           font=FONT)
feather2 = ttk.Entry(window, font=FONT, textvariable=statfe2)
featherbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe3,
                           font=FONT)
feather3 = ttk.Entry(window, font=FONT, textvariable=statfe3)
featherbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatfe4,
                           font=FONT)
feather4 = ttk.Entry(window, font=FONT, textvariable=statfe4)

# Создание интерактивных элементов часов
timepiecetext1 = ttk.Label(window, text='Часы', font=FONT)
timepiecetext2 = ttk.Label(window, text='Основной стат', font=FONT)
timepiecemain = ttk.Combobox(window, values=STAT_TI,
                             textvariable=selectmainstatti, justify='center',
                             font=FONT)
timepiecebox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatti1,
                             font=FONT)
timepiece1 = ttk.Entry(window, font=FONT, textvariable=statti1)
timepiecebox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatti2,
                             font=FONT)
timepiece2 = ttk.Entry(window, font=FONT, textvariable=statti2)
timepiecebox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatti3,
                             font=FONT)
timepiece3 = ttk.Entry(window, font=FONT, textvariable=statti3)
timepiecebox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatti4,
                             font=FONT)
timepiece4 = ttk.Entry(window, font=FONT, textvariable=statti4)

# Создание интерактивных элементов кубка
goblettext1 = ttk.Label(window, text='Кубок', font=FONT)
goblettext2 = ttk.Label(window, text='Основной стат', font=FONT)
gobletmain = ttk.Combobox(window, values=STAT_GO, textvariable=selectmainstatgo,
                          justify='center', font=FONT)
gobletbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo1,
                          font=FONT)
goblet1 = ttk.Entry(window, font=FONT, textvariable=statgo1)
gobletbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo2,
                          font=FONT)
goblet2 = ttk.Entry(window, font=FONT, textvariable=statgo2)
gobletbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo3,
                          font=FONT)
goblet3 = ttk.Entry(window, font=FONT, textvariable=statgo3)
gobletbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstatgo4,
                          font=FONT)
goblet4 = ttk.Entry(window, font=FONT, textvariable=statgo4)

# Создание интерактивных элементов шапки
headgeartext1 = ttk.Label(window, text='Шапка', font=FONT)
headgeartext2 = ttk.Label(window, text='Основной стат', font=FONT)
headgearmain = ttk.Combobox(window, values=STAT_HE,
                            textvariable=selectmainstathe, justify='center',
                            font=FONT)
headgearbox1 = ttk.Combobox(window, values=STAT, textvariable=selectstathe1,
                            font=FONT)
headgear1 = ttk.Entry(window, font=FONT, textvariable=stathe1)
headgearbox2 = ttk.Combobox(window, values=STAT, textvariable=selectstathe2,
                            font=FONT)
headgear2 = ttk.Entry(window, font=FONT, textvariable=stathe2)
headgearbox3 = ttk.Combobox(window, values=STAT, textvariable=selectstathe3,
                            font=FONT)
headgear3 = ttk.Entry(window, font=FONT, textvariable=stathe3)
headgearbox4 = ttk.Combobox(window, values=STAT, textvariable=selectstathe4,
                            font=FONT)
headgear4 = ttk.Entry(window, font=FONT, textvariable=stathe4)

# Функция подсчёта характеристик


def clicked():
    if percbox.get() == 'Не выбрано':
        messagebox.showerror("Ошибка", "Сначала выберите персонажа")
        return
    if weapbox.get() == 'Не выбрано':
        messagebox.showerror("Ошибка", "Сначала выберите оружие")
        return
    stat_dict = {'ХП': selected_perc.hp_base, 'ХП%': selected_perc.hp_perc,
                 'АТК': selected_perc.atk_base+selected_perc.weapon.weapon_atk,
                 'АТК%': selected_perc.atk_perc,
                 'КШ': selected_perc.cr_base, 'КУ': selected_perc.cd_base,
                 'МС': selected_perc.em, 'ВЭ': selected_perc.er,
                 'ЗАЩ': selected_perc.df_base, 'ЗАЩ%': selected_perc.df_perc,
                 'БОНУСЛЕЧ': selected_perc.heal,
                 'БОНУСПИРО': selected_perc.pyro_dmg_base,
                 'БОНУСКРИО': selected_perc.cryo_dmg_base,
                 'БОНУСАНЕМО': selected_perc.anemo_dmg_base,
                 'БОНУСГЕО': selected_perc.geo_dmg_base,
                 'БОНУСЭЛЕКТРО': selected_perc.electro_dmg_base,
                 'БОНУСДЕНДРО': selected_perc.dendro_dmg_base,
                 'БОНУСГИДРО': selected_perc.hydro_dmg_base,
                 'БОНУСФИЗ': selected_perc.phis_dmg_base}

    for i, j in zip([flowerbox1, flowerbox2, flowerbox3, flowerbox4,
                     featherbox1, featherbox2, featherbox3, featherbox4,
                     timepiecebox1, timepiecebox2, timepiecebox3,
                     timepiecebox4,
                     gobletbox1, gobletbox2, gobletbox3, gobletbox4,
                     headgearbox1, headgearbox2, headgearbox3, headgearbox4],
                    [flower1, flower2, flower3, flower4,
                     feather1, feather2, feather3, feather4,
                     timepiece1, timepiece2, timepiece3, timepiece4,
                     goblet1, goblet2, goblet3, goblet4,
                     headgear1, headgear2, headgear3, headgear4]):
        if j.get().replace(".", "", 1).isdigit() or j.get().replace(",", "",1
                                                                    ).isdigit():
            stat_dict[i.get()] += float(j.get().replace(",", ".",1))
        else:
            messagebox.showerror("Ошибка", "Введенные данные - не число")
            return
    stat_dict[timepiecemain.get().split()[0]] +=\
        float(timepiecemain.get().split()[1])
    stat_dict[gobletmain.get().split()[0]] +=\
        float(gobletmain.get().split()[1])
    stat_dict[headgearmain.get().split()[0]] +=\
        float(headgearmain.get().split()[1])
    stat_dict[selected_perc.weapon.second_stat] +=\
        selected_perc.weapon.weapon_second_stat
    stat_dict['ХП'] += 4780
    stat_dict['АТК'] += 311
    stat_dict['ХП'] += round(selected_perc.hp_base * (stat_dict['ХП%']/100-1),
                             1)
    stat_dict['АТК'] +=\
        round((selected_perc.atk_base+selected_perc.weapon.weapon_atk) *
              (stat_dict['АТК%'] / 100-1), 1)
    stat_dict['ЗАЩ'] +=\
        round(selected_perc.df_base * (stat_dict['ЗАЩ%'] / 100-1), 1)
    messagebox.showinfo("Итог подсчёта",
                        f'Ваша сборка оптимальна на  {None} % \n'
                        f'ХП {stat_dict["ХП"]}\n'
                        f'АТК {stat_dict["АТК"]}\n'
                        f'ЗАЩ {stat_dict["ЗАЩ"]}\n'
                        f'МС {stat_dict["МС"]}\n'
                        f'ВЭ {stat_dict["ВЭ"]}\n'
                        f'БОНУС ЛЕЧ {stat_dict["БОНУСЛЕЧ"]}\n'
                        f'БОНУС ПИРО {stat_dict["БОНУСПИРО"]}\n'
                        f'БОНУС КРИО {stat_dict["БОНУСКРИО"]}\n'
                        f'БОНУС АНЕМО {stat_dict["БОНУСАНЕМО"]}\n'
                        f'БОНУС ГЕО {stat_dict["БОНУСГЕО"]}\n'
                        f'БОНУС ЭЛЕКТРО {stat_dict["БОНУСЭЛЕКТРО"]}\n'
                        f'БОНУС ДЕНДРО {stat_dict["БОНУСДЕНДРО"]}\n'
                        f'БОНУС ГИДРО {stat_dict["БОНУСГИДРО"]}\n'
                        f'БОНУС ФИЗ {stat_dict["БОНУСФИЗ"]}\n')


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
# Кнопка вызова функции подсчета общих характеристик
button.grid(column=2, row=16, padx=20, pady=10)

# Картинка персонажа по умолчанию
img = Image.open("white.png")
img = ImageTk.PhotoImage(img.resize((150,150)))
panel = ttk.Label(window, image=img)
panel.grid(column=1, row=1, padx=20, pady=10)

window.mainloop()  # бесконечный цикл ожидания
