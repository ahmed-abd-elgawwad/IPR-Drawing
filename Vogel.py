from voggel import Vogel_DarcyIPR ,VogelIPR,vogel_fe_saturated,vogel_fe_saturated_fes,vogel_fe_undersaturated_fes
from voggel import vogel_future_saturated , vogel_future_undersaturated ,vogel_future_fe_saturated
from voggel import vogel_future_fe_undersaturated
import streamlit as st
from inputs import  vogel_ipr ,saturated_fe,saturated_fes,undersaturated_fes,saturated_future,undersaturated_future
from inputs import saturated_future_fe , undersaturated_future_fe
from draw import  draw_vogel,draw_fes,draw_future,draw_future_fe
# -------------------------------------- seting configration -------------------
st.set_page_config(page_title="Vogel-IPR")
#------------------------main model ----------
st.write("# Vogel IRP")
inputs={
    "General IPR with FE = 1":vogel_ipr,
    "Saturated Reseroir with FE != 1":saturated_fe,
    "Test Saturated Reservoir for different FE values":saturated_fes,
    "Test UnderSaturated Reservoir for different FE values":undersaturated_fes,
    "Future IPR for Saturated reservoir with FE = 1":saturated_future,
    "Future IPR for UnderSaturated reservoir with FE = 1":undersaturated_future,
    "Future IPR for Saturated reservoir with FE != 1":saturated_future_fe,
    "Future IPR for UnderSaturated reservoir with FE != 1":undersaturated_future_fe
}
functions={
    "General IPR with FE = 1":VogelIPR,
    "Saturated Reseroir with FE != 1":vogel_fe_saturated,
    "Test Saturated Reservoir for different FE values":vogel_fe_saturated_fes,
    "Test UnderSaturated Reservoir for different FE values":vogel_fe_undersaturated_fes,
    "Future IPR for Saturated reservoir with FE = 1":vogel_future_saturated,
    "Future IPR for UnderSaturated reservoir with FE = 1":vogel_future_undersaturated,
    "Future IPR for Saturated reservoir with FE != 1":vogel_future_fe_saturated,
    "Future IPR for UnderSaturated reservoir with FE != 1":vogel_future_fe_undersaturated
}
draws = {
    "General IPR with FE = 1":draw_vogel,
    "Saturated Reseroir with FE != 1":draw_vogel,
    "Test Saturated Reservoir for different FE values":draw_fes,
    "Test UnderSaturated Reservoir for different FE values":draw_fes,
    "Future IPR for Saturated reservoir with FE = 1":draw_future,
    "Future IPR for UnderSaturated reservoir with FE = 1":draw_future,
    "Future IPR for Saturated reservoir with FE != 1":draw_future_fe,
    "Future IPR for UnderSaturated reservoir with FE != 1":draw_future_fe

}

st.markdown("""
- Input the satbilized test data ( Pwf `psi` ,Qo `bbls/day` )
- Choose the condition
- input the required_data
""")
st.write("### Choose the condition")
cond = st.selectbox("choose",list(functions.keys()))
ins = inputs[cond]()
try:
    data = functions[cond](*ins)
    draws[cond](data)
except:
    st.info("enter the required data")

#--------------------------- hide the footer ------------------------------
hid_menu_bar = """
<style>
#MainMenu {visibility : hidden;}
footer {visibility : hidden;}
</style>
"""
st.markdown(hid_menu_bar,unsafe_allow_html=True)