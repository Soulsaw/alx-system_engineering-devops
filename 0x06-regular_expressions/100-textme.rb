#!/usr/bin/env ruby
SENDERS = ARGV[0].scan(/from:(\+?\d+|\w+)/).join
RECIEVERS = ARGV[0].scan(/to:(\+?\d+|\w+)/).join
FLAGS = ARGV[0].scan(/flags:(\W?\d:\W?\d:\W?\d:\W?\d:\W?\d)/).join
puts SENDERS+","+RECIEVERS+","+FLAGS

