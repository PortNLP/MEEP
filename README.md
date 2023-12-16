# MEEP

## Metric for Evaluation of Engagingness using Prompting

This repository contains the code for dialogue evaluation in multilingual settings 
that was used to produce the tests in the paper

 
[**MEEP: Is this Engaging? Prompting Large Language Models for Dialogue
Evaluation in Multilingual Settings**](https://aclanthology.org/2023.findings-emnlp.137/)

### Directory Structure

The directory structure should include a Datasets directory and Results directory at the
same level as the Evaluation directory 

>
>    MEEP
>       |___ Datasets
>                |___ DSTC_11_Track_4
>                        |___ ...

                            .

                            .

                            .

        |___ Evaluation

                |___ preprocessors

                        .

                        .

                        .

        |___ Results

### Prompts

The prompts used in the paper are in `engagingnessprompt.py`.

### Datasets

Download the datasets from DSTC11 into the Datasets directory.
Include the DSTC_11_Track_4 directory within the Datasets directory.

### SEE dataset

Code for random selection of samples from the SEE dataset is in `see_selector.py`. This is to show our process, but will create a different dataset than the one we used. To recreate our dataset, use `see_subset_maker.py`. Be sure to use the same file structure found in the DSTC11 data.

