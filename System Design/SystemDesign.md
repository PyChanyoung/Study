# Client-Server Model

### Client

- A machine or process that requests data or service from a server.

- Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Server

- A machine or process that provides data or service for a client, usually by listening for incoming network calls.

### Client-Server Model

- The paradigm by which modern systems are designed, which consists of clients requesting data or service from servers and servers providing data or service to clients.

### IP Address

- An address given to each machine connected to the public internet. IPv4 addresses consist of four numbers separated by dots: **a.b.c.d** where all four numbers are between 0 and 255. Special values include:
  - **127.0.0.1**: Your own local machine. Also referred to as **localhost.**
  - **192.168.x.y**: Your private network. For instance, your machine and all machines on your private wifi network will usually have the **192.168** prefix.

### Port

- **Port** is "a number assigned to uniquely identify a connection endpoint and to direct data to a specific service" <Wikipeida>
- In order for multiple programs to listen for new network connections on the same machine without colliding, they pick a **port** to listen on. A port is an integer between 0 and 65,535 (2^16 ports total).
- Typically, ports 0-1023 are reserved for system ports (also called well-known ports) and shouldn’t be used by user-level processes. Certain ports have pre-defined uses, and although you usually won’t be required to have them memorized, they can sometimes come in handy.
- Examples:
  - 22: Secure Shell
  - 53: DNS lookup
  - 80: HTTP
  - 443: HTTPS

### DNS (Domain Name System)

- DNS describes the entities and protocols involved in the transaction from domain names to IP addresses.
- Typically, machines make a DNS query to a well-known entity which is responsible for returning the IP address (or multiple ones) of the requested domain name in the response.

# Network Protocols

### Protocol

- An agreed-upon set of rules for an interaction between two parties.

### IP (Internet Protocol)

- This network protocol outlines how almost all machine-to-machine communications should happen in the world. Other protocol like TCP, UDP, and HTTP are built on top of the IP.
- Modern internet effectively runs on IP : when a message is sent to another machine, data is going to be sent in the form of an IP packet.

### IP Packet
- Sometimes more broadly referred to as just a (network) packet, an IP packet is effectively the smallest unit used to describe data being sent over IP, aside from bytes.
- An IP packet consists of:
  - An **IP header**, which contains the <u>source and destination IP addresses</u>('from' and 'to') as well as other information related to the network (e.g., total size of the packet, version of the internet protocol that IP packet is operating by: IPv4 or IPv6). It's usually 20 and 60 bytes (smaller portion than main data).
  - A **payload (or data)**, which is just the data being sent over the network.
- One IP packet is only 2 to the power of 16 (2^16) bytes: **~65,000bytes** or **~0.065MB**
  - This is pretty small considering that you sometimes send an email or big files. So, you'd have to send multiple packets.
  - **Problem with sending multiple files** : if all you're using is the Internet Protocol, there's <u>no way of guaranteeing that these packets are actually (1) gonna be received (2) in correct order</u>.
  - => <u>This is where TCP comes into play</u>

### TCP (Transmission Control Protocol)

- Network protocol built on top on the Internet Protocol (IP). 
- Allows for ordered, **reliable** data delivery between machines over the public internet by creating a connection.
  - Reliability: You can ensure that the packets will get to the destination OR at least know if some of the packets get corrupted or keep failing.
- **TCP Header** : In the data portion of the IP packet, there's a TCP header. Contains information about orders of packets you're sending.
- **Port Numbers** <Michigan Coursera 'Web Application Technologies'>
  - While an IP address is like a phone number, TCP port is like a phone extension.
  - A port is an application-specific or process-specific software communications endpoint/
- **Sockets**
  - A kind of file that acts like a stream. Processes can read and write to sockets and communicate in this manner. Most of the time the sockets are fronts for TCP connection.
  - "An internet socket or network socket is an endpoint of bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the internet" <Michigan Coursera>
  - Sockets are softwares / libraries. Think of it like computer phone calls. You know where you're calling, and once they answer, it's a two-way communication.
  - The key here is that it's the applications / software (sockets) talking to each other, and the Internet is the intermediary to allow that conversation to happen. When you're retrieving a picture, the socket decides whether you're allowed to see it or not. 
- **Handshake**
  - If one machine (e.g., client) wants to communicate with another machine (e.g., server) over TCP, a handshake happens first.
  - A handshake is a special TCP interaction where one computer contacts another by sending a few packets saying "I'd like to connect with you" (**SYN**C), and the other computer responds and says, "Okay" (**ACK**KNOWLEDGE). THen the client computer responds and says "We're connected" (**ACK**).
  - Once the connection is established, both machines can freely send data to another. Yey, if one computer doesn't send data in a given amount of times, the connection can be timed out. Or, one machine can end the communication by sending a special message to the other.
- TCP is usually implemented in the kernel, which exposes sockets to applications that they can use to stream data through an open connection.
- TCP is basically a more powerful and functional wrapper around IP, BUT it still lacks a robust framework that developers and engineers can use.
- => <u>This is were HTTP comes into play</u>

### HTTP (HyperText Transfer Protocol)

- The HTTP is a very common network protocol implemented on top of the TCP. It introduces a higher level abstraction above TCP and, of course, above IP.
- **Request-Response Paradigm** : Clients make HTTP requests, and servers respond with a response. This paradigm makes it very easy for developers to create robust-and-easy-to-maintain systems.

Requests typically have the following schema:

