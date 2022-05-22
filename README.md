# PEM test library

### Installation
```py
pip install pemtest
```

### What is PEM test?
> When performing data analysis, sometimes people come across a problem of checking null hypothesis for normality without knowing parameters of the distribution. 
In this case we should use tests like "Parameters Elimination Method". PEM test allows us to get rid of `mu` and `sigma^2` and move from performing a test for normality to 
performing a test for uniform distribution with parameters 0, 1.

### Looks hard. Will there be any further explanation?
> Yes. You can read full documentation on the algorithm based on PEM test **[here](https://github.com/turkunov/pem-test/blob/main/algorithm_documentation.ipynb)**.

### Are there any examples?
> Yes, here's an interactive notebook with examples: https://colab.research.google.com/drive/15SR2hJpejqQ8G-I0SXk-WZMZUpsbUdAC?usp=sharing

### Who is the author of this algorithm?
> [turkunov @ Github](https://github.com/turkunov) (me). The algorithm is based on the research done by Sarkadi K. in "On testing for normality" (1960) [p. 269-275].

