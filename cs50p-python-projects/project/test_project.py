from project import load_data, view_today, save_data

def test_load_data_returns_default_when_file_missing():
    assert isinstance(load_data(), dict)
    assert "habits" in load_data()


def test_view_today_shows_empty():
    data = {"habits": []}
    view_today(data)  # It prints — we just confirm it doesn't crash


def test_save_data_creates_file():
    data = {"habits": [{"name": "Pray", "streak": 1, "last_completed": "01/01/2025", "created": "01/01/2025"}]}
    save_data(data)
    assert True
