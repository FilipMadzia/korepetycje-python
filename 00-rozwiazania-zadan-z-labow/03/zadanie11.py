def ramka(text, znak="*"):
    print(znak * (len(text) + 4))
    print(f"* {text} *")
    print(znak * (len(text) + 4))

ramka("Hello, world!")