```
host: string (example: algoexpert.io)
port: integer (example: 80 or 443)
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

- While IP and TCP protocols are merely for transportation of data (very low-level), HTTP (this is what you'll mostly interact with) introduces the opportunity to add business logic, which is what you want when designing a large-scale system.
- Internet and sockets were created in the 70s, and HTTP was invented in 1990 and is an application protocol that runs on top of the sockets <Michigan Coursera>
  - "Sockets are the things that make the phone call, and HTTP is what we do once this call has been established"

# Storage

### Databases

- Databases are programs that either use disk or memory to do 2 core things: **record(=store, write)** data and **query (=retrieve, read)** data. 
- Databases are just **servers**. They are long-lived and interact with the rest of your application through network calls, with protocols on top of the TCP or even HTTP.
- **Persistence**
  - Some databases only keep records in memory, and the users of such databases are aware of the fact that those records may be lost forever if the machine or process dies.
  - For the most part though, databases need persistence of those records, and thus cannot use memory. This means that you have to write your data to disk. Anything written to disk will remain through power loss or network partitions, so that's what is used to keep permanent records.
- Since machines die often in a large scale system, special disk partitions or volumes are used by the database processes, and those volumes can get recovered even if the machine were to go down permanently.

### Disk

Usually refers to either **HDD (hard-disk drive)** or **SSD (solid-state drive)**. Data written to disk will persist through power failures and general machine crashes. Disk is also referred to as **non-volatile storage.**
SSD is far faster than HDD (see latencies of accessing data from SSD and HDD) but also far more expensive from a financial point of view. Because of that, HDD will typically be used for data that’s rarely accessed or updated, but that’s stored for a long time, and SSD will be used for data that’s frequently accessed and updated.

### Memory (Random Access Memory (RAM))

Data stored in memory will be lost when the process that has written that data dies.

### Persistent Storage

Usually refers to disk, but in general it is any form of storage that persists if the process in charge of managing it dies.

# 6. Latency and Throughput

## 2 Prerequisites

### Disk

Usually refers to either **HDD (hard-disk drive)** or **SSD (solid-state drive)**. Data written to disk will persist through power failures and general machine crashes. Disk is also referred to as **non-volatile storage.**
SSD is far faster than HDD (see latencies of accessing data from SSD and HDD) but also far more expensive from a financial point of view. Because of that, HDD will typically be used for data that’s rarely accessed or updated, but that’s stored for a long time, and SSD will be used for data that’s frequently accessed and updated.

### Memory (Random Access Memory (RAM))

Data stored in memory will be lost when the process that has written that data dies.

## 2 Key Terms

### Latency

The time it takes for a certain operation to complete in a system. Most often measure is a time duration, like milliseconds or seconds. You should know these orders of magnitude:

- **Reading 1MB from RAM**: 250us(0.25ms)
- **Reading 1MB from SSD**: 1,000us(1ms)
- **Transfer 1MB over Network**: 10,000us(10ms)
- **Reading 1MB from HDD**: 20,000us(20ms)
- **Inter-Continental Round Trip**: 150,000us(150ms)

Certain types of systems really care about latencies (e.g., multiplayer games), while other websites care less about latencies but care more about accuracy or up-time (never going down).

### Throughput

- The number of operations that a system can handle properly per time unit. How much data can be transferred from one point in a system to another in a given amount of time.
- Measurement: For instance the throughput of a server can often be measured in requests per second (RPS or QPS). Typically, in gigabits per second (Gbps) or Kbps or Mbps.
- Can increase throughput by paying more (e.g., to a cloud provider).
- Latency and throughput seem related, but they are **NOT correlated**. You CANNOT make assumption about latency or throughput based on the other.

# 7. Availability

## 3 Prerequisites

### Process

A program that is currently running on a machine. You should always assume that any process may get terminated at any time in a sufficiently large system.

### Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Node / Instance / Host

These three terms refer to the same thing most of the time: a virtual or physical machine on which the developer runs processes.
Sometimes the work **server** also refers to this same concept.

## 6 Key Terms

### Availability

The odds of a particular server or service being up and running at any point in time, usually measured in percentages. A server that has 99% availability will be operational 99% of the time (this would be described as having two **nines** of availability).

### High Availability

Used to describe systems that have particulary high levels of availability, typically 5 nines or more; sometimes abbreviated "HA".

### Nines

Typically refers to percentages of uptime. For example, 5 nines of availability means an uptime of 99.999% of the time. Below are the downtimes expected per year depending on those 9s:

```
- 99% (two 9s): 87.7 hours (3.65 days) - This is still quite bad and borderline unacceptable
- 99.9%(three 9s): 8.8 hours
- 99.99%: 52.6 minutes
- 99.999%: 5.3 minutes - Five nines of availability is typically regarded as the gold standard of availability, AKA High Availability
```

### Redundancy

The process of replicating parts of a system in an effort to make it more reliable.

### SLA (Service-level Agreement)

- SLA is a collection of guarantees given to a customer by a service provider.
- SLAs typically make **explicit guarantees** on a system’s availability, amongst other things. (e.g., telling customers that we guarantee you x percentage of uptime in our system)
- SLAs are made up of one or multiple SLOs.
- Cloud providers have very clear-cut of SLA.

### SLO (Service-level Objective)

- SLO is a guarantee given to a customer by a service provider.
- SLOs typically make guarantees on a system’s availability, amongst other things. (e.g., the percentage of uptime gurantee or x number of errors in the system are examples of SLO)
- SLOs constitute SLA. **SLO component of an SLA**
- How to improve availability?
  - The same question as 'How do you eliminate single points of failure with redundancy?
  - **Redundancy** : The process of replicating parts of a system in an effort to make it more reliable.
    - Passive Redundancy : When you gain redundancy by adding multiple components at a given layer in your system. If one of the components die, the others can help continue running smoothly.
    - Active Redundancy : Multiple machines work in such a way that only one or a few machines are typically handling traffic or doing work (active). If one of these fails, other machines will know that it failed and going to take over the work.
  - If you only have one server, that service can become a single point of failure. If you add more servers, then you’d need a load balancer. Yet, now the load balancer can be the single point of failure. So, you can then have redundancy at the load balancer layer in your system.
    - (ex) AlgoExpert has 5 load balancers that take in all user traffics and forward that traffic to our servers

# 8. Caching

## 3 Prerequisites

### Latency

The time it takes for a certain operation to complete in a system. Most often measure is a time duration, like milliseconds or seconds. You should know these orders of magnitude:

- **Reading 1MB from RAM**: 250us(0.25ms)
- **Reading 1MB from SSD**: 1,000us(1ms)
- **Transfer 1MB over Network**: 10,000us(10ms)
- **Reading 1MB from HDD**: 20,000us(20ms)
- **Inter-Continental Round Trip**: 150,000us(150ms)

Certain types of systems really care about latencies (e.g., multiplayer games), while other websites care less about latencies but care more about accuracy or up-time (never going down).

### Throughput

- The number of operations that a system can handle properly per time unit. How much data can be transferred from one point in a system to another in a given amount of time.
- Measurement: For instance the throughput of a server can often be measured in requests per second (RPS or QPS). Typically, in gigabits per second (Gbps) or Kbps or Mbps.
- Can increase throughput by paying more (e.g., to a cloud provider).
- Latency and throughput seem related, but they are **NOT correlated**. You CANNOT make assumption about latency or throughput based on the other.

### Memory (Random Access Memory (RAM))

Data stored in memory will be lost when the process that has written that data dies.

## 5 Key Terms

### Cache

- **Definition** : A piece of hardware or software that stores data, typically meant to retrieve that data faster than otherwise.

- **Notes**
  - Caching helps **avoiding redoing the same operations** and **reduce/improve the latency of a system**
  - Caching stores data in a location that's different from the one where the data originally is such that it's faster to retrieve this data from the new location
  - You can cache data at different levels(client, server, database, or even hardware)
    - (ex) You can have caching at the client-level (server-level) so that you no longer have to go to the server-level (database-level) to retrieve it.
    - There are lots of caches even at hardware level. (ex) CPU caches make it faster to retrieve data from memory
  - Some instances where caching is really helpful:
    - 1. **Network requests**: some network requests can be repetitive, and storing responses to requests (caching) can speed up the system response
    - 2. **Computationally-long operations**
    - 3. **Multiple servers/clients**: When multiple servers _hit the database_ with the same network request (e.g., a celebrity's instagram photo), caching at server or database levels can be helpful to **prevent reading the same info from the database too many times** and overloading it.
      - The goal here isn't to speed up the system because a network request itself is already fast enough
  - Examples:
    - **Questions List on AlgoExpert**: If you go to the question list on AlgoExpert, you'll see a loading icon for a split second.Then, if you go to another page (without closing the browser) and come back to the question list page, the icon is no longer there. ==> They cache the question list on **the client** because it is a static piece of content (the same every time you get it).
  - Data in a cache can become **stale** if the main source of truth for that data(i.e., the main database behind the cache) gets updated and the cache doesn't.

### Cache Hit

When requested data is found in a cache.

### Cache Miss

When requested data could have been found in a cache but isn't. This is typically used to refer to a negative consequence of a system failure or of a poor design choice. For example:
_If a server goes down, our load balancer will have to forward requests to a new server, which will result in cache misses._

### Cache Eviction Policy

The policy by which values get evicted or removed from a cache. Popular cache eviction policies include **LRU** (least-recently used), **FIFO** (first in first out), and **LFU** (least-frequently used).

### Content Delivery Network (CDN)

A **CDN** is a third-party service that acts like a cache for your servers. Sometimes, web applications can be slow for users in a particular region if your servers are located only in another region. A CDN has servers all around the world, meaning that the latency to a CDN’s servers will almost always be far better than the latency to your servers. A CDN’s servers are often referred to as **PoPs** (Points of Presence). Two of the most popular CDNs are **CloudFlare** and **Google Cloud CDN**.

# 9. Proxies

## 2 Prerequisites

### Client

A machine or process that requests data or service from a server.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

## 3 Key Terms

### Forward Proxy (Often reffered to as just **Proxy**)

- **Definition** : Server that sits between a client and servers and acts **on behalf of the client**
- **Perks** : To **mask the client's identity(IP address)**.
- (ex) request order: client -> (forward) proxy -> server
  - When the forward proxy _forwards_ the request to the server, the source IP address in the request is going to be that of the forward proxy (NOT the client's IP)
  - This is basically **how many VPNs work**

### Reverse Proxy

- **Definition** : Server that sits between clients and servers and acts **on behalf of the servers**
- **Perks** : Reverse Proxy is Particularly, useful when designing a complex system
  - **Load Balancer** : maybe the best case. Distribute multiple requests across servers following a certain pattern
  - **Logging** and gathering metrics
  - **Caching** (e.g., HTML pages)
  - Security : no single server receives all of the requests and gets taken by a malicious client
  - You can set up a reverse proxy in a way that it filters out requests that you want to ignore
- The client doesn't know/see that a reverse proxy exists, and thinks that it's only interacting with the server
- (ex) When your browser (client) makes a DNS query (e.g., AlgoExpert.io), it gets the reverse proxy's IP address as the destination, and then the reverse proxy forwards/reroutes the request to the server with IP address.

### Nginx

Pronounced "engine X"-- not "N jinx", Nginx is a very popular webserver that's often used as a **reverse proxy** and **load balancer**.

# 10. Load balancers

## 1 Prerequisite

### Reverse Proxy

- **Definition** : Server that sits between clients and servers and acts **on behalf of the servers**
- **Perks** : Reverse Proxy is Particularly, useful when designing a complex system
  - **Load Balancer** : maybe the best case. Distribute multiple requests across servers following a certain pattern
  - **Logging** and gathering metrics
  - **Caching** (e.g., HTML pages)
  - Security : no single serer receives all of the requests and gets taken by a malicious client
  - You can set up a reverse proxy in a way that it filters out requests that you want to ignore
- The client doesn't know/see that a reverse proxy exists, and thinks that it's only interacting with the server
- (ex) When your browser (client) makes a DNS query (e.g., AlgoExpert.io), it gets the reverse proxy's IP address as the destination, and then the reverse proxy forwards/reroutes the request to the server with IP address.

## 4 Key Terms

### Load Balancer

A type of **reverse proxy** that distributes traffic across servers. Load balancers can be found in many parts of a system, from the DNS layer all the way to the database layer.

### Server-Selection Strategy

How a **load balancer** chooses servers when distributing traffic amongst multiple servers. Commonly used strategies include round-robin, random selection, performance-based selection (choosing the server with the best performance metrics, like the fastest response time or the least amount of traffic), and IP-based routing.

### Hot Spot

When distributing a workload across a set of servers, that workload might be spread unevenly. This can happen if your **sharding key** or your **hashing function** are suboptimal, or if your workload is naturally skewed: some servers will receive a lot more traffic than others, thus creating a "hot spot".

### Nginx

Pronounced "engine X"-- not "N jinx", Nginx is a very popular webserver that's often used as a **reverse proxy** and **load balancer**.

# 11. Hashing

## 2 Prerequisites

### Hashing Function

A function that takes in a specific data type(such as a string or an identifier) and outputs a number. (Transforming arbitrary pieces of data into some fixed size value)
The arbitrary piece of data(input) can be an HTTP request, a username, or anything that can be hashed or transformed
Different inputs _may_ have the same output, but a good hashing function attempts to minimize those **hashing collisions** (which is equivalent to maximizing **uniformity**: map the expected inputs as evenly as possible over its output range).
In practice, you'd use a pre-made industry-grade hashing function (e.g., MD5, SHA-1, the Bcrypt hashing algorithm) instead of writing your own.
A simple hashing strategy of hashing our client's username, request, or the IP address and modding the hashes by the number of servers(buckets) does not work well..
- (1) when one of your servers dies
- (2) when you add another server : you'd have to divide(%) the hashes by the (new) number of buckets again, which would return a different index for different hashes. This means that all of your preexisting in-memory caches in your system are no longer nearly as useful.
=> Consistent Hashing/ Rendezvous Hashing can solve the problem

### Load Balancer

A type of **reverse proxy** that distributes traffic across servers. Load balancers can be found in many parts of a system, from the DNS layer all the way to the database layer.

## 3 Key Terms

### Consistent Hashing

A type of hashing that minimizes the number of keys that need to be remapped when a hash table gets resized. It's often used by load balancers to distribute traffic to servers; it minimizes the number of requests that get forwarded to different servers when new servers are added or when existing servers are brought down.

### Rendezvous Hashing

A type of hashing also coined **highest random weight** hashing. Allows for minimal re-distribution of mappings when a server goes down.

### 부록
Consistent Hashing
A type of hashing that minimizes the number of keys that need to be remapped when a hash table gets resized. When you ever add/remove a server, consistent hashing maintains some level of consistency between hashes and their target buckets
Method :
1. Place the servers on a (conceptual) circle using a hashing function (e.g., with server names)
2. Also, position the clients using a hashing function (e.g., IP address, HTTP requests, or usernames)
3. Move in a clockwise/counterclockwise direction for each client, and the first server you encounter is going to be the server that your load balancer will reroute this client to.

* where A, B, C, D are servers, and C1, C2, C3, C4 are clients

Often used by load balancers to distribute traffic to servers
It minimizes the number of requests that get forwarded to different servers when new servers are added or when existing servers are brought down.
Rendezvous Hashing
A type of hashing also coined highest random weight hashing
Allows for minimal re-distribution of mappings when a server goes down
SHA (Secure Hash Algorithms)
A collection of cryptographic hash functions used in the industry
SHA-3 is a popular choice to use in a system


### SHA

Short for "Secure Hash Algorithms", the SHA is a collection of cryptographic hash functions used in the industry. These days, SHA-3 is a popular choice to use in a system.

# 12. Relational Databases

## 3 Prerequisites

### Databases

Data are programs that either use disk or memory to do 2 core things: **record(=store, write)** data and **query (=retrieve, read)** data. In general, they are themselves servers(=Databases are just server) that are long-lived and interact with the rest of your application through network calls, with protocols on top of TCP or even HTTP.

Persistence

- Some databases only keep records in memory, and the users of such databases are aware of the fact that those records may be lost forever if the machine or process dies.

- For the most part though, databases need persistence of those records, and thus cannot use memory. This means that you have to write your data to disk. Anything written to disk will remain through power loss or network partitions, so that's what is used to keep permanent records.

Since machines die often in a large scale system, special disk partitions or volumes are used by the database processes, and those volumes can get recovered even if the machine were to go down permanently.

### Disk

Usually refers to either **HDD (hard-disk drive)** or **SSD (solid-state drive)**. Data written to disk will persist through power failures and general machine crashes. Disk is also referred to as **non-volatile storage.**
SSD is far faster than HDD (see latencies of accessing data from SSD and HDD) but also far more expensive from a financial point of view. Because of that, HDD will typically be used for data that’s rarely accessed or updated, but that’s stored for a long time, and SSD will be used for data that’s frequently accessed and updated.

### Memory (Random Access Memory (RAM))

Data stored in memory will be lost when the process that has written that data dies.

## 10 Key Terms

### Relational Database

A type of structured database in which data is stored following a tabular format: often supports powerful querying using SQL.

### Non-Relational Database

In contrast with relational database (SQL databases), a type of database that is free of imposed, tabular-like structure. Non-relational databases are often referred to as NoSQL databases.

### SQL

Structured Query Language. Relational databases can be used using a derivative of SQL such as PostgreSQL in the case of Postgres.

### SQL Database

Any database that supports SQL. This term is often used synonymously with "Relational Database", though in practice, not _every_ relational database supports SQL.

### NoSQL Database

Any database that is not SQL-compatible is called NoSQL.

### ACID Transaction

A type of database transaction that has four important properties:

- **Atomicity**: The operations that constitute the transaction will either all succeed or all fail. There is no in-between state.
- **Consistency**: The transaction cannot bring the database to an invalid state. After the transaction is committed or rolled back, the rules for each record will still apply, and all future transactions will see the effect of the transaction. Also named **Strong Consistency.**
- **Isolation**: The execution of multiple transactions concurrently will have the same effect as if they had been executed sequentially.
- **Durability**: Any committed transaction is written to non-volatile storage. It will not be undone by a crash, power loss, or network partition.

### Database Index

A special auxiliary data structure that allows your database to perform certain queries much faster. Indexes can typically only exist to reference structured data, like data stored in relational databases. In practice, you create an index on one or multiple columns in your database to greatly speed up **read** queries that you run very often, with the downside of slightly longer **writes** to your database, since writes have to also take place in the relevant index.

### Strong Consistency

Strong Consistency usually refers to the consistency of ACID transactions, as opposed to **Eventually Consistency**.

### Eventually Consistency

A consistency model which is unlike **Strong Consistency**. In this model, reads might return a view of the system that is stale. An eventually consistent datastore will give guarantees that the state of the database will eventually reflect writes within a time period (could be 10 seconds, or minutes.)

### Postgres

A relational database that uses a dialect of SQL called PostgreSQL. Provides ACID transactions.

# 13. Key-Value Stores

## 2 Prerequisites

### Relational Database

A type of structured database in which data is stored following a tabular format: often supports powerful querying using SQL.

### Non-Relational Database

In contrast with relational database (SQL databases), a type of database that is free of imposed, tabular-like structure. Non-relational databases are often referred to as NoSQL databases.

## 4 Key Terms

### Key-Value Store

A Key-Value Store is a flexible NoSQL database that's often used for caching and dynamic configuration. Popular options include DynamoDB, Etcd, Redis, and ZooKeeper.

### Etcd

Etcd is a strongly consistent and highly available key-value store that's often used to implement leader election in a system.

### Redis

An in-memory key-value store. Does offer some persistent storage options but is typically used as a really fast, best-effort caching solution. Redis is also often used to implement **rate limiting**.

### ZooKeeper

ZooKeeper is a strongly consistent, highly available key-value store. it's often used to store important configuration or to perform leader election.

### 부록

Key-Value Store
Key-Value Store is a flexible (non-tabular structure) NoSQL database that's often used for caching and dynamic configuration
Dynamic configuration : having special parameters or constants in your system that different systems can rely on (ex) AlgoExpert has a parameter called SystemExpert_is_launched that other parts of their systems rely on. It makes sense to store this using a key-value mapping (e.g., ‘SystemExpert_is_launched’: True)
Allow you to store key-value pairs where keys (typically strings) are mapped to arbitrary values. Similar to hash tables.
Popular options include DynamoDB, Etcd, Redis, and ZooKeeper.
Etcd : a strongly consistent and highly available key-value store that's often used to implement leader election in a system.
Redis : An in-memory key-value store. Does offer some persistent storage options but is typically used as a really fast, best-effort caching solution. Redis is also often used to implement rate limiting.
ZooKeeper :  a strongly consistent, highly available key-value store. it's often used to store important configuration or to perform leader election.

# 14. Specialized Storage Paradigms

## 8 Prerequisites

### Relational Database

A type of structured database in which data is stored following a tabular format: often supports powerful querying using SQL.

### Non-Relational Database

In contrast with relational database (SQL databases), a type of database that is free of imposed, tabular-like structure. Non-relational databases are often referred to as NoSQL databases.

### SQL

Structured Query Language. Relational databases can be used using a derivative of SQL such as PostgreSQL in the case of Postgres.

### SQL Database

Any database that supports SQL. This term is often used synonymously with "Relational Database", though in practice, not _every_ relational database supports SQL.

### NoSQL Database

Any database that is not SQL-compatible is called NoSQL.

### Key-Value Store

A Key-Value Store is a flexible NoSQL database that's often used for caching and dynamic configuration. Popular options include DynamoDB, Etcd, Redis, and ZooKeeper.

### Database Index

A special auxiliary data structure that allows your database to perform certain queries much faster. Indexes can typically only exist to reference structured data, like data stored in relational databases. In practice, you create an index on one or multiple columns in your database to greatly speed up **read** queries that you run very often, with the downside of slightly longer **writes** to your database, since writes have to also take place in the relevant index.

### Postgres

A relational database that uses a dialect of SQL called PostgreSQL. Provides ACID transactions.

## 11 Key Terms

### Blob Storage

Widely used kind of storage, in small and large scale systems. They don't really count as databases per se, partially because they only allow the user to store and retrieve data based on the name of the blob. This is sort of like a key-value store but usually blob stores have different guarantees. They might be slower than KV stores but values can be megabytes large (or sometimes gigabytes large). Usually people use this to store things like **large binaries, database snapshots, or images** and other static assets that a website might have.

Blob storage is rather complicated to have on premise, and only giant companies like Google and Amazon have infrastructure that supports it. So usually in the context of System Design interviews you can assume that you will be able to use **GCS** or **S3**.  
These are blob storage services hosted by Google and Amazon respectively, that cost mony depending on how much storage you use and how often you store and retrieve blobs from that storage.

### Time Series Database

A **TSDB** is a special kind of database optimized for storing and analyzing time-indexed data: data points that specifically occur at a given moment in time. Examples of TSDBs are InfluxDB, Prometheus, and Graphite.

### Graph Database

A type of database that stores data following the graph data model. Data entries in a graph database can have explicitly defined relationships, much like nodes in a graph can have edges.

Graph databases take advantage of their underlying graph structure to perform complex queries on deeply connected data very fast.

Graph databases are thus often preferred to relational databases when dealing with systems where data points naturally from a graph and have multiple levels of relationships - for example, social networks.

### Cypher

A **graph query language** that was originally developed for the Neo4j graph database, but that has since been standardized to be used with other graph databases in an effort to make it the "SQL for graphs."

Cypher queries are often much simpler than their SQL counterparts. Example Cypher queryl to find data in **Neo4j**, a popular graph database:

`MATCH (some_node:SomeLabel)-[:SOME_RELATIONSHIP]->(some_other_node:SomeLabel {some_property:'value'})`

### Spatial Database

A type of database optimized for storing and querying spatial data like locations on a map. Spatial databases rely on spatial indexes like **quadtrees** to quickly perform spatial queries like finding all locations in the vicinity of a region.

### Quadtree

A tree data structure most commonly used to index two-dimensional spatial data. Each node in a quadtree has either zero children nodes (and is therefore a leaf node) or exactly four children nodes.

Typically, quadtree nodes contain some form of spatial data - for example, locations on a map - with a maximum capacity of some specified number **n**. So long as nodes aren't at capacity, they remain leaf nodes; once they reach capacity, they're given four children nodes, and their data entries are split across the four children nodes.

A quadtree lends itself well to storing spatial data because it can be represented as a grid filled with rectangles that are recursively subdivided into four sub-rectangles, where each quadtree node is represented by a rectangle and each rectangle represents a spatial region. Assuming we're storing locations in the world, we can imagine a quadtree with a maximum node-capacity **n** as follows:

- The root node, which represents the entilre world, is the outermost rectangle.
- If the entire world has more than **n** locations, the outermost rectangle is divided into four quadrants, each representing a region of the world.
- So long as a region has more than **n** locations, its corresponding rectangle is subdivided into four quadrants (the corresponding node in the quadtree is given four children nodes).
- Regions that have fewer that **n** locations are undivided rectangles (leaf nodes).
- The parts of the grid that have many subdivided rectangles represent densely populated area (like cities), while the parts of the grid that have few subdivided rectangles represent sparsely populated areas (like rural ares).

Finding a given location in a perfect quadtree is an extremely fast operation that runs in **log4(x)** time (where **x** is the total number of locations), since quadtree nodes have four children nodes.

### Google Cloud Storage

GCS is a blob storage service provided by Google.

### S3

S3 is a blob storage service provided by Amazon through **Amazon Web Services(AWS)**.

### InfluxDB

A popular open-source time series database.

### Prometheus

A popular open-source series database, typically used for monitoring purposes.

### Neo4j

A popular graph database that consists of **nodes, relationship, properties**, and **labels**.

# 15. Replication And Sharding

## 6 Prerequisites

### Availability

The odds of a particular server or service being up and running at any point in time, usually measured in percentages. A server that has 99% availability will be operational 99% of the time (this would be described as having two **nines** of availability).

### Latency

The time it takes for a certain operation to complete in a system. Most often measure is a time duration, like milliseconds or seconds. You should know these orders of magnitude:

- **Reading 1MB from RAM**: 250us(0.25ms)
- **Reading 1MB from SSD**: 1,000us(1ms)
- **Transfer 1MB over Network**: 10,000us(10ms)
- **Reading 1MB from HDD**: 20,000us(20ms)
- **Inter-Continental Round Trip**: 150,000us(150ms)

Certain types of systems really care about latencies (e.g., multiplayer games), while other websites care less about latencies but care more about accuracy or up-time (never going down).

### Throughput

- The number of operations that a system can handle properly per time unit. How much data can be transferred from one point in a system to another in a given amount of time.
- Measurement: For instance the throughput of a server can often be measured in requests per second (RPS or QPS). Typically, in gigabits per second (Gbps) or Kbps or Mbps.
- Can increase throughput by paying more (e.g., to a cloud provider).
- Latency and throughput seem related, but they are **NOT correlated**. You CANNOT make assumption about latency or throughput based on the other.

### Redundancy

The process of replicating parts of a system in an effort to make it more reliable.

### Databases

Data are programs that either use disk or memory to do 2 core things: **record(=store, write)** data and **query (=retrieve, read)** data. In general, they are themselves servers(=Databases are just server) that are long-lived and interact with the rest of your application through network calls, with protocols on top of TCP or even HTTP.

Persistence

- Some databases only keep records in memory, and the users of such databases are aware of the fact that those records may be lost forever if the machine or process dies.

- For the most part though, databases need persistence of those records, and thus cannot use memory. This means that you have to write your data to disk. Anything written to disk will remain through power loss or network partitions, so that's what is used to keep permanent records.

Since machines die often in a large scale system, special disk partitions or volumes are used by the database processes, and those volumes can get recovered even if the machine were to go down permanently.

### Reverse Proxy

- **Definition** : Server that sits between clients and servers and acts **on behalf of the servers**
- **Perks** : Reverse Proxy is Particularly, useful when designing a complex system
  - **Load Balancer** : maybe the best case. Distribute multiple requests across servers following a certain pattern
  - **Logging** and gathering metrics
  - **Caching** (e.g., HTML pages)
  - Security : no single serer receives all of the requests and gets taken by a malicious client
  - You can set up a reverse proxy in a way that it filters out requests that you want to ignore
- The client doesn't know/see that a reverse proxy exists, and thinks that it's only interacting with the server
- (ex) When your browser (client) makes a DNS query (e.g., AlgoExpert.io), it gets the reverse proxy's IP address as the destination, and then the reverse proxy forwards/reroutes the request to the server with IP address.

## 3 Key Terms

### Replication

**The act of duplicating the data from one database server to others**. This is sometimes used to increase the redundancy of your system and tolerate regional failures for instance. Other times you can use replication to move data closer to your clients, thus decreasing the latency of accessing specific data.

### Sharding

Sometimes called **data partitioning**, **sharding is the act of splitting a database into two or more pieces called ***shard*** and is typically done to increase the throughput of your database**. Popular sharding strategies include:

- Sharding based on a client's region
- Sharding based on the type of data being stored (e.g: user data gets stored in one shard, payments data gets stored in another shard)
- SHarding based on the hash of a column (only for structured data)

### Hot Spot

When distributing a workload across a set of servers, that workload might be spread unevenly. This can happen if your **sharding key** or your **hashing function** are suboptimal, or if your workload is naturally skewed: some severs will receive a lot more traffic than others, thus creating a "hot spot".

### Appendix
### Replication and Sharding
#### Replication
**Definition** : The act of duplicating the data from one database server to others.
**Benefits** :
- <u>Improve availability</u> : increase the redundancy of your system and tolerate regional failures for instance.
  - Say, you have one main database and have a replica (duplicate version) of the main database. The replica will take over if the main database fails. In order for this to work, whenever there's an update with the main database, this update needs to also happen in the replica in a <u>synchronous</u> way.
    - If 'WRITE' operation fails on the replica, the WRITE operation should not complete on the main database.
- Some feeds/posts (e.g.,on Linkedin) may not need to be up-to-date, in which case updates can be made in an <u>asynchronous</u> way.
- Other times you can use replication to move data closer to your clients, thus decreasing the latency of accessing specific data.

#### Sharding (or Data partitioning)
**Definition** : Sharding is the act of splitting a database into two or more pieces called **shard** and is typically done <u>to increase the throughput of your database.</u>
**Popular sharding strategies :**
  - Sharding based on a client's region
  - Sharding based on the type of data being stored (e.g: user data gets stored in one shard, payments data gets stored in another shard)
  - Sharding based on the hash of a column (only for structured data)
- You can have the logic that dictates what shard a database read or write gets forwarded to in the reverse proxy (instead of inside application server). Have your application server be a client to your database servers(shard) and a reverse proxy act on behalf of your database servers.

#### Hot Spot
**Definition** : 
- When distributing a workload across a set of servers, that workload might be spread unevenly. 
  - (Ex) If you partition data by the first letter of the customer's names, a shard with 'X,Y,Z' would get way less traffic than the others.
- This can happen if your sharding key or your hashing function are suboptimal, or if your workload is naturally skewed: some servers will receive a lot more traffic than others, thus creating a "hot spot".
  - You want to use a smart sharding strategy/ hashing function that guarantees uniformity,


# 16. Leader Election

## 5 Prerequisites

### Availability

The odds of a particular server or service being up and running at any point in time, usually measured in percentages. A server that has 99% availability will be operational 99% of the time (this would be described as having two **nines** of availability).

### High Availability

Used to describe systems that have particulary high levels of availability, typically 5 nines or more; sometimes abbreviated "HA".

### Redundancy

The process of replicating parts of a system in an effort to make it more reliable.

### Strong Consistency

Strong Consistency usually refers to the consistency of ACID transactions, as opposed to **Eventually Consistency**.

### Eventually Consistency

A consistency model which is unlike **Strong Consistency**. In this model, reads might return a view of the system that is stale. An eventually consistent datastore will give guarantees that the state of the database will eventually reflect writes within a time period (could be 10 seconds, or minutes.)

## 5 Key Terms

### Leader Election

The process by which nodes in a cluster (for instance, servers in a set of servers) elect a so-called "leader" amongst them, responsible for the primary operations of the service that these nodes support. When correctly implemented, leader election guarantees that all nodes in the cluster know which one is the leader at any given time and can elect a new leader if the leader dies for whatever reason.

### Consensus Algorithm

A type of complex algorithms used to have multiple entities agree on a single data value, like who the "leader" is amongst a group of machines, Two popular consensus algorithms are **Paxos** and **Raft**.

### Paxos & Raft

Two consensus algorithms that, when implemented correctly, allow for the synchronization of certain operations, even in a distributed setting.

### Etcd

Etcd is a strongly consistent and highly available key-value store that's often used to implement leader election in a system.

### ZooKeeper

ZooKeeper is a strongly consistent, highly available key-value store. it's often used to store important configuration or to perform leader election.

# 17. Peer-To-Peer Networks

## 2 Prerequisites

### Client-Server Model

The paradigm by which modern systems are designed, which consists of clients requesting data or service from servers and servers providing data or service to clients.

### Throughput

- The number of operations that a system can handle properly per time unit. How much data can be transferred from one point in a system to another in a given amount of time.
- Measurement: For instance the throughput of a server can often be measured in requests per second (RPS or QPS). Typically, in gigabits per second (Gbps) or Kbps or Mbps.
- Can increase throughput by paying more (e.g., to a cloud provider).
- Latency and throughput seem related, but they are **NOT correlated**. You CANNOT make assumption about latency or throughput based on the other.

## 2 Key Terms

### Peer-To-Peer Network

A collection of machines referred to as peers that divide a workload between themselves to presumably complete the workload faster than would otherwise be possible. Peer-to-peer networks are often used in file-distribution systems.

### Gossip Protocol

When a set of machines talke to each other in a uncoordinated manner in a cluster to spread information through a system without requiring a central source of data.

# 18. Polling And Streaming

## 2 Prerequisites

### Client-Server Model

The paradigm by which modern systems are designed, which consists of clients requesting data or service from servers and servers providing data or service to clients.

### Socket

A kind of file that acts like a stream. Processes can read an write to sockets and communicate in this manner. Most of the time the sockets are fronts for TCP connection.

## 2 Key Terms

### Polling

The act of fetching a resource or piece of data regularly at an interval to make sure your data is not too stale.

### Streaming

In networking, it usually refers to the act of continuously getting a feed of information from a server by keeping an open connection between the two machines or processes.

# 19. Configuration

## 3 Prerequisites

### JSON

A file format heavily used in APIs and configuration. Stands for **J**ava**S**cript **O**bject **N**otation. Example:

```
{
  "version": 1.0,
  "name": "AlgoExpert Configuration"
}
```

### YAML

A file format mostly used in configuration. Example:

```
version: 1.0
name: AlgoExpert Configuration
```

### Key-Value Store

A Key-Value Store is a flexible NoSQL database that's often used for caching and dynamic configuration. Popular options include DynamoDB, Etcd, Redis, and ZooKeeper.

## 1 Key Term

### Configuration

A set of parameters or constants that are critical to a system. Configuration is typically written in **JSON** or **YAML** and can be either **static**, meaning that it's hard-coded in and shipped with your system's application code (like frontend code, for instance), or **dynamic**, meaning that it lives outside of your system's application code.

# 20. Rate Limiting

### 2 Prerequisites

### Availability

The odds of a particular server or service being up and running at any point in time, usually measured in percentages. A server that has 99% availability will be operational 99% of the time (this would be described as having two **nines** of availability).

### Key-Value Store

A Key-Value Store is a flexible NoSQL database that's often used for caching and dynamic configuration. Popular options include DynamoDB, Etcd, Redis, and ZooKeeper.

## 4 Key Terms

### Rate Limiting

The act of limiting the number of requests sent to or from a system. Rate limiting is most often used to limit the number of incoming requests in order to prevent **DoS attacks** and can be enforced at the IP-address level, at the user-account level, or at the region level, for example. Rate limiting can also be implemented in tiers; for instance, a type of network request could be limited to 1 per second, 5 per 10 seconds, and 10 per minute.

### DoS Attack

Short for "denial-of-service attack", a DoS attack is an attack in which a malcious user tries to bring down or damage a system in order to render it unavailable to users. Much of the time, it consists of flooding it with traffic. Some DoS attacks are easily preventable with rate limiting, while others can be far trickier to defend against.

### DDoS Attack

Short for "distributed denial-of-service attack", a DDoS attack is a DoS attack in which the traffic flooding the target system comes from many different sources (like thousands of machines), making it much harder to defend against.

### Redis

An in-memory key-value store. Does offer some persistent storage options but is typically used as a really fast, best-effort caching solution. Redis is also often used to implement **rate limiting**.

# 21. Logging And Monitoring

## 1 Prerequisite

### JSON

A file format heavily used in APIs and configuration. Stands for **J**ava**S**cript **O**bject **N**otation. Example:

```
{
  "version": 1.0,
  "name": "AlgoExpert Configuration"
}
```

## 3 Key Terms

### Logging

The act of collecting and storing logs--useful information about events in your system. Typically your programs will output log messages to its STDOUT or STDERR pipes, which will automatically get aggregated into a **centralized logging solution**.

### Monitoring

The process of having visibility into a system's key metrics, monitoring is typically implemented by collecting important events in a system and aggregating them in human-readable charts.

### Alerting

The process through which system administrators get notified when critical system issues occur. Alerting can be set up by defining specific thresholds on monitoring charts, past which alerts are sent to a communication channel like Slack.

# 22. Publish/Subscribe Pattern

## 3 Prerequisites

### Polling

The act of fetching a resource or piece of data regularly at an interval to make sure your data is not too stale.

### Streaming

In networking, it usually refers to the act of continuously getting a feed of information from a server by keeping an open connection between the two machines or processes.

### Persistent Storage

Usually refers to disk, but in general it is any form of storage that persists if the process in charge of managing it dies.

## 4 Key Terms

### Publish/Subscribe Patter

Often shortened as **Pub/Sub**, the Publish/Subscribe pattern is a popular messaging model that consists of **publishers** and **subscribers**. Publishers publish message to special **topics** (sometimes called **channels**) without caring about or even knowing who will read those messages, and subscribers subscribe to topics and read messages coming through those topics.

Pub/Sub systems often come with very powerful guarantees like **at-least-once delivery, persistent storage, ordering** of messages, and **replayability** of messages.

### Idempotent Operation

An operation that has the same ultimate outcome regardless of how many times it's performed. If an operation can be performed multiple times without changing its overall effect, it's idempotent. Operations performed through a **Pub/Sub** messaging system typically have to be idempotent, since Pub/Sub systems tend to allow the same messages to be consumed multiple times.

For example, increasing an integer value in a database is _not_ an idempotent operation, since repeating this operation will not have the same effect as if it had been performed only once. Conversely, setting a value to "COMPLETE" _is_ an idempotent operation, since repeating this operation will always yield the same result: the value will be "COMPLETE".

### Apache Kafka

A distributed messaging system created by LinkedIn. Very useful when using the **streaming** paradigm as opposed to **polling**.

### Cloud Pub/Sub

A highly-scalable Pub/Sub messaging service created by Google. Guarantees **at-least-once delivery** of messages and supports "rewinding" in order to reprocess messages.

# 23. MapReduce

## 2 Prerequisites

### File System

An abstraction over a storage medium that defines how to manage data. While there exist many different types of file systems, most follow a hierarchical structure that consists of directories and files, like the <u>Unix file system’s</u> structure.

### Idempotent Operation

An operation that has the same ultimate outcome regardless of how many times it’s performed. If an operation can be performed multiple times without changing its overall effect, it’s idempotent. Operations performed through a **Pub/Sub** messaging system typically have to be idempotent, since Pub/Sub systems tend to allow the same messages to be consumed multiple times.
For example, increasing an integer value in a database is not an idempotent operation, since repeating this operation will not have the same effect as if it had been performed only once. Conversely, setting a value to “COMPLETE” is an idempotent operation, since repeating this operation will always yield the same result: the value will be “COMPLETE”.

## 3 Key Terms

### MapReduce

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

### Distributed File System (DFS)

A DFS is an abstraction over a (usually large) cluster of machines that allows them to act like one large file system. The two most popular implementations of a DFS are the **Google File System** (GFS) and the **Hadoop Distributed File System** (HDFS).
Typically, DFSs take care of the classic <u>availability</u> and <u>replication</u> guarantees that can be tricky to obtain in a distributed system setting. The overarching idea is that files are split into chunks of a certain size (4MB or 64MB, for instance), and those chunks are sharded across a large cluster of machines. A central control plane is in charge of deciding where each chunk resides, routing reads to the right nodes, and handling communication between machines.
Different DFS implementations have slightly different APIs and semantics, but they achieve the same common goal: extremely large-scale persistent storage.

### Hadoop

A popular, open-source framework that supports MapReduce jobs and many other kinds of data-processing pipelines. Its central component is HDFS (Hadoop Distributed File System), on top of which other technologies have been developed.

# 24. Security And HTTPS

## 4 Prerequisites

### Client

A machine or process that requests data or service from a server.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### IP Packet

Sometimes more broadly referred to as just a (network) **packet,** an IP packet is effectively the smallest unit used to describe data being sent over **IP,** aside from bytes. An IP packet consists of:

- an **IP header,** which contains the source and destination **IP addresses** as well as other information related to the network (e.g., total size of the packet, version of the internet protocol that this IP packet is operating by: IPv4 or IPv6). It's usually between 20 and 60 bytes (smaller portion than main data).
- a **payload,** which is just the data being sent over the network

One IP packets are only two to the power of 16 (2^16) bytes: ~65,000 bytes or ~0.065MB. - This is pretty small considering that you sometimes send an email or big files. So, you'd have to send multiple packets. - **Problem with sending multiple files**: if all you're using is the Internet Protocol, there's <u>NO way of guaranteeing that these packets are actually (1) gonna be received (2) in correct order.</u> - ==> **this is where TCP comes into play**

### HTTP

The **H**yper**T**ext**T**ransfer**P**rotocol is a very common network protocol implemented on top of TCP. Clients make HTTP requests, and servers respond with a response.

Requests typically have the following schema:

```
host: string (example: algoexpert.io)
port: integer (example: 80 or 443)
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

