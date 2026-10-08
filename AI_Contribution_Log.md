# AI Contribution Log – SLE-1
Course: 02AML204 – Introduction to Artificial Intelligence  
PRN: 25UAM045  
Name: Aniket Anandrao Mane  
Date: August 31, 2026  

---

## 1. AI Tools Used
- **Gemini / ChatGPT:** Used for generating the initial skeleton of the Environment class, drafting PEAS structural code, and formatting the markdown template.

---

## 2. AI-Generated Code
- Initial skeleton for `Environment` and `ReflexVacuumAgent` classes.
- Basic boilerplate logic for state-action mapping (`Suck`, `Right`, `Left`).

---

## 3. My Own Contribution
- Designed and refined the simulation termination condition using the `are_all_clean()` method.
- Added step limits and handled edge-case termination to prevent infinite loops when both rooms become clean.
- Created proper CLI output logs and tested execution across various initial state configurations.
- Created the diagrams using draw.io website.

---

## 4. Issues Found in AI Code & Fixes
- **Issue:** The AI-generated agent kept oscillating back and forth between Room A and Room B indefinitely after cleaning both rooms.
- **Fix:** Added a state check (`are_all_clean()`) and implemented a `'NoOp'` termination action once the entire environment was verified clean.
