# 4.1 Description of the problem
This project focuses on the Symbolic Regression problem, which is a machine learning task aimed at discovering mathematical formulas or expressions that best represent a given dataset. The goal is to identify a symbolic expression that effectively captures the relationship between input variables and corresponding output values, enabling accurate predictions and providing insights into the underlying data patterns. The problem is defined as follows: given a dataset consisting of input-output pairs, the objective is to find a symbolic expression that closely approximates the relationship between the inputs and outputs. In this particular project, we work with 8 distinct datasets, each containing a varying number of input variables and output values. The challenge is to find the formula that provides the best fit for each dataset.

# 4.2 Implementation
The Symbolic Regression (SR) implementation is an evolutionary algorithm that aims to discover symbolic expressions that model a given dataset. The goal is to evolve a population of mathematical expressions, represented as trees, using genetic operators like crossover and mutation, and iteratively improving the models through fitness evaluation. The implementation follows a modular approach, breaking down the problem into smaller tasks such as tree creation, selection, mutation, and evolution. Here is a detailed explanation of the entire implementation:

## 1. Initialization and Data Loading
The `SymbolicRegression` class begins by initializing important parameters such as population size, number of generations, mutation and crossover rates, and the path to a `.npz` file containing the dataset. The dataset is loaded using `numpy`, extracting `x` (input features) and `y` (target output) arrays. The number of variables in the dataset is determined by the shape of `x`, and variable names are dynamically generated to match the number of features.

## 2. Tree Creation and Representation
One of the key components of symbolic regression is the creation of symbolic trees that represent mathematical expressions. Each individual in the population is represented as a tree, where nodes are either operators (such as addition, multiplication, or sine) or leaf nodes that hold variables (like `x0`, `x1`) or constants.

The challenge in this implementation is building these trees correctly, especially ensuring the proper usage of binary and unary operators. For binary operators, which require two child nodes (left and right), the tree creation must ensure balanced subtrees. Unary operators, like `sin` or `sqrt`, require only one child node. Therefore, the tree-building function must handle both types of operators properly, ensuring that no illegal tree structures (e.g., unary operators with more than one child) are created.

The process starts with recursive calls that build the tree from the root, and at each step, the algorithm decides whether to create a binary operator node or a unary operator node. If a leaf node is needed, it will choose either a constant or a variable. A crucial part of this function is managing the node count to avoid overly deep trees, which can lead to overfitting or computational inefficiency.

## 3. Fitness Evaluation
Fitness evaluation is an essential step to guide the evolution of the population. The fitness of each individual (symbolic tree) is calculated by measuring how well its corresponding expression fits the data. The fitness function is typically the Mean Squared Error (MSE) between the predicted and actual output values, and the goal is to minimize this error.

Each tree in the population is evaluated by applying the symbolic expression it represents to the input data and calculating the MSE. The fitness value is then assigned to the individual, which will be used in subsequent selection, crossover, and mutation operations. The implementation also includes error handling to ensure that individuals with invalid expressions (e.g., division by zero or mathematical errors) are assigned high fitness values (poor solutions) to avoid their selection in future generations.

## 4. Selection Mechanism
Selection is a critical aspect of evolutionary algorithms, ensuring that individuals with better fitness values have a higher chance of being selected for reproduction. In this implementation, tournament selection is used. During tournament selection, a random subset of the population is chosen, and the best individual (the one with the lowest fitness value) is selected from this group.

This method promotes the survival of the fittest individuals while maintaining diversity in the population. The size of the tournament is dynamically adjusted based on the fitness of the best individual, favoring exploration when the model's error is high and exploitation when the model is performing well.

## 5. Crossover (Recombination)
Crossover is the genetic operator that combines two parent individuals to produce offspring. In symbolic regression, this involves selecting random subtrees from two parent trees and swapping them to create new offspring. This process is known as subtree crossover.

The crossover function ensures that the resulting child trees are valid, i.e., they must respect the rules for binary and unary operators. The depth of the trees is also controlled to ensure that the offspring do not grow too deep, which could lead to overfitting or computational inefficiency. If a child tree violates the depth constraints, the algorithm reverts to the parent tree.

The challenge here is maintaining the structural integrity of the trees after crossover while ensuring that the resulting offspring can still represent valid mathematical expressions.

## 6. Mutation
Mutation introduces small, random changes to an individual to explore the search space further. In this implementation, a point mutation is applied to randomly selected nodes in a tree. If the selected node is a leaf node (constant or variable), it is replaced with a new randomly selected leaf. If the node is an operator, it is replaced with a randomly chosen operator of the same type (either unary or binary).

