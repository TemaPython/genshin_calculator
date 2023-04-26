from classes import *
from tkinter import *
from tkinter import ttk
window = Tk()
window.title('Калькулятор артефактов')
window.geometry('1100x750')

perc_dict = {"Ху Тао":HuTao()}
weapon_dict = {"Коршун":Korshun, "Хома":Homa}

def selected_perc(event):
    # получаем выделенный элемент
    selected_perc = list_perc.get()
    global p
    p = perc_dict[selected_perc]

def selected_weapon(event):
    # получаем выделенный элемент
    selected_weapon = list_weapon.get()
    w = weapon_dict[selected_weapon]
    p.give_weapon(w)
    print(p.weapon)

def click_button_after_perc():
    weapon = ['Коршун', 'Хома']

    l2.pack(anchor=N, padx=6, pady=20)

    global list_weapon
    list_weapon = ttk.Combobox(textvariable=weapon, values=weapon, state="readonly")
    list_weapon.pack(anchor=N, padx=6, pady=6)
    list_weapon.bind("<<ComboboxSelected>>", selected_weapon)

    ttk.Button(text="Далее", command=click_button_after_weapon).pack()

def click_button_after_weapon():
    stat = ['КУ', 'КШ', 'АТК', 'АТК%', 'ХП', 'ХП%', 'МС', 'ЗАЩ', 'ЗАЩ%', 'ВЭ']
    stat_t = ['АТК%','ХП%', 'МС','ЗАЩ%', 'ВЭ']
    stat_g = ['АТК%', 'ХП%', 'МС', 'ЗАЩ%', 'БОНУС ПИРО','БОНУС КРИО','БОНУС АНЕМО','БОНУС ГЕО','БОНУС ЭЛЕКТРО',
              'БОНУС ДЕНДРО','БОНУС ГИДРО','БОНУС ФИЗ',]
    stat_h = ['КУ', 'КШ','АТК%','ХП%', 'МС', 'ЗАЩ%', 'БОНУС ЛЕЧ']
    l3.pack(anchor=N, padx=6, pady=20)

    l_art1.place(x=80, y=320)
    l_art1_main1.place(x=35, y=350)
    l_art1_main2.place(x=75, y=380)
    global list_stat_fl1, list_stat_fl2, list_stat_fl3, list_stat_fl4
    global entry_fl1, entry_fl2, entry_fl3, entry_fl4
    list_stat_fl1 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_fl1 = ttk.Entry()
    list_stat_fl2 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_fl2 = ttk.Entry()
    list_stat_fl3 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_fl3 = ttk.Entry()
    list_stat_fl4 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_fl4 = ttk.Entry()
    list_stat_fl1.place(x=50, y=410)
    entry_fl1.place(x=50, y=440)
    list_stat_fl2.place(x=50, y=470)
    entry_fl2.place(x=50, y=500)
    list_stat_fl3.place(x=50, y=530)
    entry_fl3.place(x=50, y=560)
    list_stat_fl4.place(x=50, y=590)
    entry_fl4.place(x=50, y=620)


    l_art2.place(x=320, y=320)
    l_art2_main1.place(x=250, y=350)
    l_art2_main2.place(x=300, y=380)
    global list_stat_ft1, list_stat_ft2, list_stat_ft3, list_stat_ft4
    global entry_ft1, entry_ft2, entry_ft3, entry_ft4
    list_stat_ft1 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_ft1 = ttk.Entry()
    list_stat_ft2 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_ft2 = ttk.Entry()
    list_stat_ft3 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_ft3 = ttk.Entry()
    list_stat_ft4 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_ft4 = ttk.Entry()
    list_stat_ft1.place(x=275, y=410)
    entry_ft1.place(x=275, y=440)
    list_stat_ft2.place(x=275, y=470)
    entry_ft2.place(x=275, y=500)
    list_stat_ft3.place(x=275, y=530)
    entry_ft3.place(x=275, y=560)
    list_stat_ft4.place(x=275, y=590)
    entry_ft4.place(x=275, y=620)

    l_art3.place(x=535, y=320)
    list_stat_t_main = ttk.Combobox(exportselection=0, values=stat_t, state="readonly")
    entry_t_main = ttk.Entry()
    list_stat_t_main.place(x=490, y=350)
    entry_t_main.place(x=490, y=380)
    global list_stat_t1, list_stat_t2, list_stat_t3, list_stat_t4
    global entry_t1, entry_t2, entry_t3, entry_t4
    list_stat_t1 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_t1 = ttk.Entry()
    list_stat_t2 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_t2 = ttk.Entry()
    list_stat_t3 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_t3 = ttk.Entry()
    list_stat_t4 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_t4 = ttk.Entry()
    list_stat_t1.place(x=490, y=410)
    entry_t1.place(x=490, y=440)
    list_stat_t2.place(x=490, y=470)
    entry_t2.place(x=490, y=500)
    list_stat_t3.place(x=490, y=530)
    entry_t3.place(x=490, y=560)
    list_stat_t4.place(x=490, y=590)
    entry_t4.place(x=490, y=620)

    l_art4.place(x=720, y=320)
    list_stat_g_main = ttk.Combobox(exportselection=0, values=stat_g, state="readonly")
    entry_g_main = ttk.Entry()
    list_stat_g_main.place(x=690, y=350)
    entry_g_main.place(x=690, y=380)
    global list_stat_g1, list_stat_g2, list_stat_g3, list_stat_g4
    global entry_g1, entry_g2, entry_g3, entry_g4
    list_stat_g1 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_g1 = ttk.Entry()
    list_stat_g2 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_g2 = ttk.Entry()
    list_stat_g3 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_g3 = ttk.Entry()
    list_stat_g4 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_g4 = ttk.Entry()
    list_stat_g1.place(x=690, y=410)
    entry_g1.place(x=690, y=440)
    list_stat_g2.place(x=690, y=470)
    entry_g2.place(x=690, y=500)
    list_stat_g3.place(x=690, y=530)
    entry_g3.place(x=690, y=560)
    list_stat_g4.place(x=690, y=590)
    entry_g4.place(x=690, y=620)

    l_art5.place(x=950, y=320)
    list_stat_h_main = ttk.Combobox(exportselection=0, values=stat_h, state="readonly")
    entry_h_main = ttk.Entry()
    list_stat_h_main.place(x=690, y=350)
    entry_h_main.place(x=690, y=380)
    global list_stat_h1, list_stat_h2, list_stat_h3, list_stat_h4
    global entry_h1, entry_h2, entry_h3, entry_h4
    list_stat_h1 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_h1 = ttk.Entry()
    list_stat_h2 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_h2 = ttk.Entry()
    list_stat_h3 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_h3 = ttk.Entry()
    list_stat_h4 = ttk.Combobox(exportselection=0, values=stat, state="readonly")
    entry_h4 = ttk.Entry()
    list_stat_h1.place(x=690, y=410)
    entry_h1.place(x=690, y=440)
    list_stat_h2.place(x=690, y=470)
    entry_h2.place(x=690, y=500)
    list_stat_h3.place(x=690, y=530)
    entry_h3.place(x=690, y=560)
    list_stat_h4.place(x=690, y=590)
    entry_h4.place(x=690, y=620)

    ttk.Button(text="Далее", command=test_art).place(x=400, y=700)
