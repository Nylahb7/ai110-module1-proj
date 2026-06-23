# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50 | "Go HIGHER" hint | "Go LOWER" hint | none |
| 90 | "Go LOWER" hint | "Go HIGHER" hint | none |
| unselected and selected "Show Hint" | Hint show back up | Nothing happened | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The game had it's hints switched and the AI suggested swapping the messages so guess > secret → "Go LOWER!" and guess < secret → "Go HIGHER!". This suggestion was 100% correct and I verified it by using the test cases in test_game_logic.py and by replaying the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
There turned out to be another issue with the "Go LOWER!" hint. The AI suggested that there were 2 bugs listed. The AI stated that on every even-numbered attempt, secret is cast to a string before being passed to check_guess and when check_guess receives guess=9 (int) and secret="20" (str), guess > secret raises a TypeError (Python 3 can't compare int and str). The except block catches it and falls back to string comparison. This was missleading because is lead me to think that I had 2 sections of code to fix when I only had to fix 1. I followed the instructions to prompt the AI to complete tasks step by step so after the first bug was fixed I tested it and there wasn't an issue anymore. I also used pytest.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided after all of the pytest created passed and it worked after I went into the game and tested it myself as well.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
The prepare_secret test set secret to 20. It then passed 9 to make sure that the hit given was "Go HIGHER" since the problem was that the code only took the first number in an even number. The issue would have been 9 > 2 instead of what it should have been, 9 < 20.

- Did AI help you design or understand any tests? How?
AI definetly helped me understand the prepare_secret test. When the issue first arose I did not understand what the problem was and AI broke it down to me like this...
Lexicographically, "9" > "20" is True because '9' (ASCII 57) > '2' (ASCII 50) the first character wins regardless of number length. So guess 9 against secret 20 is judged "Too High" and you're told to go lower, when you should go higher.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the script from top to bottom whenever something changes and session state is how you save values so they don't disappear during reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Giving multi-step instructions and attatching relevant files. I will also keep using the terminal to commit changes here on out.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time I will be sure to seperate my sessions accordingly and name each session based on what I did. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project helped me become more confident in AI generated code.
