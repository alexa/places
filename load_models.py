"""
Helper functions to return model, tokenizer for multiple different models.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
import torch.nn as nn


device = "cuda" if torch.cuda.is_available() else "cpu"
NoneType = type(None)


def load_opt30b():
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-30b")
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-30b", device_map="auto")
    return model, tokenizer


def load_gptneo20b():
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
    model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neox-20b", device_map="auto")
    return model, tokenizer


def load_opt13b():
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-13b")
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-13b", device_map="auto")
    return model, tokenizer


def load_opt66b():
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-66b")
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-66b", device_map="auto")
    return model, tokenizer


def freeze_params(model: nn.Module, exclude: list = None):
    """Set requires_grad=False for each of model.parameters()"""
    print("Start freezing params...")
    print("========================")
    for name, param in model.named_parameters():
        print(name)
        if exclude and name in exclude:
            print(f"exclude {name} from freezing!")
            continue
        param.requires_grad = False
    print("========================")


def load_gptj(model_path="EleutherAI/gpt-j-6B"):
    print("Loading GPT-J 6B")
    # --- Load models ---
    modelname = model_path.split('/')[-1]
    if os.path.exists("gpt-j-6B.pt"):
        model = torch.load("gpt-j-6B.pt")
        print("Loaded {} from memory onto CPU".format(modelname))
    else:        
        model = AutoModelForCausalLM.from_pretrained(model_path)

    if device == "cuda":
        model.parallelize()
        print("Moved models onto GPU")
    tokenizer = AutoTokenizer.from_pretrained(model_path, truncation_side="left")
    return model, tokenizer
