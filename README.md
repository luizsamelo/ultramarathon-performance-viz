# ultramarathon-performance-viz

A data visualization project exploring how performance and participation in
ultra-marathon running have evolved over five decades.

**Group 17 — Luiz Samelo, Maximilian Staudacher, Rayudu Muralikrishna**
*Information Visualization (VU 2.0), TU Wien, 2026*

---

## Research Question

Has national dominance in ultra-marathon running shifted over the past five
decades as the sport grew from a niche activity into a globally participated
discipline?

---

## Dataset

[The Big Dataset of Ultra-Marathon Running](https://www.kaggle.com/datasets/aiaiaidavid/the-big-dataset-of-ultra-marathon-running)
— David Davydov, Kaggle (~7 million race records, 1798–2022).

**Download** `TWO_CENTURIES_OF_UM_RACES.csv` from Kaggle and place it in the
`data/` folder before running any notebook.

---

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ultramarathon-performance-trends.git
cd ultramarathon-performance-trends

# 2. Install dependencies
pip install pandas numpy seaborn matplotlib plotly country_converter

# 3. Place the dataset
# Copy TWO_CENTURIES_OF_UM_RACES.csv into the data/ folder

# 4. Open the notebooks
jupyter notebook
```

Python 3.9+ recommended.

---

## Repository Structure
ultramarathon-performance-viz/
├── data/
│   └── TWO_CENTURIES_OF_UM_RACES.csv   ← download from Kaggle (not tracked)
├── notebooks/
│   ├── ......ipynb
│   ├── ultra_partB.ipynb
│   └── .......ipynb
├── Viz/
├── .gitignore
└── README.md