Mutation is typically applied with a lower probability compared to crossover, as the goal is to introduce small variations rather than large changes. The mutation rate is adaptive, changing during the evolution process based on the error (MSE) of the best individual. When the error is high, the mutation rate is increased to promote exploration; when the error is low, the mutation rate is decreased to allow for more exploitation of the current best solutions.

## 7. Elitism
Elitism is a mechanism that ensures the best individuals are preserved in each generation. The top `elitism_size` individuals, based on their fitness values, are carried over to the next generation without any changes. This guarantees that the population does not lose the best solutions and that they can continue to evolve and improve.

The elitism size is dynamically determined, with a default of 10% of the population, but it can be adjusted based on the size of the population.

## 8. Evolutionary Process
The main loop of the evolutionary process involves iterating through multiple generations, each of which consists of the following steps:
1. **Evaluate Fitness**: Evaluate the fitness of each individual in the population.
2. **Selection**: Select individuals based on their fitness using tournament selection.
3. **Crossover and Mutation**: Apply crossover and mutation to create offspring.
4. **Elitism**: Carry over the best individuals from the current generation.
5. **Replace Population**: Replace the old population with the new generation.

The process continues until a stopping condition is met, such as reaching the maximum number of generations or achieving a satisfactory error threshold. During evolution, the algorithm dynamically adjusts parameters like the mutation rate and tournament size based on the MSE percentage of the best individual, helping to guide the exploration-exploitation tradeoff.

## 9. Stopping Criteria
The algorithm includes stopping conditions based on both the number of generations and the MSE of the best individual. If the best individual reaches a satisfactory MSE (e.g., below 10%), the algorithm will terminate early, as it has found a good solution. If the MSE is still high after the maximum number of generations, the algorithm can extend its runtime to continue evolving and refining the solution.

Additionally, there are safeguards to ensure that the population remains valid throughout the process, with checks for invalid individuals and tree structures.

# Overview
The overall approach to symbolic regression combines genetic algorithms with the symbolic representation of mathematical expressions. One of the most challenging aspects of the implementation is correctly building and managing the tree structures, especially handling binary and unary operators properly. The algorithm's effectiveness depends on balancing exploration (mutation and crossover) with exploitation (elitism and fitness-based selection). The adaptive nature of the algorithm, including dynamic mutation rates and tournament sizes, helps it find optimal or near-optimal solutions for symbolic regression tasks.

## 4.3 Results and Discussion

### Problem 1
The symbolic regression algorithm successfully evolved a solution for Problem 1 within the specified 50 generations. The best individual achieved a Mean Squared Error (MSE) percentage of 0.1658%, indicating a highly accurate approximation of the target function. The best-performing individual was represented by the expression:

$$ \text{Best Individual: } \frac{x_0}{\cosh{\left(\log_{10}{\left|\left|\tan{\left(\log{10}\right)}\right|\right|}\right)}} $$

This individual consisted of 9 nodes in its expression tree. The solution demonstrates the algorithm's ability to effectively balance exploration and exploitation during the evolutionary process, resulting in a precise symbolic expression for the given problem.

### Problem 2
Unlike Problem 1, the algorithm was unable to find a feasible solution for Problem 2. By the 50th generation, the best individual's MSE percentage was recorded as NaN (Not a Number), with a fitness value of 10101010, indicating an infeasible or invalid solution. The best individual for this problem was:

$$ \text{Best Individual: } \left|{\tanh{\left(\tan{\left(34242.424242424226\right)}\right)}}^{x_0}\right) $$

This individual consisted of 6 nodes. Despite the algorithm's attempts to adapt through mechanisms such as dynamic mutation rates and tournament selection adjustments, the problem remained unfeasible within the given parameters. This result highlights the inherent complexity or possible issues in the dataset or problem definition for Problem 2.

### Problem 3
The evolutionary process for Problem 3 reached 90 generations with the best individual's Mean Squared Error (MSE) percentage at 523.71%, suggesting a suboptimal solution. The fitness of the best individual was recorded as 1682.16, and the solution was represented by the expression:

$$ \text{Best Individual: } \cosh{\left(\sqrt{\left|\log_2{\left(\left|\left|\sqrt{1.6875 \mod x_1}\right|\right|\right)}\right|}\right)} $$

This individual contained 10 nodes in its expression tree. Given the high MSE percentage, the algorithm was extended by an additional 20 generations to explore improved solutions. However, no significantly better individual emerged. The high error indicates that the algorithm struggled to approximate the target function effectively within the given constraints. This could be due to the problem's complexity or the choice of evolutionary parameters.

