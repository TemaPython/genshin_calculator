"""
Модуль classes предназначен для хранения основных классов и базы данных
 персонажей и оружия. Он состоит из блоков:
- Родительский класс Person с методами выдачи оружия и артефактов
 (give_weapon и give_artifact соответственно)
- Классы артефактов (Flower, Feather, Timepiece, Goblet и Headgear)
 хранят введенные характеристики
- Классы персонажей, распределенные по принципу типа оружия
(sword, claymore, polearm, catalyst, bow) и содержат базовые характеристики
- Классы оружия, распределенные по принципу типа оружия
 (sword, claymore, polearm, catalyst, bow) и содержат базовые характеристики
"""


class Person(object):
    """
    Класс Person родительский класс с методами:
    give_weapon - выдать оружие персонажу (атрибуту weapon присваивается
    объект класса оружия)
    give_artifact - выдать персонажу набор артефактов (от 1 до 5)(аттрибутам
    flower, feather, timepiece, goblet, headgear присваивает соответственный
    объект класса артефакта)
    """

    def give_weapon(self, Weapon):
        if self.weapon_type == Weapon.weapon_type:
            self.weapon = Weapon

    def give_artifact(self, Flower=None, Feather=None, Timepiece=None,
                      Goblet=None, Headgear=None):
        self.flower = Flower
        self.feather = Feather
        self.timepiece = Timepiece
        self.goblet = Goblet
        self.headgear = Headgear


# Классы артефактов

class Flower:
    """
    Класс цветок, имеет основную характеристику hp и 4 дополнительных любых,
    кроме основной характеристики
    """

    def __init__(self, cd=0, cr=0, atk=0, atk_perc=0,
                 hp_perc=0, em=0, df=0, df_perc=0, er=0):
        self.hp = 4780
        self.cd = cd
        self.cr = cr
        self.atk = atk
        self.atk_perc = atk_perc
        self.hp_perc = hp_perc
        self.em = em
        self.df = df
        self.df_perc = df_perc
        self.er = er


class Feather:
    """
    Класс перо, имеет основную характеристику atk и 4 дополнительных любых,
    кроме основной характеристики
    """

    def __init__(self, hp=0, cd=0, cr=0, atk_perc=0,
                 hp_perc=0, em=0, df=0, df_perc=0, er=0):
        self.hp = hp
        self.cd = cd
        self.cr = cr
        self.atk = 311
        self.atk_perc = atk_perc
        self.hp_perc = hp_perc
        self.em = em
        self.df = df
        self.df_perc = df_perc
        self.er = er


class Timepiece:
    """
    Класс часы, имеет основную характеристику, которая указывается
    при вызове функции (atk_perc, hp_perc, em, df_perc, er)
    и 4 дополнительных любых, кроме основной характеристики
    """

    def __init__(self, main_stat: str, hp=0, cd=0, cr=0, atk=0, atk_perc=0,
                 hp_perc=0, em=0, df=0, df_perc=0, er=0):
        self.hp = hp
        self.cd = cd
        self.cr = cr
        self.atk = atk
        self.atk_perc = atk_perc
        self.hp_perc = hp_perc
        self.em = em
        self.df = df
        self.df_perc = df_perc
        self.er = er
        self.main_stat = main_stat

        if main_stat == 'atk_perc':
            self.atk_perc = 46.6
        elif main_stat == 'hp_perc':
            self.hp_perc = 46.6
        elif main_stat == 'em':
            self.em = 187
        elif main_stat == 'df_perc':
            self.df_perc = 58.3
        elif main_stat == 'er':
            self.er = 51.8


