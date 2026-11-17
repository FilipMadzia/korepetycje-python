[Tutorial po polsku](https://www.youtube.com/watch?v=I1uOp-e03rw)

```py
tekst = "  #hello world   "
tekst = tekst.strip() # usuwa spacje po bokach tekstu

tekst.replace("world", "Rodion") # zamienia ciąg znaku w tekście
# #hello Rodion

if tekst[0] == "#": # sprawdza, czy tekst zaczyna się od #
    ...

tekst2 = "jakies zdanie kilka slow"
slowa = tekst2.split(" ") # tablica słów ["jakies", "zdanie", "kilka", "slow"]
z_powrotem = " ".join(slowa) # string z tablicy "jakies zdanie kilka slow"
```