# -*- coding: utf-8 -*-
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import string
import time  # ����ʱ��ģ��

def create_file(filename):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=200))
    with open(filename, 'w',encoding='gbk') as f:
        f.write(random_string)  # д��һЩ���ݻ�������

def create_files(directory, num_files):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filenames = [os.path.join(directory, f'1025newfile_{i}.doc') for i in range(num_files)]
    with ThreadPoolExecutor(max_workers=100) as executor:  # ���Ե���max_workers�����������Ʋ�����
        executor.map(create_file, filenames)

# Start Time
start_time = time.time()
create_files('D:\\bigdata', 100000)

# ��¼����ʱ�䲢�����ʱ
end_time = time.time()
execution_time = end_time - start_time

print(f"Program execution completed!")
print(f"Total time: {execution_time:.2f} seconds")
