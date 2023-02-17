# PLACES: Prompting Language Models for Social Conversation Synthesis

Citation:
```commandline
@inproceedings{chen2023places,
  title={PLACES: Prompting Language Models for Social Conversation Synthesis},
  author={Chen, Maximillian and Papangelis, Alexandros and Tao, Chenyang and Kim, Seokhwan and Rosenbaum, Andy and Liu, Yang and Yu, Zhou, and Hakkani-Tur, Dilek},
  booktitle={Findings of the Association for Computational Linguistics: EACL 2023},
  pages={to appear},
  year={2023}
}
```

## Quick Start

This code can be used to recreate the conversations from the paper, which used a list of reference topics from FITS. 
Feel free to try out different topic and prompt inputs!

Follow these steps to generate synthetic conversations with PLACES.

### 1. Download Data
PLACES can use existing conversations as examples in the prompt, or hand-crafted ones.
In the paper, we use 3 datasets: TopicalChat [1], DailyDialog [2], and FITS [3].

#### DailyDialog

Download from [here](http://yanran.li/dailydialog).

#### Topical Chat

Download from [here](https://github.com/alexa/Topical-Chat).

#### FITS

Download [FITS](https://parl.ai/projects/fits/) data from ParlAI.

First, you need to install ParlAI: `pip install parlai`

Using: `parlai display_data -t fits` will tell you where the FITS data is stored on your local machine.
It may take some time to download the data the first time you call it.

### 2. Set up your environment

We've tested our code with Python 3.8 and `transformers 4.26.0` but it should work with earlier versions of transformers too. After creating a virtual environment, you can install the requirements:

`pip install transformers`

### 3. Run PLACES

If you want to use Topical Chat conversations as prompts, you need to first 
parse Topical-Chat into a simpler format:

```commandline
python parse_topical_chat.py --tc_path <PATH_TO_TOPICAL_CHAT>
```

This will produce a `.jsonlist` file into the `prompts` directory.

The general command to run PLACES is:

`python conversation_synthesis.py <ARGUMENTS>`

For example:
```commandline
python conversation_synthesis.py --fits_path <PATH_TO_FITS>                                 
```

Or:

```commandline
python conversation_synthesis.py --fits_path <PATH_TO_FITS>
                                 --in_context_dataset "daily_dialog"
                                 --in_context_dataset_path <PATH_TO_DAILY_DIALOG>                                 
```

If you want to run triadic conversations, use the `--triadic` flag:

For example:
```commandline
python conversation_synthesis.py --fits_path <PATH_TO_FITS>       
                                 --triadic                          
```

Or:

```commandline
python conversation_synthesis.py --fits_path <PATH_TO_FITS>
                                 --in_context_dataset "daily_dialog"
                                 --in_context_dataset_path <PATH_TO_DAILY_DIALOG>
                                 --triadic                                 
```

While we haven't tested multi-party conversations with more than 3 participants, it should be possible to do so by 
creating the appropriate prompts in `utils.py`.

## References

1. Karthik Gopalakrishnan, Behnam Hedayatnia, Qinlang Chen, Anna Gottardi, Sanjeev Kwatra, Anushree Venkatesh, Raefer Gabriel, Dilek Hakkani-Tür, Topical-Chat: Towards knowledge-grounded open-domain conversations, Interspeech 2019
2. Yanran Li, Hui Su, Xiaoyu Shen, Wenjie Li, Ziqiang Cao, and Shuzi Niu. DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset. IJCNLP 2017.
3. Xu J, Ung M, Komeili M, Arora K, Boureau YL, Weston J. Learning New Skills after Deployment: Improving open-domain internet-driven dialogue with human feedback. arXiv preprint 2022.