## 9 Key Terms

### Man-In-The-Middle Attack

An attack in which the attacker intercepts a line of communication that is thought to be private by its two communicating parties.

If a malicious actor intercepted and mutated an IP packet on its way from a client to a server, that would be a man-in-the-middle attack.

MITM attacks are the primary threat that encryption and **HTTPS** aim to defend against.

### Symmetric Encryption

A type of encryption that relies on only a single key to both encrypt and decrypt data. The key must be known to all parties involved in communication and must therefore typically be shared between the parties at one point or another.

Symmetric-key algorithms tend to be faster than their asymmetric counterparts.

The most widely used symmetric-key algorithms are part of the Advanced Encryption Standard (**AES**).

### Asymmetric Encryption

Also known as public-key encryption, asymmetric encryption relies on two keys—a public key and a private key—to encrypt and decrypt data. The keys are generated using cryptographic algorithms and are mathematically connected such that data encrypted with the public key can only be decrypted with the private key.

While the private key must be kept secure to maintain the fidelity of this encryption paradigm, the public key can be openly shared.

Asymmetric-key algorithms tend to be slower than their symmetric counterparts.

### AES

Stands for **Advanced Encryption Standard**. AES is a widely used encryption standard that has three symmetric-key algorithms (AES-128, AES-192, and AES-256).

