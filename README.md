# Universiti Malaya WQD7009 Big Data Applications and Analytics

This repo is served as the main code to be deployed into MS Azure's Virtual Machines Cluster for SVD machine learning purposes.

# How To

We recommend the usage of miniconda or pyenv to run the streamlit application. 

For Windows user, please run the following scripts accordingly to start streamlit server:
- pip install -r requirements.txt
- python start.py
- streamlit run app.py

For Mac/Linux user, the process is automated. Sinmply run the following command to start streamlit server:
- make start

You may tweak the `./streamlit/config.toml` to edit:
- Theme Setting
- Server Setting
- Browser Behavior Setting

# Credits
- MovieLens 1M Dataset - https://grouplens.org/datasets/movielens/1m/
- Tutorial Guide - https://analyticsindiamag.com/singular-value-decomposition-svd-application-recommender-system/
