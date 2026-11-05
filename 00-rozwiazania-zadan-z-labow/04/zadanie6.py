def zamowienie(*kawy, **uwagi):
    print(f"Kawy: {", ".join(kawy)}")

    for uwaga in uwagi:
        print(f"{uwaga}: {uwagi[uwaga]}")
    

zamowienie("latte", "espresso", "mocha", mleko="owsiane", cukier=1)