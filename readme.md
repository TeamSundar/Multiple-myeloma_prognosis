<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--

*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<p align="center">
  <h3 align="center">Neural Network Based Pattern Recognition Model for predic-tion of Survival Prognosis of Multiple Myeloma Patients</h3>
 <p align="center">
 <a align="center">Vidhi Malik 1, Shayoni Dutta 2, Navaneethan Radhakrishnan 1, Ritu Gupta 3,* and Durai Sundar 1,* </a>
<p align="center">
<a align="centre">1	DAILAB, Department of Biochemical Engineering & Biotechnology, Indian Institute of Technology (IIT) Delhi, New Delhi - 110 016, India; </a>
<p align="center">
<a align="centre">2	Language of Technical Computing, Data Analytics, MathWorks, New Delhi, 110001, India; </a>
<p align="center">
<a align="centre">3	Laboratory Oncology Unit, Dr. B.R.A.IRCH, All India Institute of Medical Sciences (AIIMS), Ansari Nagar, New Delhi, 110029, India.
</a>
</p>


<!-- TABLE OF CONTENTS
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements) -->



<!-- ABOUT THE PROJECT -->
## About The Project

Multiple myeloma (MM) is malignancy of plasma cells, found in the bone marrow, which aids in fighting infections by synthesis of immunoglobulins. Clonal proliferation of abnormal plasma cell outgrows normal plasma cells and carry on synthesis of abnormal proteins, leading to MM. With advancements in clinical research, the disease has become highly manageable, but not curable. Various clinical factors are considered by medical practitioners for prediction of prognosis and treatment regimens for patients. An attempt has been made here to develop a tool that can help in predicting the survival and prognosis of MM patients, which will eventually support clinicians in designing suitable treatment regimen for the patients.


### Built With

* [MATLAB R2020a: academic license](https://jquery.com)



<!-- GETTING STARTED
## Getting Started

### Installation

Clone the repo
```sh
git clone https://github.com/TeamSundar/Multiple-myeloma_prognosis.git
```

<!-- USAGE EXAMPLES -->
## Usage

To use the proposed neural network based survival prediction model for Multiple myeloma patients, 
use commands: 
```
cd TeamSundar/Multiple-myeloma_prognosis/NCA-Neuralnet

load mm_NCANN.mat
newoutput = mm_NCANN(newinput);
```


The pipeline require two input files:
1. Clinical features file should have seven columns in a format specified below


| aCGH ID_1      | Age | Gender | OS_Time (days) | Chemotherapy Regimen | ISS Staging | 
|----------------|-----|--------|----------------|----------------------|-------------|
| 253058713873_1 | 73  | 1      | 52             | 1                    |      2      |
| 253058713873_3 | 75  | 0      | 175            | 4                    |      2      |
| 253058713877_1 | 54  | 1      | 182            | 2                    |      3      |
| 253058713877_2 | 58  | 1      | 203            | 7                    |      3      |


Please refer following table for symbols used for features like gender, chemotherapy regimen, ISS satging and response columns:


| Gender     | Chemotherapy Regimen                                    | Staging (International Staging   System) |
|------------|---------------------------------------------------------|------------------------------------------|
| 0 (Male)   | 1 : lenalidomide-dexamethasone (RD)                     | 1 (ISS 1)                                |
| 1 (Female) | 2 : thalidomide-dexamethasone (TD)                      | 2 (ISS 2)                                | 
|            | 3 : bortezomib-dexamethasone (VD)                       | 3 (ISS 3)                                |
|            | 4 : melphalan-prednisone-thalidomide   (MPT)            |                                          |
|            | 5 : bortezomib-   thalidomide-dexamethasone (VTD)       |                                          |
|            | 6 :   bortezomib-lenalidomide-dexamethasone (VRD)       |                                          |
|            | 7 :   bortezomib-cyclophosphamide-dexamethasone (VCD)   |                                          |
|            | 8: cyclophosphamide, thalidomide,   dexamethasone (CTD) |                                          |


2. CNV file
The required CNV input file should in the format specified in table below:


| Sample   | Gene1 | Gene2 | ..| GeneN   |
|----------|-------|-------|---|---------|
| Sample 1 |       |       |   |         |
| Sample2  |       |       |   |         |
| ..       |       |       |   |         |
| SampleN  |       |       |   |         |

The neighbourhood component analysis (NCA) algorithm was used to reduce the dimension of input dataset that provided us a gene signature comprised of 211 genes that were able to classify the patients into three classes based on the progression event and death event of the participant. The input file should have CNV values for these 211 genes. The input file can be formatted using script ./Input_Data/Input_prep.py


Model will classifiy patient into three classes based on progression and death event chances i.e.,
1. Class 1: 11 (Dead with relapse i.e., Progression event: 1 and death event :1)
2. Class 2: 10 (alive with relapse i.e., Progression event : 1 and death event: 0)
3. Class 3:  0 (alive with no relapse i.e., Progression event :0 and death event: 0)

## The Matlab live script for proposed NCA-Neural network-based model is located in ./NCA-Neuralnet/ArrayCGH_NCA_Neural_net_92_7percent_accuracy_final_model.mlx

## The Matlab live scripts for autoencoder based prediction models, DNN1 and DNN2 is located in directory ./DNN1_and_DNN2/ArrayCGH_DNN1_52_6_andDNN2_68_4percent_SVM_41_2_RUS_33percent.mlx



<!-- CONTRIBUTING
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT
## Contact

Vidhi Malik - vidhi0205@gmail.com
Shayoni Dutta - shayonid@mathworks.com


<!-- ACKNOWLEDGEMENTS
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com) -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
