from torchtext.data import get_tokenizer
from collections import Counter
import json,jieba,torch
import numpy as np
from tqdm import tqdm
from torch.utils.data import DataLoader, Dataset
from torch.nn.utils.rnn import pad_sequence
import pickle

SOS_ID = 0
EOS_ID = 1
UNK_ID = 2
PAD_ID = 3

tokenizer = get_tokenizer('basic_english')
# english = tokenizer(english)

def read_file(json_path):
    english_sentences = []
    chinese_sentences = []
    tokenizer = get_tokenizer('basic_english')
    name = json_path.split('/')
    name = name[-1]
    with open(json_path, 'r') as fp:
        fp = fp.readlines()
        for line in tqdm(fp, desc=name, total=len(fp)):
            line = json.loads(line)
            english, chinese = line['english'], line['chinese']
            # Correct mislabeled data
            if not english.isascii():
                english, chinese = chinese, english
            # Tokenize
            english = tokenizer(english)
            chinese = list(jieba.cut(chinese))
            chinese = [x for x in chinese if x not in {' ', '\t'}]
            english_sentences.append(english)
            chinese_sentences.append(chinese)
    return english_sentences, chinese_sentences

def create_vocab(sentences, max_element=None):
    """Note that max_element includes special characters"""

    default_list = ['<sos>', '<eos>', '<unk>', '<pad>']

    char_set = Counter()
    for sentence in tqdm(sentences, total=len(sentences)):
        c_set = Counter(sentence)
        char_set.update(c_set)

    if type(max_element) == float and max_element < 1 and max_element > 0:
        max_element = len(char_set.keys())*max_element
        max_element = int(max_element)
        print('max_element:',max_element)

    if max_element is None:
        return default_list + list(char_set.keys())
    else:
        max_element -= 4
        words_freq = char_set.most_common(max_element)
        # pair array to double array
        words, freq = zip(*words_freq)
        print('cover rate:',sum(freq)/sum(char_set.values()))
        return default_list + list(words)

def sentence_to_tensor(sentences, vocab):
    vocab_map = {k: i for i, k in enumerate(vocab)}

    def process_word(word):
        return vocab_map.get(word, UNK_ID)

    res = []
    for sentence in sentences:
        sentence = np.array(list(map(process_word, sentence)), dtype=np.int32)
        res.append(sentence)

    return np.array(res, dtype=object)

def tensor_to_sentence(tensor, mapping, insert_space=False):
    res = ''
    first_word = True
    for id in tensor:
        word = mapping[int(id.item())]

        if insert_space and not first_word:
            res += ' '
        first_word = False

        res += word

    return res

def load_vocab(isMain=False,max_element = None):
    f = True
    while f:
        try:
            vocab = np.load(f'./translation2019zh/vocab{max_element}.npy',
                            allow_pickle=True).item()
            f = False
        except FileNotFoundError:
            if isMain:
                raise FileNotFoundError
            main(max_element)
    en_vocab = vocab['en']
    zh_vocab = vocab['zh']
    return en_vocab, zh_vocab

def load_sentences(isMain=False,max_element=None):
    f = True
    while f:
        try:
            tensors = np.load(f'./translation2019zh/sentences{max_element}.npy',
                              allow_pickle=True).item()
            f = False
        except FileNotFoundError:
            if isMain:
                raise FileNotFoundError
            main()
    en_tensors_train = tensors['en_train']
    zh_tensors_train = tensors['zh_train']
    en_tensors_valid = tensors['en_valid']
    zh_tensors_valid = tensors['zh_valid']
    return (en_tensors_train, zh_tensors_train, en_tensors_valid,
            zh_tensors_valid)

def load_sentences_pkl(isMain=False):
    f = True
    while f:
        try:
            with open('./translation2019zh/sentences.pkl','rb') as file:
                sentences = pickle.load(file)
            f = False
        except FileNotFoundError:
            if isMain:
                raise FileNotFoundError
            main()
    en_tensors_train = sentences['en_sens_train']
    zh_tensors_train = sentences['zh_sens_train']
    en_tensors_valid = sentences['en_sens_valid']
    zh_tensors_valid = sentences['zh_sens_valid']
    return (en_tensors_train, zh_tensors_train, en_tensors_valid,
            zh_tensors_valid)

