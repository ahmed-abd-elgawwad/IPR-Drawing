import streamlit as st

def vogel_ipr():
    col1,col2= st.columns(2)
    with col1:
        p = st.number_input("Reservoir pressure `psi`")
        pb = st.number_input("Bubble point pressure `psi`")
    with col2:
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")

    return [int(p),pb,pwf,Q,1000]


def saturated_fe():
    col1, col2= st.columns(2)
    with col1:
        p = st.number_input("Reservoir pressure `psi`")
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")
    with col2:
        fe = st.number_input("FE")

    return [int(p),pwf, Q,fe,20]


def saturated_fes():
    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Reservoir pressure `psi`")
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")
    with col2:
        fe = st.number_input("FE")
        fes = st.text_input("FE list")
        fes = [float(i) for i in fes.split()]
    return [int(p), pwf, Q, fe,fes, 20]


def undersaturated_fes():
    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Reservoir pressure `psi`")
        pb = st.number_input("Bubble point pressure `psi`")
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")
    with col2:
        fe = st.number_input("FE")
        fes = st.text_input("FE list")
        fes = [float(i) for i in fes.split()]
    return [int(p),pb ,pwf, Q, fe,fes, 20]

def saturated_future():
    col1, col2 , col3 = st.columns(3)
    with col1:
        st.markdown("#### Present data")
        Pp = st.number_input("reservoir pressure (P_resent) `psi`")
        vis_pre = st.number_input(" Vicosity prenset`cp`")
        beta_pres = st.number_input(" Bo present")
        per_pres = st.number_input("Kro present")
    with col2:
        st.markdown("#### Future data")
        Pf = st.number_input("reservoir pressure (P_future) `psi`")
        vis_f = st.number_input(" Vicosity future`cp`")
        beta_f = st.number_input(" Bo future ")
        per_f = st.number_input("Kro future")
    with col3:
        st.markdown("#### Stabilized Test")
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")

    return [int(Pp),int(Pf),vis_pre,beta_pres,per_pres,vis_f,beta_f,per_f,pwf,Q,20]


def undersaturated_future():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Present data")
        Pp = st.number_input("reservoir pressure (P_resent) `psi`")
        pb = st.number_input("bubble point pressure `psi`")
        vis_pre = st.number_input(" Vicosity prenset`cp`")
        beta_pres = st.number_input(" Bo present")
        per_pres = st.number_input("Kro present")
    with col2:
        st.markdown("#### Future data")
        Pf = st.number_input("reservoir pressure (P_future) `psi`")
        vis_f = st.number_input(" Vicosity future`cp`")
        beta_f = st.number_input(" Bo future ")
        per_f = st.number_input("Kro future")
    with col3:
        st.markdown("#### Stabilized Test")
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")

    return [int(Pp),int(pb), int(Pf), vis_pre, beta_pres, per_pres, vis_f, beta_f, per_f, pwf, Q, 20]


def saturated_future_fe():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Present data")
        Pp = st.number_input("reservoir pressure (P_resent) `psi`")
        fe = st.number_input("FE")
        vis_pre = st.number_input(" Vicosity prenset`cp`")
        beta_pres = st.number_input(" Bo present")
        per_pres = st.number_input("Kro present")
    with col2:
        st.markdown("#### Future data")
        Pf = st.number_input("reservoir pressure (P_future) `psi`")
        vis_f = st.number_input(" Vicosity future`cp`")
        beta_f = st.number_input(" Bo future ")
        per_f = st.number_input("Kro future")
    with col3:
        st.markdown("#### Stabilized Test")
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")

    return [int(Pp), int(Pf),fe, vis_pre, beta_pres, per_pres, vis_f, beta_f, per_f, pwf, Q, 20]


def undersaturated_future_fe():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Present data")
        Pp = st.number_input("reservoir pressure (P_resent) `psi`")
        pb = st.number_input("bubble point pressure `psi`")
        fe = st.number_input("FE")
        vis_pre = st.number_input(" Vicosity prenset`cp`")
        beta_pres = st.number_input(" Bo present")
        per_pres = st.number_input("Kro present")
    with col2:
        st.markdown("#### Future data")
        Pf = st.number_input("reservoir pressure (P_future) `psi`")
        vis_f = st.number_input(" Vicosity future`cp`")
        beta_f = st.number_input(" Bo future ")
        per_f = st.number_input("Kro future")
    with col3:
        st.markdown("#### Stabilized Test")
        pwf = st.number_input("Test Pwf `psi`")
        Q = st.number_input("Test Q `bbls/day`")

    return [int(Pp), int(Pf),int(pb),fe, vis_pre, beta_pres, per_pres, vis_f, beta_f, per_f, pwf, Q, 20]


