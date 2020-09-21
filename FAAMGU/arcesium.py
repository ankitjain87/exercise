#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateNAV' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts STRING date as parameter.
#

import requests

HOLDING_API = 'https://raw.githubusercontent.com/arcjsonapi/HoldingValueCalculator/master/paging/holding_start'
PRICING_API = 'https://raw.githubusercontent.com/arcjsonapi/HoldingValueCalculator/master/paging/pricing_start'


class APIException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def make_get_call(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise APIException("Not able to get data from %s" % url)

    return response.json()


def make_holding_data(date, day_holdings, data):
    found, is_done = False, False
    for row in data:
        if row['date'] == date:
            if not found:
                found = True
            
            if row['security'] not in day_holdings:
                day_holdings[row['security']] = 0
            
            day_holdings[row['security']] += row['quantity']
        else:
            if found:
                is_done = True
                break

    return day_holdings, found, is_done


def make_price_data(date, day_price, data):
    found, is_done = False, False
    for row in data:
        if row['date'] == date:
            if not found:
                found = True

            day_price[row['security']] = row['price']
        else:
            if found:
                is_done = True
                break

    return day_price, found, is_done


def get_data(date, api_url, is_holding_data=False):
    data_json = make_get_call(api_url)
    data = data_json['data']

    day_data = {}
    while data_json:
        if is_holding_data:
            day_data, found, is_done = make_holding_data(
                date, day_data, data)
        else:
            day_data, found, is_done = make_price_data(
                date, day_data, data)

        if (found and is_done) or 'nextPage' not in data_json:
            break

        data_json = make_get_call(data_json['nextPage'])
        data = data_json['data']

    return day_data


def calculateNAV(date):
    try:
        day_holdings = get_data(date, HOLDING_API, is_holding_data=True)
        day_price = get_data(date, PRICING_API)

        holding_value = 0
        for name, quantity in day_holdings.items():
            holding_value += day_price[name] * quantity

        return round(holding_value, 2)
    except APIException as ex:
        return str(ex)
    except Exception as ex:
        return "Error while calculating NAV " + str(ex)



print(calculateNAV('20190725'))
# print(get_prices('20190725'))

