def is_anagram(first_string, second_string):
    lower_string = first_string.lower()
    lower_string2 = second_string.lower()
    lower_string = quicksort_string(lower_string)  # abcd
    lower_string2 = quicksort_string(lower_string2)
    if lower_string == "" or lower_string2 == "":
        return lower_string, lower_string2, False
    if len(lower_string) != len(lower_string2):
        return (lower_string, lower_string2, False)
    else:
        if lower_string == lower_string2:
            return (lower_string, lower_string2, True)
        else:
            return (lower_string, lower_string2, False)


def quicksort_string(string):
    string
    if len(string) <= 1:
        return string
    else:
        pivot = string[0]
        less = "".join(
            [letra for letra in string[1:] if ord(letra) < ord(pivot)]
        )
        greater = "".join(
            [letra for letra in string[1:] if ord(letra) >= ord(pivot)]
        )
        return quicksort_string(less) + pivot + quicksort_string(greater)


# devo receber duas strings
# ordenar essas strings por ordem alfabética (?)
# retornar uma tupla (string_ordenada, string_ordenada,
#  booleano_se_é_ou_não_um_anagrama)

# print(is_anagram("teste", "sette"))
