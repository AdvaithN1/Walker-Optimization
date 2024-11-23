### Walker Dataset and Optimization

Paper can be found here: https://arxiv.org/pdf/2310.18772  
All the project code and data can be found under the directory Walker-Optimization-FINAL  
The complete dataset is in formattedData_with_perf_values.csv

## Design Generation

All the code for the design generation can be found in Walker-Optimization-FINAL/Walker_Sobol_Dataset_Generation

- getInvalid.py checks for invalid designs (invalid geometry, thickness checks, etc).
- Sobol_Generation_Walker.ipynb contains code for generating and scaling generated designs from sobol sampling.
- dataSplitter.ipynb splits the generated data from Sobol_Generation_Walker.ipynb into material combinations.

This directory includes the generated designs sorted by material combinations. E.g. tistdf.csv contains walker designs that have titanium front crossbeams and steel frames. These are to be inputted into the parametric model.

## Parametric Model

The parametric model and simulation setups of the walker can be found in the SolidWorks part file Walker-Optimization-Final/parametric_model.SLDPRT
The above file is compatible with SOLIDWORKS 2022.

To input and simulate walker configurations, use the Design Study feature in the SolidWorks desktop app. This outputs CSV files with the raw simulation data. This data is run in batches of 200.

Please refer to the paper for more details on the parametric model.

## Simulation Result Formatting

The directory Walker-Optimization-FINAL/Walker_Dataset_and_Formatting/dataset_formatting_code contains all the code for formatting the raw simulation data.
- dataset_formatting.ipynb concatenates and formats all the raw 200-batch simulation CSV files into one file.

The directory Walker-Optimization-FINAL/Walker_Dataset_and_Formatting/Dataset contains all the raw simulation data and the formatted simulation data files.
- formattedData_with_perf_values contains all the formatted design and simulation data.

## Surrogate ML Model and Optimization

The directory Walker-Optimization-FINAL/Walker_Result_Fitting_and_Optimization contains all code for fitting the ML model and optimization.
- MLFitting_and_Optimization contains all the code for creating and training the ML model and optimizing.
- generated_counterfactuals.csv contains all generated optimized designs. This can be directly inputted into the SolidWorks parametric model to re-simulate and evaluate the optimized models.
