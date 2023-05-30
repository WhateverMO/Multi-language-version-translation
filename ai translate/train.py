from dataset import *
from model import Transformer
import torch,time
import torch.nn as nn
# Config
# batch_size = 2
# lr = 0.0001
# d_model = 64
# d_ff = 128
# n_layers = 3
# heads = 8
# batch_size = 2
# lr = 0.1
# d_model = 32
# d_ff = 64
# n_layers = 3
# heads = 8

max_element = 0.05
lr = 0.1
batch_size = 16
epoches = 10
d_model = 512   # 字 Embedding 的维度
d_ff = 1024     # 前向传播隐藏层维度
d_k = d_v = 64  # K(=Q), V的维度
n_layers = 6    # 有多少个encoder和decoder
n_heads = 8     # Multi-Head Attention设置为8
# src_vocab_size,tgt_vocab_size,d_model,d_ff,d_k,d_v,n_heads,n_layers

print_interval = 1000
max_generate_length_precent = 2

def predict(model,sentences,src_vocab,tgt_vocab,insert_space=False):
    start_symbol = 0
    enc_input = sentence_to_tensor(sentences=[sentences],
                                   vocab=src_vocab)
    max_generate_length = enc_input.size*max_generate_length_precent
    enc_input = enc_input.astype(int)
    enc_input = torch.from_numpy(enc_input)
    enc_outputs, enc_self_attns = model.Encoder(enc_input)
    dec_input = torch.zeros(1, 1).type_as(enc_input.data)
    next_symbol = start_symbol
    i = 0
    while i<max_generate_length:
        dec_input[0][i] = next_symbol
        if next_symbol == 1:
            break
        dec_cell = torch.zeros(1, 1).type_as(enc_input.data)
        dec_input = torch.cat((dec_input,dec_cell),1)
        dec_outputs, _, _ = model.Decoder(dec_input, enc_input, enc_outputs)
        projected = model.projection(dec_outputs)
        prob = projected.squeeze(0).max(dim=-1, keepdim=False)[1]
        next_word = prob.data[i]
        next_symbol = next_word.item()
        print('\r  ',tensor_to_sentence(dec_input[0],tgt_vocab,insert_space),end='')
        i += 1
    output = tensor_to_sentence(dec_input[0],tgt_vocab,insert_space)
    print()
    return output

