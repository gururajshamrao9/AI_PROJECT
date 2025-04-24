def prioritize_tests(changes):
    mapping = {
        'login': ['test_login_success', 'test_login_invalid'],
        'checkout': ['test_checkout_cart', 'test_checkout_payment']
    }
    return mapping.get(changes, [])

print(prioritize_tests('login'))
