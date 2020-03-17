#!/usr/bin/env python3
import json

print('statistics_http_method start')
METHOD = 'xretail.item.detail.getV2'

def avg_time(rt_list):
    print('avg_time')
    rt_list_len = 0
    rt_total = 0
    for rt in rt_list:
        rt_total = rt_total + rt;
        rt_list_len = rt_list_len + 1
    avg_time = rt_total / rt_list_len
    print('avg_time:', avg_time)
    return avg_time

def p_value(rt_list):
    print('p_value')
    rt_list.sort()
    length = len(rt_list)
    # print(rt_list)
    p90_index = int(0.9 * length)
    p95_index = int(0.95 * length)
    p99_index = int(0.99 * length)
    print('p90:', rt_list[p90_index])
    print('p95:', rt_list[p95_index])
    print('p99:', rt_list[p99_index])

def create_rt_list(json_list, rt_list):
    print('create_rt_list')
    if type(json_list) == list :
        for item in json_list:
            # print('item:', item)
            content_str = item['_source']['eventEs']['content']
            # print('content_str:', content_str)
            content_json = json.loads(content_str)
            http_code = content_json['http_code']
            # print('http_code:', http_code)
            http_url = content_json['url']
            # print('http_url:', http_url)
            # http code == 200 && method == METHOD
            rt = content_json['time']
            if http_code == 200 and http_url.find(METHOD):
                # print('match request')
                if rt <= 30000:
                    rt_list.append(rt)
    return rt_list

try:
    print(METHOD)
    f1 = open('./json/r_7_9.json', 'r')
    f2 = open('./json/r_9_11.json', 'r')
    f3 = open('./json/r_11_13.json', 'r')
    f4 = open('./json/r_13_17.json', 'r')
    f5 = open('./json/r_17_19.json', 'r')
    f6 = open('./json/r_19_21.json', 'r')
    s1 = f1.read()
    s2 = f2.read()
    s3 = f3.read()
    s4 = f4.read()
    s5 = f5.read()
    s6 = f6.read()
    # result_str = result_file.read()
    # print(result_str)

    j1 = json.loads(s1)
    j2 = json.loads(s2)
    j3 = json.loads(s3)
    j4 = json.loads(s4)
    j5 = json.loads(s5)
    j6 = json.loads(s6)
    # result_json = json.loads(result_str)

    l1 = j1['hits']['hits']
    l2 = j2['hits']['hits']
    l3 = j3['hits']['hits']
    l4 = j4['hits']['hits']
    l5 = j5['hits']['hits']
    l6 = j6['hits']['hits']

    # hits_json_list = result_json['hits']['hits']
    # print(hits_json_list)

    rt_list = []
    # if type(hits_json_list) == list :
    #     for item in hits_json_list:
    #         # print('item:', item)
    #         content_str = item['_source']['eventEs']['content']
    #         # print('content_str:', content_str)
    #         content_json = json.loads(content_str)
    #         http_code = content_json['http_code']
    #         # print('http_code:', http_code)
    #         http_url = content_json['url']
    #         # print('http_url:', http_url)
    #         # http code == 200 && method == METHOD
    #         rt = content_json['time']
    #         if http_code == 200 and http_url.find(METHOD):
    #             # print('match request')
    #             if rt <= 30000:
    #                 rt_list.append(rt)
    create_rt_list(l1, rt_list)
    create_rt_list(l2, rt_list)
    create_rt_list(l3, rt_list)
    create_rt_list(l4, rt_list)
    create_rt_list(l5, rt_list)
    create_rt_list(l6, rt_list)
                
    # print('rt_list:', rt_list)
    print('rt_list.len:', len(rt_list))
    avg_time(rt_list)
    p_value(rt_list)
    


    
finally:
    if f1:
        f1.close()
    if f2:
        f2.close()
    if f3:
        f3.close()
    if f4:
        f4.close()
    if f5:
        f5.close()
    if f6:
        f6.close()