# ultramarathon-performance-viz

A data visualization project exploring how performance and participation in
ultra-marathon running have evolved over five decades.

**Group 17 — Luiz Samelo , Maximilian Staudacher, Rayudu Muralikrishna**
*Information Visualization (193.171), TU Wien, 2026*

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

**Python 3.9+ required.**

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ultramarathon-performance-trends.git
cd ultramarathon-performance-trends

# 2. Install dependencies
pip install -r requirements.txt

# 3. Place the dataset
# Download TWO_CENTURIES_OF_UM_RACES.csv from Kaggle and place it in data/

# 4. Open the notebooks
jupyter notebook
```

### Interactive Server (Choropleth + Dominance Chart)

The `choropleth_app/` folder contains a web app for the interactive choropleth visualization as well as the top ten finishing countries.
Before running the server for the first time, you need to run the aggregation function first to create clean datasets for the visualisation.

**Build the aggreagated data**

```bash
cd choropleth_app
python aggregation.py
```

**Start the server**

```bash
cd choropleth_app
python app.py
```

Then open [http://localhost:5050](http://localhost:5050) in your browser.

---

## Repository Structure

- `data/`
- `choropleth_app`
- `Notebooks/`
  - `ultra_partB.ipynb` — Part B 
  - `ultra_partC.ipynb` — Part C
- `Viz/` — Visualization screenshots
- `.gitignore`
- `requirements.txt`
- `README.md`
---

## Visualizations

| # | Visualization | Notebook | Author     |
|---|--------------|----------|------------|
| 1 | Choropleth map — avg pace by country with year slider | ultra_partA | Maximilian |
| 2 | Top 10 national dominance line chart | ultra_partA | Rayudu     |
| 3 | Speed distribution by distance (box plots) | ultra_partB | Luiz       |
| 4 | Elite vs. median speed over time | ultra_partB | Luiz       |
| 5 | Age vs. speed scatter by gender | ultra_partC | Rayudu     |
| 6 | Athlete career arc (individual trajectories) | ultra_partC | Maximilian |

---

## Key Findings

- A democratization of ultra marathon running has happened. Not only did people from more countries participate, but the average finishing speed has also declined. This suggests the emergence of a stronger amateur base in addition to the top performing athletes.
- Elite 50 km performance has remained stable (~17–18 km/h) since the 1990s,
  while field median speed has declined — evidence of the sport's democratization.
- Speed decreases and variability increases with distance (50 km to 50 mi to 100 km),
  consistent with a broader recreational participation base in longer races.
-  National dominance has shifted significantly as early decades were dominated by a handful of countries, while post-2000 shows broader global participation.
- Countries with highest avg speed in 50km races are concentrated in Europe and East Africa.
- The USA leads in total finishers volume, reflecting the sport's mass popularization in North America.
- Peak performance age differs by gender, with both groups showing a gradual speed decline after their prime years.
- Long-term career arcs show that top athletes maintain competitive speeds for 10+ years, with a gradual decline in later career stages.
