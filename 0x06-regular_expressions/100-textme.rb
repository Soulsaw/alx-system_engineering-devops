#!/usr/bin/env ruby
SENDERS = ARGV[0].scan(/[A-Z]/).join
RECEIVERS = ARGV[0].scan(/[A-Z]/).join
FLAGS = ARGV[0].scan(/[A-Z]/).join
puts SENDERS+","+RECEIVERS+","+FLAGS