class Goblet:
    """
    Класс кубок, имеет основную характеристику, которая указывается
    при вызове функции (atk_perc, hp_perc, em, df_perc, pyro_dmg, cryo_dmg,
    hydro_dmg, dendro_dmg, electro_dmg, anemo_dmg, geo_dmg, phis_dmg)
    и 4 дополнительных любых, кроме основной характеристики
    """

    def __init__(self, main_stat: str, hp=0, cd=0, cr=0, atk=0, atk_perc=0,
                 hp_perc=0, em=0, df=0, df_perc=0, er=0):
        self.hp = hp
        self.cd = cd
        self.cr = cr
        self.atk = atk
        self.atk_perc = atk_perc
        self.hp_perc = hp_perc
        self.em = em
        self.df = df
        self.df_perc = df_perc
        self.er = er
        self.main_stat = main_stat

        if main_stat == 'atk_perc':
            self.atk_perc = 46.6
        elif main_stat == 'hp_perc':
            self.hp_perc = 46.6
        elif main_stat == 'em':
            self.em = 187
        elif main_stat == 'df_perc':
            self.df_perc = 58.3
        elif main_stat == 'pyro_dmg':
            self.pyro_dmg = 46.6
        elif main_stat == 'cryo_dmg':
            self.cryo_dmg = 46.6
        elif main_stat == 'hydro_dmg':
            self.hydro_dmg = 46.6
        elif main_stat == 'dendro_dmg':
            self.dendro_dmg = 46.6
        elif main_stat == 'electro_dmg':
            self.electro_dmg = 46.6
        elif main_stat == 'anemo_dmg':
            self.anemo_dmg = 46.6
        elif main_stat == 'geo_dmg':
            self.geo_dmg = 46.6
        elif main_stat == 'phis_dmg':
            self.phis_dmg = 46.6


class Headgear:
    """
    Класс шапка, имеет основную характеристику, которая указывается
    при вызове функции (atk_perc, hp_perc, em, cr, cd, heal)
    и 4 дополнительных любых, кроме основной характеристики
    """

    def __init__(self, main_stat: str, hp=0, cd=0, cr=0, atk=0, atk_perc=0,
                 hp_perc=0, em=0, df=0, df_perc=0, er=0):
        self.hp = hp
        self.cd = cd
        self.cr = cr
        self.atk = atk
        self.atk_perc = atk_perc
        self.hp_perc = hp_perc
        self.em = em
        self.df = df
        self.df_perc = df_perc
        self.er = er
        self.main_stat = main_stat

        if main_stat == 'atk_perc':
            self.atk_perc = 46.6
        elif main_stat == 'hp_perc':
            self.hp_perc = 46.6
        elif main_stat == 'em':
            self.em = 187
        elif main_stat == 'df_perc':
            self.df_perc = 58.3
        elif main_stat == 'cd':
            self.cd = 62.2
        elif main_stat == 'cr':
            self.cr = 31.1
        elif main_stat == 'heal':
            self.heal = 35.9


# Классы персонажей с родительским Person
# У каждого персонажа есть атрибуты:
# element - стихия
# weapon_type - тип оружия (sword, claymore, polearm, catalyst, bow)
# hp_base - базовое значение здоровья на 90 ур
# atk_base - базовое значение силы атаки на 90 ур
# df_base - базовое значение защиты на 90 ур
# cd_base - базовое значение крит урона на 90 ур
# cr_base - базовое значение крит шанса на 90 ур
# heal - базовое значение бонуса лечения на 90 ур
# em - базовое значение мастерства стихий на 90 ур
# er - базовое значение восстановления энергии на 90 ур
# базовые значения бонуса элементального урона
# pyro_dmg_base
# cryo_dmg_base
# hydro_dmg_base
# dendro_dmg_base
# electro_dmg_base
# anemo_dmg_base
# geo_dmg_base
# phis_dmg_base
# weapon - присвоенное оружие (по умолчанию None)

# Одноручники
class Albedo(Person):
    element = 'geo'
    weapon_type = 'sword'
    hp_base = 12296
    atk_base = 233
    df_base = 815
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 28.8
    phis_dmg_base = 0
    weapon = None


