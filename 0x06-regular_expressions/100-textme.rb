#!/usr/bin/env ruby
puts ARGV[0].scan(/\[sender:(.*?)\] \[receiver:(.*?)\] \[flags:(.*?)\]/).join(",")
