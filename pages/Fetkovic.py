import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress as lr
import streamlit as st
plt.style.use("seaborn")
# -------------------------------------- seting configration -------------------
st.set_page_config(page_title="Fetkovic-IPR")

class FetkovicSaturated:
    def __init__(self, Pr, test_points: list):
        """
        test_points : list of tuples of each is (q,pwf)
        """
        self.pr = Pr
        self.test_points = test_points
        self.n = None
        self.c = None
        self.result = None

    # get the n value from regression
    def get_n(self):
        # check number of test points
        if len(self.test_points) == 1:
            self.n = 1
        else:
            # separate the data
            q = np.array([i[0] for i in self.test_points])
            pwf = np.array([i[1] for i in self.test_points])
            # square the difference
            pr_pwf_2 = np.power(self.pr, 2) - np.power(pwf, 2)
            # log values
            log_q = np.log10(q)
            self.log_q = log_q
            log_p = np.log10(pr_pwf_2)
            result = lr(x=log_q, y=log_p)
            self.n = round((1 / result.slope), 4)
            self.result = result

    def get_c(self):
        if not self.n:
            raise Exception("Get the (n) value first ")
        if len(self.test_points) == 1:
            p = self.test_points[0][1]
            q = self.test_points[0][0]
            pp = (np.power(self.pr, 2) - np.power(p, 2))
            self.c = q / pp
        else:
            a = self.result.slope
            b = self.result.intercept
            q = self.log_q.mean()
            p = b + q * a
            Pwf = (10 ** p)
            q = (10 ** q)
            c = q / (Pwf ** (self.n))
            self.c = c

    # draw the ipr
    def draw(self):
        Pwf = [self.pr]
        Q = [0]
        step = 20
        for p in range(int(self.pr - step), 0, -20):
            Pwf.append(p - 15)
            pp = (np.power(self.pr, 2) - np.power(p, 2))
            q = self.c * np.power(pp, self.n)
            Q.append(q)
        return [[Q, Pwf,"Present"]]

    # main funcion
    def main(self):
        self.get_n()
        self.get_c()
        data = self.draw()
        return data

# --------------------------------------------- future for Fetkovich -----------------------------------
class Future_Fetkovic(FetkovicSaturated):
    def __init__(self, Pr, test_points: list,Prf):
         # initalize the orginal model
        super().__init__(Pr, test_points)
        self.prf = Prf
        self.new_c = None
    def get_new_c(self):
        if not self.c :
            raise Exception("You must get c_present first")
        self.new_c = self.c * (self.prf / self.pr)
    def draw_future(self):
        if not self.new_c:
            raise Exception("Get the c_present value first")
        Pwf = [self.prf]
        Q = [0]
        step = 20
        for p in range(int(self.prf - step), 0, -20):
            Pwf.append(p - 15)
            pp = (np.power(self.prf, 2) - np.power(p, 2))
            q = self.new_c * np.power(pp, self.n)
            Q.append(q)
        return [Q, Pwf]
    def main(self):
        self.get_n()
        self.get_c()
        self.get_new_c()
        data1 = self.draw()
        data2= self.draw_future()
        return [[*data1[0],"Present"],[*data2,"Future"]]

# --------------------------------------------- take inputs ---------------------------------
st.write("# Saturated Fetkovic IRP")
st.markdown("""
- Reservoir pressur  `psia`
- Choose the number of test points
- input test points data ( Q , Pwf )
""")
condition = st.selectbox("Select condition to draw",["Present_IPR","Present & Future IPR"])
pr = st.number_input("Reservoir pressure `psia`")
if condition == "Present & Future IPR":
    prf = st.number_input("Future Reservoir pressure `psia`")
ts = int(st.number_input("Number of test points",min_value=1,max_value=10))
col1,col2 = st.columns(2)
Qs = [0 for i in range(ts) ]
Ps = [0 for i in range(ts) ]
for i in range(ts) :
    with col1:
        Qs[i]= st.number_input(f"Q ({i+1}) bbls/day")
    with col2:
        Ps[i] = st.number_input(f"Pwf ({i+1})  psia")
# combine the data
points = list(zip(Qs,Ps))
#
# try :
if condition == "Present_IPR":
    F = FetkovicSaturated(pr,points)
else :
    F = Future_Fetkovic(pr,points,prf)
data = F.main()
# draw
fig ,ax = plt.subplots(1,1)
for lis in data:
    q = lis[0]
    p = lis[1]
    l = lis[2]
    ax.plot(q,p,label=l)
fig.suptitle("Fetkovic model")
ax.set_ylabel("Pressure");
ax.set_xlabel("Rate");ax.legend()
st.pyplot(fig,use_container_width=True)
# except:
#     st.info("Enter all the required data")



# #--------------------------- hide the footer ------------------------------
# hid_menu_bar = """
# <style>
# #MainMenu {visibility : hidden;}
# footer {visibility : hidden;}
# </style>
# """
# st.markdown(hid_menu_bar,unsafe_allow_html=True)



