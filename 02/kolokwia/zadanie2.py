def podpis_zeszytu(przedmiot, imie, nazwisko, klasa="1a", **dodatkowe_informacje):
    print(przedmiot.upper())
    print(f"{imie} {nazwisko}")
    print(klasa)

    for x in dodatkowe_informacje:
        print(f"{x}: {dodatkowe_informacje[x]}")

podpis_zeszytu("religia", "Ola", "Nowak", szkola="SP 5")