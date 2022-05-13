# Client-Server Model

## Client

A machine or process that requests data or service from a server.
</br>
Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

## Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.
</br>
Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

## Client-Server Model

The paradigm by which modern systems are desinged, which consists of clients requesting data or service from servers and servers providing data or service to clients.

## IP Address

An address given to each machine connected to the public internet. IPv4 addresses consist of four numbers separated by dots: **a.b.c.d** where all four numbers are between 0 and 255. Special values include:

- **127.0.0.1**: Your own local machine. Also referred to as **localhost.**
- **192.168.x.y**: Your private network. For instance, your machine and all machines on your private wifi network will usually have the **192.168** prefix.

## Port

In order for multiple programs to listen for new network connections on the same machine without colliding, they pick a **port** to listen on. A port is an integer between 0 and 65,535 (2^16 ports total).
</br>
Typically, ports 0-1023 are reserved for system ports (also called well-known ports) and shouldn’t be used by user-level processes. Certain ports have pre-defined uses, and although you usually won’t be required to have them memorized, they can sometimes come in handy. Below are some examples:
</br>

- 22: Secure Shell</br>
- 53: DNS lookup</br>
- 80: HTTP</br>
- 443: HTTPS

## DNS

Short for Domain Name System, it describes the entities and protocols involved in the translation from domain names to IP addresses. Typically, machines make a DNS query to a well-known entity which is responsible for returning the IP address (or multiple ones) of the requested domain name in the response.

# Network Protocol

## IP

Stands for **Internet Protocol.** This network protocol outlines how almost all machine-to-machine communications should happen in the world. Other protocols like **TCP, UDP** and **HTTP** are built on top of IP.

## TCP

Network protocol built on top on the Internet Protocol (IP). Allows for ordered, reliable data delivery between machines over the public internet by creating a **connection.**
</br>

TCP is usually implemented in the kernel, which exposes **sockets** to applications that they can use to stream data through an open connection.

## HTTP

The **H**yper**T**ext**T**ransfer**P**rotocol is a very common network protocol implemented on top of TCP. Clients make HTTP requests, and servers respond with a response.
</br>
Requests typically have the following schema:
</br>

```
host: string (example: algoexpert.io)
port: ilnteger (example: 80 or 443)
method: string (example: GET, PUT, POST, DELETE, OPTIONS or PATCH)
path: string
headers: pair list (example: "Content-Type" => "application/json")
body: opaque sequence of bytes
```

Responses typically have the following schema:

```
status code: integer (example: 200, 401)
headers: pair list (example: "Content-Length" => 1238)
body: opaque sequence of bytes
```

## IP Packet

Sometimes more broadly referred to as just a (network) **packet,** an IP packet is effectively the smallest unit used to describe data being sent over **IP,** aside from bytes. An IP packet consists of:

- an **IP header,** which contains the source and destination **IP addresses** as well as other information related to the network (e.g., total size of the packet, version of the internet protocol that this IP packet is operating by: IPv4 or IPv6). It's usually between 20 and 60 bytes (smaller portion than main data).
- a **payload,** which is just the data being sent over the network

One IP packets are only two to the power of 16 (2^16) bytes: ~65,000 bytes or ~0.065MB. - This is pretty small considering that you sometimes send an email or big files. So, you'd have to send multiple packets. - **Problem with sending multiple files**: if all you're using is the Internet Protocol, there's <u>NO way of guaranteeing that these packets are acually (1) gonna be received (2) in correct order.</u> - ==> **this is where TCP comes into play**

# Storage

## Databases

Data are programs that either use disk or memory to do 2 core things: **record(=store, write)** data and **query (=retrieve, read)** data. In general, they are themselves servers(=Databases are just server) that are long-lived and interact with the rest of your application through network calls, with protocols on top of TCP or even HTTP.

Persistence

- Some databases only keep records in memory, and the users of such databases are aware of the fact that those records may be lost forever if the machine or process dies.

- For the most part though, databases need persistence of those records, and thus cannot use memory. This means that you have to write your data to disk. Anything written to disk will remain through power loss or network partitions, so that's what is used to keep permanent records.

