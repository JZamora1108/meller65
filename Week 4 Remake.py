{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Week 4 Jesse Zamora\n",
                "\n",
                "http://thinkstats2.com\n",
                "\n",
                "Copyright 2016 Allen B. Downey\n",
                "\n",
                "MIT License: https://opensource.org/licenses/MIT\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Exercise 3.1: \n",
                "Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.\n",
                "\n",
                "Use the NSFG respondent variable numkdhh to construct the actual distribution for the number of children under 18 in the respondents' households."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 19,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": "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\n",
                        "text/plain": [
                            "<Figure size 432x288 with 1 Axes>"
                        ]
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                }
            ],
            "source": [
                "from __future__ import print_function, division\n",
                "\n",
                "%matplotlib inline\n",
                "\n",
                "import numpy as np\n",
                "\n",
                "import nsfg\n",
                "import first\n",
                "import thinkstats2\n",
                "import thinkplot\n",
                "\n",
                "resp = nsfg.ReadFemResp()\n",
                "pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')\n",
                "thinkplot.Pmf(pmf)\n",
                "thinkplot.Config(xlabel='# of children under 18', ylabel='Probability')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 20,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEJCAYAAACOr7BbAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAdvklEQVR4nO3df5xVdb3v8dc7fgphdYA6HsDgJgpkA9IIdvCqcAsdj8fRNMGblRqXB94oqkfduD2OHj2e+0i9mamoI4+kzJOCHeMcbuGvtHMNxWRQGgShCEnnYg9GTYUUYfJz/1hrbLNZM3vPsNfsmfH9fDzmMXut9f2u/dnjQ957fdda36WIwMzMrNi7ql2AmZn1TA4IMzPL5IAwM7NMDggzM8vkgDAzs0wOCDMzy5RrQEg6TdJWSdskLe6g3fGS/izp3M72NTOzfOQWEJL6ATcBdcAk4HxJk9ppdzVwf2f7mplZfvrnuO9pwLaI2A4gaTlQD2wuavdF4B7g+C70PcCIESNi7NixFSnezOydYP369S9GxMisbXkGxCjg+YLlZmB6YQNJo4CzgVkcGBAl+2YZO3YsjY2NXa3XzOwdR9Lv29uW5zkIZawrntfju8A3IuLPXeibNJTmS2qU1NjS0tKFMs3MLEueRxDNwJiC5dHAzqI2tcBySQAjgNMltZbZF4CIWAosBaitrfXEUmZmFZJnQKwDxksaB/w/YC7wXwsbRMS4tteSfgD8NCL+TVL/Un3NzCxfuQVERLRKWkhydVI/YFlEbJK0IN3e0Nm+edVqZj3b/v37aW5uZu/evdUupdcaPHgwo0ePZsCAAWX3UV+a7ru2tjZ8ktqs73n22WcZNmwYw4cPJx2Stk6ICF566SV2797NuHHjDtgmaX1E1Gb1853UZtbj7d271+FwCCQxfPjwTh+BOSDMrFdwOByarvz98jxJbdZl//7wr1lxbyNv7ttf7VIqYtDAAcypq6V+1uRql2JWNh9BWI/Ul8IB4M19+1lxr8+P9TU7duzg2GOPrXYZBznllFMqctOwA8J6pL4UDm364meyymttba12CW/zEJP1ePdcv6DaJRyScxa1e0W39TLf+c53WLZsGQDz5s3jrLPOorW1lc997nM89dRTHH300fzwhz9kyJAhLF68mFWrVtG/f39mz57Nt7/9bVpaWliwYAHPPfccAN/97neZMWMGl19+OTt37mTHjh2MGDGC3/3udyxbtowPf/jDQHJEcO211zJhwgS++MUvsnHjRlpbW7n88supr6/njTfe4KKLLmLz5s1MnDiRN954oyKf1wFhZr1KnoHb0ZeR9evX8/3vf59f/epXRATTp0/n5JNPZuvWrdx2223MmDGDiy++mJtvvpmLL76YlStXsmXLFiTxyiuvALBo0SK+8pWvcOKJJ/Lcc89x6qmn8swzz7y9/zVr1nDYYYdx3XXXcffdd3PFFVfwwgsvsHPnTj760Y/yzW9+k1mzZrFs2TJeeeUVpk2bxsc//nFuvfVWhgwZQlNTE01NTUydOrUifw8PMZmZlWHNmjWcffbZDB06lHe/+9188pOf5Je//CVjxoxhxowZAFxwwQWsWbOGww8/nMGDBzNv3jx+8pOfMGTIEAB+/vOfs3DhQqZMmcKZZ57Ja6+9xu7duwE488wzOeywwwA477zz+PGPfwzA3Xffzac+9SkAHnjgAa666iqmTJnCKaecwt69e3nuued45JFHuOCCCwCoqamhpqamIp/ZRxBmZmVo76bi4stHJdG/f3+eeOIJHnroIZYvX86SJUt4+OGHeeutt1i7du3bQVBo6NChb78eNWoUw4cPp6mpiRUrVnDrrbe+XcM999zDMcccU7KOSnBAmFmvUq1zUieddBIXXnghixcvJiJYuXIld9xxB4sWLWLt2rV87GMf46677uLEE09kz549vP7665x++umccMIJHHXUUQDMnj2bJUuW8PWvfx2ADRs2MGXKlMz3mzt3Ltdccw2vvvoqH/nIRwA49dRTufHGG7nxxhuRxFNPPcVxxx3HSSedxI9+9CNmzpzJ008/TVNTU0U+s4eYzMzKMHXqVC688EKmTZvG9OnTmTdvHu973/uYOHEit99+OzU1Nbz88stccskl7N69mzPOOIOamhpOPvlkrrvuOgBuuOEGGhsbqampYdKkSTQ0tH8+5dxzz2X58uWcd955b6+79NJL2b9/PzU1NRx77LFceumlAFxyySXs2bOHmpoarrnmGqZNm1aRz+y5mKxHKjwR2ZeuYurtn6VannnmGSZOnFjtMnq9rL+j52IyM7NOc0CYmVkmB4SZ9Qp9aTi8Grry93NAmFmPN3jwYF566SWHRBe1PQ9i8ODBnerny1zNrMcbPXo0zc3N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\n",
                        "text/plain": [
                            "<Figure size 432x288 with 1 Axes>"
                        ]
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                }
            ],
            "source": [
                "def BiasPmf(pmf, label):\n",
                "    new_pmf = pmf.Copy(label=label)\n",
                "\n",
                "    for x, p in pmf.Items():\n",
                "        new_pmf.Mult(x, x)\n",
                "        \n",
                "    new_pmf.Normalize()\n",
                "    return new_pmf\n",
                "biased_pmf = BiasPmf(pmf, label = 'observed')\n",
                "thinkplot.Pmf(biased_pmf)\n",
                "thinkplot.Config(xlabel='# of children under 18', ylabel='Probability')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Plot the actual and biased distributions, and compute their means."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 21,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAEGCAYAAABo25JHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAc4klEQVR4nO3df5xVdb3v8deb32hoCZyuAgUXReWBI+DwQ0EFNRSPgiYK3bTQvKY3TqTZPd48lt5++OOWlpq/yl9ZR9CQtOKkhXYRRIURIlBUNNK5UAIeU1SEgc/9Yy9oM86PPcNes2fv9X4+HvOYvdf6rrU/awbmvdZ3rfVdigjMzCy7OpS6ADMzKy0HgZlZxjkIzMwyzkFgZpZxDgIzs4zrVOoCWqpXr17Rv3//UpdhZlZWampqNkZE74bmlV0Q9O/fn6VLl5a6DDOzsiLpL43Nc9eQmVnGOQjMzDLOQWBmlnFld47AzCrTtm3bqK2tZcuWLaUupax169aNvn370rlz54KXcRCYWbtQW1tLjx496N+/P5JKXU5Zigg2bdpEbW0tAwYMKHg5dw2ZWbuwZcsWevbs6RDYA5Lo2bNni4+qHARm1m44BPZca36Gmekaevjptcx+8hU+2La91KUURdfOHZl69EAmj+5f6lLMrMxl5oigkkIA4INt25n95CulLsPMCjBu3Lhmb4S95557mDFjBgDTp0/nF7/4xYfa/OEPf+CUU04pen2ZCYJKCoGdKnGbzKztZaZrKN+cr08odQl75IzvPlbqEswq0tq1a5k4cSJjx47lqaeeok+fPjz88MNMnDiR733ve1RXV7Nx40aqq6tZu3Yt99xzD7/85S/Zvn07K1eu5Ktf/Spbt27lvvvuo2vXrsybN4/99ttv1/p37NjBueeeS79+/fj2t7/N3XffzdVXX83+++/PoEGD6Nq16662CxYs4Prrr+evf/0r1113HVOmTAFg8+bNTJkyhZUrV3LEEUfws5/9bI/PrWQyCMysfUtzZ6e5HcGXX36Z+++/nx//+MecddZZzJkzp8n2K1euZNmyZWzZsoUDDzyQa6+9lmXLlnHxxRfz05/+lK985SsA1NXV8dnPfpYhQ4Zw+eWXs379er75zW9SU1PDvvvuy/jx4xk2bNiu9a5fv56FCxeyevVqJk2atCsIli1bxqpVqzjggAMYM2YMixYtYuzYsXv0M8lM15CZWSEGDBjA0KFDATjiiCNYu3Ztk+3Hjx9Pjx496N27N/vuuy+nnnoqAIcddthuy37xi1/cFQIAzzzzDOPGjaN379506dKFqVOn7rbe0047jQ4dOjB48GD+9re/7Zo+cuRI+vbtS4cOHRg6dGiz9RXCQWBmlie/e6Zjx47U1dXRqVMnduzYAfCha/Tz23fo0GHX+w4dOlBXV7dr3lFHHcUTTzyx2/JNdenkrzcimqxvT7lryMzanfZ2Hq9///7U1NQwcuTIBq/mKcQXvvAFFixYwJlnnsncuXMZNWoUM2fOZNOmTeyzzz48+OCDHH744UWuvDA+IjAza8all17KrbfeylFHHcXGjRtbvZ5LLrmE4cOHc8455/Dxj3+cK6+8kiOPPJITTjiB4cOHF7HillH+IUc5qK6ujtY8mCb/5FN729toqUraFrOdXnjhBQ499NBSl1ERGvpZSqqJiOqG2vuIwMws4xwEZmYZ5yAwM8s4B4GZWcY5CMzMMs5BYGaWcQ4CM7NGrF27liFDhpS6jA8pZFjrlnAQmJm1oWIMCVFsDgIzs8T111/PkCFDGDJkCD/4wQ+A3B/uz3/+81RVVTFlyhTee+89AC677DIGDx5MVVUVl156KQAbNmzgjDPOYMSIEYwYMYJFixYBcOWVV3LBBRcwYcIEPve5zzFq1ChWrVq163PHjRtHTU0N7777Lueddx4jRoxg2LBhPPzwwwC8//77TJs2jaqqKqZOncr7779f1O32WENm1u5c/qvVqa37O6ce0uD0mpoa7r77bp555hkiglGjRnHsscfy4osvcueddzJmzBjOO+88brnlFs477zzmzp3L6tWrkcRbb70FwMyZM7n44osZO3Ysr732GieeeCIvvPDCrvUvXLiQ7t27c8MNN/DAAw9w1VVXsX79etatW8cRRxzB17/+dY477jjuuusu3nrrLUaOHMkJJ5zA7bffzl577cWKFStYsWJF0Yej8BGBmRmwcOFCTj/9dPbee28+8pGP8OlPf5onn3ySfv36MWbMGADOPvtsFi5cyD777EO3bt04//zzeeihh9hrr70A+P3vf8+MGTMYOnQokyZN4u233+add94BYNKkSXTv3h2As846iwcffBCABx54gDPPPBOAxx57jGuuuYahQ4cybtw4tmzZwmuv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\n",
                        "text/plain": [
                            "<Figure size 432x288 with 1 Axes>"
                        ]
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                }
            ],
            "source": [
                "thinkplot.PrePlot(2)\n",
                "thinkplot.Pmfs([pmf,biased_pmf])\n",
                "thinkplot.Config(xlabel='# of children under 18', ylabel='Probability')"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 22,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "1.024205155043831"
                        ]
                    },
                    "execution_count": 22,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "pmf.Mean()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 23,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "2.403679100664282"
                        ]
                    },
                    "execution_count": 23,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "biased_pmf.Mean()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "The mean for the actual distribution is 1.02, while the mean for the biased distribution is 2.4."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Exercise 3.2:\n",
                "Write functions called PmfMean and PmfVar that take a Pmf object and compute the mean and variance. To test these methods, check that they are consistent with the methods Mean and Var provided by Pmf."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 24,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "1.024205155043831"
                        ]
                    },
                    "execution_count": 24,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "def PmfMean(pmf):\n",
                "    mean = 0.0\n",
                "    for x, p in pmf.d.items():\n",
                "        mean += p * x\n",
                "    return mean\n",
                "PmfMean(pmf)\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 25,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "1.024205155043831"
                        ]
                    },
                    "execution_count": 25,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "pmf.Mean()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 26,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "1.4128643263531195"
                        ]
                    },
                    "execution_count": 26,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "def PmfVar(pmf):\n",
                "    mu = pmf.Mean()\n",
                "    var = 0.0\n",
                "    for x, p in pmf.d.items():\n",
                "        var += p * (x - mu) ** 2\n",
                "    return var\n",
                "PmfVar(pmf)\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 27,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "1.4128643263531195"
                        ]
                    },
                    "execution_count": 27,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "pmf.Var()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Exercise 4.1:\n",
                "How much did you weigh at birth? I weighed 6 pounds and 15 ounces. According to Downey (2014), totalwgt_lb is equal to pounds + ounces/ 16.0. Therefore, my totalwgt_lb = 6 + 15/16 = 6.9.\n",
                "\n",
                "Using the NSDG data (all live births), compute the distribution of birth weights and use it to find your percentile rank. If you were a first baby (which I was), find your percentile rank in the distribution for first babies."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 28,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": "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\n",
                        "text/plain": [
                            "<Figure size 432x288 with 1 Axes>"
                        ]
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                },
                {
                    "data": {
                        "text/plain": [
                            "37.65757506303002"
                        ]
                    },
                    "execution_count": 28,
                    "metadata": {},
                    "output_type": "execute_result"
                },
                {
                    "data": {
                        "text/plain": [
                            "<Figure size 576x432 with 0 Axes>"
                        ]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": [
                "preg = nsfg.ReadFemPreg()\n",
                "live = preg[preg.outcome == 1]\n",
                "live, firsts, others = first.MakeFrames()\n",
                "first_cdf = thinkstats2.Cdf(firsts.totalwgt_lb, label='first')\n",
                "thinkplot.Cdf(first_cdf)\n",
                "thinkplot.Show(xlabel = 'weight (pounds)', ylabel = \"CDF\")\n",
                "first_cdf.PercentileRank(6.9)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "I am in the 38th percentile (rounding up), meaning that I weighed at birth the same or more than 38% of babies. "
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Exercise 4.2:\n",
                "\n",
                "The numbers generated by numpy.random.random are supposed to be uniform between 0 and 1; that is, every value in the range should have the same probability.\n",
                "\n",
                "Generate 1000 numbers from numpy.random.random and plot their PMF. What goes wrong?\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 29,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": "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\n",
                        "text/plain": [
                            "<Figure size 432x288 with 1 Axes>"
                        ]
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                }
            ],
            "source": [
                "sample = np.random.random(1000)\n",
                "pmf = thinkstats2.Pmf(sample)\n",
                "thinkplot.Pmf(pmf)\n",
                "thinkplot.Config(xlabel='random sample', ylabel='Probability')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "    The problem with the above PMF graph is that there are 1000 data points. PMFs work well when N is small, and 1000 is not small. The probabilities are so small for the large number of data points that the random noise increases (Downey, 2014)."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Now plot the CDF. Is the distribution uniform?"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 30,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": "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\n",
                        "text/plain": [
                            "<Figure size 432x288 with 1 Axes>"
                        ]
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                }
            ],
            "source": [
                "cdf = thinkstats2.Cdf(sample)\n",
                "thinkplot.Cdf(cdf)\n",
                "thinkplot.Config(xlabel='random sample', ylabel='CDF')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "The graph above shows that the CDF is a straight line, therefore the distribution is uniform (Downey, 2014)."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# References:\n",
                "Downey, A. B. (2014). Think Stats: Exploratory Data Analysis (2nd ed.). O'Reilly. "
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.6"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 1
}