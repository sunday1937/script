#!/usr/bin/env python3
import json

# statistics methods
METHODS = ['xretail.user.badge.get',
            'xretail.item.detail.getV2',
            'xretail.event.page.show']
# nanosecond to second
DEFAULT_TIME_VALUE = 1000000

# parse RT json list
def parse_content_time(result_list):
    print('parse_content start')
    # content_list = []
    method_list = []

    for item in result_list:
        # print(item)
        # print(type(item))
        content = item['_source']['eventEs']['content']
        # print(content)
        # print(type(content))
        content_json = json.loads(content)
        # print(type(content_json))
        # print('')

        rts = content_json['rts']
        # print(rts)
        if len(rts) != 0:
            # print(type(rts))
            for rt_item in rts:
                # print('rt_item type:{}'.format(type(rt_item)))
                method_list.append(rt_item)

        # content_list.append(content)
    print('method_list length:{}'.format(len(method_list)))
    return method_list

# average_time
def generate_method_time_dic(rt_list):
    print('generate_time_list')
    method_time_dic = {}
    for method in METHODS:
        # print('method: {}'.format(method))
        time_list = []
        for rt in rt_list:
            # print('rt:{}'.format(rt))
            if rt['method'] == method:
                # print('true')
                dis_time = (rt['eTime'] - rt['sTime']) / DEFAULT_TIME_VALUE;
                # print('dis_time:{}'.format(dis_time))
                time_list.append(dis_time)
        print('method:{}, time size:{}'.format(method, len(time_list)))
        method_time_dic[method] = time_list
    print('method_time_dic len:{}'.format(len(method_time_dic)))
    print('dic:{}'.format(method_time_dic.items()))
    return method_time_dic

# avg time method
def statistics_avg_time(time_dic):
    print('statistics_avg_time')
    for time_item_key in time_dic:
        # print(time_item_key)
        time_list = time_dic[time_item_key]
        total_time = 0
        for time_item in time_list:
            # print(time_item)
            total_time = total_time + time_item
        average_time = total_time / len(time_list)
        print('method:{}, time size:{}'.format(time_item_key, len(time_list)))
        print('method:{}, avg time:{}'.format(time_item_key, average_time))

# p90 p95 p99
def statistics_p_value(time_dic):
    print('statistics_p_value')
    for time_item_key in time_dic:
        time_list = time_dic[time_item_key]
        time_list.sort()
        # print('time_list sort:', time_list)
        print(time_item_key)
        length = len(time_list)
        p90_index = int(0.9 * length)
        p95_index = int(0.95 * length)
        p99_index = int(0.99 * length)
        print('list len:', length)
        print('p90 index:{} p95 index:{} p99 index:{}'.format(p90_index, p95_index, p99_index))
        print('p90:', time_list[p90_index])
        print('p95:', time_list[p95_index])
        print('p99:', time_list[p99_index])
        print('method:{} p90:{} p95:{} p99:{}'.format(time_item_key, time_list[p90_index], time_list[p95_index], time_list[p99_index]))

# average_time
def statistics_average_time(rt_list):
    print('statistics_time')
    for method in METHODS:
        # print('method: {}'.format(method))
        time_list = []
        for rt in rt_list:
            # print('rt:{}'.format(rt))
            if rt['method'] == method:
                # print('true')
                dis_time = (rt['eTime'] - rt['sTime']) / DEFAULT_TIME_VALUE;
                # print('dis_time:{}'.format(dis_time))
                time_list.append(dis_time)
        print('method:{}, time size:{}'.format(method, len(time_list)))
        total_time = 0
        for time_item in time_list:
            # print(time_item)
            total_time = total_time + time_item
        average_time = total_time / len(time_list)
        print('method:{}, count:{}'.format(method, average_time))

    

print('msgchannel handle start!')
try:
    result_file = open('./json/result.json', 'r')
    result_str = result_file.read()
    # print(result_str)

    result_json = json.loads(result_str)

    hits_json_list = result_json['hits']['hits']
    # print(hits_json_array)
    # print(type(hits_json_array))
    rt_list = []
    if type(hits_json_list) == list :
        # print('hits_json_list is list type')
        rt_list = parse_content_time(hits_json_list)
        # print(rt_list)
    # statistics_average_time(rt_list)
    method_time_dic = generate_method_time_dic(rt_list)
    statistics_avg_time(method_time_dic)
    statistics_p_value(method_time_dic)
finally:
    if result_file:
        result_file.close()
