from generator import generate_sequence, get_next_input, generate_text


def test_generate_sequence():
    input_str = 'If the execution of this test fails, the deployment'
    result = generate_sequence(input_str, 1.0)
    assert result == ' fails and the certificate is revoked in accordance' \
                     ' with the certificate authority.\n\nFor example, we' \
                     ' can specify an error message in the deployment' \
                     ' configuration.'


def test_get_next_input():
    outputs = ['An example ', 'for test ', 'this function']
    result = get_next_input(outputs, 3)
    assert result == 'test this function'


def test_get_next_input_smallest_than_max():
    outputs = ['An example ', 'for test ', 'this function']
    result = get_next_input(outputs, 10)
    assert result == 'An example for test this function'


def test_generate_text():
    input_str = 'If the execution of this test fails, the deployment'
    result = generate_text(input_str, 2)

    ex_result1 = ' of an SQL database will not be executed with the following' \
                 ' consequences:\n\nThe SQL client will be blocked and will' \
                 ' have problems completing the data validation'

    ex_result2 = '. (See Error Handling with SQL Server 2005.)\n\nIf a SQL' \
                 ' Server 2003 database contains more than one type, all' \
                 ' queries in the database'

    assert result == [ex_result1, ex_result2]
