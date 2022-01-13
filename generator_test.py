from generator import generate_sequence


def test_generate_sequence():
    input_str = 'If the execution of this test fails, the deployment'
    result = generate_sequence(input_str, 1.0)
    assert result == ' fails and the certificate is revoked in accordance' \
                     ' with the certificate authority.\n\nFor example, we' \
                     ' can specify an error message in the deployment' \
                     ' configuration.'