### Problem 4
For Problem 4, the algorithm required 93 generations to evolve a solution with an MSE percentage of 45.90% and a fitness of 6.82. The best individual was expressed as:

$$ \text{Best Individual: } \sinh{\left(\exp{\left(\tanh{\left(8.020833333333332 \div \left(\cos{\left(x_1\right)} \mod 6.041666666666666\right) - 5.645833333333333\right)}\right)}\right)} $$

This individual had 11 nodes in its expression tree. While the MSE percentage indicates a reasonable approximation of the target function, there remains room for improvement. The slightly lower error compared to Problem 3 suggests that the algorithm performed better but still faced challenges in achieving a highly accurate result.

### Problem 5
For Problem 5, the evolutionary process concluded at Generation 50, achieving an exceptionally low Mean Squared Error (MSE) percentage of 1.92e-08%. This indicates a highly accurate solution. The best individual evolved by the algorithm was represented as:

$$ \text{Best Individual: } \left(\log_2{\left(\exp{\left(\log_2{\left(\sin{\left(2.4791666666666665\right)} \mod 5.645833333333333\right)} \cdot \exp{\left(3.6666666666666665\right)}\right)}\right)}\right) \cdot \tanh{\left(\exp{\left(\log_2{\left(\sin{\left(2.4791666666666665\right)} \mod 5.645833333333333\right)} \cdot \exp{\left(3.6666666666666665\right)}\right)}\right)} $$

This individual had 21 nodes in its expression tree, indicating moderate complexity. The extremely low error highlights the algorithm's effectiveness in evolving a near-perfect solution for this problem. The process also identified a "nice solution," demonstrating the algorithm's capability to converge on highly optimized symbolic expressions.

### Problem 6
For Problem 6, the process also ended at Generation 50, producing a solution with an MSE percentage of 11.84% and a fitness value of 1.95. The best individual was represented as:

$$ \text{Best Individual: } \left(\left(\left(x_1 \cdot \left(10.0^{0.3020408163265306}\right)\right) \cdot \sqrt{\cos\left(\tanh\left(2.1204081632653065\right)\right)}\right) - \exp\left(\cos\left(\log_{10}\left(\log_{10}\left(1.3122448979591839\right)\right)\right)\right)\right) + \log_2\left(\cosh\left(\cosh\left(0.5040816326530613\right)\right)\right) \right) \div \cos\left(\log\left(\cosh\left(\tanh\left(\sqrt{x_1}\right)^{2.7265306122448982}\right)\right)\right) $$

This individual contained 30 nodes, making it the most complex solution among all problems. The relatively higher MSE percentage suggests the solution was less optimal than that of Problem 5. The high node count and complex mathematical operators in the expression imply potential challenges in both interpretability and generalization.

### Problem 7
For Problem 7, the evolutionary process continued up to Generation 90, with an observed Best Fitness of 357.85 and an MSE percentage of 70.56%. These results indicate that while the algorithm found a feasible solution, the accuracy was significantly lower than that of earlier problems. The best individual found by the algorithm is expressed as:

$$ \text{Best Individual: } \exp{\left(\log_2{\left(\exp{\left(x_0 \cdot x_1\right)}\right)}\right)} $$

This individual consists of 6 nodes, making it one of the simpler solutions. Despite the relatively small node count, the high MSE percentage indicates that the solution could not fit the data well. The algorithm seems to have struggled to optimize the solution fully within the given number of generations, which led to the lower fitness value. To address this, the evolution process was extended by 20 additional generations, reflecting the attempt to explore more promising solutions over a longer duration.

### Problem 8
For Problem 8, the evolutionary algorithm concluded at Generation 50, but the best solution obtained was unfeasible. The Best Fitness reached was 1,000,000.0, with an MSE percentage of NaN (not a number), which typically indicates that the solution could not be evaluated properly due to an error or failure in the algorithm's computation. The best individual evolved by the algorithm was expressed as:

$$ \text{Best Individual: } \cos{\left(\sqrt{\left(x_5^{x_5} + \sin{\left(x_3\right)}\right)}\right)} $$

This solution contained 8 nodes. However, due to the unfeasibility of the problem (likely due to division by zero, undefined operations, or invalid input parameters), the solution could not be evaluated or optimized successfully. The “NaN” result typically signals such issues where the function's output becomes undefined.

## Acknowledgment
This symbolic regression project was undertaken and completed independently. All stages of the implementation, including the design, coding, testing, and analysis, were carried out by me. Throughout the process, I applied my understanding of evolutionary algorithms, symbolic regression techniques learned during the ‘Computation Intelligence’ course, and Python programming to create a functional and efficient solution.
