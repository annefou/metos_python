---
title: "Introduction"
teaching: 0
exercises: 0
questions:
- "Where to start?"
- "Why using common data formats?"
objectives:
- "Background on the rise of common data formats in our scientific disciplines"
keypoints:
- "Data formats to exchange, archive and disseminate scientific results"
---

Before using "standard" data formats, each project often invented their own data formats, 
raw binary or even ASCII. These approaches had a number of problems:

- Machine dependent byte ordering [endianess](https://en.wikipedia.org/wiki/Endianness) or 
[floating point representations](https://en.wikipedia.org/wiki/Floating-point_arithmetic)

- Required a detailed documentation to be able to read the right data in a file

- A new custom reader/writer is needed for each different data organization making difficult to collaborate between organizations. 

- Upgrading a program working in a new programming language could be very difficult since you have to redevelop the reader from scratch.

