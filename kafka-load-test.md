# Kafka Load Test (Ciaca)

* Note all commands should be run inside kafka container in `crowd_orchestrator`
* Frame has 269,760 bytes after compression (record size will be 270000)

## 1 Broker

### Producer

* --num-records [100, 1000, 10000]

```
kafka-producer-perf-test.sh --topic test --num-records 100 \
--throughput -1 --producer-props bootstrap.servers=localhost:9092 \--record-size 270000
```


#### Results

##### 100

100 records sent, 202.020202 records/sec (52.02 MB/sec), 136.98 ms avg latency, 302.00 ms max latency, 142 ms 50th, 200 ms 95th, 302 ms 99th, 302 ms 99.9th.

##### 1000

1000 records sent, 387.296669 records/sec (99.73 MB/sec), 274.66 ms avg latency, 504.00 ms max latency, 245 ms 50th, 478 ms 95th, 501 ms 99th, 504 ms 99.9th.

##### 10000

2576 records sent, 452.7 records/sec (116.57 MB/sec), 181.6 ms avg latency, 1764.0 ms max latency.
3631 records sent, 549.7 records/sec (141.53 MB/sec), 223.3 ms avg latency, 1947.0 ms max latency.
2234 records sent, 395.6 records/sec (101.87 MB/sec), 358.5 ms avg latency, 2504.0 ms max latency.
10000 records sent, 503.473970 records/sec (129.64 MB/sec), 243.46 ms avg latency, 2504.00 ms max latency, 152 ms 50th, 1062 ms 95th, 2459 ms 99th, 2502 ms 99.9th.

### Consumer

* --messages [100, 1000, 10000]


```
kafka-consumer-perf-test.sh --topic test --bootstrap-server localhost:9092 \
--messages 10000000
```

#### Results

##### 100

start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
2021-07-22 00:35:02:066, 2021-07-22 00:35:02:838, 0.9632, 1.2477, 203, 262.9534, 403, 369, 2.6103, 550.1355

##### 1000

start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
2021-07-22 00:36:15:654, 2021-07-22 00:36:18:413, 206.4419, 74.8249, 1001, 362.8126, 313, 2446, 84.3998, 409.2396

##### 10000

start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
2021-07-22 00:36:34:798, 2021-07-22 00:37:03:070, 2523.8705, 89.2710, 10001, 353.7422, 326, 27946, 90.3124, 357.8687

## 3 Brokers

### Producer

* --num-records [100, 1000, 10000]

```
kafka-producer-perf-test.sh --topic test --num-records 100 \
--throughput -1 --producer-props bootstrap.servers=localhost:9092,kafka2:9092,kafka3:9092 \--record-size 270000
```


#### Results

##### 100

100 records sent, 203.665988 records/sec (52.44 MB/sec), 122.31 ms avg latency, 288.00 ms max latency, 105 ms 50th, 206 ms 95th, 288 ms 99th, 288 ms 99.9th.

##### 1000

1000 records sent, 469.483568 records/sec (120.89 MB/sec), 224.78 ms avg latency, 379.00 ms max latency, 195 ms 50th, 366 ms 95th, 377 ms 99th, 379 ms 99.9th.

##### 10000

2876 records sent, 226.0 records/sec (58.20 MB/sec), 169.7 ms avg latency, 8800.0 ms max latency.
3600 records sent, 718.3 records/sec (184.95 MB/sec), 462.2 ms avg latency, 8799.0 ms max latency.
375 records sent, 22.0 records/sec (5.66 MB/sec), 488.3 ms avg latency, 16197.0 ms max latency.
10000 records sent, 255.983617 records/sec (65.91 MB/sec), 482.55 ms avg latency, 16198.00 ms max latency, 137 ms 50th, 466 ms 95th, 15892 ms 99th, 16194 ms 99.9th.



### Consumer

* --messages [100, 1000, 10000]


```
kafka-consumer-perf-test.sh --topic test --broker-list localhost:9092, kafka2:9092, kafka3:9092 \
--messages 10000
```

#### Results

##### 100

start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
WARNING: Exiting before consuming the expected number of messages: timeout (10000 ms) exceeded. You can use the --timeout option to increase the timeout.
2021-07-22 01:15:51:452, 2021-07-22 01:16:01:531, 0.0000, 0.0000, 0, 0.0000, 300, 9779, 0.0000, 0.0000



##### 1000

start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
WARNING: Exiting before consuming the expected number of messages: timeout (10000 ms) exceeded. You can use the --timeout option to increase the timeout.
2021-07-22 01:15:13:143, 2021-07-22 01:15:23:238, 0.0000, 0.0000, 0, 0.0000, 315, 9780, 0.0000, 0.0000



##### 10000

start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
WARNING: Exiting before consuming the expected number of messages: timeout (10000 ms) exceeded. You can use the --timeout option to increase the timeout.
2021-07-22 01:12:47:155, 2021-07-22 01:12:57:266, 0.0000, 0.0000, 0, 0.0000, 340, 9771, 0.0000, 0.0000

/////////

start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
WARNING: Exiting before consuming the expected number of messages: timeout (30000 ms) exceeded. You can use the --timeout option to increase the timeout.
2021-07-22 01:13:17:474, 2021-07-22 01:13:47:562, 0.0000, 0.0000, 0, 0.0000, 304, 29784, 0.0000, 0.0000

