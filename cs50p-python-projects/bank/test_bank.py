from bank import value

def test_hello():
    assert value("hello") == 0

def test_hi():
    assert value("hi") == 20

def test_random():
    assert value("welcome") == 100

if __name__ == "__main__":
    main()
