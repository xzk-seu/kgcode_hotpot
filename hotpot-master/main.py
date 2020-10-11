import os
from prepro import prepro
from run import train, test
import argparse
# 命令行参数解析器
# 用法：parser = argparse.ArgumentParser()  config = parser.parse_args()
parser = argparse.ArgumentParser()
# glove词表
glove_word_file = "glove.840B.300d.txt"
# 需要的一些文件
word_emb_file = "word_emb.json"
char_emb_file = "char_emb.json"
train_eval = "train_eval.json"
dev_eval = "dev_eval.json"
test_eval = "test_eval.json"
word2idx_file = "word2idx.json"
char2idx_file = "char2idx.json"
idx2word_file = 'idx2word.json'
idx2char_file = 'idx2char.json'
train_record_file = 'train_record.pkl'
dev_record_file = 'dev_record.pkl'
test_record_file = 'test_record.pkl'
# mode 模型类型、data_file 数据文件、glove_word_file glove文件、save 保存名
parser.add_argument('--mode', type=str, default='train')
parser.add_argument('--data_file', type=str)
parser.add_argument('--glove_word_file', type=str, default=glove_word_file)
parser.add_argument('--save', type=str, default='HOTPOT')
# word_emb_file 字嵌入文件、train_eval_file 训练评价文件、word2idx_file word转idx文件、idx2word idx转word文件
parser.add_argument('--word_emb_file', type=str, default=word_emb_file)
parser.add_argument('--char_emb_file', type=str, default=char_emb_file)
parser.add_argument('--train_eval_file', type=str, default=train_eval)
parser.add_argument('--dev_eval_file', type=str, default=dev_eval)
parser.add_argument('--test_eval_file', type=str, default=test_eval)
parser.add_argument('--word2idx_file', type=str, default=word2idx_file)
parser.add_argument('--char2idx_file', type=str, default=char2idx_file)
parser.add_argument('--idx2word_file', type=str, default=idx2word_file)
parser.add_argument('--idx2char_file', type=str, default=idx2char_file)
# train_record_file 训练记录文件
parser.add_argument('--train_record_file', type=str, default=train_record_file)
parser.add_argument('--dev_record_file', type=str, default=dev_record_file)
parser.add_argument('--test_record_file', type=str, default=test_record_file)
# glove_char_size glove的char大小、glove_word_size glove的word大小、glove_dim glove的维度、char_dim char的维度
parser.add_argument('--glove_char_size', type=int, default=94)
parser.add_argument('--glove_word_size', type=int, default=int(2.2e6))
parser.add_argument('--glove_dim', type=int, default=300)
parser.add_argument('--char_dim', type=int, default=8)
#para_limit、ques_limit、sent_limit、char_limit
parser.add_argument('--para_limit', type=int, default=1000)
parser.add_argument('--ques_limit', type=int, default=80)
parser.add_argument('--sent_limit', type=int, default=100)
parser.add_argument('--char_limit', type=int, default=16)
# batch_size 训练周期、checkpoint 存储周期、period 、init_lr 、keep_prob 、hidden 隐藏层数、char_hidden char嵌入层数、patience、seed 随机种子
parser.add_argument('--batch_size', type=int, default=64)
parser.add_argument('--checkpoint', type=int, default=1000)
parser.add_argument('--period', type=int, default=100)
parser.add_argument('--init_lr', type=float, default=0.5)
parser.add_argument('--keep_prob', type=float, default=0.8)
parser.add_argument('--hidden', type=int, default=80)
parser.add_argument('--char_hidden', type=int, default=100)
parser.add_argument('--patience', type=int, default=1)
parser.add_argument('--seed', type=int, default=13)
# sp_lambda
parser.add_argument('--sp_lambda', type=float, default=0.0)
# data_split 数据划分、fullwiki 全wiki、prediction_file 预测文件、sp_threshold
parser.add_argument('--data_split', type=str, default='train')
parser.add_argument('--fullwiki', action='store_true')
parser.add_argument('--prediction_file', type=str)
parser.add_argument('--sp_threshold', type=float, default=0.3)
# config 记录参数
config = parser.parse_args()

'''
_concat
概况：生成fullwiki文件名称
参数：filename
内容：就是很简单结合文件名
'''
def _concat(filename):
    if config.fullwiki:
        return 'fullwiki.{}'.format(filename)
    return filename

# 使用_concat，构建训练记录文件、训练评价文件（亦或是验证、测试的相应文件）

# config.train_record_file = _concat(config.train_record_file)
config.dev_record_file = _concat(config.dev_record_file)
config.test_record_file = _concat(config.test_record_file)
# config.train_eval_file = _concat(config.train_eval_file)
config.dev_eval_file = _concat(config.dev_eval_file)
config.test_eval_file = _concat(config.test_eval_file)

# 根据config.mode，选择train 训练、prepro 预训练、test 测试、cnt_len 记录长度（这是啥？）
if config.mode == 'train':
    train(config)
elif config.mode == 'prepro':
    prepro(config)
elif config.mode == 'test':
    test(config)
elif config.mode == 'count':
    cnt_len(config)
