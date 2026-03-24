## [How the Internet works](https://www.youtube.com/watch?v=7_LPdttKXPc)

### Internet

- The **internet** is a wire buried in the ground.
- Two computers connected directly to this wire can communicate.

### Server

- A **server** is a special computer connected directly to the internet, web pages/files on it's hard drive.
- Every server has a unique internet protocol (IP) address.
- IP addresses help computers find each other.
- IP addresses are given names, so we can use them easily.

### Client

- Your computer is a client, it's connected indirectly to the internet through an Internet Service Provider (ISP).
- I use my laptop with DSL, go through my ISP onto the internet and look at _google.com_, my laptop connects with _google.com_ and I can look at its web pages.

### Packets

- Whenever an email/picture/web page travels across the internet, computers break the information int smaller pieces called **packets**.
- When information reaches its destination, the packets are reassembled
  in their original order.

### IP Addresses and Routers

- Everything connected directly or indirectly to the internet has an IP address.
- Anywhere two or more parts of the internet intersect, there's a piece of equipment called a **router**.
- Routers direct your packets around the internet, helping each packet get one step closer to its destination.
- Every time you visit a website, upwards of 10 to 15 routes may help your packets find their way to and from your computer.
- Imagine each packet as a piece of candy wrapped in several layers, the first layer is your computer's IP address, your computer sends the packet to the first router which adds its own IP address, each time the packet reaches a new router, another layer is added until it reaches the server, then when the server sends back information, it creates packets with an identical wrapping, as the packet makes its way over the internet back to your computer, each router unwraps a layer to discover where to send the packet next until it reaches your computer not anyone else.

## [HTTP](https://www.youtube.com/watch?v=iYM2zFP3Zn0)

### HTTP

- Hyper Text Transfer Protocol.
- Responsible for communication between web servers & clients.

### HTTP Is Stateless

- Every request is completely **independent**.
- When you make one request visiting a web page, or you go to another page after that, or reload the page, it doesn't remember anything about the previous one.
- Each request is a single transaction.
- Programming, local storage, cookies, sessions are used to create enhanced user experiences.
