# Dungeon: You need a general class that encapsulates the entire
# concept of the dungeon game.

# Player: The player provides the link between the dungeon and you.
# All experience of the dungeon comes through the player. The player
# can move between rooms in the dungeon

# Rooms: The rooms of the dungeon are the locations that the player
# can navigate between. These will be linked together in multiple ways
# (e.g., doors to the north, west, east, and south) and have descriptions.
#
# So startet man das programm korrekt:

# Terminal in VS Code öffnen.
# Befehl ausführen: ruby ruby/exercises/dungeon.rb
# Dann Befehle eintippen: nord, sued, hilfe, beenden.
class Dungeon
  attr_accessor :player

  def initialize(player)
    @player = player
    @rooms = {}
  end

  def add_room(reference, name, description, connections)
    @rooms[reference] = Room.new(reference, name, description, connections)
  end

  def start(location)
    @player.location = location
    show_current_description
  end

  def show_current_description
    puts find_room_in_dungeon(@player.location).full_description
  end

  def find_room_in_dungeon(reference)
    @rooms[reference]
  end

  def find_room_in_direction(direction)
    find_room_in_dungeon(@player.location).connections[direction]
  end

  DIRECTIONS = {
    north: 'Norden',
    south: 'Süden',
    east: 'Osten',
    west: 'Westen'
  }.freeze

  def go(direction)
    next_room = find_room_in_direction(direction)
    if next_room.nil?
      puts "Du kannst nicht nach #{DIRECTIONS[direction] || direction} gehen!"
    else
      puts "Du gehst nach #{DIRECTIONS[direction] || direction}."
      @player.location = next_room
      show_current_description
    end
  end

  def show_exits
    current_room = find_room_in_dungeon(@player.location)
    exits = current_room.connections.keys.map { |dir| "#{DIRECTIONS[dir] || dir} (#{dir})" }
    puts "Ausgänge: #{exits.join(' | ')}"
  end

  def room(reference)
    @rooms[reference]
  end

  def play
    puts '=' * 50
    puts "  DUNGEON - Willkommen, #{@player.name}!"
    puts '=' * 50
    puts ''
    show_exits

    loop do
      puts ''
      puts '-' * 50
      puts 'Befehle: nord | sued | ost | west | hilfe | beenden'
      print '> '
      raw_input = gets
      if raw_input.nil?
        puts '\nKeine Eingabe verfuegbar. Spiel wird beendet.'
        break
      end

      input = raw_input.chomp.downcase.strip

      case input
      when 'nord', 'n'
        go(:north)
        show_exits
      when 'sued', 's'
        go(:south)
        show_exits
      when 'ost', 'o'
        go(:east)
        show_exits
      when 'west', 'w'
        go(:west)
        show_exits
      when 'hilfe', 'h'
        puts 'Befehle: nord/n, sued/s, ost/o, west/w, hilfe/h, beenden/q'
      when 'beenden', 'q'
        puts 'Auf Wiedersehen!'
        break
      else
        puts "Unbekannter Befehl: '#{input}'. Tippe 'hilfe' für eine Befehlsliste."
      end
    end
  end
end

class Player
  attr_accessor :name, :location

  def initialize(name)
    @name = name
  end
end

class Room
  attr_accessor :reference, :name, :description, :connections

  def initialize(reference, name, description, connections)
    @reference = reference
    @name = name
    @description = description
    @connections = connections
  end

  def full_description
    "#{@name}\n\nDu bist in: #{@description}"
  end
end

# Spieler anlegen
me = Player.new('Guybrush Threepwood')
my_dungeon = Dungeon.new(me)

# Räume definieren
my_dungeon.add_room(:keller, 'Keller', 'Ein dunkler Kellerraum.', { north: :smallcave })
my_dungeon.add_room(:largecave, 'Große Höhle', 'Eine große, gewölbte Höhle.', { west: :smallcave })
my_dungeon.add_room(:smallcave, 'Kleine Höhle', 'Eine kleine, klaustrophobische Höhle.',
                    { east: :largecave, south: :keller })

# Spiel starten
my_dungeon.start(:keller)
my_dungeon.play