class TravelerGeo(Person):
    element = 'geo'
    weapon_type = 'sword'
    hp_base = 10122
    atk_base = 198
    df_base = 635
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Alhaitham(Person):
    element = 'dendro'
    weapon_type = 'sword'
    hp_base = 12410
    atk_base = 292
    df_base = 727
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 28.8
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class TravelerDendro(Person):
    element = 'dendro'
    weapon_type = 'sword'
    hp_base = 10122
    atk_base = 198
    df_base = 635
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Kaeya(Person):
    element = 'cryo'
    weapon_type = 'sword'
    hp_base = 10830
    atk_base = 208
    df_base = 737
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 126.7
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class KamisatoAyaka(Person):
    element = 'cryo'
    weapon_type = 'sword'
    hp_base = 11954
    atk_base = 318
    df_base = 729
    cd_base = 88.4
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Layla(Person):
    element = 'cryo'
    weapon_type = 'sword'
    hp_base = 10324
    atk_base = 202
    df_base = 610
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Qiqi(Person):
    element = 'cryo'
    weapon_type = 'sword'
    hp_base = 11499
    atk_base = 267
    df_base = 857
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 22.2
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Bennett(Person):
    element = 'pyro'
    weapon_type = 'sword'
    hp_base = 11539
    atk_base = 178
    df_base = 718
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 126.7
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class KamisatoAyato(Person):
    element = 'hydro'
    weapon_type = 'sword'
    hp_base = 12751
    atk_base = 278
    df_base = 715
    cd_base = 88.4
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Nilou(Person):
    element = 'hydro'
    weapon_type = 'sword'
    hp_base = 14117
    atk_base = 214
    df_base = 677
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 128.8
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Xingqiu(Person):
    element = 'hydro'
    weapon_type = 'sword'
    hp_base = 9514
    atk_base = 188
    df_base = 705
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Keqing(Person):
    element = 'electro'
    weapon_type = 'sword'
    hp_base = 12182
    atk_base = 300
    df_base = 743
    cd_base = 88.4
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class KukiShinobu(Person):
    element = 'electro'
    weapon_type = 'sword'
    hp_base = 11438
    atk_base = 198
    df_base = 699
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class TravelerElectro(Person):
    element = 'electro'
    weapon_type = 'sword'
    hp_base = 10122
    atk_base = 198
    df_base = 635
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Jean(Person):
    element = 'anemo'
    weapon_type = 'sword'
    hp_base = 13662
    atk_base = 222
    df_base = 715
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 22.2
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class KaedeharaKazuha(Person):
    element = 'anemo'
    weapon_type = 'sword'
    hp_base = 12410
    atk_base = 276
    df_base = 750
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 115
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class TravelerAnemo(Person):
    element = 'anemo'
    weapon_type = 'sword'
    hp_base = 10122
    atk_base = 198
    df_base = 635
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None
# Двуручники


class AratakiItto(Person):
    element = 'geo'
    weapon_type = 'claymore'
    hp_base = 11954
    atk_base = 211
    df_base = 892
    cd_base = 50
    cr_base = 24.2
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Noelle(Person):
    element = 'geo'
    weapon_type = 'claymore'
    hp_base = 11235
    atk_base = 178
    df_base = 743
    cd_base = 50
    cr_base = 5
    df_perc = 130
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Kaveh(Person):
    element = 'dendro'
    weapon_type = 'claymore'
    hp_base = 11962
    atk_base = 234
    df_base = 751
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 96
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Eula(Person):
    element = 'cryo'
    weapon_type = 'claymore'
    hp_base = 12296
    atk_base = 318
    df_base = 698
    cd_base = 88.4
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Chongyun(Person):
    element = 'cryo'
    weapon_type = 'claymore'
    hp_base = 10223
    atk_base = 208
    df_base = 603
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Dehya(Person):
    element = 'pyro'
    weapon_type = 'claymore'
    hp_base = 14573
    atk_base = 247
    df_base = 584
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 128.8
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Diluc(Person):
    element = 'pyro'
    weapon_type = 'claymore'
    hp_base = 12068
    atk_base = 311
    df_base = 729
    cd_base = 50
    cr_base = 24.2
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Xinyan(Person):
    element = 'pyro'
    weapon_type = 'claymore'
    hp_base = 10425
    atk_base = 231
    df_base = 743
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Beidou(Person):
    element = 'electro'
    weapon_type = 'claymore'
    hp_base = 12146
    atk_base = 210
    df_base = 603
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 24
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Dori(Person):
    element = 'electro'
    weapon_type = 'claymore'
    hp_base = 11539
    atk_base = 208
    df_base = 673
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Razor(Person):
    element = 'electro'
    weapon_type = 'claymore'
    hp_base = 11134
    atk_base = 217
    df_base = 699
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 30
    weapon = None


class Sayu(Person):
    element = 'anemo'
    weapon_type = 'claymore'
    hp_base = 11033
    atk_base = 227
    df_base = 693
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 96
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None
# Копейщики


class YunJin(Person):
    element = 'geo'
    weapon_type = 'polearm'
    hp_base = 9919
    atk_base = 178
    df_base = 684
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 126.7
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Zhongli(Person):
    element = 'geo'
    weapon_type = 'polearm'
    hp_base = 13662
    atk_base = 233
    df_base = 686
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 28.8
    phis_dmg_base = 0
    weapon = None


