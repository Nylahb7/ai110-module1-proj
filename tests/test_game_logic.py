from logic_utils import check_guess, prepare_secret

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a 🎉 Correct!
    _, message = check_guess(50, 50)
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    _, message = check_guess(60, 50)
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    _, message = check_guess(40, 50)
    assert message == "📈 Go HIGHER!"

def test_prepare_secret_does_not_corrupt_type():
    # Bug 1: prepare_secret was returning str(secret) on even attempts.
    # String comparison "9" > "20" is True (lexicographic), so check_guess
    # wrongly returned "Too High" for a guess that was actually too low.
    secret = prepare_secret(20)
    _, message = check_guess(9, secret)
    assert message == "📈 Go HIGHER!", f"Expected '📈 Go HIGHER!' but got '{message}' — type corruption bug may have returned"