Of note, AES is considered to be the "gold standard" in encryption and is even used by the U.S. National Security Agency to encrypt top secret information.

### HTTPS

The **H**yper**T**ext **T**ransfer **P**rotocol **S**ecure is an extension of **HTTP** that's used for secure communication online. It requires servers to have trusted certificates (usually **SSL certificates**) and uses the Transport Layer Security (**TLS**), a security protocol built on top of **TCP**, to encrypt data communicated between a client and a server.

### TLS

The **T**ransport **L**ayer **S**ecurity is a security protocol over which **HTTP** runs in order to achieve secure communication online. "HTTP over TLS" is also known as **HTTPS**.

### SSL Certificate

A digital certificate granted to a server by a **certificate authority**. Contains the server's public key, to be used as part of the **TLS handshake** process in an **HTTPS** connection.

An SSL certificate effectively confirms that a public key belongs to the server claiming it belongs to them. SSL certificates are a crucial defense against **man-in-the-middle attacks**.

### Certificate Authority

A trusted entity that signs digital certificates—namely, SSL certificates that are relied on in **HTTPS** connections.

### TLS Handshake

The process through which a client and a server communicating over **HTTPS** exchange encryption-related information and establish a secure communication. The typical steps in a TLS handshake are roughly as follows:

- The client sends a **client hello**—a string of random bytes—to the server.
- The server responds with a **server hello**—another string of random bytes—as well as its **SSL certificate**, which contains its **public key**.
- The client verifies that the certificate was issued by a **certificate authority** and sends a **premaster secret**—yet another string of random bytes, this time encrypted with the server's public key—to the server.
- The client and the server use the client hello, the server hello, and the premaster secret to then generate the same **symmetric-encryption** session keys, to be used to encrypt and decrypt all data communicated during the remainder of the connection.

