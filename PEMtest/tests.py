import scipy.stats as st
from PEMtest.pem import pemtest_class

W = st.norm(2,7)
X = W.rvs(size=15000)

pemtest_object = pemtest_class(sample=X)
print(pemtest_object.pemtest())
pemtest_object.plot()