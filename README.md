

---

# ⏰ Python Countdown Timer

A simple **command-line countdown timer** written in Python.
The user enters a starting time in **hours:minutes:seconds** format, and the program counts down to zero, displaying the remaining time in real-time.

---

## 🧠 How It Works

1. The program asks you to enter a time in the format `h:m:s` (for example, `0:1:30` for 1 minute and 30 seconds).
2. It checks whether the minutes and seconds are valid (0–59).
3. Then it counts down, updating every second, until the timer reaches `00:00:00`.
4. Each second is printed to the terminal with a short delay using `time.sleep(1)`.

---

## 🖥️ Example Run

```
Insert time to count down (h:m:s) 0:0:10
00:00:10
00:00:09
00:00:08
00:00:07
00:00:06
00:00:05
00:00:04
00:00:03
00:00:02
00:00:01
00:00:00
```

---

## ⚙️ Features

* ⏳ Simple command-line countdown display
* ✅ Validates user input for proper time format
* 💤 Uses `time.sleep(1)` for accurate timing intervals
* 🔢 Displays time in `hh:mm:ss` format


## 📂 File Structure

```
countdown-timer/
│
├── countdown_timer.py     # Main program
└── README.md              # Project documentation
```

---

## 🧩 Example Inputs

| Input    | Description         |
| -------- | ------------------- |
| `0:0:30` | 30-second countdown |
| `0:2:0`  | 2-minute countdown  |
| `1:0:0`  | 1-hour countdown    |

---
## 🧑‍💻 Author

**Narek**
A lightweight and educational project to practice Python loops, input validation, and time handling.
