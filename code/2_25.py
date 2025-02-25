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

# from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")

# batch_sentences = [
#     ["But what about second breakfast?","i am a sentence"],
#     "Don't think he knows about second breakfast, Pip.",
#     "What about elevensies?",
# ]
# encoded_input = tokenizer(batch_sentences, padding=True, truncation = True)
# print(encoded_input)

# {'input_ids': [[101, 1252, 1184, 1164, 1248, 6462, 136, 102, 178, 1821, 170, 5650'to, 102, 0, 0], [101, 1790, 112, 189, 1341, 1119, 3520, 1164, 1248, 6462, 117, 2190 0,2, 1643, 119, 102], [101, 1327, 1164, 5450, 23434, 136, 102, 0, 0, 0, 0, 0, 0, 0,ion 0]], 
# 'token_type_ids': [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 
# 'attention_mask': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]}

class Solution:
    def combinationSum3(self, k, n):
        result = []
        self.backtracking(n, k, 0, 1, [], result)
        return result
    
    def backtracking(self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum:
            return 
        
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9 - (k - len(path)) + 2):
            currentSum += i
            path.append(i)
            self.backtracking(targetSum, k, currentSum + i, i + 1, path, result)
            currentSum -= i
            path.pop()