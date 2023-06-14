from challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    try:
        encrypt_message("2", "a")
    except TypeError as error:
        assert str(error) == "tipo inválido para key"
    try:
        encrypt_message(2, 2)
    except TypeError as error:
        assert str(error) == "tipo inválido para message"
    assert encrypt_message("abcd", 4) == "".join(reversed("abcd"))
    assert encrypt_message("abcde", 3) == "cba_ed"
    assert encrypt_message("abcde", 2) == "edc_ba"
