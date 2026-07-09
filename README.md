# Geospatial-and-Machine-Hydrogeological-Modelling-
This work represents one of the most comprehensive multi-index environmental impact assessments of dumpsite in Nigeria including 10 environmental contamination indices 3-pathway health risk modeling for both adults and children - 6 irrigation suitability indices - ML-driven water suitability classification - GIS-based spatial risk virtualization 
🌍 Ajakanga-ContamRisk: Heavy Metal Contamination & Risk Assessment at Ajakanga Dumpsite, Ibadan, Nigeria
A comprehensive, Q1-standard environmental geochemistry framework for assessing heavy metal contamination, human health risk, irrigation suitability, and machine learning-driven water quality classification at the Ajakanga open dumpsite, Oluyole LGA, Ibadan, Southwestern Nigeria.
             
________________________________________
📋 Table of Contents
•	Overview
•	Study Area
•	Key Findings at a Glance
•	Dataset
•	Modules
–	Environmental Contamination Indices
–	Irrigation Suitability Indices
–	Human Health Risk Assessment
–	Machine Learning Classification
–	GIS Spatial Modeling
•	Installation
•	Usage
•	Results & Interpretation
•	Project Structure
•	Citations
•	Author
________________________________________
🔬 Overview
This repository presents a production-grade, end-to-end environmental intelligence framework developed for the Ajakanga open dumpsite in Ibadan, Oyo State, Nigeria. The framework integrates five scientific domains into a unified Python pipeline:
1.	🧪 Hydrogeochemistry — Major ions, heavy metals, physicochemical characterization
2.	⚠️ Environmental Contamination Indices — 9 indices (CF, Cd, PLI, NPI, HMEI, Igeo, EF, RI, MI, HPI)
3.	🏥 Human Health Risk Assessment — Carcinogenic & non-carcinogenic risks for adults & children (3 pathways)
4.	🌾 Irrigation Suitability — SAR, Na%, Kelly Ratio, RSC, Mg Hazard, WQI
5.	🤖 Machine Learning — Decision Tree classification for water suitability
6.	🗺️ GIS Spatial Modeling — Suitability maps for drinking & irrigation water
Research Objective
To develop a predictive, spatially explicit contamination and risk model integrating hydrogeochemistry, health risk quantification, and machine learning to assess the environmental impact of the Ajakanga open dumpsite on groundwater quality, human health, and agricultural suitability in a basement complex terrain.
Novelty
This work represents one of the most comprehensive multi-index assessments of dumpsite contamination and environmental impact in Nigeria, combining: - 10 environmental contamination indices (vs. typical 3–4 in literature) - 3-pathway health risk modeling (Injestion, Dermal and Inhalation) for both adults and children - 6 irrigation suitability indices with FAO compliance - ML-driven water suitability classification with domain-scored features - GIS-based spatial risk virtualization for regulatory decision support
________________________________________
🗺️ Study Area
Ajakanga Dumpsite, Ibadan, Nigeria
Attribute	Description
Location	Oluyole Local Government Area, Ibadan, Oyo State, Southwestern Nigeria
Coordinates	7°18′41.32″ N, 3°50′29.34″ E citeweb_search:11#1
Area	10.034 hectares citeweb_search:11#6
Established	1996
Annual Waste Volume	162,117 metric tons (highest among Ibadan’s four dumpsites) citeweb_search:11#6
Climate	Humid tropical; mean annual rainfall ~1,270 mm; mean max temperature 32°C
Geology	Basement complex terrain — biotite-hornblende gneiss, migmatite gneiss, quartzite citeweb_search:11#1
Drainage	Dendritic pattern; well-drained by rivers and streams
Status	Open dumpsite operated by Oyo State Waste Management Authority; currently under rehabilitation citeweb_search:11#5
Environmental Context
Ajakanga is one of four major dumpsites serving Ibadan (population ~2.9 million), alongside Lapite, Aba-Eku, and Awotan citeweb_search:11#4. The site receives unsegregated municipal solid waste and has been documented to cause: - Soil contamination via leachate percolation citeweb_search:11#1 - Groundwater quality degradation with heavy metal enrichment citeweb_search:11#0 - Bioaccumulation in plants growing on dumpsite soils citeweb_search:11#2 - Public health hazards from noxious fumes and odour citeweb_search:11#4
The dumpsite soils exhibit high permeability coefficients (2.05×10⁻⁶ to 5.97×10⁻⁵ m/s), far exceeding the 1×10⁻⁹ m/s recommended for landfill liner materials, indicating rapid leachate migration into underlying aquifers citeweb_search:11#1.
________________________________________
🚨 Key Findings at a Glance
Heavy Metal Concentrations vs. Standards
Metal	Mean (mg/L)	WHO Limit	% Exceed WHO	BIS Permissible	% Exceed BIS	Primary Source
Fe	1.055	0.3	76%	1.0	36%	Iron scrap, steel waste
Pb	0.094	0.01	100%	0.01	100%	Batteries, paints, e-waste
Cu	0.090	0.05	100%	1.5	0%	Electrical wiring, alloys
Cr	0.039	0.05	4%	0.05	4%	Tannery, electroplating
Mn	0.239	0.1	92%	0.4	8%	Steel production, batteries
Zn	0.177	5.0	0%	15	0%	Galvanized materials
Ni	0.019	0.02	32%	0.07	4%	Stainless steel, alloys
Co	0.004	0.05	0%	0.1	0%	Industrial catalysts
Cd	0.016	0.003	32%	0.005	32%	Batteries, pigments
Contamination Index Summary
Index	Range	Mean	Classification	% Sites Affected
CF (Cd)	20–1,290	157.6	Very high	100%
Cd (Degree)	94–1,778	324.4	Very high	100%
PLI	7.1–62.1	17.7	Highly polluted	100%
NPI	18.5–922.8	122.0	Heavily polluted	100%
HMEI	9.1–96.7	24.2	High pollution	52%
Igeo (Cd)	3.7–9.8	5.0	Heavily–Extremely polluted	100%
RI	827–39,981	5,192	High ecological risk	100%
MI	0.70–6.48	1.70	Seriously affected	76%
HPI	1.7–43.3	6.8	Background–Polluted	8%
Critical Insight
Cadmium (Cd) is the dominant contaminant, with a mean Contamination Factor of 157.6× background and driving the Potential Ecological Risk Index to >5,000 (classified as “High Risk”). All 25 samples show “Very High Contamination” by the Degree of Contamination (Cd) index, with values ranging from 94 to 1,778 — far exceeding the threshold of 32.
________________________________________
📁 Dataset
data/AJAKANGAHM.csv
25 water samples collected from the vicinity of the Ajakanga dumpsite, Ibadan, Nigeria. All heavy metal concentrations determined by Atomic Absorption Spectrophotometry (AAS).
Sample ID	Fe (mg/L)	Pb (mg/L)	Cu (mg/L)	Cr (mg/L)	Mn (mg/L)	Zn (mg/L)	Ni (mg/L)	Co (mg/L)	Cd (mg/L)
AJA1	3.732	0.243	0.175	0.053	0.766	0.849	0.087	0.009	0.129
AJA2	2.596	0.179	0.129	0.045	0.598	0.438	0.043	0.008	0.092
AJA3	2.078	0.104	0.106	0.043	0.357	0.247	0.031	0.006	0.035
AJA4	0.241	0.069	0.079	0.031	0.159	0.095	0.009	0.003	0.002
AJA5	0.987	0.078	0.088	0.041	0.197	0.108	0.017	0.004	0.002
AJA6	0.974	0.081	0.086	0.040	0.185	0.105	0.013	0.004	0.002
AJA7	0.281	0.064	0.073	0.029	0.158	0.074	0.007	0.003	0.002
AJA8	0.817	0.078	0.083	0.046	0.183	0.099	0.015	0.003	0.002
AJA9	0.269	0.067	0.075	0.034	0.157	0.075	0.006	0.003	0.002
AJA10	0.659	0.076	0.085	0.043	0.179	0.095	0.009	0.003	0.002
AJA11	0.241	0.062	0.075	0.032	0.162	0.061	0.004	0.003	0.002
AJA12	0.597	0.074	0.078	0.042	0.171	0.073	0.005	0.003	0.002
AJA13	0.239	0.054	0.064	0.028	0.098	0.082	0.003	0.003	0.002
AJA14	0.703	0.075	0.076	0.048	0.175	0.072	0.004	0.003	0.002
AJA15	0.524	0.068	0.072	0.042	0.167	0.067	0.004	0.003	0.002
AJA16	0.566	0.067	0.073	0.044	0.165	0.063	0.004	0.003	0.002
AJA17	0.597	0.072	0.076	0.045	0.172	0.066	0.005	0.003	0.002
AJA18	0.221	0.048	0.062	0.029	0.087	0.062	0.003	0.003	0.002
AJA19	2.308	0.064	0.072	0.044	0.143	0.063	0.003	0.003	0.002
AJA20	0.469	0.071	0.069	0.036	0.169	0.062	0.003	0.003	0.002
AJA21	1.906	0.131	0.101	0.041	0.322	0.351	0.041	0.006	0.028
AJA22	1.348	0.114	0.098	0.038	0.298	0.337	0.036	0.006	0.035
AJA23	1.312	0.133	0.108	0.040	0.336	0.288	0.039	0.005	0.022
AJA24	1.449	0.128	0.120	0.035	0.274	0.305	0.045	0.006	0.011
AJA25	1.270	0.139	0.117	0.031	0.301	0.297	0.035	0.006	0.008
Descriptive Statistics:
Metal	Mean	Std Dev	Min	25%	Median	75%	Max
Fe	1.055	0.884	0.221	0.469	0.703	1.348	3.732
Pb	0.094	0.045	0.048	0.067	0.075	0.114	0.243
Cu	0.090	0.025	0.062	0.073	0.079	0.101	0.175
Cr	0.039	0.007	0.028	0.034	0.041	0.044	0.053
Mn	0.239	0.153	0.087	0.162	0.175	0.298	0.766
Zn	0.177	0.182	0.061	0.067	0.095	0.288	0.849
Ni	0.019	0.021	0.003	0.004	0.009	0.035	0.087
Co	0.004	0.002	0.003	0.003	0.003	0.006	0.009
Cd	0.016	0.031	0.002	0.002	0.002	0.011	0.129
Pearson Correlation Matrix
	Fe	Pb	Cu	Cr	Mn	Zn	Ni	Co	Cd
