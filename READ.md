# Swamp-of-Life

This is a simulation of different species living in a swamp. It includes 5 different species: Duck, Newt, Shrimp, Algae, Rock. The simulation runs for a certain amount of time and shows how the different species interact with each other and their environment.

Prerequisites
The following libraries are required to run the simulation:
•	numpy
•	matplotlib

Installation
Clone the repository:
git clone https://github.com/Gabnix/Swamp-of-Life.git

Usage
The simulation can be run using the following command:
$ python3 swampLife.py <Movement> <Duck> <Newt> <Shrimp> <Algae> <Rock> <Timestep> 

where:
•	<Movement>: type of movement (von Neumann or Moore)
•	<Duck>: number of ducks in the simulation
•	<Newt>: number of newts in the simulation
•	<Shrimp>: number of shrimps in the simulation
•	<Algae>: number of algae in the simulation
•	<Rock>: number of rocks in the simulation
•	<Timestep>: number of timesteps for the simulation to run

If the arguments are not provided, the simulation will run with the following default values:
•	<Movement>: von Neumann
•	<Duck>: 5
•	<Newt>: 5
•	<Shrimp>: 5
•	<Algae>: 5
•	<Rock>: 5
•	<Timestep>: 15

Simulation Details
Each species has its own properties and behaviors:
Duck:
•	They move around and eat algae
•	They reproduce if they are in close proximity with another duck
•	They grow as they eat

Newt:
•	They move around and eat shrimp
•	They reproduce if they are in close proximity with another newt
•	They grow as they eat

Shrimp:
•	They move around and eat algae
•	They reproduce if they are in close proximity with another shrimp
•	They grow as they eat

Algae:
•	They grow over time

Rock:
•	They are immovable

Output
The simulation shows a scatter plot of the different species in the swamp, with different colors for each species. The size of each point represents the size of the species. The simulation also prints out the state and position of each species at the end of each timestep.

Example:
python3 swampLife.py V 20 20 20 30 5 15 

This will run the simulation with von Neumann movement, 20 ducks, 20 newts, 20 shrimps, 30 algae, 5 rocks, and 15 timesteps.

Conclusion
swampLife is a simple simulation to show how different species can interact and change over time in a given environment. It is a good starting point for learning about agent-based simulations and can be further extended to include additional species and behaviors.

