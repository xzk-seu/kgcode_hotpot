# HOTPOTQA

![image-20201009201433467](/Users/zhongkai/Library/Application Support/typora-user-images/image-20201009201433467.png)





##关键特点

1. 问题需要从多个支持文档中推理并找出答案；
2. 多样性：不局限于特定的知识库；
3. 提供句子级别的事实，支撑问答系统的推理和解释；
4. 新的问题类型：比较（comparison），需要问答系统对多个事实进行比较。“A和B的国籍是否相同？”（we require systems to compare two entities on some shared properties to test their understanding of both language and common concepts such as numerical magnitude.）



## 众包

1. 要求众包工作者从多个支持文档中提出需要在多个文档中进行推理的问题，并给出答案。
2. 确保提出的多跳问题更自然，不是针对于现有的知识库进行设计。
3. 要求众包工作者找出支撑事实。







##数据格式

The top level structure of each JSON file is a list, where each entry represents a question-answer data point. Each data point is a dict with the following keys:

- `_id`: a unique id for this question-answer data point. This is useful for evaluation.
- `question`: a string.
- `answer`: a string. The test set does not have this key.
- `supporting_facts`: a list. Each entry in the list is a list with two elements `[title, sent_id]`, where `title` denotes the title of the paragraph, and `sent_id` denotes the supporting fact's id (0-based) in this paragraph. The test set does not have this key.
- `context`: a list. Each entry is a paragraph, which is represented as a list with two elements `[title, sentences]` and `sentences` is a list of strings.

There are other keys that are not used in our code, but might be used for other purposes (note that these keys are not present in the test sets, and your model should not rely on these two keys for making preditions on the test sets):

- `type`: either `comparison` or `bridge`, indicating the question type. (See our paper for more details). **`comparison`对应的答案是否只是yes or no？**
- `level`: one of `easy`, `medium`, and `hard`. (See our paper for more details).





![image-20201010212842411](/Users/zhongkai/Library/Application Support/typora-user-images/image-20201010212842411.png)

- 单跳问题：18089；多跳问题：94690；
- 单跳问题作为`train-easy`；
- 多跳问题中的baseline模型损失最小的前60%作为`train-medium`；
- 剩余40%的多跳问题**随机划分**为四个部分：(1)`train-hard` (2)`dev   ` (3)`test-distractor` (4) `test-fullwiki` ; 大约2:1:1:1;



- The two test sets *test-distractor* and *test-fullwiki* are used in two different benchmark settings. 评价指标不同。
- **distractor**：以问题为查询，从维基百科上检索出的8段话作为干扰项，加上两段正确的gold paragraphs（用来让众包工作者生成问题和答案的段落）；
- **full wiki** ：？？从所有维基百科中定位事实查找答案？？最后给出10个context，所以支撑事实不一定在当前问题的context中。
  In the second setting, we fully test the model’s ability to locate relevant facts as well as reasoning about them by requiring it to answer the question given the first paragraphs of all Wikipedia articles without the gold paragraphs specified.
- **full wiki** 的支撑事实不一定在当前问题的context中。hotpot_dev_fullwiki_v1.json中有7405个数据，其中支撑事实不在context中的有5316个。

![image-20201011002440919](/Users/zhongkai/Library/Application Support/typora-user-images/image-20201011002440919.png)



- `train-easy`: **single-hop questions**. an overwhelming percentage in the sample only required **reasoning over one of the paragraphs**. 

![image-20201010213756574](/Users/zhongkai/Library/Application Support/typora-user-images/image-20201010213756574.png)

- `train-medium`: the models(baseline) were able to correctly answer 60% of the questions with high confidence.  损失最小的前60%的多跳问题。
- 





## 问题推理类型

![image-20201010222115102](/Users/zhongkai/Library/Application Support/typora-user-images/image-20201010222115102.png)



1. `Type I` 两跳问题的尾节点（某比赛-[MVP]->(person)-[效率于]->（？哪支球队）），其中（person）节点被称为*bridge entity*；
2. `Comparison` 比较两个实体的属性，是否相等（大于、小于）；
3. `Type II` 通过多个属性，确定一个实体，星状查询。
4. `Type I` 两跳问题的尾节点的属性；
5. `Other` 需要多于两个的支撑事实；

