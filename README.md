# WindFarmTwin 🌬️⚡

**Light-weight digital twin for wind-farm layout & yaw optimisation**

This project combines  
* 🌀 CFD (OpenFOAM) to generate high-fidelity wake-loss data  
* 🤖 Machine-learning surrogates for 100× faster layout what-ifs  
* 📊 Streamlit dashboard so planners can tweak turbine spacing, yaw and instantly see power output & wake contours

> **Status:** Week 1 — repo skeleton & environment. Follow our [Roadmap](#roadmap).

## Roadmap
- **Week 1:** Repo skeleton, Conda env, fetch first open wind dataset
- Week 2: Run two baseline OpenFOAM cases (on Triton?)
- Week 3: Train & validate surrogate model
- Week 4: Build Streamlit UI
- Week 5: Docs, tests, CI, deploy
- Week 6: Polish & write blog post

## TODO (Week 1)

- [x] Project skeleton & env file
- [x] Fetch sample wind-speed dataset (NREL WIND Toolkit covers US lat/lon only; use the ERA5 script for other regions.)
- [x] EDA notebook
- [x] Local debug CFD case converged
- [x] Requested computing resources on Triton



