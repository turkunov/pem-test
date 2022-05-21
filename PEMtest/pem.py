from random import randint
from math import sqrt
import scipy.stats as st
from time import process_time
import matplotlib.pyplot as plt
import numpy as np

class pemtest_class:
    def __init__(self, sample: np.ndarray):
        self.sample = sample
        self.Fk = None
        self.pvalue = None

    def pvalue_distribution(self, number_of_tests: int):
        """
            pvalue_distribution() runs the PEM test `number_of_tests` times and then performs K-S test for uniform
            distribution on p-values distribution

            :param: number_of_tests - number of desired PEM tests applied to the sample

            :returns: matplotlib plot
        """
        pvalues = []
        for i in range(number_of_tests):
            start_test = process_time()
            pvalues.append(pemtest_class(self.sample).pemtest()['pvalue'])
            print(f'Test performed {i+1} time(s) ({process_time()-start_test}s)')
        ks_test = st.kstest(pvalues, 'uniform', args=(0, 1))
        plt.hist(pvalues, bins=50, density=True, edgecolor='black', label=r"$P_{value}$s distribution")
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True)
        plt.title(r'$\rho_{value}$ =' + f' {ks_test[ 1 ]}')
        plt.show()


    def plot(self):
        """
            plot() plots sample distribution alongside with Fk value distribution and p-value

            :returns: matplotlib plot
        """
        if self.pvalue is not None:
            figure, axis = plt.subplots(2)
            axis[ 0 ].hist(self.sample, bins=50, density=True, edgecolor='black', label="Sample distribution")
            axis[ 0 ].legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True)
            W2 = st.uniform()
            z = np.linspace(0, 1, 1000)
            y = W2.pdf(z)
            axis[ 1 ].plot(z, y, label=r"PDF of $U([0,1])$")
            axis[ 1 ].hist(self.Fk, bins=50, density=True, edgecolor='black', label=r"$F_k$ distribution")
            axis[ 1 ].legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, ncol=2, shadow=True)
            figure.suptitle(r'$\rho _{value}$ =' + f' {self.pvalue}',fontsize=16)
            figure.tight_layout()
            plt.show()
        else:
            raise Exception('There\'s nothing to plot because the test hasn\'t been carried out yet')

    def pemtest(self, calculate_time: bool = False):
        """
            pemtest() performs a test for normality based on Parameter Elimination Method

            :param: calculate_time (optional) - returns time it took the function to finish

            :returns: dictionary with test statistic ('stat') and p-value ('pvalue') and execution time in seconds if
            needed
        """
        start_test = process_time()
        X = self.sample
        n = len(X)
        m = randint(0, n - 1)
        Xm = X[ m ]
        Am = np.sum(X) / (n + sqrt(n)) - Xm / (1 + sqrt(n))
        Yj = [ X[ j ] - Am if j < m - 1 else X[ j + 1 ] - Am for j in range(n - 1) ]
        Bk = [ 1 / (n - k - 1) * sum(list(map(lambda x: x ** 2, Yj[ k:n - 2 ]))) for k in range(n - 2) ]
        Zk = [ Yj[ k ] / sqrt(Bk[ k ]) for k in range(n - 2) ]
        Fk = np.array([ st.t.cdf(x=Zk[ k ], df=n - (k + 1) - 1) for k in range(len(Zk)) ])
        self.Fk = Fk
        ks_test = st.kstest(Fk, 'uniform', args=(0, 1))
        self.pvalue = ks_test[ 1 ]
        return {'stat': ks_test[ 0 ], 'pvalue': ks_test[ 1 ], 'execution_time': None if not calculate_time else process_time()-start_test}