class TranslationDataset(Dataset):

    def __init__(self, frm_tensor: np.ndarray, to_tensor: np.ndarray):
        super().__init__()
        assert len(frm_tensor) == len(to_tensor)
        self.length = len(frm_tensor)
        self.frm_tensor = frm_tensor
        self.to_tensor = to_tensor

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        x = np.concatenate(([SOS_ID], self.frm_tensor[index], [EOS_ID]))
        x = torch.from_numpy(x)
        y = np.concatenate(([SOS_ID], self.to_tensor[index], [EOS_ID]))
        y = torch.from_numpy(y)
        return x, y[:-1],y[1:]

def get_dataloader(frm_tensor: np.ndarray,
                   to_tensor: np.ndarray,
                   batch_size=16):

    def collate_fn(batch):
        x, y,y1 = zip(*batch)
        x_pad = pad_sequence(x, batch_first=True, padding_value=PAD_ID)
        y_pad = pad_sequence(y, batch_first=True, padding_value=PAD_ID)
        y_1_pad = pad_sequence(y1, batch_first=True, padding_value=PAD_ID)

        return x_pad, y_pad,y_1_pad

    dataset = TranslationDataset(frm_tensor, to_tensor)
    dataloader = DataLoader(dataset,
                            batch_size=batch_size,
                            shuffle=True,
                            collate_fn=collate_fn)

    return dataloader

def main(max_element = None):
    try:
        print('loading sentences pkl')
        en_sens_train,zh_sens_train,en_sens_valid,zh_sens_valid = load_sentences_pkl(True)
        print('loaded')
    except FileNotFoundError:
        print('process json')
        en_sens_train, zh_sens_train = read_file(
            './translation2019zh/translation2019zh_train.json')
        en_sens_valid, zh_sens_valid = read_file(
            './translation2019zh/translation2019zh_valid.json')
        print('processed')
        sentences = {
            'en_sens_valid':en_sens_valid,
            'en_sens_train':en_sens_train,
            'zh_sens_train':zh_sens_train,
            'zh_sens_valid':zh_sens_valid
        }
        print('writing')
        with open('./translation2019zh/sentences.pkl','wb') as file:
            pickle.dump(sentences,file)
        print('written')
    try:
        print('loading vocab')
        en_vocab,zh_vocab = load_vocab(True,max_element)
        print('loaded')
    except FileNotFoundError:
        print('process vocab')
        en_vocab = create_vocab(en_sens_train,max_element)
        zh_vocab = create_vocab(zh_sens_train,max_element)
        print('processed')
        vocab = {'en': en_vocab, 'zh': zh_vocab}
        print('writing')
        np.save(f'./translation2019zh/vocab{max_element}.npy', vocab)
        print('written')
    try:
        print('loading sentences')
        en_tensors_train, zh_tensors_train, en_tensors_valid, zh_tensors_valid = load_sentences(True,max_element)
        print('loaded')
    except FileNotFoundError:
        print('process tensor')
        en_tensors_train = sentence_to_tensor(en_sens_train, en_vocab)
        zh_tensors_train = sentence_to_tensor(zh_sens_train, zh_vocab)
        en_tensors_valid = sentence_to_tensor(en_sens_valid, en_vocab)
        zh_tensors_valid = sentence_to_tensor(zh_sens_valid, zh_vocab)
        print('processed')
        tensors = {
            'en_train': en_tensors_train,
            'zh_train': zh_tensors_train,
            'en_valid': en_tensors_valid,
            'zh_valid': zh_tensors_valid
        }
        print('writing')
        np.save(f'./translation2019zh/sentences{max_element}.npy', tensors)
        print('written')

if __name__ == '__main__':
    main()
    # load_vocab()
    # load_sentences()
    # load_sentences_pkl(True)

__all__ = ['load_vocab','load_sentences','load_sentences_pkl',
           'sentence_to_tensor','tensor_to_sentence','get_dataloader',
           'SOS_ID','EOS_ID','UNK_ID','PAD_ID']