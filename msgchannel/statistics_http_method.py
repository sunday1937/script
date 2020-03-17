#!/usr/bin/env python3
import json

print('statistics_http_method start')
METHOD = 'xretail.user.badge.get'

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

try:
    print(METHOD)
    result_file = open('./json/result_http_user_badge_get3.json', 'r')
    result_str = result_file.read()
    # print(result_str)

    result_json = json.loads(result_str)

    hits_json_list = result_json['hits']['hits']
    # print(hits_json_list)
    rt_list = []
    if type(hits_json_list) == list :
        for item in hits_json_list:
            # print('item:', item)
            content_str = item['_source']['eventEs']['content']
            # print('content_str:', content_str)
            content_json = json.loads(content_str)
            print('content_json:', content_json)
            http_code = content_json['http_code']
            # print('http_code:', http_code)
            http_url = content_json['url']
            # print('http_url:', http_url)
            # http code == 200 && method == METHOD
            rt = content_json['time']
            app_status = 2
            if content_json.has_key('app_status'):
                app_status = content_json['app_status']
            
            if http_code == 200 and http_url.find(METHOD) and app_status < 2:
                # print('match request')
                if rt <= 30000:
                    rt_list.append(rt)
                
    # print('rt_list:', rt_list)
    print('rt_list.len:', len(rt_list))
    avg_time(rt_list)
    p_value(rt_list)
    


    
finally:
    if result_file:
        result_file.close()