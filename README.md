### Notes on the Project. 

In the sandbox we see the first try where we built a descriptor that has solely elemental information based on the chemical formula. Then we train a XGBr model where in the pipeline we used PCA to select the first 5 strongest feautures. This did not work well enough, what happend is that it overfitted the training set and could not predict the enthalpy of formation of the test set (possible solution to make the model less complex. Make the descriptor better.)

In sandbox_2 we created a new descriptor based on that prompt. 
```
You are a ML engineer. I want you to come up with a good descriptor for the prediction of the formation enthalpy given that you have the compound formula which can be binary or ternary and mendeleev library. Pick from these choices Based on the search results, some of the simplest descriptors used in machine learning models to predict formation energies of crystals include:
Elemental properties: Basic properties of the constituent elements are often used as descriptors, such as:
Atomic number
Electronegativity
Atomic radius
Valence electron count
Compositional features:
Stoichiometric ratios of elements
Average atomic mass
Structural features:
Coordination numbers
Nearest neighbor distances
Unit cell parameters (lattice constants, angles)
Simple statistical measures:
Mean, standard deviation, minimum, and maximum values of elemental properties within the compound
Heuristic quantities:
Differences in electronegativity between neighboring atoms
Atomic packing fraction or add new ones. If there is redundancy try to avoid it. We want a concise and descriptive one. 
```
that was used on ChatGPT. These values were taken by asking perplexity.ai to search the bibliography for this kind of work and come up with the easiest descriptors that have been used so far for this problem. 