# 25. API Design

## 4 Prerequisites

### HTTP

The **H**yper**T**ext**T**ransfer**P**rotocol is a very common network protocol implemented on top of TCP. Clients make HTTP requests, and servers respond with a response.

Requests typically have the following schema:

```
host: string (example: algoexpert.io)
port: integer (example: 80 or 443)
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

### JSON

A file format heavily used in APIs and configuration. Stands for **J**ava**S**cript **O**bject **N**otation. Example:

```
{
  "version": 1.0,
  "name": "AlgoExpert Configuration"
}
```

### YAML

A file format mostly used in configuration. Example:

```
version: 1.0
name: AlgoExpert Configuration
```

### ACL

Short for **Access-Control List**. This term is often used to refer to a permissioning model: which users in a system can perform which operations. For instance, APIs often come with ACLs defining which users can delete, edit, or view certain entities.

## 2 Key Terms

### Pagination

When a network request potentially warrants a really large response, the relevant API might be designed to return only a single **page** of that response (i.e., a limited portion of the response), accompanied by an identifier or token for the client to request the next page if desired.

Pagination is often used when designing **List** endpoints. For instance, an endpoint to list videos on the YouTube Trending page could return a huge list of videos. This wouldn't perform very well on mobile devices due to the lower network speeds and simply wouldn't be optimal, since most users will only ever scroll through the first ten or twenty videos. So, the API could be designed to respond with only the first few videos of that list; in this case, we would say that the API response is **paginated**.

### CRUD Operations

Stands for **Create, Read, Update, Delete** Operations. These four operations often serve as the bedrock of a functioning system and therefore find themselves at the core of many APIs. The term **CRUD** is very likely to come up during an API-design interview.
