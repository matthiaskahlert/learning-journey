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
##
# Hauptklasse fuer das Dungeon-Spiel.
# Verwaltet Spieler, Raeume und die Navigation.
# @example
#   me = Player.new('Guybrush Threepwood')
#   game = Dungeon.new(me)
#   game.start(:keller)
class Dungeon
  attr_accessor :player

  ##
  # Erstellt ein neues Dungeon mit Spieler.
  # @param player [Player] Aktiver Spieler.
  # @return [void]
  def initialize(player)
    @player = player
    @rooms = {}
  end

  ##
  # Fuegt einen Raum zum Dungeon hinzu.
  # @param reference [Symbol] Interner Raum-Key.
  # @param name [String] Raumname.
  # @param description [String] Raum-Beschreibung.
  # @param connections [Hash{Symbol => Symbol}] Ausgaenge mit Zielraum.
  # @return [void]
  def add_room(reference, name, description, connections)
    @rooms[reference] = Room.new(reference, name, description, connections)
  end

  ##
  # Startet das Spiel an einer Position.
  # @param location [Symbol] Start-Raum.
  # @return [void]
  def start(location)
    @player.location = location
    show_current_description
  end

  ##
  # Zeigt die Beschreibung des aktuellen Raums.
  # @return [void]
  def show_current_description
    puts find_room_in_dungeon(@player.location).full_description
  end

  ##
  # Sucht einen Raum ueber seinen Referenz-Key.
  # @param reference [Symbol] Raum-Key.
  # @return [Room, nil] Gefundener Raum oder nil.
  def find_room_in_dungeon(reference)
    @rooms[reference]
  end

  ##
  # Ermittelt den Zielraum in einer Richtung.
  # @param direction [Symbol] Bewegungsrichtung.
  # @return [Symbol, nil] Raum-Referenz oder nil.
  def find_room_in_direction(direction)
    find_room_in_dungeon(@player.location).connections[direction]
  end

  ##
  # Zuordnung interner Richtungen zu deutschen Anzeigenamen.
  # @return [Hash{Symbol => String}] Richtungs-Map.
  DIRECTIONS = {
    north: 'Norden',
    south: 'Süden',
    east: 'Osten',
    west: 'Westen'
  }.freeze

  ##
  # Bewegt den Spieler in die gewuenschte Richtung.
  # @param direction [Symbol] Richtung, z. B. :north.
  # @return [void]
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

  ##
  # Zeigt alle verfuegbaren Ausgaenge des aktuellen Raums.
  # @return [void]
  def show_exits
    current_room = find_room_in_dungeon(@player.location)
    exits = current_room.connections.keys.map { |dir| "#{DIRECTIONS[dir] || dir} (#{dir})" }
    puts "Ausgänge: #{exits.join(' | ')}"
  end

  ##
  # Zugriff auf einen Raum ueber Referenz-Key.
  # @param reference [Symbol] Raum-Key.
  # @return [Room, nil] Raum oder nil.
  def room(reference)
    @rooms[reference]
  end

  ##
  # Hauptschleife fuer die interaktive Spielsteuerung.
  # @return [void]
  # @example
  #   dungeon.play
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

##
# Spielerobjekt mit Name und aktueller Position.
class Player
  attr_accessor :name, :location

  ##
  # Erstellt einen Spieler.
  # @param name [String] Spielername.
  # @return [void]
  def initialize(name)
    @name = name
  end
end

##
# Datenklasse fuer einen Raum im Dungeon.
class Room
  attr_accessor :reference, :name, :description, :connections

  ##
  # Erstellt einen Raum mit Metadaten und Verbindungen.
  # @param reference [Symbol] Interner Raum-Key.
  # @param name [String] Anzeigename des Raums.
  # @param description [String] Beschreibung des Raums.
  # @param connections [Hash{Symbol => Symbol}] Ausgaenge mit Zielraum.
  # @return [void]
  def initialize(reference, name, description, connections)
    @reference = reference
    @name = name
    @description = description
    @connections = connections
  end

  ##
  # Gibt die formatierte Vollbeschreibung eines Raums zurueck.
  # @return [String] Name und Beschreibung als Text.
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
