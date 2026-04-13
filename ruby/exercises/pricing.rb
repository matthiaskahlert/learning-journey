# Modul Pricing aus Aufgabe 6.A.02
# Berechnet den Preis nach Steuern.
module Pricing
  # Berechnet den Preis nach Steuern.
  # @param base_price [Numeric] Basispreis des Produkts.
  # @param tax_rate [Numeric] Steuersatz in Prozent.
  # @return [Numeric] Preis inklusive Steuern.
  def calculate_price(base_price, tax_rate)
    base_price + (base_price * tax_rate / 100.0)
  end
end
