from main import all_operations

from func.func import last_five, correct_date, correct_count, correct_card


def test_last_five():
    assert last_five(all_operations) == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614', '2019-11-13T17:38:04.800051', '2019-11-05T12:04:13.781725']


def test_correct_date():
    assert correct_date('2018-10-14T08:21:33.419441') == '14.10.2018'


def test_correct_count():
    assert correct_count('Счет 90424923579946435907') == 'Счет **5907'


def test_correct_card():
    assert correct_card('Maestro 3928549031574026') == 'Maestro 3928 54** **** 4026'
