# 🧠 TalentIQ AI

AI-powered candidate ranking and discovery system built for intelligent recruitment. TalentIQ AI goes beyond keyword matching by using semantic search, hybrid scoring, and explainable AI to identify candidates who genuinely fit a role.

---

## 🚀 Problem Statement

Traditional applicant tracking systems rely heavily on keyword matching, often overlooking strong candidates whose profiles may not contain exact keywords from a job description.

TalentIQ AI addresses this challenge by understanding the meaning and context of both job descriptions and candidate profiles, enabling recruiters to discover the most relevant candidates efficiently.

---

## ✨ Key Features

* Semantic candidate matching using vector embeddings
* Hybrid ranking engine combining multiple candidate signals
* Experience-based scoring
* Skill relevance analysis
* Behavioral signal evaluation
* Explainable AI recommendations
* Interactive Streamlit dashboard
* Scalable architecture supporting large candidate datasets

---

## 🏗️ System Architecture

Job Description

↓
JD Parser

↓

SentenceTransformer Embeddings

↓

Semantic Similarity Engine

↓

Hybrid Ranking Engine

├── Experience Score (25%)

├── Skill Score (20%)

├── Behaviour Score (15%)

└── Semantic Match Score (40%)

↓

Candidate Ranking

↓

Explainable AI Dashboard

---

## 🧠 Ranking Methodology

Each candidate receives a final score based on four components:

**Semantic Score (40%)**
Measures contextual similarity between the job description and candidate profile using Sentence Transformers.

**Experience Score (25%)**
Evaluates relevance of previous roles and career history.

**Skill Score (20%)**
Measures overlap between candidate skills and required job skills.

**Behaviour Score (15%)**
Uses recruiter engagement and platform activity signals to assess candidate quality.

Final Score =

0.40 × Semantic Score +
0.25 × Experience Score +
0.20 × Skill Score +
0.15 × Behaviour Score

---

## 📸 Screenshots

### Home Dashboard

![Home](screenshots/home.png)

### Ranked Candidates

![Ranking](screenshots/ranking.png)

### Candidate Snapshot

![Candidate Snapshot](screenshots/candidate_snapshot.png)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Ishita-0504/TalentIQ-AI.git
cd TalentIQ-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Sentence Transformers
* NumPy
* Pandas
* Plotly
* Scikit-Learn

---

## 📊 Output

The system generates:

* Ranked candidate shortlist
* Candidate score breakdown
* AI-generated recruiter insights
* Exportable ranked candidate CSV

---

## 🔮 Future Enhancements

* FAISS vector indexing for faster retrieval
* Multi-language job description support
* Resume PDF parsing
* LLM-powered candidate summaries
* Real-time recruiter feedback loop

---

## 👩‍💻 Author

**Ishita Das**

Built as part of an AI Recruitment Challenge focused on intelligent candidate discovery and ranking.
