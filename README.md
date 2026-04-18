# AI Password Security Analyzer

Generative AI-Based Password Strength Evaluation & Credential Leak Prevention

## Overview

AI Password Security Analyzer is a hybrid, machine learning-driven system designed to evaluate password strength and generate secure, high-entropy alternatives. The system combines statistical modeling, rule-based validation, and generative techniques to address real-world password vulnerabilities, particularly in the Indian user context.

Unlike traditional password strength meters that rely on simple heuristics, this system leverages **data-driven learning from leaked credential patterns** and provides **explainable, context-aware recommendations**.

---

## Live Demo

Access the live application:
https://luxury-quokka-31e69c.netlify.app/

---

## Problem Statement

A large proportion of users create weak, predictable passwords using:

* Names, birth years, and phone-number patterns
* Reused credentials across platforms
* Structurally simple combinations

Traditional strength meters fail to capture these real-world patterns, leading to poor security and high vulnerability to brute-force and probabilistic attacks.

---

## Solution

This project introduces a **hybrid password evaluation system** that:

* Uses machine learning to detect structural weaknesses
* Applies rule-based validation aligned with security standards
* Generates strong, culturally relevant passphrases
* Provides real-time feedback without storing user credentials

---

## Key Features

### 1. Hybrid Strength Evaluation

* Combines Random Forest predictions with zxcvbn scoring
* Uses calibrated probability outputs for reliable classification

### 2. Explainable AI

* Provides feature-based reasoning for each password
* Highlights specific weaknesses (patterns, repetition, low entropy)

### 3. Generative Passphrase System

* Generates high-entropy, secure passwords
* Uses culturally familiar word structures for better memorability

### 4. Real-Time Client-Side Analysis

* Instant feedback while typing
* No backend dependency → ensures privacy

### 5. Multilingual Support

* Supports multiple Indian languages and scripts
* Generates secure passphrases tailored to linguistic familiarity

---

## System Architecture

The system follows a multi-stage pipeline:

1. Data Collection (Leaked credentials + structured datasets)
2. Data Preprocessing (cleaning, normalization)
3. Feature Engineering (entropy, length, patterns, etc.)
4. Machine Learning Model (Random Forest classifier)
5. Rule-Based Validation (clinical-style rules for security checks)
6. Probability Calibration (Platt scaling)
7. Hybrid Scoring Mechanism
8. Output: Strength + Explanation + Suggested Password

---

## Methodology

* Dataset size after preprocessing: ~13,120 valid passwords
* Feature set: 10 engineered features (entropy, repetition, character diversity, etc.)
* Model: Random Forest (ensemble learning)
* Data split: 80% training / 20% testing
* Hybrid scoring:
  Combined Score = 0.6 × zxcvbn score + 0.4 × calibrated ML confidence

---

## Performance Metrics

* Overall Accuracy: **87%**
* Weak Class: Precision 0.91, Recall 0.93, F1-score 0.92
* Strong Class: F1-score 0.89
* False negative rate for weak passwords: ~2.5%

As shown in evaluation results , the model effectively distinguishes weak and strong passwords while maintaining reliability across classes.

---

## Example Output

Input: `rahul123`
Output:

* Strength: Weak
* Hybrid Score: 0.16
* Suggested secure passphrase

Input: Complex passphrase

* Strength: Strong
* Estimated crack time: >100 years

---

## Tech Stack

* Programming: Python
* ML Libraries: Scikit-learn, NumPy, Pandas
* Security Library: zxcvbn
* Frontend: JavaScript (Client-side evaluation)
* Deployment: Browser-based interface

---

## Key Strengths

* Combines ML + rule-based + generative approaches
* Region-specific modeling improves real-world accuracy
* Reduces false positives compared to traditional meters
* Fully privacy-preserving (no password storage)
* Scalable for integration into banking or enterprise systems

---

## Limitations

* Dataset size relatively small compared to global password corpora
* Medium-strength classification remains ambiguous
* Generative module depends on predefined wordlists

---

## Future Work

* Integration with real-time authentication systems
* LLM-based adaptive password generation
* Expansion to multilingual and global datasets
* Deployment as API/microservice architecture

---

## Conclusion

This project demonstrates a practical, explainable, and hybrid approach to password security. By combining machine learning with rule-based reasoning and generative techniques, the system improves both **accuracy and usability**, making it suitable for real-world deployment in secure systems.

---

## Disclaimer

This project is intended for research and educational purposes only. Not for direct production use without validation and security auditing.
