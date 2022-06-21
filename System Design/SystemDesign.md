# Client-Server Model

## 6 Key Terms

### Client

A machine or process that requests data or service from a server.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Client-Server Model

The paradigm by which modern systems are desinged, which consists of clients requesting data or service from servers and servers providing data or service to clients.

### IP Address

An address given to each machine connected to the public internet. IPv4 addresses consist of four numbers separated by dots: **a.b.c.d** where all four numbers are between 0 and 255. Special values include:

- **127.0.0.1**: Your own local machine. Also referred to as **localhost.**
- **192.168.x.y**: Your private network. For instance, your machine and all machines on your private wifi network will usually have the **192.168** prefix.

### Port

In order for multiple programs to listen for new network connections on the same machine without colliding, they pick a **port** to listen on. A port is an integer between 0 and 65,535 (2^16 ports total).

Typically, ports 0-1023 are reserved for system ports (also called well-known ports) and shouldn’t be used by user-level processes. Certain ports have pre-defined uses, and although you usually won’t be required to have them memorized, they can sometimes come in handy. Below are some examples:

- 22: Secure Shell
- 53: DNS lookup
- 80: HTTP
- 443: HTTPS

### DNS

Short for Domain Name System, it describes the entities and protocols involved in the translation from domain names to IP addresses. Typically, machines make a DNS query to a well-known entity which is responsible for returning the IP address (or multiple ones) of the requested domain name in the response.

# Network Protocols

## 3 Prerequisites

### Client

A machine or process that requests data or service from a server.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### IP Address

An address given to each machine connected to the public internet. IPv4 addresses consist of four numbers separated by dots: **a.b.c.d** where all four numbers are between 0 and 255. Special values include:

- **127.0.0.1**: Your own local machine. Also referred to as **localhost.**
- **192.168.x.y**: Your private network. For instance, your machine and all machines on your private wifi network will usually have the **192.168** prefix.

## 4 Key Terms

### IP

Stands for **Internet Protocol.** This network protocol outlines how almost all machine-to-machine communications should happen in the world. Other protocols like **TCP, UDP** and **HTTP** are built on top of IP.

### TCP

Network protocol built on top on the Internet Protocol (IP). Allows for ordered, reliable data delivery between machines over the public internet by creating a **connection.**

TCP is usually implemented in the kernel, which exposes **sockets** to applications that they can use to stream data through an open connection.

### HTTP

The **H**yper**T**ext**T**ransfer**P**rotocol is a very common network protocol implemented on top of TCP. Clients make HTTP requests, and servers respond with a response.

Requests typically have the following schema:

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

### IP Packet

Sometimes more broadly referred to as just a (network) **packet,** an IP packet is effectively the smallest unit used to describe data being sent over **IP,** aside from bytes. An IP packet consists of:

- an **IP header,** which contains the source and destination **IP addresses** as well as other information related to the network (e.g., total size of the packet, version of the internet protocol that this IP packet is operating by: IPv4 or IPv6). It's usually between 20 and 60 bytes (smaller portion than main data).
- a **payload,** which is just the data being sent over the network

One IP packets are only two to the power of 16 (2^16) bytes: ~65,000 bytes or ~0.065MB. - This is pretty small considering that you sometimes send an email or big files. So, you'd have to send multiple packets. - **Problem with sending multiple files**: if all you're using is the Internet Protocol, there's <u>NO way of guaranteeing that these packets are acually (1) gonna be received (2) in correct order.</u> - ==> **this is where TCP comes into play**

# Storage

## 4 Key Terms

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

### Persistent Storage

Usually refers to disk, but in general it is any form of storage that persists if the process in charge of managing it dies.

# Latency and Throughput

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

# Availability

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

# Caching

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

# Proxies

## 2 Prerequisites

### Client

A machine or process that requests data or service from a server.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

### Server

A machine or process that provides data or service for a client, usually by listening for incoming network calls.

Note that a single machine or piece of software can be both a client and a server at the same time. For instance, a single machine could act as a server for end users and as a client for a database.

## 3 Key Terms

### Forward Proxy (Often reffered to as just **Proxy**)

- **Definition** : Server that sits between a client and serers and acts **on behalf of the client**
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
  - Security : no single serer receives all of the requests and gets taken by a malicious client
  - You can set up a reverse proxy in a way that it filters out requests that you want to ignore
- The client doesn't know/see that a reverse proxy exists, and thinks that it's only interacting with the server
- (ex) When your browser (client) makes a DNS query (e.g., AlgoExpert.io), it gets the reverse proxy's IP address as the destination, and then the reverse proxy forwards/reroutes the request to the server with IP address.

### Nginx

Pronounced "engine X"-- not "N jinx", Nginx is a very peopular webserver that's often used as a **reverse proxy** and **load balancer**.

# Load balancers

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

Pronounced "engine X"-- not "N jinx", Nginx is a very peopular webserver that's often used as a **reverse proxy** and **load balancer**.

# Hashing

## 2 Prerequisites

### Hashing Function

A function that takes in a specific data type(such as a string or an identifier) and outputs a number. Different inputs _may_ have the same output, but a good hashing function attempts to minimize those **hashing collisions** (which is equivalent to maximizing **uniformity**).

### Load Balancer

A type of **reverse proxy** that distributes traffic across servers. Load balancers can be found in many parts of a system, from the DNS layer all the way to the database layer.

## 3 Key Terms

### Consistent Hashing

A type of hashing that minimizes the number of keys that need to be remapped when a hash table gets resized. It's often used by load balancers to distribute traffic to servers; it minimizes the number of requests that get forwarded to different servers when new servers are added or when existing servers are brought down.

### Rendezvous Hashing

A type of hashing also coined **highest ramdom weight** hashing. Allows for minimal re-distribution of mappings when a server goes down.

### SHA

Short for "Secure Hash Algorithms", the SHA is a collection of cryptographic hash functions used in the industry. These days, SHA-3 is a popular choice to use in a system.

# Relational Databases

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

# Key-Value Stores

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

# Specialized Storage Paradigms

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

A quadtree lends itself well to storing spatial data becuase it can be represented as a grid filled with rectangles that are recursively subdivided into four sub-rectangles, where each quadtree node is represented by a rectangle and each rectangle represents a spatial region. Assuming we're storing locations in the world, we can imagine a quadtree with a maximum node-capacity **n** as follows:

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
