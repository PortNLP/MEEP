# MEEP

## Metric for Evaluation of Engagingness using Prompting

This repository contains the code for dialogue evaluation in multilingual settings 
that was used to produce the tests in the paper

 
[**MEEP: Is this Engaging? Prompting Large Language Models for Dialogue
Evaluation in Multilingual Settings**](https://aclanthology.org/2023.findings-emnlp.137/)

published in EMNLP 2023 Findings.

### Directory Structure

The directory structure should include a Datasets directory at the
same level as the Evaluation directory.

<ul>
    <li>MEEP</li>
        <ul>
            <li>|___ Datasets</li>
                <ul>
                    <li>|___ DSTC_11_Track_4</li>
                        <ul>
                            <li>|___ ...</li>
                                <ul>
                                    <li>.</li>
                                    <li>.</li>
                                    <li>.</li>
                                </ul>
                        </ul>
                </ul>
            <li>|___ Evaluation</li>
                <ul>
                    <li>|___ preprocessors</li>
                </ul>
        </ul>
</ul>


### Prompts

The prompts used in the paper are in `engagingnessprompt.py`.

### Datasets

Download the datasets from DSTC11 into the Datasets directory.
Include the DSTC_11_Track_4 directory within the Datasets directory.

### SEE dataset

Code for random selection of samples from the SEE dataset is in `see_selector.py`. This is to show our process, but will create a different dataset than the one we used. To recreate our dataset, use `see_subset_maker.py`. Use the same file structure found in the DSTC11 data.

### Citation

If you use the material in this repository or in the paper, please cite our work as

Amila Ferron, Amber Shore, Ekata Mitra, and Ameeta Agrawal. 2023. [MEEP: Is this Engaging? Prompting Large Language Models for Dialogue Evaluation in Multilingual Settings](https://aclanthology.org/2023.findings-emnlp.137). In *Findings of the Association for Computational Linguistics: EMNLP 2023*, pages 2078–2100, Singapore. Association for Computational Linguistics.

Bibtex and other citation code can be found on the paper's ACL Anthology [page](https://aclanthology.org/2023.findings-emnlp.137/).