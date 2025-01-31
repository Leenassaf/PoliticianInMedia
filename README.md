# COMP 370 Final Project – Donald Trump’s Coverage in the North American Media

## Overview
This project analyzes over 500 North American news articles covering Donald Trump, collected in the weeks leading up to and following the recent US election. The objective is to assess media sentiment and topic coverage to determine whether coverage was predominantly positive, negative, or neutral, and to identify the key topics discussed.

## Authors
- **Duru Aran** – duru.aran@mail.mcgill.ca
- **Omar Assaadi** – omar.assaadi@mail.mcgill.ca
- **Leen Assaf** – leen.assaf@mail.mcgill.ca  

## Dataset
The dataset was sourced from **NewsAPI.org**, with a total of **600 articles** initially retrieved from 59 North American news sources (USA, Canada, and Mexico). After data cleaning and annotation, the final dataset contained **581 articles**. The dataset includes the following columns:
- **Title**
- **Description**
- **Source**
- **Initial Summary** (manually added)

**Data Collection Process:**
- Data was collected day by day to avoid duplicates due to NewsAPI’s 100-result-per-day limit.
- Articles were retrieved in English and only from North American sources.
- A Python script was used to automate data retrieval and cleaning.

## Methodology
### 1. Open Coding
- A subset of **200 articles** was manually annotated to identify main topics.
- Each article was assigned to one of six predefined topics based on its title and introduction.

### 2. Topic Identification
- Six main topics emerged from open coding and TF-IDF analysis:
  1. **Consequences of Trump’s Re-Election**
  2. **Election Analysis**
  3. **Trump Campaign**
  4. **Opinions on Trump and his Supporters**
  5. **Trump’s Policies**
  6. **Coverage Focusing on Kamala Harris**

### 3. TF-IDF Analysis
- TF-IDF was computed to determine the top 10 significant words for each topic.
- Stopwords were removed to improve keyword significance.

### 4. Sentiment Analysis
- Three sentiment analysis tools were tested: **TextBlob, BERT, and VADER**.
- **VADER** was selected as the final tool due to its nuanced classification of sentiment levels (e.g., "strongly positive," "neutral," etc.).
- Articles were classified as **positive, negative, or neutral**.

## Results
### **Topic Distribution**
The dataset was evenly split between four main topics:
- **Opinions on Trump and his Supporters**
- **Trump’s Campaign**
- **Consequences of Trump’s Re-Election**
- **Election Analysis**

The other two topics (**Trump’s Policies** and **Coverage Focusing on Kamala Harris**) accounted for only **5% of the dataset**.

### **Sentiment Analysis Findings**
| Topic | Positive (%) | Neutral (%) | Negative (%) |
|--------|------------|------------|------------|
| Consequences of Trump’s Reelection | 56 | 24 | 20 |
| Trump Campaign | 58 | 24 | 18 |
| Election Analysis | 34 | 34 | 32 |
| Opinions on Trump and Supporters | 61 | 7 | 32 |
| Trump’s Policies | 48 | 32 | 20 |
| Coverage Focusing on Kamala Harris | 42 | 20 | 38 |

- **Over 50% of articles portrayed Trump positively.**
- **27% of articles were negative,** showing some polarization.
- **Opinions on Trump and his Supporters was the most polarized category.**

### **TF-IDF Key Findings**
- **Consequences of Trump’s Reelection**: Keywords like "bitcoin," "stocks," and "market" suggest a focus on economic impacts.
- **Election Analysis**: Frequent words included "battleground," "Georgia," and "news," reflecting election coverage.
- **Trump’s Policies**: Keywords like "Ukraine," "India," and "Modi" indicate a focus on foreign policy.
- **Coverage Focusing on Kamala Harris**: Words like "vice" and "husbands" highlight media focus on her personal and political role.

## Team Contributions
- **Duru Aran**: Methods, Discussion, VADER Sentiment Analysis, Graphs.
- **Omar Assaadi**: Introduction, Results, TextBlob Sentiment Analysis.
- **Leen Assaf**: Data, TF-IDF Scoring Code, BERT Sentiment Analysis.

## Citations
- Karabiber, F. "TF-IDF - Term Frequency-Inverse Document Frequency." Learn Data Science.
- Malde, R. "A Short Introduction to Vader." Towards Data Science.
- pawangfg. "Sentiment Classification Using Bert." GeeksforGeeks.
- Watson, E. "A Beginner’s Guide to Performing Sentiment Analysis on Text with Python." Medium.