def test_art():
    print(list_stat_fl1.get(), entry_fl1.get())
    print(list_stat_fl2.get(), entry_fl2.get())
    print(list_stat_fl3.get(), entry_fl3.get())
    print(list_stat_fl4.get(), entry_fl4.get())


perc = ['Не выбрано',"Ху Тао"]

# блок надписей
l1 = ttk.Label(text='Выберите персонажа', font=50)
l2 = ttk.Label(text='Выберите оружие', font=50)
l3 = ttk.Label(text='Выберите статы артфеактов', font=50)
l_art1 = ttk.Label(text='Цветок', font=30)
l_art1_main1 = ttk.Label(text='Основной стат - ХП', font=10)
l_art1_main2 = ttk.Label(text='ХП 4780', font=10)
l_art2 = ttk.Label(text='Перо', font=30)
l_art2_main1 = ttk.Label(text='Основной стат - АТК', font=10)
l_art2_main2 = ttk.Label(text='АТК 311', font=10)
l_art3 = ttk.Label(text='Часы', font=30)
l_art4 = ttk.Label(text='Кубок', font=30)
l_art5 = ttk.Label(text='Шапка', font=30)
l1.pack(anchor=N, padx=6, pady=20)

list_perc = ttk.Combobox(textvariable=perc, values=perc, state="readonly")
list_perc.pack(anchor=N, padx=6, pady=6)
list_perc.bind("<<ComboboxSelected>>", selected_perc)



ttk.Button(text="Далее", command=click_button_after_perc).pack()

window.mainloop()
