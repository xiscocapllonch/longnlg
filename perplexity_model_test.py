from perplexity_model import train_perplexity_model


def test_train_perplexity_model():
    corpus = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed' \
             ' nibh velit, faucibus nec libero ac, venenatis ornare lacus.' \
             ' Proin luctus vel dui non porta. Pellentesque odio nunc,' \
             ' condimentum sed orci in, pretium aliquet massa. Cras accumsan' \
             ' elementum blandit.'

    perplexity_model = train_perplexity_model(corpus)

    assert perplexity_model.perplexity([('lorem', 'ipsum')]) == 1.0
    assert perplexity_model.perplexity([('sed', 'orci')]) == 2.0
    assert perplexity_model.perplexity([('test', 'case')]) == float('inf')
