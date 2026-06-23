# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [To correctly guess the secret number] 
Describe the game's purpose.

- [guess > secret, the message says "Go HIGHER!" but should say "Go LOWER!" | guess > secret, the message says "Go LOWER!" but should say "Go HIGHER!" | Even attempts corrupt the secret type to string → type mismatch triggers the fallback → fallback uses string ordering → digit-length differences produce wrong comparisons] 
Detail which bugs you found.

- [swapping the messages so guess > secret → "Go LOWER!" and guess < secret → "Go HIGHER!" | remove the attempt_number % 2 == 0 branch that was converting secret to a string on even attempts] 
Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 20
2. Game returns "Go HIGHER!"
3. User enters a guess of 20 → "Go LOWER!"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
=================== test session starts ====================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\Nylah\OneDrive\AI110\ai110-module1-proj
plugins: anyio-4.13.0
collected 4 items                                           

tests\test_game_logic.py ....                         [100%]

==================== 4 passed in 0.02s =====================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
