# Network Anomaly Detection System [NADS]

## Overview

This repository contains the implementation files for "Anomaly Detection in Networks Using Machine Learning," 

## Requirements

Before running the implementation files, make sure you have Python 3.11.5 installed along with the following libraries:

- Sklearn: Machine Learning Library
- Numpy: Mathematical Operations
- Pandas: Data Analysis Tools
- Matplotlib, seaborn: Graphics and Visualization
- flask: Model deployment 


## Implementation Steps

### 1. Pre-processing

This step consists of a single file (data_preprocessing.ipynb). To use this program, place the [data](https://www.unb.ca/cic/datasets/ids-2017.html) files in the "CSVs" folder at the same location as the program.

After executing this file, a file named "all_data.csv" will be created, which is a prerequisite for the other steps.

### 2. Exploratory Data Analaysis 

This step consists of a single file (data_preprocessing.ipynb). It examines the "all_data.csv" file and does data exploration. It is not a prerequisite for other files. It provides information only.

### 3. Feature Selection

This program (feature_selection.ipynb) applies feature selection to the entire dataset using the "all_data.csv" file and the Random Forest Regressor algorithm. The feature importance are displayed with the help of a bar chart.

### 4. Machine Learning Implementation

This program (seven_featured_ML_implementation.ipynb) implements machine learning methods on the "all_data.csv" file using features selected from the previous step. It applies 7 machine learning algorithms, records the results.

### 5. Model Deployment

Model deployment is the process of making trained machine learning models accessible and operational for real-world use. Deployed models allow automated
and efficient execution of predictions on new data. “Pickle Library” of Python was used to save and export the best model.
Frontend development plays a crucial role in delivering user-friendly and visually appealing web applications that meet both functional and aesthetic
requirements. For this project we used “Flask Library” of Python to build the API which was deployed on AWS and private server as well.

## Execution Time

Here are the approximate execution times for each step based on the author's hardware configuration:


| Program                                          |   Execution Time (seconds)|
|--------------------------------------------------|---------------------------|
| Data processing                                  |    157 seconds            |          
| Exploratory Data Analysis                        |    13 seconds             |          
| Feature Selection                                |    55,626 seconds         |       
| Machine Learning Implementation with 18 Features |    25,082 seconds         |   
| Machine Learning Implementation with 7 Features  |    12,714 seconds         |

## Hardware Specifications

```
       _,met$$$$$gg.          
    ,g$$$$$$$$$$$$$$$P.      
  ,g$$P"     """Y$$.".        OS ➜ Debian GNU/Linux 12 (bookworm) x86_64 
 ,$$P'              `$$$.     ├ Kernel ➜ 6.1.0-11-amd64 
',$$P       ,ggs.     `$$b:   ├ Uptime ➜ 10 hours, 37 mins 
`d$$'     ,$P"'   .    $$$    └ Packages ➜ 2257 (dpkg), 14 (snap) 
 $$P      d$'     ,    $$P     
 $$:      $$.   -    ,d$$'    PC ➜ 20L6S69W02 ThinkPad T480 
 $$;      Y$b._   _,d$P'      ├ CPU ➜ i5-8350U (8) @ 3.6GHz [47.0°on] 
 Y$$.    `.`"Y$$$$P"'         ├ Memory ➜ 7208MiB / 15735MiB (45%) 
 `$$b      "-.__              ├ GPU ➜ Intel UHD Graphics 620 
  `Y$$                        └ Resolution ➜ 1920x1080 
   `Y$$.                       
     `$$b.                    WM ➜ i3 
       `Y$$b.                 ├ Bar ➜ Polybar 


```
## Contributing

We welcome contributions from the community to enhance and improve this project. If you'd like to get involved, here's how you can contribute:

1. **Clone the Repository**: Start by cloning this repository to your local machine using the following command:

```shell
git clone https://github.com/AnupPainuly/Network_Anomaly_Detection_System.git
```

2. **Create a New Branch**: Create a new branch for your contribution to keep your work isolated. You can do this using the following command:

```shell
git checkout -b feature/my-contribution
```

3. **Make Changes**: Make your desired changes or enhancements to the project.

4. **Commit Your Changes**: Commit your changes with a descriptive commit message:

5. **Push to Your Fork**: Push your changes to your forked repository:

6. **Open a Pull Request**: Finally, open a pull request (PR) on the main repository's `main` branch to propose your changes. Be sure to provide a clear and concise description of your changes in the PR.

7. **Review and Collaborate**: Collaborate with the community to address any feedback and get your changes merged into the project.

By contributing to this project, you are helping us make it better for everyone. Thank you for your contributions!

Feel free to clone the repository or fork it to get started with your contributions.

