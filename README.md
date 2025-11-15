# README #

Note: This repo was recovered from a backup as the original was lost, unfortunately commit history is lost.

Technologies: Python

Status: Complete

AEMOS or AI Enabled Multi Objective Scheduler is a system used for optimizing test cases by using a combination of classic AI techniques (heuristics and Simulated Annealing) and clustering.

This is the code that implements my Masters Degree Thesis. I am not sure if I can publish the actual thesis because we are still looking for publication, or a derived piece of it.

# What works #
The code implements a notation used to represent arbitrary worlds and its restrictions, a feature based coverage model used to model the coverage of a test case by measuring the number of features that touches and a solver which takes the world description and a list of test cases, processes it and returns a selection of test cases with the most coverage and less runtime.

# The objective #
Verify that the assumptions in my thesis were correct, specifically: that a realistic problem can be represented, a working solutions is found in an acceptable time and that a multi objective optimization target can be represented. With less priority, verify that the solution can be easy to use.

#More Information#

AEMOS is based on 3 parts: a world representation, a clusterer and an optimizer.

The world representation allows the test designer to model the environment, the test cases, its dependencies and restrictions. For example, a test case can be modelled such that it depends on an specific piece of hardware or a restriction can be specified such that two software versions cannot be installed simultaneously. Additionally, it allows setting the language and characteristics needed for the optimisation, for example define that each test case has an associated cost in time and define the cost for each one.

The world representation uses python as input language, but the library has been modelled in such a way that closely resembles Prolog, which greatly simplifies the representation. Example [here](https://github.com/karurosu/AEMOS/blob/main/src/sample1/world.py).

The clusterer uses a greedy algorithm and heuristics to simplify the search space by grouping test cases based on its characteristics and the world restrictions. A side effect is that the resulting clusters require less time to run. A sample output is [here](https://github.com/karurosu/AEMOS/blob/main/src/real-clusters.txt):

For the optimiser, each one of the variables is weighted and combined into a value function, then the optimizer uses the clusters and a Simulated Annealing process to select test cases that optimise the value function.

# My participation #
I did all the theoretical work and implementation.

# What is broken #
The application was never packaged as a program, everything is hard coded in test.py. Other than that, it is fully functional.
