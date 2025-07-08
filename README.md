# Light-weight digital twin for wind-farm layout & yaw optimisation

This project combines  
* 🌀 **CFD** (OpenFOAM) — generates high-fidelity wake-loss data  
* 🤖 **ML surrogates** — 100 × faster “what-if” layout sweeps  
* 📊 **Streamlit dashboard** — planners drag spacing / yaw sliders and instantly see power & wake contours

> **Status:** Week 2 — cloud VM online, first OpenFOAM test run next.

---

## Roadmap (July → Aug 2025)

| Week | Goal | Progress |
|------|------|----------|
| **W 1** | repo + Conda env · ERA5 sample · local debug case | ✅ done |
| **W 2** | ─ request Triton access<br>─ spin-up GCP spot VM<br>─ run *one* baseCase on 16 vCPU | ▶ Triton request **sent**<br>▶ **VM created** (`wf-twin`, e2-standard-16) |
| **W 3** | 9-case yaw × spacing sweep on GCP · post-process to `cfd_results.csv` | ☐ |
| **W 4** | train & validate first surrogate (model = Random Forest / small MLP) | ☐ |
| **W 5** | build Streamlit UI (sliders + wake plot) · add unit tests & CI | ☐ |
| **W 6** | polish docs · write Medium/GitHub blog post | ☐ |

---

## TODO (this sprint)

- [x] Repo skeleton & env file  
- [x] ERA5 downloader + EDA notebook  
- [x] Local debug CFD case converged  
- [x] Triton visitor request sent  
- [x] Google Cloud trial activated, 16-core VM up  
- [x] Install OpenFOAM on VM (`apt install openfoam10`)  
- [x] Run single baseCase on VM  
- [ ] Duplicate 9 yaw/spacing cases (`clone_9cases.sh`)  
- [ ] Push `cfd_results.csv` and update Readme

---

### Usage (coming soon)

```bash
conda env create -f environment.yml
conda activate windfarm-twin
streamlit run app.py      # placeholder dashboard

