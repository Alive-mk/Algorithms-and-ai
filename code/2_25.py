from datasets import load_dataset

dataset = load_dataset("dataset_name", "configuration", split="split_name")

# 索引获取样本
train_dataset[0]
train_dataset[:5]
