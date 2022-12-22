# pcap-parse
###Parsing packets for fun &amp; profit

##FAQ:
####First and foremost, how do I even run this?
It's always best to make the common case fast, that's why no arguments are required.
The repository contains the pre-processed `pcap` files for ease-of-use. Providing
no arguments will run all available strategies.

`python ProcessPCAP.py`

Use `python ProcessPCACP.py -h` to see all the available options.

####What's a strategy?
It's a way of using parsed frames (from .pcap) to generate an understanding
of the lowest-latency -n (default=2) sources.

####Suppose I don't know what a strategy is ... can I just decide to not provide one?
No problem - the program will run them all.

####What if I want to add a strategy because I'm clever?
Please do. Just add to the `main.strategies` package and adjust the 
`StrategyMap` accordingly.

