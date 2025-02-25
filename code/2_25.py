# from datasets import load_dataset

# dataset = load_dataset("dataset_name", "configuration", split="split_name")
# #不指定参数返回DatasetDict，指定参数返回Dataset
# # 索引获取样本
# train_dataset[0]
# train_dataset[:5]

# # tokenizer  句子到tokens，tokens到数字然后到张量成为模型的输入。
# # 文本的拆分方式一致 标记索引的方式一致
# from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_trained("googlr-bert/bert-base-cased")

# encoded_text = tokenizer("hello, i am a sentence")

# print(encoded_text)
# {
#     'input_ids'
#     'token_types_id'
#     'attention_mask'
# }

# tokenizer.decode(encoded_text['input_ids'])

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")

batch_sentences = [
    ["But what about second breakfast?","i am a sentence"],
    "Don't think he knows about second breakfast, Pip.",
    "What about elevensies?",
]
encoded_input = tokenizer(batch_sentences, padding=True, truncation = True)
print(encoded_input)