import ujson as json
from toolkit import get_logger, quick_clean, save
from config import config
import sys
from random import randrange
from tqdm import tqdm

def tester(in_file, logger):
    with open(in_file, "r") as fh:
        source = json.load(fh)
        for topic in tqdm(source["data"]):
            for para in topic["paragraphs"]:
                for qas in para['qas']:
                    if not qas["is_impossible"]:
                        for answer in qas["answers"]:
                            og_ans = answer['text']
                            len_ans = len(answer['text'])
                            ans_start = answer['answer_start']
                            ans_end = ans_start + len_ans
                            new_ans = (para['context'])[ans_start:ans_end]
                            if og_ans != new_ans:
                                log.info("error")
                                log.info(f"Question: {qas['question']}")
                                log.info(f"Orig answer: {og_ans}")
                                log.info(f"New Answer: {new_ans}")

if __name__ == "__main__":
    flags = sys.argv
    c = config()
    logger = get_logger(log_dir=c.logging_dir, name="exp_1 data transformer")

    tester(c.toy_data_exp1, logger)
