import matplotlib.pyplot as plt
import streamlit as st
plt.style.use("seaborn")

def draw_vogel(ins):
    q= ins[0]
    p = ins[1]
    fig ,ax = plt.subplots(1,1)
    ax.plot(q,p)
    fig.suptitle("Voggel model With FE=1")
    ax.set_ylabel("Pressure (psi)");
    ax.set_xlabel("Rate (bbls/day)");
    st.pyplot(fig,use_container_width=True)

def draw_fes(ins):
    qs= ins[0]
    ps = ins[1]
    fig ,ax = plt.subplots(1,1)
    for i in range(len(qs)):
        ax.plot(qs[i],ps[i])
    fig.suptitle("Voggel model With FE != 1")
    ax.set_ylabel("Pressure (psi)");
    ax.set_xlabel("Rate (bbls/day)");
    st.pyplot(fig,use_container_width=True)

def draw_future(data):
    fig, ax = plt.subplots(1, 1)
    for i, (x, y, label) in enumerate(data):
        ax.plot(data[i][0],data[i][1], label=data[i][2])
    fig.suptitle("Voggel model With FE = 1")
    ax.set_ylabel("Pressure (psi)");
    ax.set_xlabel("Rate (bbls/day)");
    ax.legend()
    st.pyplot(fig, use_container_width=True)

def draw_future_fe(data):
    fig, ax = plt.subplots(1, 1)
    for i, (x, y, label) in enumerate(data):
        ax.plot(data[i][0],data[i][1], label=data[i][2])
    fig.suptitle("Voggel model With FE != 1")
    ax.set_ylabel("Pressure (psi)");
    ax.set_xlabel("Rate (bbls/day)");
    ax.legend()
    st.pyplot(fig, use_container_width=True)

