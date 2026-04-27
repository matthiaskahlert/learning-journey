"""Tests for the bookstore domain module."""

import importlib.util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BOOKSTORE_PATH = PROJECT_ROOT / "bookstore.py"

BOOKSTORE_SPEC = importlib.util.spec_from_file_location("bookstore", BOOKSTORE_PATH)
if BOOKSTORE_SPEC is None or BOOKSTORE_SPEC.loader is None:
    raise ImportError(f"Could not load module specification for {BOOKSTORE_PATH}")

bookstore = importlib.util.module_from_spec(BOOKSTORE_SPEC)
BOOKSTORE_SPEC.loader.exec_module(bookstore)

import pytest

Buch = bookstore.Buch
Buchladen = bookstore.Buchladen
baue_demo_inventar = bookstore.baue_demo_inventar


def test_buch_string_representation_formats_price() -> None:
    """Formats book data as a readable string including a 2-decimal price."""
    buch = Buch("1984", "George Orwell", "Roman", 15.99)

    assert str(buch) == '"1984" von George Orwell (Roman) - 15.99 EUR'


def test_suche_nach_kategorie_is_case_insensitive_and_trimmed() -> None:
    """Finds categories independent of case and surrounding whitespace."""
    laden = Buchladen()
    laden.buch_hinzufuegen(Buch("A", "Autor 1", "Roman", 10.0))
    laden.buch_hinzufuegen(Buch("B", "Autor 2", "Wissenschaft", 20.0))

    result = laden.suche_nach_kategorie("  roman  ")

    assert len(result) == 1
    assert result[0].titel == "A"


def test_gesamtpreis_works_for_empty_list() -> None:
    """Returns zero when no books are provided for price aggregation."""
    laden = Buchladen()

    assert laden.gesamtpreis([]) == 0


def test_demo_inventory_workflow_returns_expected_totals() -> None:
    """Validates the demo inventory workflow and expected aggregate totals."""
    laden = baue_demo_inventar()

    wissenschaft = laden.suche_nach_kategorie("wissenschaft")
    gesamt_wissenschaft = laden.gesamtpreis(wissenschaft)
    gesamt_alle = laden.gesamtpreis(laden.inventar)

    assert len(wissenschaft) == 2
    assert gesamt_wissenschaft == pytest.approx(39.99)
    assert gesamt_alle == pytest.approx(98.97)
