import streamlit as st   
import scipy.stats
import time
import pandas as pd 

if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0 

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])
st.header('Tossing a Coin')

chart = st.line_chart([0.5])
def toss_coin:
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial outcomes: 
        outcome_no +=1
        if r == 1: 
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        times.sleep(0.05)

    return mean 

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f"Running the experiment of {number_of_trials} trials")
    mean = toss_coint(number_of_trials)

