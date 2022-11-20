import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress as lr
import streamlit as st

plt.style.use("seaborn")
# -------------------------------------- seting configration -------------------
st.set_page_config(page_title="Jones-IPR")

class Jones:
    def __init__(self, Pr, test_points: list):
        """
        test_points : list of tuples of each is (q,pwf)
        """
        self.pr = Pr
        self.test_points = test_points
        self.a = None
        self.b = None
        self.result = None

    # get the n value from regression
    def get_a_b(self):
        # separate the data
        q = np.array([i[0] for i in self.test_points])
        pwf = np.array([i[1] for i in self.test_points])
        # get ( pr - pwf) / q
        y = (self.pr - pwf) / q
        # fit the data
        self.result = lr(x=q, y=y)
        self.a = self.result.intercept
        self.b = self.result.slope

    # draw the ipr
    def draw(self):
        Pwf = [self.pr]
        Q = [0]
        step = 20
        for p in range(int(self.pr - step), 0, -20):
            Pwf.append(p - 15)
            aa = np.power(self.a, 2) + 4 * self.b * (self.pr - p)
            aa = np.power(aa, .5)
            q = (-self.a + aa) / (2 * self.b)
            Q.append(q)
        return [Q, Pwf]

    # main funcion
    def main(self):
        self.get_a_b()
        data = self.draw()
        return data


    # take inputs
st.write("# Jones IRP")
st.markdown("""
- Reservoir pressure  `psi`
- Choose the number of test points
- input test points data ( Q , Pwf )
""")
pr = st.number_input("Reservoir pressure `psi`")
ts = int(st.number_input("Number of test points",min_value=1,max_value=10))
col1,col2 = st.columns(2)
Qs = [0 for i in range(ts) ]
Ps = [0 for i in range(ts) ]
for i in range(ts) :
    with col1:
        Qs[i]= st.number_input(f"Q ({i+1}) bbls/day")
    with col2:
        Ps[i] = st.number_input(f"Pwf ({i+1})  psi")
# combine the data
points = list(zip(Qs,Ps))
try:
    J = Jones(pr,points)
    data_J = J.main()
    # draw
    q= data_J[0]
    p = data_J[1]
    fig ,ax = plt.subplots(1,1)
    ax.plot(q,p)
    fig.suptitle("Jones etal model")
    ax.set_ylabel("Pressure");
    ax.set_xlabel("Rate");
    st.pyplot(fig,use_container_width=True)
except:
    st.info("Enter all the required data")

#--------------------------- hide the footer ------------------------------
hid_menu_bar = """
<style>
#MainMenu {visibility : hidden;}
footer {visibility : hidden;}
</style>
"""
st.markdown(hid_menu_bar,unsafe_allow_html=True)