Since machines die often in a large scale system, special disk partitions or volumes are used by the database processes, and those volumes can get recovered even if the machine were to go down permanently.

## Disk

Usually refers to either **HDD (hard-disk drive)** or **SSD (solid-state drive)**. Data written to disk will persist through power failures and general machine crashes. Disk is also referred to as **non-volatile storage.**
SSD is far faster than HDD (see latencies of accessing data from SSD and HDD) but also far more expensive from a financial point of view. Because of that, HDD will typically be used for data that’s rarely accessed or updated, but that’s stored for a long time, and SSD will be used for data that’s frequently accessed and updated.

## Memory (Random Access Memory (RAM))

Data stored in memory will be lost when the process that has written that data dies.

## Persistent Storage

Usually refers to disk, but in general it is any form of storage that persists if the process in charge of managing it dies.

# Latency and Throughput

## Latency

The time it takes for a certain operation to complete in a system. Most often measure is a time duration, like milliseconds or seconds. You should know these orders of magnitude:

- Reading 1MB from RAM: 250us(0.25ms)
- Reading 1MB from SSD: 1,000us(1ms)
- Transfer 1MB over Network: 10,000us(10ms)
- Reading 1MB from HDD: 20,000us(20ms)
- Inter-Continental Round Trip: 150,000us(150ms)

Certain types of systems really care about latencies (e.g., multiplayer games), while other websites care less about latencies but care more about accuracy or up-time (never going down).

## Throughput

- The number of operations that a system can handle properly per time unit. How much data can be transferred from one point in a system to another in a given amount of time.
- Measurement: For instance the throughput of a server can often be measured in requests per second (RPS or QPS). Typically, in gigabits per second (Gbps) or Kbps or Mbps.
- Can increase throughput by paying more (e.g., to a cloud provider).
- Latency and throughput seem related, but they are **NOT correlated**. You CANNOT make assumption about latency or throughput based on the other.

# Availability

## Process

A program that is currently running on a machine. You should always assume that any process may get terminated at any time in a sufficiently large system.

## Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

## Node / Instance / Host

These three terms refer to the same thing most of the time: a virtual or physical machine on which the developer runs processes.
Sometimes the work **server** also refers to this same concept.

## Availability

The odds of a particular server or service being up and running at any point in time, usually measured in percentages. A server that has 99% availability will be operational 99% of the time (this would be described as having two **nines** of availability).

## High Availability

Used to describe systems that have particulary high levels of availability, typically 5 nines or more; sometimes abbreviated "HA".

## Nines

Typically refers to percentages of uptime. For example, 5 nines of availability means an uptime of 99.999% of the time. Below are the downtimes expected per year depending on those 9s:

```
- 99% (two 9s): 87.7 hours
- 99.9%(three 9s): 8.8 hours
- 99.99%: 52.6 minutes
- 99.999%: 5.3 minutes
```

## Redundancy

The process of replicating parts of a system in an effort to make it more reliable.

## SLA (Service-level Agreement)

SLA is a collection of guarantees given to a customer by a service provider.
SLAs typically make guarantees on a system’s availability, amongst other things.
SLAs are made up of one or multiple SLOs.

## SLO (Service-level Objective)

SLO is a guarantee given to a customer by a service provides. SLOs typically make guarantees on a system’s availability, amongst other things.
SLOs constitute SLA

# MapReduce

## File System

An abstraction over a storage medium that defines how to manage data. While there exist many different types of file systems, most follow a hierarchical structure that consists of directories and files, like the <u>Unix file system’s</u> structure.

## Idempotent Operation

An operation that has the same ultimate outcome regardless of how many times it’s performed. If an operation can be performed multiple times without changing its overall effect, it’s idempotent. Operations performed through a **Pub/Sub** messaging system typically have to be idempotent, since Pub/Sub systems tend to allow the same messages to be consumed multiple times.
For example, increasing an integer value in a database is not an idempotent operation, since repeating this operation will not have the same effect as if it had been performed only once. Conversely, setting a value to “COMPLETE” is an idempotent operation, since repeating this operation will always yield the same result: the value will be “COMPLETE”.

