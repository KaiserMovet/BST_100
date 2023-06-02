require 'time'
require_relative 'tree'

def get_numbers(path)
  numbers = []
  File.open(path, "r") do |f|
    f.each_line do |line|
      line.split.each do |num|
        numbers.push(num.to_i)
      end
    end
  end
  numbers
end

amount = ARGV[0].to_i

add_numbers = get_numbers("/datasets/add.txt")[0...amount]
check_numbers = get_numbers("/datasets/check.txt")[0...amount]

bst = Tree.new

# Add elements
start_time = Time.now
add_numbers.each do |i|
  bst.add(i)
end
end_time = Time.now
puts "ADD_TEST:#{end_time - start_time}"

# Check elements
start_time = Time.now
check_numbers.each do |i|
  bst.contain(i)
end
end_time = Time.now
puts "CHECK_TEST:#{end_time - start_time}"

# Len elements
start_time = Time.now
10.times do
  bst.length
end
end_time = Time.now
puts "LEN_TEST:#{(end_time - start_time)/10}"

# Height elements
start_time = Time.now
10.times do
  bst.height
end
end_time = Time.now
puts "HEIGHT_TEST:#{(end_time - start_time)/10}"

puts "VALIDATION:#{bst.length}:#{bst.height}"
