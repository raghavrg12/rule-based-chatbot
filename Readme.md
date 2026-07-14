# Rule-Based AI Chatbot - DecodeLabs Project 1

## Overview
This repository contains a deterministic, rule-based AI chatbot developed as part of the DecodeLabs Industrial Training Kit (Batch: 2026)[cite: 1]. 

Before diving into probabilistic deep learning (System 1), this project focuses on mastering the "White Box" logic engine (System 2)[cite: 1]. It serves as a foundational exercise in control flow, intent matching, and algorithmic efficiency[cite: 1]. 

## ⚙️ Architecture & IPO Model
The system is built on the Input-Process-Output (IPO) model to ensure 100% traceability and zero hallucination risk[cite: 1]:
* **Input & Sanitization:** Raw data is captured, converted to lowercase, and stripped of whitespaces for normalized processing[cite: 1].
* **Process (The Logic Skeleton):** Intent matching is handled through a Python dictionary (Hash Map)[cite: 1].
* **Output:** Generates a predefined response or an atomic fallback for unknown intents[cite: 1].

## 🚀 Key Engineering Decisions
* **Algorithmic Efficiency:** The chatbot avoids the "anti-pattern" of rigid `if-elif` ladders, which carry a linear time complexity of O(n)[cite: 1]. Instead, it uses a Python dictionary for intent routing, achieving O(1) constant time complexity for instant lookups regardless of scale[cite: 1].
* **The Infinite Loop:** The program runs on a continuous `while` cycle (the heartbeat) that only terminates when a specific kill command (`exit`) is received[cite: 1].
* **Control Layer Foundation:** This deterministic approach mimics the foundational logic used in modern AI guardrails (like NVIDIA NeMo and Llama Guard) to filter probabilistic outputs[cite: 1]. 

## 💻 How to Run
1. Ensure Python 3.x is installed on your machine.
2. Clone this repository.
3. Open a terminal and navigate to the project directory.
4. Run the script:
   ```bash
   python chatbot.py