## MapReduce

**Background** : Early 2000s, Google engineers faced a problem that data sets are getting incredibly larger, and there’s only so much vertical scaling possible. You eventually have to horizontally scale your system by adding more machines. When dealing with a distributed system, otherwise simple tasks like processing a dataset become very difficult.

A popular framework for processing very large datasets in a distributed setting efficiently, quickly, and in a fault-tolerant manner. A MapReduce job is comprised of 3 main steps:

- **Map** step : Runs a <u>map function</u> on the various chunks of the dataset and transforms these chunks into intermediate <u>key-value pairs.</u>
- **Shuffle** step : Reorganizes the intermediate <u>key-value pairs</u> such that pairs of the same key are routed to the same machine in the final step.
- **Reduce** step : Runs a <u>reduce function</u> on the newly shuffled <u>key-value pairs</u> and transforms them into more meaningful data.

The canonical example of a MapReduce use case is counting the number of occurrences of words in a large text file.
When dealing with a MapReduce library, engineers and/or systems administrators only need to worry about the map and reduce functions, as well as their inputs and outputs. All other concerns, including the parallelization of tasks and the fault-tolerance of the MapReduce job, are abstracted away and taken care of by the MapReduce implementation.

Important Notes :
(1) Distributed File System : when dealing with a MapReduce model, we assume that we have a distributed system where large datasets are split up into chunks, and these chunks are replicated and spread across multiple machines.

    - This system has a central control plane that is aware of everything going on in the MapReduce job/process. It knows :
        - Where all of the chunks of data reside
        - How to communicate with various machines that store all of this data
        - How to communicate with the machines that are gonna be performing the Map operations (‘Worker Machines’)
        - How to communicate with reduce workers
        - Where the output is going to live

(2) We do NOT want to move the large data sets. We’d like to let them live where they currently reside on their respective machines, but rather have our Map programs move to the data and operate on the data locally. Instead of grabbing all the data and moving them elsewhere, we send the Map program to the data.

(3) Key-value (KV) pairs structure of the data (in the intermediate step). When you ‘reduce’ data (which by the way are multiple chunks of the same large data set), you’ll notice some sort of commonality in these pieces of data. The key-value pair structure is useful because there will be some keys that are going to be common, and they can aggregate and reduce data in one single meaningful value.

(4) Handling fault. When there’s a network/machine failure (for one of the chunks), a MapReduce job is going to re-perform a Map or Reduce operation where a failure occurred.

    - The central control plane will orchestrate this (reperforming).
    - Map/Reduce functions are idempotent. In other words, if we repeat a Map/Reduce function, the result will be the same regardless of how many times we’ve repeated.

(5) You as an engineer or systems administrator only need to worry about the map and reduce functions, as well as their inputs and outputs. All other concerns, including the parallelization of tasks and the fault-tolerance of the MapReduce job, are abstracted away and taken care of by the MapReduce implementation.

## Distributed File System (DFS)

A DFS is an abstraction over a (usually large) cluster of machines that allows them to act like one large file system. The two most popular implementations of a DFS are the **Google File System** (GFS) and the **Hadoop Distributed File System** (HDFS).
Typically, DFSs take care of the classic <u>availability</u> and <u>replication</u> guarantees that can be tricky to obtain in a distributed system setting. The overarching idea is that files are split into chunks of a certain size (4MB or 64MB, for instance), and those chunks are sharded across a large cluster of machines. A central control plane is in charge of deciding where each chunk resides, routing reads to the right nodes, and handling communication between machines.
Different DFS implementations have slightly different APIs and semantics, but they achieve the same common goal: extremely large-scale persistent storage.

## Hadoop

A popular, open-source framework that supports MapReduce jobs and many other kinds of data-processing pipelines. Its central component is HDFS (Hadoop Distributed File System), on top of which other technologies have been developed.
