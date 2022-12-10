# -*- coding: utf-8 -*-
# @Author: Ang Jian Hwee
# @Date:   2022-12-10 19:16:05
# @Last Modified by:   Ang Jian Hwee
# @Last Modified time: 2022-12-10 19:22:04


import redis, datetime
def test_redis_connection_is_aiven_cloud():
	try:
		r = redis.Redis("redis-1bbf2d0d-nightorb-d1fc.aivencloud.com", 21416, 0,
						'AVNS_RjXI0p9WSMhwkj2j1RW')
		r.ping()
	except:
		r = redis.Redis("redis-10701.c62.us-east-1-4.ec2.cloud.redislabs.com",
						10701, 0, 'G5geqLgrwhoY569qaXYWcX6oNCHdFWht')
		r.ping()
	
	assert str(vars(vars(r)['connection_pool'])['connection_kwargs']['host'].split(".")[-2]) == "aivencloud"
