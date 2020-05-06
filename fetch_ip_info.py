#!/usr/bin/python

import requests, sqlite3, time, fire, time

headers={'Content-Type': 'application/json', 'Acccept': 'application/json'}

def getCurrentTimestamp():
    _timestamp = int(time.time())
    return(_timestamp)

def fetch_ip_info(ip=""):
    db_connect = sqlite3.connect('ipinfo.db')
    db_cursor = db_connect.cursor()
    db_cursor.execute('create table if not exists ip_info (timestamp text, ip text, city text, region_code text, region_name text, time_zone text, longitude real, latitude real, metro_code real, country_code text, country_name text, zip_code text)')
    _request = requests.get('https://freegeoip.app/json/'+str(ip), headers=headers).json()

    _ip = str(_request['ip'])
    _timestamp = str(getCurrentTimestamp())
    _city = str(_request['city'])
    _region_code = _request['region_code']
    _region_name = _request['region_name']
    _tz = _request['time_zone']
    _long = _request['longitude']
    _lat = _request['latitude']
    _metro_code = _request['metro_code']
    _country_code = _request['country_code']
    _country_name = _request['country_name']
    _zip_code = str(_request['zip_code'])

    db_cursor.execute("insert into ip_info values ('{0}','{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')".format(
        getCurrentTimestamp(),
        _ip,
        _city,
        _region_code,
        _region_name,
        _tz,
        _long,
        _lat,
        _metro_code,
        _country_code,
        _country_name,
        _zip_code,
        ))

    db_connect.commit()
    db_connect.close()

if __name__ == '__main__':
    while True:
        fire.Fire(fetch_ip_info)
        time.sleep(5)