class Yaoyao(Person):
    element = 'dendro'
    weapon_type = 'polearm'
    hp_base = 11438
    atk_base = 198
    df_base = 699
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Mika(Person):
    element = 'cryo'
    weapon_type = 'polearm'
    hp_base = 11640
    atk_base = 208
    df_base = 664
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Rosaria(Person):
    element = 'cryo'
    weapon_type = 'polearm'
    hp_base = 11438
    atk_base = 223
    df_base = 661
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Shenhe(Person):
    element = 'cryo'
    weapon_type = 'polearm'
    hp_base = 12080
    atk_base = 282
    df_base = 772
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 128.8
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Thoma(Person):
    element = 'pyro'
    weapon_type = 'polearm'
    hp_base = 9616
    atk_base = 188
    df_base = 699
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Xiangling(Person):
    element = 'pyro'
    weapon_type = 'polearm'
    hp_base = 10122
    atk_base = 210
    df_base = 623
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 96
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class HuTao(Person):
    element = 'pyro'
    weapon_type = 'polearm'
    hp_base = 14459
    atk_base = 99
    df_base = 815
    cd_base = 88.4
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Candace(Person):
    element = 'hydro'
    weapon_type = 'polearm'
    hp_base = 10122
    atk_base = 198
    df_base = 635
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Cyno(Person):
    element = 'electro'
    weapon_type = 'polearm'
    hp_base = 11613
    atk_base = 296
    df_base = 799
    cd_base = 88.4
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class RaidenShogun(Person):
    element = 'electro'
    weapon_type = 'polearm'
    hp_base = 12000
    atk_base = 314
    df_base = 734
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 132
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Xiao(Person):
    element = 'anemo'
    weapon_type = 'polearm'
    hp_base = 11840
    atk_base = 325
    df_base = 743
    cd_base = 50
    cr_base = 24.2
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None
# Каталисты


class Ningguang(Person):
    element = 'geo'
    weapon_type = 'catalyst'
    hp_base = 9110
    atk_base = 198
    df_base = 534
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 24
    phis_dmg_base = 0
    weapon = None


class Baizhu(Person):
    element = 'dendro'
    weapon_type = 'catalyst'
    hp_base = 13348
    atk_base = 193
    df_base = 500
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 128.8
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Nahida(Person):
    element = 'dendro'
    weapon_type = 'catalyst'
    hp_base = 9140
    atk_base = 278
    df_base = 586
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 115
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Klee(Person):
    element = 'pyro'
    weapon_type = 'catalyst'
    hp_base = 9563
    atk_base = 289
    df_base = 572
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 28.8
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Yanfei(Person):
    element = 'pyro'
    weapon_type = 'catalyst'
    hp_base = 8705
    atk_base = 223
    df_base = 546
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 24
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Barbara(Person):
    element = 'hydro'
    weapon_type = 'catalyst'
    hp_base = 9110
    atk_base = 148
    df_base = 623
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 124
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Mona(Person):
    element = 'hydro'
    weapon_type = 'catalyst'
    hp_base = 9677
    atk_base = 267
    df_base = 607
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 132
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class SangonomiyaKokomi(Person):
    element = 'hydro'
    weapon_type = 'catalyst'
    hp_base = 12524
    atk_base = 218
    df_base = 611
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 28.8
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Lisa(Person):
    element = 'electro'
    weapon_type = 'catalyst'
    hp_base = 8907
    atk_base = 215
    df_base = 534
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 96
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class YaeMiko(Person):
    element = 'electro'
    weapon_type = 'catalyst'
    hp_base = 9643
    atk_base = 316
    df_base = 529
    cd_base = 50
    cr_base = 24.2
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class ShikanoinHeizou(Person):
    element = 'anemo'
    weapon_type = 'catalyst'
    hp_base = 9919
    atk_base = 210
    df_base = 637
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 24
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Sucrose(Person):
    element = 'anemo'
    weapon_type = 'catalyst'
    hp_base = 9140
    atk_base = 278
    df_base = 586
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 24
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Wanderer(Person):
    element = 'anemo'
    weapon_type = 'catalyst'
    hp_base = 9450
    atk_base = 305
    df_base = 564
    cd_base = 50
    cr_base = 24.2
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None
# Лучники


