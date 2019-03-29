def skautska_hra():
    from random import choice

    key_ot = ["Kdo? ", "Kdy? ", "S kým ", "Co dělali ", "Kde? ", "Proč? "]

    slovník_hra = dict([(key, []) for key in key_ot])


    print("Odpovídej na otázky dokud budeš chtít, pokud neodpovíš, přeskočí hra na další otázku, nebo se ukončí ")

    for i in key_ot:
        while True:
            odpoved = input(i)
            if not odpoved:
                break
            else:
                if i in slovník_hra.keys():
                    slovník_hra[i].extend([odpoved])
    veta = ''

    for i in key_ot:
        veta = veta + choice(slovník_hra[i]) + ' '

    print(veta)
skautska_hra()
