# Cryptocurrency Trend Predictor System

Category: Machine Learning / Multi-Agent Systems  
Context: Hackathon Project  
Responsibility: End-to-end ownership of data pipelines, ML components, and agent logic  
Outcome: 1st Runner-Up (50+ teams)  
Timeline: Built and delivered within 48 hours

---

## Problem Statement

Cryptocurrency markets are highly volatile and influenced by both historical price movements and real-time public sentiment.  
The goal of this project was to **identify market trends and regimes** for major cryptocurrencies so users can make more informed decisions about when to invest and when to avoid entering the market.

---

## Approach

The system was designed as a **multi-agent trend analysis framework**, where each agent focused on extracting signals from different data sources. Instead of relying on a single predictive model, the system combined **unsupervised market regime detection** with **real-time sentiment analysis**.

Each agent contributed independent insights, which were aggregated by a master agent to produce a final trend assessment.

---

## System Overview

High-level workflow:
1. Collect historical cryptocurrency price data via APIs
2. Engineer numerical features from historical market data
3. Apply **PCA-based dimensionality reduction** on historical price features and use KMeans clustering to classify incoming real-time data into market regimes
4. Use **KMeans clustering** to identify market regimes and trend states
5. Scrape real-time data from social media and news sources
6. Perform sentiment analysis on public discussions related to cryptocurrencies
7. Run multiple agents, each analysing a different signal source
8. Aggregate all signals through a master agent to generate the final trend output

The system focused on major cryptocurrencies such as **Bitcoin and Ethereum**.

---

## Tools & Technologies

- Python
- NumPy, Pandas
- Scikit-learn (PCA, KMeans, StandardScaler)
- Natural Language Processing (NLTK, VADER sentiment analysis)
- Web scraping & APIs (Requests, JSON)
- Multi-agent framework (uAgents)
- LangGraph & LangChain
- OpenAI API (for agent reasoning and orchestration)
- Matplotlib (visualisation)

---

## Evidence of Skill

- Implemented **unsupervised learning pipelines** for market regime detection
- Designed and executed **feature engineering** on historical crypto price data
- Built PCA-based dimensionality reduction to stabilise clustering
- Implemented KMeans clustering to extract interpretable trend states
- Scraped and processed real-time data from social media and news sources
- Built sentiment analysis pipelines from raw text data
- Contributed to **multi-agent coordination and decision logic**
- Integrated all components into a **production-style system**

---

## Results & Outcome

- Achieved **1st Runner-Up** position among **50+ teams**
- Successfully demonstrated a working multi-agent crypto trend analysis system
- Produced interpretable market regime signals combining long-term data and short-term sentiment
- Recognised for system design, adaptability, and practical applicability

---

## Challenges & Constraints

- Entire system was designed and built within **48 hours**
- Original project idea was **pivoted mid-hackathon** after discussions with the company founder
- Limited time required rapid architectural decisions and prioritisation
- Balanced correctness, interpretability, and delivery speed under pressure

Despite these constraints, the team successfully delivered a competitive and functional system.

---

## Why This Project Matters

This project demonstrates:
- Strong **machine learning engineering fundamentals**
- Practical use of **unsupervised learning** in noisy real-world data
- Experience working with **multi-agent architectures**
- Ability to ship under extreme time constraints
- Adaptability when requirements change suddenly

It reflects real-world startup and hackathon conditions more closely than typical academic projects.

---

## Future Directions

- Improve agent specialisation and weighting
- Incorporate on-chain metrics
- Add probabilistic confidence estimates
- Deploy as a real-time dashboard
