# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
  - The game looked normal to me, simple desgin.
- List at least two concrete bugs you noticed at the start: 
  - The game shows your out of tries when i had one more left
  - My game histroy was inaccurate (For example, for tries 4-6 it shows my input as 7 each time , when i put in 7, 7.5, and 7.3)
  - The first time i played, i input 12 and the hint told me to go lower event though the answer was 84 and i shouldve went higher.
  - When i lost the first game, it didnt allow me to restart the game using the button and i had to reopen it on a new tab.
  - The answer is shown in the developer debug info
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Chatgpt to figure out how to clone the fork to my computer in order to open it in VS Code. I also used Ai when i needed to install the game requirnemtns. Because my MAC had pip3 instead of pip, i couldnt dowlaod the requirments with the document command and had to tweak it in order for it to work.
- Give one example of an AI suggestion you accepted and why.
  - One example of an AI suggestion that i took was using pip3 to install the game requirements instead of just pip. This worked since my Mac has pip3 installed and i was able to get past that challenge.
- Give one example of an AI suggestion you changed or rejected and why.
   - One AI suggestion was to regenerate the secret number on every rerun to avoid errors. I rejected this because it caused the game to change unpredictably during normal play. Instead, I kept the secret stored in session state so it only changes when starting a new game or changing the difficulty, which made the game work as intended.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
  - I tested the game multiple times by playing it and repeating the same actions to see if the issue happened again. If the behavior stayed consistent and the bug didn’t come back, I knew the fix worked. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - One test I ran was clearing the answer input to make sure the game didn’t break or reset incorrectly. This showed me that the input could reset without changing the secret number.
- Did AI help you design or understand any tests? How?
  - Yes, AI helped me think through what actions to test and what behavior to expect. It also helped explain why certain bugs were happening and how to verify they were fixed.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The secret number kept changing because Streamlit reruns the app every time the user interacts with it. Each rerun caused the code to generate a new random number instead of keeping the old one. Since the secret wasn’t stored properly in session state, it reset whenever the app refreshed or the difficulty changed.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - In Streamlit, the app reruns from top to bottom whenever you click or change something. Session state is how Streamlit remembers important values between those reruns. Without session state, everything resets, which is why the game kept losing its secret number.
- What change did you make that finally gave the game a stable secret number?
  - I stored the secret number in session state and only regenerated it when starting a new game or changing the difficulty. This made sure the secret stayed the same during gameplay. The game now only resets when it’s supposed to.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I want to keep the habit of testing my code frequently after every small change instead of waiting until the end. This helped me catch bugs early and understand exactly what caused them.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Next time, I would be more specific in my prompts and double-check AI suggestions before applying them. This would help avoid changes that fix one problem but create another.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project taught me that AI-generated code is a helpful starting point, but it still needs careful review and testing. AI can assist, but it can’t replace understanding how the code actually works.