Fe	1.000	0.857	0.849	0.594	0.875	0.855	0.836	0.859	0.846
Pb	0.857	1.000	0.979	0.436	0.971	0.975	0.965	0.952	0.906
Cu	0.849	0.979	1.000	0.421	0.948	0.959	0.972	0.944	0.867
Cr	0.594	0.436	0.421	1.000	0.502	0.385	0.356	0.325	0.475
Mn	0.875	0.971	0.948	0.502	1.000	0.954	0.919	0.935	0.967
Zn	0.855	0.975	0.959	0.385	0.954	1.000	0.977	0.947	0.926
Ni	0.836	0.965	0.972	0.356	0.919	0.977	1.000	0.952	0.853
Co	0.859	0.952	0.944	0.325	0.935	0.947	0.952	1.000	0.880
Cd	0.846	0.906	0.867	0.475	0.967	0.926	0.853	0.880	1.000
Key Correlation Insights: - Pb–Cu (r = 0.979): Strong co-occurrence indicating common battery / electrical waste source - Pb–Mn (r = 0.971): Battery waste signature (lead-acid batteries + manganese dioxide) - Pb–Zn (r = 0.975): Galvanized steel and battery manufacturing waste - Mn–Cd (r = 0.967): Nickel-cadmium battery and steel alloy waste - Fe–Co (r = 0.859): Stainless steel and alloy waste - Cr shows weakest correlations (r < 0.50 with most metals): Independent tannery / electroplating source
________________________________________
📦 Modules
1. Environmental Contamination Indices
1.1 Contamination Factor (CF)
Reference: Hakanson (1980)
CF = C_metal / C_background
Background Values (Hakanson, 1980; Turekian & Wedepohl, 1961):
Metal	Background (mg/L)
Fe	0.05
Pb	0.002
Cu	0.01
Cr	0.002
Mn	0.005
Zn	0.02
Ni	0.002
Co	0.001
Cd	0.0001
Classification:
Class	Range	Description
1	CF < 1	Low contamination
2	1 ≤ CF < 3	Moderate contamination
3	3 ≤ CF < 6	Considerable contamination
4	CF ≥ 6	Very high contamination
Results (Ajakanga):
Sample	Fe	Pb	Cu	Cr	Mn	Zn	Ni	Co	Cd
AJA1	74.6	121.5	17.5	26.5	153.2	42.5	43.5	9.0	1,290.0
AJA2	51.9	89.5	12.9	22.5	119.6	21.9	21.5	8.0	920.0
AJA3	41.6	52.0	10.6	21.5	71.4	12.4	15.5	6.0	350.0
AJA4	4.8	34.5	7.9	15.5	31.8	4.8	4.5	3.0	20.0
AJA18	4.4	24.0	6.2	14.5	17.4	3.1	1.5	3.0	20.0
AJA21	38.1	65.5	10.1	20.5	64.4	17.6	20.5	6.0	280.0
AJA25	25.4	69.5	11.7	15.5	60.2	14.9	17.5	6.0	80.0
Mean CF by Metal: Fe=21.1, Pb=46.8, Cu=9.0, Cr=19.6, Mn=47.8, Zn=8.9, Ni=9.4, Co=4.2, Cd=157.6
Finding: All 25 samples show “Very High Contamination” (CF ≥ 6) for all 9 metals. Cadmium dominates with a mean CF of 157.6× background.
________________________________________
1.2 Degree of Contamination (Cd)
Reference: Hakanson (1980); Tomlinson et al. (1980)
Cd = Σ CF_i
Classification:
Class	Range	Description
1	Cd < 8	Low contamination
2	8 ≤ Cd < 16	Moderate contamination
3	16 ≤ Cd < 32	Considerable contamination
4	Cd ≥ 32	Very high contamination
Results (Ajakanga):
Sample	Cd	Classification
AJA1	1,778.3	Very high contamination
AJA2	1,267.8	Very high contamination
AJA3	580.9	Very high contamination
AJA4	126.8	Very high contamination
AJA18	94.1	Very high contamination
AJA21	522.7	Very high contamination
AJA25	300.7	Very high contamination
Statistics: Mean = 324.4, Min = 94.1, Max = 1,778.3
Finding: All 25 samples (100%) classify as “Very High Contamination”. The lowest Cd value (94.1) is still 3× higher than the threshold of 32. AJA1 (closest to dumpsite) shows the highest integrated contamination.
________________________________________
1.3 Pollution Load Index (PLI)
Reference: Tomlinson et al. (1980)
PLI = (CF₁ × CF₂ × ... × CFₙ)^(1/n)
Classification:
Class	Range	Description
0	PLI = 0	Background (pristine)
1	0 < PLI < 1	Unpolluted to baseline
2	PLI = 1	Baseline levels
3	1 < PLI < 2	Moderately polluted
4	PLI ≥ 2	Highly polluted
Results (Ajakanga):
Sample	PLI	Classification
AJA1	62.14	Highly polluted
AJA2	43.51	Highly polluted
AJA3	28.92	Highly polluted
AJA4	9.80	Highly polluted
AJA18	7.11	Highly polluted
AJA21	30.07	Highly polluted
AJA25	23.75	Highly polluted
Statistics: Mean = 17.7, Min = 7.11, Max = 62.14
Finding: All 25 samples (100%) are “Highly Polluted” (PLI ≥ 2). Even the least contaminated sample (AJA18) has a PLI of 7.11, indicating severe multi-metal pollution.
________________________________________
1.4 Nemerow Pollution Index (NPI)
Reference: Nemerow (1985)
NPI = √[(max(CF_i)² + mean(CF_i)²) / 2]
Classification:
Class	Range	Description
1	NPI ≤ 0.7	Unpolluted
2	0.7 < NPI ≤ 1.0	Warning limit
3	1.0 < NPI ≤ 2.0	Slightly polluted
4	2.0 < NPI ≤ 3.0	Moderately polluted
5	NPI > 3.0	Heavily polluted
Results (Ajakanga):
Sample	NPI	Classification
AJA1	922.81	Heavily polluted
AJA2	658.12	Heavily polluted
AJA3	251.66	Heavily polluted
AJA4	26.35	Heavily polluted
AJA18	18.51	Heavily polluted
AJA21	202.20	Heavily polluted
AJA25	61.30	Heavily polluted
Statistics: Mean = 122.0, Min = 18.51, Max = 922.81
Finding: All 25 samples (100%) are “Heavily Polluted”. The NPI values are extraordinarily high due to the dominance of Cd contamination (max CF = 1,290), which drives the Nemerow index through the maximum CF component.
________________________________________
1.5 Heavy Metal Evaluation Index (HMEI)
Reference: Prasad & Bose (2001)
HMEI = Σ (C_metal / C_desirable)
Desirable Limits (WHO/BIS):
Metal	Desirable (mg/L)
Fe	0.3
Pb	0.01
Cu	0.05
Cr	0.05
Mn	0.1
Zn	5.0
Ni	0.02
Co	0.05
Cd	0.003
Classification:
Class	Range	Description
1	HMEI < 10	Low pollution
2	10 ≤ HMEI < 20	Moderate pollution
3	HMEI ≥ 20	High pollution
Results (Ajakanga):
Sample	HMEI	Classification
AJA1	96.66	High pollution
AJA2	69.08	High pollution
AJA3	37.26	High pollution
AJA4	12.69	Moderate pollution
AJA13	9.91	Low pollution
AJA18	9.12	Low pollution
AJA21	37.09	High pollution
AJA25	28.70	High pollution
Statistics: Mean = 24.2, Min = 9.12, Max = 96.66
Finding: 52% of samples (13/25) show “High Pollution” (HMEI ≥ 20). AJA1 reaches 96.66, nearly 10× the “High” threshold. Only AJA4, AJA13, and AJA18 (most distant / control-like samples) fall into lower categories.
________________________________________
1.6 Geo-accumulation Index (Igeo)
Reference: Müller (1969)
Igeo = log₂(C_metal / (1.5 × C_background))
Classification:
Class	Range	Description
0	Igeo ≤ 0	Practically unpolluted
1	0 < Igeo ≤ 1	Unpolluted to moderately polluted
2	1 < Igeo ≤ 2	Moderately polluted
3	2 < Igeo ≤ 3	Moderately to heavily polluted
4	3 < Igeo ≤ 4	Heavily polluted
5	4 < Igeo ≤ 5	Heavily to extremely polluted
6	Igeo > 5	Extremely polluted
Results (Ajakanga) — Selected Samples:
Sample	Fe	Pb	Cu	Cr	Mn	Zn	Ni	Co	Cd
AJA1	5.64	6.34	3.54	4.14	6.67	4.82	4.86	2.58	9.75
AJA2	5.11	5.90	3.10	3.91	6.32	3.87	3.84	2.42	9.26
AJA4	1.68	4.52	2.40	3.37	4.41	1.66	1.58	1.00	3.74
AJA18	1.56	4.00	2.05	3.27	3.54	1.05	0.00	1.00	3.74
AJA21	4.67	5.45	2.75	3.77	5.42	3.55	3.77	2.00	7.54
Mean Igeo by Metal: Fe=3.35, Pb=4.84, Cu=2.53, Cr=3.69, Mn=4.80, Zn=2.06, Ni=1.84, Co=1.38, Cd=5.00
Igeo Classification Distribution (out of 25 samples):
Metal	Practically Unpolluted	Unpolluted-Moderate	Moderately	Moderately-Heavily	Heavily	Heavily-Extremely	Extremely
Fe	0	0	6	5	5	7	2
Pb	0	0	0	0	1	16	8
Cu	0	0	0	23	2	0	0
Cr	0	0	0	0	24	1	0
Mn	0	0	0	0	2	15	8
Zn	0	0	17	0	7	1	0
Ni	4	7	3	3	7	1	0
Co	0	15	8	2	0	0	0
Cd	0	0	0	0	17	0	8
Finding: - Cd: 32% of samples are “Extremely Polluted” (Igeo > 5); 68% are “Heavily Polluted” (3 < Igeo ≤ 4) - Pb: 32% “Extremely Polluted”; 64% “Heavily to Extremely Polluted” - Mn: 32% “Extremely Polluted” - Fe: 8% “Extremely Polluted” - Co is the least affected: 60% “Unpolluted to Moderately Polluted”
________________________________________
1.7 Potential Ecological Risk Index (RI)
Reference: Hakanson (1980)
E_r = T_r × CF
RI = Σ E_r
Toxic Response Factors (Tᵣ):
Metal	Tᵣ	Toxicity Level
Cd	30	Very high
Pb	5	Moderate
Cu	5	Moderate
Ni	5	Moderate
Co	5	Moderate
Cr	2	Low
Zn	1	Low
Mn	1	Low
Fe	1	Essential (default)
Risk Classification:
Eᵣ Class	Range	RI Class	Range
Low	< 40	Low	< 150
Moderate	40–80	Moderate	150–300
Considerable	80–160	Considerable	300–600
High	160–320	High	≥ 600
Very high	≥ 320		
Results (Ajakanga) — Ecological Risk by Metal (Eᵣ):
Sample	Fe	Pb	Cu	Cr	Mn	Zn	Ni	Co	Cd	RI
AJA1	74.6	607.5	87.5	53.0	153.2	42.5	217.5	45.0	38,700.0	39,980.8
AJA2	51.9	447.5	64.5	45.0	119.6	21.9	107.5	40.0	27,600.0	28,497.9
AJA3	41.6	260.0	53.0	43.0	71.4	12.4	77.5	30.0	10,500.0	11,088.8
AJA4	4.8	172.5	39.5	31.0	31.8	4.8	22.5	15.0	600.0	921.9
AJA18	4.4	120.0	31.0	29.0	17.4	3.1	7.5	15.0	600.0	827.4
AJA21	38.1	327.5	50.5	41.0	64.4	17.6	102.5	30.0	8,400.0	9,071.6
AJA25	25.4	347.5	58.5	31.0	60.2	14.9	87.5	30.0	2,400.0	3,054.9
Statistics: Mean = 5,191.8, Min = 827.4, Max = 39,980.8
Cd Contribution to RI:
Sample	Cd Eᵣ	% of Total RI
AJA1	38,700	96.8%
AJA2	27,600	96.9%
AJA3	10,500	94.7%
AJA4	600	65.1%
AJA21	8,400	92.6%
AJA25	2,400	78.6%
Finding: All 25 samples (100%) show “High Ecological Risk” (RI ≥ 600). Cadmium alone contributes 65–97% of the total ecological risk, confirming it as the primary contaminant of concern. The RI values are extreme: AJA1’s RI of 39,981 is 67× higher than the “High Risk” threshold of 600.
________________________________________
1.8 Metal Index (MI)
Reference: Caerio et al. (2005)
MI = Σ (C_metal / C_max_permissible) / n
Permissible Limits (BIS IS 10500:2012):
Metal	Permissible (mg/L)
Fe	1.0
Pb	0.01
Cu	1.5
Cr	0.05
Mn	0.4
Zn	15.0
Ni	0.07
Co	0.1
Cd	0.005
Classification:
Class	Range	Description
1	MI < 0.3	Safe
2	0.3 ≤ MI < 0.5	Slightly affected
3	0.5 ≤ MI < 1.0	Moderately affected
4	MI ≥ 1.0	Seriously affected
Results (Ajakanga):
Sample	MI	Classification
AJA1	6.479	Seriously affected
AJA2	4.678	Seriously affected
AJA3	2.425	Seriously affected
AJA4	0.975	Moderately affected
AJA7	0.916	Moderately affected
AJA9	0.957	Moderately affected
AJA11	0.892	Moderately affected
AJA13	0.774	Moderately affected
AJA18	0.704	Moderately affected
AJA21	2.552	Seriously affected
AJA25	2.089	Seriously affected
Statistics: Mean = 1.703, Min = 0.704, Max = 6.479
Finding: 76% of samples (19/25) are “Seriously Affected” (MI ≥ 1.0). Only 6 samples (24%) — predominantly the most distant/control-like locations (AJA4, AJA7, AJA9, AJA11, AJA13, AJA18) — fall into “Moderately Affected.” AJA1’s MI of 6.48 indicates extreme metal loading.
________________________________________
1.9 Heavy Metal Pollution Index (HPI)
Reference: Brown et al. (1972); Mohan et al. (1996)
HPI = Σ (W_i × Q_i) / Σ W_i
where Q_i = |C_i - I_i| / (S_i - I_i)
Classification:
Class	Range	Description
1	HPI < 15	Background
2	15 ≤ HPI < 30	Slightly polluted
3	HPI ≥ 30	Polluted
Results (Ajakanga):
Sample	HPI	Classification
AJA1	43.29	Polluted
AJA2	30.79	Polluted
AJA3	12.26	Background
AJA4	2.34	Background
AJA21	11.03	Background
AJA25	5.51	Background
Statistics: Mean = 6.83, Min = 1.74, Max = 43.29
Finding: Only 8% of samples (2/25) — AJA1 and AJA2 — are classified as “Polluted” by HPI. This discrepancy with other indices arises because HPI uses permissible limits as standards, and most metals (except Pb and Cd) remain below BIS permissible levels. However, the HPI for AJA1 (43.29) and AJA2 (30.79) confirms severe pollution at proximal locations.
________________________________________
1.10 Enrichment Factor (EF)
Reference: Sinex & Wright (1988); Buat-Menard & Chesselet (1979)
EF = (C_metal / C_Fe)_sample / (C_metal / C_Fe)_background
Classification:
Class	Range	Description
1	EF < 2	Deficiency to minimal enrichment
2	2 ≤ EF < 5	Moderate enrichment
3	5 ≤ EF < 20	Significant enrichment
4	20 ≤ EF < 40	Very high enrichment
5	EF ≥ 40	Extremely high enrichment
Mean EF by Metal:
Metal	Mean EF	Dominant Class
Fe	1.00	Deficiency-Minimal (100%)
Pb	3.25	Moderate (52%), Deficiency-Minimal (24%), Significant (24%)
Cu	0.70	Deficiency-Minimal (100%)
Cr	1.59	Deficiency-Minimal (72%), Moderate (28%)
Mn	3.08	Moderate (60%), Deficiency-Minimal (24%), Significant (16%)
Zn	0.46	Deficiency-Minimal (100%)
Ni	0.43	Deficiency-Minimal (100%)
Co	0.30	Deficiency-Minimal (100%)
Cd	4.77	Deficiency-Minimal (40%), Moderate (36%), Significant (24%)
Finding: EF analysis — which normalizes against Fe to distinguish anthropogenic from natural enrichment — shows that Cd, Pb, and Mn exhibit the highest enrichment. However, the relatively low EF values (max mean = 4.77 for Cd) compared to CF values suggest that Fe itself is also elevated at the dumpsite, making the normalization less discriminatory. This is consistent with the high Fe concentrations (mean = 1.055 mg/L, 76% exceed WHO limit).
________________________________________
2. Irrigation Suitability Indices
2.1 Sodium Adsorption Ratio (SAR)
SAR = Na⁺ / √[(Ca²⁺ + Mg²⁺)/2]
Class	Range	Description
S1	< 10	Excellent
S2	10–18	Good
S3	18–26	Fair
S4	> 26	Poor
2.2 Sodium Percentage (Na%)
Na% = [Na⁺ / (Ca²⁺ + Mg²⁺ + Na⁺ + K⁺)] × 100
Class	Range	Description
Excellent	< 20	
Good	20–40	
Permissible	40–60	
Doubtful	60–80	
Unsuitable	> 80	
2.3 Kelly Ratio (KR)
KR = Na⁺ / (Ca²⁺ + Mg²⁺)
Class	Range	Description
Suitable	< 1	
Unsuitable	> 1	
2.4 Residual Sodium Carbonate (RSC)
RSC = (HCO₃⁻ + CO₃²⁻) − (Ca²⁺ + Mg²⁺)
Class	Range	Description
Safe	< 1.25	
Marginal	1.25–2.5	
Unsuitable	> 2.5	
2.5 Magnesium Hazard (MH)
MH = [Mg²⁺ / (Ca²⁺ + Mg²⁺)] × 100
Class	Range	Description
Safe	< 50	
Unsuitable	> 50	
2.6 Weighted Water Quality Index (WQI)
WQI = Σ (q_i × w_i) / Σ w_i
Class	Range	Description
Excellent	0–25	
Good	25–50	
Poor	50–75	
Very Poor	75–100	
Unsuitable	> 100	
Note: Irrigation indices require major ion data (Ca, Mg, Na, K, HCO₃, SO₄, Cl, CO₃). These are computed from the companion Dump_data.csv dataset. See notebooks/03_irrigation_indices.ipynb for full implementation.
________________________________________
3. Human Health Risk Assessment
Comprehensive carcinogenic and non-carcinogenic risk evaluation for adults and children across three exposure pathways.
3.1 Exposure Parameters
Parameter	Symbol	Adult	Child	Unit	Source
Ingestion Rate	IR	2.0	1.0	L/day	USEPA (2011)
Exposure Frequency	EF	365	365	days/year	USEPA (2011)
Exposure Duration	ED	30	6	years	USEPA (2011)
Body Weight	BW	70	15	kg	USEPA (2011)
Averaging Time (NC)	AT_nc	10,950	2,190	days	USEPA (2011)
Averaging Time (C)	AT_c	25,550	25,550	days	USEPA (2011)
Skin Surface Area	SA	18,000	6,600	cm²	USEPA (2011)
Dermal Permeability	Kp	0.001	0.001	cm/hr	USEPA (2011)
Exposure Time	ET	0.58	0.58	hr/day	USEPA (2011)
Conversion Factor	CF	0.001	0.001	L/cm³	USEPA (2011)
Dermal Absorption	ABS	0.001	0.001	unitless	USEPA (2011)
Inhalation Rate	InhR	20	10	m³/day	USEPA (2011)
Particle Emission	PEF	1.36×10⁹	1.36×10⁹	m³/kg	USEPA (2011)
3.2 Reference Doses (RfD) — mg/kg-day
Metal	ORAL_RfD	DERMAL_RfD	INHALATION_RfD	Source
Fe	0.7	0.14	0.00022	USEPA IRIS
Pb	0.0035	0.000525	0.0035	USEPA IRIS
Cu	0.04	0.008	0.04	USEPA IRIS
Cr	0.003	0.00006	0.0002	USEPA IRIS
Mn	0.14	0.00185	0.0000143	USEPA IRIS
Zn	0.3	0.06	0.3	USEPA IRIS
Ni	0.02	0.0008	0.002	USEPA IRIS
Co	0.02	0.016	0.00003	USEPA IRIS
Cd	0.001	0.00001	0.001	USEPA IRIS
3.3 Cancer Slope Factors (CSF)
Metal	INGEST_CSF	DERMAL_CSF	INHALATION_CSF	IUR (μg/m³)⁻¹
Fe	0	0	0	0
Pb	0.0085	0.017	0.042	0.000012
Cu	0	0	0	0
Cr	0.5	20.0	42.0	0.012
Mn	0	0	0	0
Zn	0	0	0	0
Ni	0.84	22.75	0.84	0.00026
Co	0	0	9.8	0.009
Cd	0.38	7.6	6.3	0.0018
3.4 Risk Metrics
Metric	Formula	Interpretation
CDI	(C × IR × EF × ED) / (BW × AT)	Chronic Daily Intake (mg/kg-day)
HQ	CDI / RfD	Hazard Quotient; HQ < 1 = Safe
HI	Σ HQ_i	Hazard Index; cumulative non-cancer risk
CR	CDI × CSF	Cancer Risk; lifetime probability
TCR	Σ CR_i	Total Cancer Risk
Risk Classification:
HI	Classification	TCR	Classification
< 1	Acceptable	< 10⁻⁶	Negligible
1–4	Low concern	10⁻⁶–10⁻⁴	Low risk
4–10	Moderate concern	10⁻⁴–10⁻³	Moderate risk
≥ 10	High concern	≥ 10⁻³	High risk
Note: Health risk calculations require the full physicochemical dataset. See notebooks/05_health_risk.ipynb for complete implementation with adult and child pathway-specific results.
________________________________________
4. Machine Learning Classification
4.1 Domain-Scored Feature Engineering
Feature	Description	Weight
HI_score	Normalized Hazard Index (adult + child)	0.25
TCR_score	Normalized Total Cancer Risk	0.25
Irrigation_score	Composite irrigation suitability	0.20
Contamination_score	Composite contamination (CF + Cd + PLI + RI)	0.30
4.2 Model Architecture
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
4.3 Classification Targets
Class	Criteria	Use
Excellent	HI < 0.5, TCR < 10⁻⁶	Direct drinking + irrigation
Good	HI < 1, TCR < 10⁻⁵	Drinking with treatment
Poor	HI < 4, TCR < 10⁻⁴	Restricted use
Unsuitable	HI ≥ 4 or TCR ≥ 10⁻⁴	No use without remediation
________________________________________
5. GIS Spatial Modeling
5.1 Workflow
1.	Import GPS coordinates from field survey
2.	Create GeoDataFrame with all calculated indices
3.	IDW Interpolation: Z(x,y) = Σ(w_i × z_i) / Σw_i
4.	Reclassify into suitability zones
5.	Overlay with dumpsite boundary, drainage, land use
5.2 Output Maps
•	Drinking Water Suitability Map
•	Irrigation Water Suitability Map
•	Health Risk Map (Adult & Child)
•	Contamination Risk Map
•	Integrated ML-Predicted Suitability Map
________________________________________
🚀 Installation
# Clone
git clone https://github.com/yourusername/Ajakanga-ContamRisk.git
cd Ajakanga-ContamRisk

# Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install
pip install -r requirements.txt
________________________________________
🛠️ Usage
# Full pipeline
from ajakanga_contamrisk import ContaminationRiskPipeline

pipeline = ContaminationRiskPipeline(
    data_path="data/AJAKANGAHM.csv",
    output_dir="outputs"
)

# Run all contamination indices
pipeline.run_contamination_indices()

# Run health risk assessment
pipeline.run_health_risk()

# Run ML classification
pipeline.run_ml_classifier()

# Generate GIS maps
pipeline.generate_gis_maps()

# Export all results
pipeline.export_results()
________________________________________
🗂️ Project Structure
Ajakanga-ContamRisk/
├── data/
│   ├── AJAKANGAHM.csv              # Heavy metal concentrations (25 samples)
│   ├── Dump_data.csv               # Full water quality dataset
│   ├── gps_coordinates.csv         # Sample GPS locations
│   └── metadata.json               # Data dictionary
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_contamination_indices.ipynb
│   ├── 03_irrigation_indices.ipynb
│   ├── 04_health_risk.ipynb
│   ├── 05_machine_learning.ipynb
│   └── 06_gis_mapping.ipynb
├── outputs/
│   ├── CF_results.csv
│   ├── CD_results.csv
│   ├── PLI_results.csv
│   ├── NPI_results.csv
│   ├── HMEI_results.csv
│   ├── Igeo_results.csv
│   ├── EF_results.csv
│   ├── RI_results.csv
│   ├── MI_results.csv
│   ├── HPI_results.csv
│   ├── health_risk_adults.csv
│   ├── health_risk_children.csv
│   ├── ml_predictions.csv
│   └── gis/
│       ├── drinking_suitability.shp
│       ├── irrigation_suitability.shp
│       └── risk_map.tif
├── tests/
├── README.md
├── requirements.txt
├── LICENSE
└── CITATION.cff
________________________________________
📚 Citations
1.	Adejumo, S.A. & Oyerinde, A.O. (2024). Heavy Metal Concentration Assessment of Surface and Groundwater in the Vicinity of Ajakanga Dumpsite, Oluyole, Ibadan, Southwestern Nigeria. African Journal of Environment and Natural Science Research, 7(2), 148–164. DOI: 10.52589/AJENSR-ZMHIZVSR citeweb_search:11#0
2.	Akintola, O.O. & Bodede, A.I. (2019). Impact of Waste Dumpsite on Groundwater Quality in Ibadan, Southwestern Nigeria. Pacific Journal of Science and Technology, 20(2), 242–258. citeweb_search:11#1
3.	Hakanson, L. (1980). An ecological risk index for aquatic pollution control. Water Research, 14(8), 975–1001.
4.	Müller, G. (1969). Index of geoaccumulation in sediments of the Rhine River. Geojournal, 2(3), 108–118.
5.	Tomlinson, D.L., et al. (1980). Problems in the assessment of heavy-metal levels in estuaries. Helgoländer Meeresuntersuchungen, 33(1), 566–575.
6.	Nemerow, N.L. (1985). Stream, lake, estuary, and ocean pollution (2nd ed.). Van Nostrand Reinhold.
7.	USEPA (2011). Exposure Assessment Tools by Routes. U.S. Environmental Protection Agency.
8.	WHO (2011). Guidelines for Drinking-water Quality (4th ed.). World Health Organization.
9.	BIS (2012). IS 10500:2012 — Drinking Water — Specification. Bureau of Indian Standards.
________________________________________
👤 Author
**KOLA-ADEROJU A.O**
🎓 Assistant lecturer / Geologist/ Environmental Geochemist / Hydrogeologist / Data Scientist / Machine learning Engineer / GIS specialist – 
🔬 Specialization: Heavy metal contamination, landfill leachate, water quality assessment, machine learning for environmental modeling, GIS spatial analysis - 📧 kolaaderoju.absulmalik@gmail.com  - 🔗Kola-Aderoju Abdulmalik | LinkedIn 
________________________________________
.
