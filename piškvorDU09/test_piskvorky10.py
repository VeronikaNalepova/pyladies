import pytest

from ai import tah_pocitace
from piskvorky import vyhodnot
from util import tah



def test_vyhodnot_vyhra_x():
    """
    Křížky vyhrály pole 10.
    """
    assert vyhodnot("xxx-------") == "x"
    assert vyhodnot("---xxx----") == "x"
    assert vyhodnot("-------xxx") == "x"
    assert vyhodnot("-xoxoxxxoo") == "x"
    assert vyhodnot("-oxooxxxox") == "x"
    assert vyhodnot("xxxoxoxox-") == "x"
    assert vyhodnot("oxxxoxxoo-") == "x"
    assert vyhodnot("oxo-oxoxxx") == "x"
    assert vyhodnot("oxx-ooxxxo") == "x"
    assert vyhodnot("xxxo-oxoxo") == "x"
    assert vyhodnot("o-xxx-oxoo") == "x"


def test_vyhodnot_vyhra_o():
    """
    Kolečka vyhrála pole 10.
    """
    assert vyhodnot("ooo-------") == "o"
    assert vyhodnot("---ooo----") == "o"
    assert vyhodnot("-------ooo") == "o"
    assert vyhodnot("-xoxoooxox") == "o"
    assert vyhodnot("-xoooxooxx") == "o"
    assert vyhodnot("xoooxoxox-") == "o"
    assert vyhodnot("oooxxooxx-") == "o"
    assert vyhodnot("oxox-xooox") == "o"
    assert vyhodnot("xxox-oxooo") == "o"
    assert vyhodnot("x-ooo-xoxx") == "o"
    assert vyhodnot("xo-xoooxox") == "o"
    assert vyhodnot("x--ooo-x-x") == "o"


def test_vyhodnot_remiza():
    """
    Nastala remíza pole 10.
    """
    assert vyhodnot("oxoxoxoxox") == "!"
    assert vyhodnot("xxooxxooxo") == "!"
    assert vyhodnot("ooxxooxxoo") == "!"


def test_vyhodnot_hra():
    """
    Hra neskončila pole 10.
    """
    assert vyhodnot("----------") == "-"
    assert vyhodnot("xx------oo") == "-"
    assert vyhodnot("-xoxoxoxox") == "-"
    assert vyhodnot("-oxxooxxoo") == "-"
    assert vyhodnot("xoxoxoxox-") == "-"
    assert vyhodnot("xxooxxoox-") == "-"
    assert vyhodnot("oxoxo-oxox") == "-"
    assert vyhodnot("xxoox-ooxo") == "-"
    assert vyhodnot("--oo--xx--") == "-"


def test_tah_x():
    """
    Pozitivní testy se symbolem "x" pole 10.
    """
    assert tah("----------", 0, "x") == "x---------"
    assert tah("----------", 5, "x") == "-----x----"
    assert tah("----------", 9, "x") == "---------x"
    assert tah("----------", 3, "x") == "---x------"


def test_tah_o():
    """
    Pozitivní testy se symbolem "o" pole 10.
    """
    assert tah("----------", 0, "o") == "o---------"
    assert tah("----------", 5, "o") == "-----o----"
    assert tah("----------", 9, "o") == "---------o"
    assert tah("----------", 3, "o") == "---o------"


def test_tah_pocitace_prazdne():
    """
    Hra na prázdné pole pole 10.
    """
    pole = "----------"
    result = tah_pocitace(pole, "o")
    assert len(result) == 10
    assert result.count("-") == 9
    assert result.count("o") == 1


def test_tah_pocitace_skoro_plne():
    """
    Hra na skoro plné pole (volno uprostřed) pole 10.
    """
    pole = "xxoxo-xoxo"
    result = tah_pocitace(pole, "o")
    assert len(result) == 10
    assert result.count("x") == 5
    assert result.count("o") == 5


def test_tah_pocitace_skoro_plne_zacatek():
    """
    Hra na skoro plné pole (volno na začátku) pole 10.
    """
    pole = "-xoxoxoxox"
    result = tah_pocitace(pole, "o")
    assert len(result) == 10
    assert result.count("x") == 5
    assert result.count("o") == 5


def test_tah_pocitace_skoro_plne_konec():
    """
    Hra na skoro plné pole (volno na konci) pole 10.
    """
    pole = "xoxoxoxox-"
    result = tah_pocitace(pole, "o")
    assert len(result) == 10
    assert result.count("x") == 5
    assert result.count("o") == 5


def test_tah_pocitace_skoro_plne_konec_2():
    """
    Hra na skoro plné pole (2× volno na konci) pole 10.
    """
    pole = "xooxoxox--"
    result = tah_pocitace(pole, "o")
    assert len(result) == 10
    assert result.count("x") == 4
    assert result.count("o") == 5
    assert result.count("-") == 1

def test_tah_chyba1():
    """Chyba úplně plné pole"""
    with pytest.raises(ValueError):
        tah_pocitace('oxoxoxoxox', "o")

def test_tah_chyba2():
    """Chyba nevyplněné pole"""
    with pytest.raises(ValueError):
        tah_pocitace('          ', "o")

def test_tah_chyba3():
    """Chyba pole délky 0"""
    with pytest.raises(ValueError):
        tah_pocitace('', "o")

def test_tah_chyba4():
    """Chyba pole delší/kratší než daná délka pole"""
    with pytest.raises(ValueError):
        tah_pocitace("------------", "o")
        tah_pocitace("------", "o")






if __name__ == "__main__":
    pytest.main()
