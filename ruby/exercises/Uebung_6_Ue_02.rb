module Devices
  class Computer
    CATEGORY = 'Desktop'

    def category
      CATEGORY
    end
  end

  class Smartphone
    CATEGORY = 'Mobile'

    def category
      CATEGORY
    end
  end
end

# Demonstration
computer = Devices::Computer.new
smartphone = Devices::Smartphone.new

puts "Computer category: #{computer.category}"
puts "Smartphone category: #{smartphone.category}"