def test():
    en_vocab, zh_vocab = load_vocab(max_element=max_element)
    src_vocab_size = len(en_vocab)
    tgt_vocab_size = len(zh_vocab)
    en_train, zh_train, en_valid, zh_valid = load_sentences(max_element=max_element)
    print('inited')
    device = 'cpu'
    model = Transformer(src_vocab_size, tgt_vocab_size, d_model, d_ff, d_k, d_v, n_heads, n_layers, device)
    dataloader_valid = get_dataloader(en_valid, zh_valid,batch_size=1)
    print('data loaded')
    criterion = nn.CrossEntropyLoss(ignore_index=PAD_ID)         # 忽略 占位符 索引为0.
    model.to(device=device)
    model.load_state_dict(torch.load('model0_0.pth'))
    model.eval()
    print('model loaded')
    tic = time.time()
    cnter,loss_sum = 0,0
    dataset_len = len(dataloader_valid.dataset)
    print('Dataset size:', dataset_len)
    for enc_inputs, dec_inputs, dec_outputs in dataloader_valid:  # enc_inputs : [batch_size, src_len]
        enc_inputs, dec_inputs, dec_outputs = enc_inputs.to(device), dec_inputs.to(device), dec_outputs.to(device)
        outputs, enc_self_attns, dec_self_attns, dec_enc_attns = model(enc_inputs, dec_inputs)
        loss = criterion(outputs, dec_outputs.view(-1))
        loss_sum += loss.item()
        toc = time.time()
        interval = toc - tic
        minutes = int(interval // 60)
        seconds = int(interval % 60)
        if cnter % print_interval == 0:
            print(f'{cnter:08d} {minutes:02d}:{seconds:02d}'
                  f' loss: {loss.item()}')
        cnter += 1
    print(f'test valid. loss: {loss_sum / len(dataloader_valid.dataset)}')

def valid(model,device,src_valid,tgt_valid,src_vocab,tgt_vocab):
    print('#'*20)
    print('valid:')
    dataloader_valid = get_dataloader(src_valid, tgt_valid,batch_size=1)
    print('data loaded')
    criterion = nn.CrossEntropyLoss(ignore_index=PAD_ID)         # 忽略 占位符 索引为0.
    tic = time.time()
    cnter,loss_sum = 0,0
    dataset_len = len(dataloader_valid.dataset)
    print('Dataset size:', dataset_len)
    for enc_inputs, dec_inputs, dec_outputs in dataloader_valid:  # enc_inputs : [batch_size, src_len]
        enc_inputs, dec_inputs, dec_outputs = enc_inputs.to(device), dec_inputs.to(device), dec_outputs.to(device)
        outputs, enc_self_attns, dec_self_attns, dec_enc_attns = model(enc_inputs, dec_inputs)
        loss = criterion(outputs, dec_outputs.view(-1))
        loss_sum += loss.item()
        toc = time.time()
        interval = toc - tic
        minutes = int(interval // 60)
        seconds = int(interval % 60)
        input = tensor_to_sentence(enc_inputs[0], src_vocab,True)
        output = tensor_to_sentence(outputs[0], tgt_vocab,True)
        if cnter % print_interval == 0:
            print(f'{cnter:08d} {minutes:02d}:{seconds:02d}'
                  f' loss: {loss.item()}  {input} #-># {output[:len(input)]}')
        cnter += 1
    print(f'test valid. loss: {loss_sum / len(dataloader_valid.dataset)}')
    print('#'*20)

def main():
    en_vocab, zh_vocab = load_vocab(max_element=max_element)
    src_vocab_size = len(en_vocab)
    tgt_vocab_size = len(zh_vocab)
    en_train, zh_train, en_valid, zh_valid = load_sentences(max_element=max_element)
    print('inited')
    device = 'cuda:0'
    model = Transformer(src_vocab_size, tgt_vocab_size, d_model, d_ff, d_k, d_v, n_heads, n_layers, device)
    print(model)
    dataloader_train = get_dataloader(en_train, zh_train, batch_size)
    print('data loaded')
    model.to(device)
    # model.init_weights()
    # optimizer = torch.optim.Adam(model.parameters(), lr)
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3, momentum=0.99)
    criterion = nn.CrossEntropyLoss(ignore_index=PAD_ID)         # 忽略 占位符 索引为0.
    # citerion = nn.CrossEntropyLoss(ignore_index=PAD_ID)
    tic = time.time()
    cnter = 0
    dataset_len = len(dataloader_train.dataset)
    print('Dataset size:', dataset_len)
    for epoch in range(epoches):
        loss_sum = 0
        for enc_inputs, dec_inputs, dec_outputs in dataloader_train:  # enc_inputs : [batch_size, src_len]
            enc_inputs, dec_inputs, dec_outputs = enc_inputs.to(device), dec_inputs.to(device), dec_outputs.to(device)
            outputs, enc_self_attns, dec_self_attns, dec_enc_attns = model(enc_inputs, dec_inputs)
            loss = criterion(outputs, dec_outputs.view(-1))
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)
            optimizer.step()
            loss_sum += loss.item()
            toc = time.time()
            interval = toc - tic
            day = int(interval // 60 // 60 // 24)
            hour = int((interval // 60 // 60)%24)
            minutes = int((interval // 60)%60)
            seconds = int(interval % 60)
            if cnter % print_interval == 0:
                print(f'{cnter*batch_size:08d} {day:02d} {hour:02d} {minutes:02d}:{seconds:02d}'
                      f' loss: {loss.item()}')
                if cnter % (print_interval*50) == 0:
                    torch.save(model.state_dict(), f'model{epoch}_{cnter}.pth')
            cnter += 1

        print(f'Epoch {epoch}. loss: {loss_sum / dataset_len * batch_size}')
        valid(model, device, en_valid, zh_valid, en_vocab, zh_vocab)

        # if valid_period

        torch.save(model.state_dict(), f'model{epoch}.pth')
    print('Done.')

if __name__ == '__main__':
    main()
    # test()
    # device = 'cpu'
    # en_vocab, zh_vocab = load_vocab(max_element=max_element)
    # src_vocab_size = len(en_vocab)
    # tgt_vocab_size = len(zh_vocab)
    # model = Transformer(src_vocab_size, tgt_vocab_size, d_model, d_ff, d_k, d_v, n_heads, n_layers, device)
    # model.load_state_dict(torch.load('model0_3000.pth'))
    # print(predict(model, 'He calls the Green Book, his book of teachings, “the new gospel.', en_vocab, zh_vocab))