# Modul Weight
# Berechnet das Gesamtgewicht eines Produkts.
module Weight
  # Berechnet das Gesamtgewicht.
  # @param base_weight [Numeric] Basisgewicht des Produkts.
  # @param packaging_weight [Numeric] Gewicht der Verpackung.
  # @return [Numeric] Gesamtgewicht.
  def calculate_weight(base_weight, packaging_weight)
    base_weight + packaging_weight
  end
end
