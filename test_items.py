link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_is_enabled(browser):
    browser.get(link)
    add_to_basket_btn = browser.find_element_by_css_selector(
        '#add_to_basket_form .btn-add-to-basket')

    is_enabled = add_to_basket_btn.is_enabled()
    assert is_enabled, 'add to basket button is not enabled'
