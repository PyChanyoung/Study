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

## Latency

The time it takes for a certain operation to complete in a system. Most often measure is a time duration, like milliseconds or seconds. You should know these orders of magnitude:

- Reading 1MB from RAM: 250us(0.25ms)
- Reading 1MB from SSD: 1,000us(1ms)
- Transfer 1MB over Network: 10,000us(10ms)
- Reading 1MB from HDD: 20,000us(20ms)
- Inter-Continental Round Trip: 150,000us(150ms)

## Throughput

The number of operations that a system can handle properly per time unit. For instance the throughput of a server can often be measured in requests per second (RPS or QPS).
