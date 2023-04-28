class Person(object):
    '''
    Класс Person родительский класс с методами:
    give_weapon - выдать оружие персонажу (атрибуту weapon присваивается
    объект класса оружия)
    give_artifact - выдать персонажу набор артефактов (от 1 до 5)(аттрибутам
    flower, feather, timepiece, goblet, headgear присваивает соответственный
    объект класса артефакта)
    '''

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
    '''
    Класс цветок, имеет основную характеристику hp и 4 дополнительных любых,
    кроме основной характеристики
    '''

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
    '''
    Класс перо, имеет основную характеристику atk и 4 дополнительных любых,
    кроме основной характеристики
    '''

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
    '''
    Класс часы, имеет основную характеристику, которая указывается
    при вызове функции (atk_perc, hp_perc, em, df_perc, er)
    и 4 дополнительных любых, кроме основной характеристики
    '''

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
    '''
    Класс кубок, имеет основную характеристику, которая указывается
    при вызове функции (atk_perc, hp_perc, em, df_perc, pyro_dmg, cryo_dmg,
    hydro_dmg, electro_dmg, anemo_dmg, geo_dmg, phis_dmg)
    и 4 дополнительных любых, кроме основной характеристики
    '''

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
        elif main_stat == 'electro_dmg':
            self.electro_dmg = 46.6
        elif main_stat == 'anemo_dmg':
            self.anemo_dmg = 46.6
        elif main_stat == 'geo_dmg':
            self.geo_dmg = 46.6
        elif main_stat == 'phis_dmg':
            self.phis_dmg = 46.6


class Headgear:
    '''
    Класс шапка, имеет основную характеристику, которая указывается
    при вызове функции (atk_perc, hp_perc, em, cr, cd, heal)
    и 4 дополнительных любых, кроме основной характеристики
    '''

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


# Классы персонжаей с родительским Person
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
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 28.8
    phis_dmg_base = 0
    weapon = None

class TravelerGeo(Person):
    element = 'geo'
    weapon_type = 'sword'
    hp_base = 10122
    atk_base = 245.52
    df_base = 635
    cd_base = 50
    cr_base = 5
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
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
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
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
    df_base = 965.9
    cd_base = 50
    cr_base = 5
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
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
    heal = 0
    em = 0
    er = 26.7
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
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
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 28.8
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
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
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
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 24
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
    heal = 0
    em = 0
    er = 0
    pyro_dmg_base = 0
    cryo_dmg_base = 0
    hydro_dmg_base = 0
    electro_dmg_base = 0
    anemo_dmg_base = 0
    geo_dmg_base = 24
    phis_dmg_base = 0
    weapon = None



# Классы оружия: (присутствуют оружия от 3 до 5 звезд)
# У каждого оружия есть свои атрибуты:
# weapon_type - тип оружия (sword, claymore, polearm, catalyst, bow)
# weapon_atk - значение силы атаки на 90 ур
# second_stat - определяет какой дополнительный стат есть у оржия 
# (hp%, atk&, kr, kd, df, em, er, phis_dmg)
# weapon_second_stat - значение дополнительного стата оружия

class Homa:
    weapon_type = 'polearm'
    weapon_atk = 608
    second_stat = 'cd'
    weapon_second_stat = 66.2


class Korshun:
    weapon_type = 'polearm'
    weapon_atk = 674
    second_stat = 'cr'
    weapon_second_stat = 22.4