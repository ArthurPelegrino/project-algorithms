from challenges.challenge_encrypt_message import encrypt_message


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


def test_encrypt_message_incorrect_return():
    right_odd = encrypt_message("abcde", 3)
    even_odd = encrypt_message("abcde", 2)
    if right_odd == "edc_ba":
        raise AssertionError("unnexpected result 'edc_ba'")
    if even_odd == "cba_ed":
        raise AssertionError("unnexpected result 'cba_ed'")

    # encrypt_message("abcde", 3) == "cba_ed" // resultado correto com ímpar

    # assert encrypt_message("abcde", 2) == "edc_ba" // resultado corre com par