class Gorou(Person):
    element = 'geo'
    weapon_type = 'bow'
    hp_base = 8907
    atk_base = 170
    df_base = 603
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 24
    phis_dmg_base = 0
    weapon = None


class Collei(Person):
    element = 'dendro'
    weapon_type = 'bow'
    hp_base = 9110
    atk_base = 186
    df_base = 559
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Tighnari(Person):
    element = 'dendro'
    weapon_type = 'bow'
    hp_base = 10087
    atk_base = 270
    df_base = 586
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 28.8
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Aloy(Person):
    element = 'cryo'
    weapon_type = 'bow'
    hp_base = 10133
    atk_base = 217
    df_base = 629
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 28.8
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Diona(Person):
    element = 'cryo'
    weapon_type = 'bow'
    hp_base = 8907
    atk_base = 198
    df_base = 559
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 24
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Ganyu(Person):
    element = 'cryo'
    weapon_type = 'bow'
    hp_base = 9108
    atk_base = 311
    df_base = 586
    cd_base = 88.3
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Amber(Person):
    element = 'pyro'
    weapon_type = 'bow'
    hp_base = 8806
    atk_base = 208
    df_base = 559
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Yoimiya(Person):
    element = 'pyro'
    weapon_type = 'bow'
    hp_base = 9450
    atk_base = 300
    df_base = 572
    cd_base = 50
    cr_base = 24.2
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Tartaglia(Person):
    element = 'hydro'
    weapon_type = 'bow'
    hp_base = 12182
    atk_base = 280
    df_base = 757
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 28.8
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Yelan(Person):
    element = 'hydro'
    weapon_type = 'bow'
    hp_base = 13434
    atk_base = 227
    df_base = 509
    cd_base = 50
    cr_base = 24.2
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Fischl(Person):
    element = 'electro'
    weapon_type = 'bow'
    hp_base = 8553
    atk_base = 227
    df_base = 553
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class KujouSara(Person):
    element = 'electro'
    weapon_type = 'bow'
    hp_base = 8907
    atk_base = 182
    df_base = 584
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Faruzan(Person):
    element = 'anemo'
    weapon_type = 'bow'
    hp_base = 8907
    atk_base = 183
    df_base = 584
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 124
    hp_perc = 100
    heal = 0
    em = 0
    er = 100
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None


class Venti(Person):
    element = 'anemo'
    weapon_type = 'bow'
    hp_base = 9791
    atk_base = 245
    df_base = 622
    cd_base = 50
    cr_base = 5
    df_perc = 100
    atk_perc = 100
    hp_perc = 100
    heal = 0
    em = 0
    er = 132
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    dendro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 0
    phis_dmg_base = 0
    weapon = None

# Классы оружия: (присутствуют оружия от 3 до 5 звезд)
# У каждого оружия есть свои атрибуты:
# weapon_type - тип оружия (sword, claymore, polearm, catalyst, bow)
# weapon_atk - значение силы атаки на 90 ур
# second_stat - определяет какой дополнительный стат есть у оржия 
# (hp%, atk&, kr, kd, df, em, er, phis_dmg)
# weapon_second_stat - значение дополнительного стата оружия

# Одноручные мечи


class AquilaFavonia:
    weapon_type = 'sword'
    weapon_atk = 674
    second_stat = 'БОНУСФИЗ'
    weapon_second_stat = 41.3
# Двуручные мечи


class BeaconOfTheReedSea:
    weapon_type = 'claymore'
    weapon_atk = 608
    second_stat = 'КШ'
    weapon_second_stat = 33.1
# Копья


class Homa:
    weapon_type = 'polearm'
    weapon_atk = 608
    second_stat = 'КУ'
    weapon_second_stat = 66.2


class Korshun:
    weapon_type = 'polearm'
    weapon_atk = 674
    second_stat = 'КШ'
    weapon_second_stat = 22.4

# Катализаторы


class AThousandFloatingDreams:
    weapon_type = 'catalyst'
    weapon_atk = 542
    second_stat = 'МС'
    weapon_second_stat = 265
# Луки


class AmosBow:
    weapon_type = 'bow'
    weapon_atk = 608
    second_stat = 'АТК%'
    weapon_second_stat = 49.6
