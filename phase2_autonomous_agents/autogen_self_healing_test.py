def heal_locator(broken_selector, history):
    for record in history:
        if record['text'] == 'Login' and broken_selector in record['old_selectors']:
            return record['new_selector']
    return None

example = heal_locator('div.login-btn-old', [
    {'text': 'Login', 'old_selectors': ['div.login-btn-old'], 'new_selector': 'button.login'}
])

print("Healed selector:", example)
