import copy
from time import time
from functools import lru_cache


class Model:
    def __init__(self):
        self._anagrammi = set()

    def calcola_anagrammi(self, parola):
        self._anagrammi = set()
        self.ricorsione("", "".join(sorted(parola)))
    #    self.ricorsione_list([], parola)
        return self._anagrammi

    @lru_cache(maxsize=None)
    def ricorsione(self, parziale, lettere_rimanenti):
        # caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(parziale)
            return
        # caso non terminale, dobbiamo provare ad aggiungere una lettera per volta e andare avanti nella ricorsione
        else:
            for i in range(len(lettere_rimanenti)):
                parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[ :i] + lettere_rimanenti[i+1 : ]
                self.ricorsione(parziale, nuove_lettere_rimanenti)
                parziale = parziale[: -1]

    def ricorsione_list(self, parziale, lettere_rimanenti):
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(copy.deepcopy(parziale))
            return
        # caso non terminale, dobbiamo provare ad aggiungere una lettera per volta e andare avanti nella ricorsione
        else:
            for i in range(len(lettere_rimanenti)):
                parziale.append(lettere_rimanenti[i])
                nuove_lettere_rimanenti = lettere_rimanenti[ :i] + lettere_rimanenti[i+1 : ]
                self.ricorsione_list(parziale, nuove_lettere_rimanenti)
                parziale.pop()



if __name__ == "__main__":
    model = Model()
    start_time = time()
    print(model.calcola_anagrammi("qwerty"))
    end_time = time()
    print(end_time - start_time)
