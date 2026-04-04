stringArray = %w[Ruby Strings Arrays Looping if unless]
stringArrayLong = []

stringArray.each do |element|
  stringArrayLong.push(element) if element.length > 5
end
puts "Wörter im alten Array: #{stringArray.join(', ')}"
puts "Wörter im neuen Array da >5: #{stringArrayLong.join(', ')}"
