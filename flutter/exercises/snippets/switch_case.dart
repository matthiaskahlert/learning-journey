void main() {
  // Klassisches Switch-Case
  String note = 'B';
  print('Klassisches Switch-Case:');
  switch (note) {
    case 'A':
      print('Sehr gut'); // Note A
      break;
    case 'B':
      print('Gut'); // Note B
      break;
    case 'C':
      print('Befriedigend'); // Note C
      break;
    case 'D':
      print('Ausreichend'); // Note D
      break;
    case 'E':
      print('Mangelhaft'); // Note E
      break;
    default:
      print('Andere Note'); // Default-Fall
  }

  // Moderne Switch-Expression
  print('\nModerne Switch-Expression:');
  String bewertung = switch (note) {
    'A' => 'Sehr gut',
    'B' => 'Gut',
    'C' => 'Befriedigend',
    'D' => 'Ausreichend',
    'E' => 'Mangelhaft',
    _ => 'Andere Note', // Default-Fall
  };
  print('Note: $note, Bewertung: $bewertung');
}
