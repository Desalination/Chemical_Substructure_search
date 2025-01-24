# import httpx
#
# r = httpx.get("http://localhost:8000/molecules/get_all")
# print(r.json())


# from fastapi.testclient import TestClient
# from main import app
# from models.Molecule import Molecule
# from src.main import app
# from src.models.Molecule import Molecule
# client = TestClient(app)

# mol = Molecule(id="1", smile_notation="CC(=O)Oc1ccccc1C(=O)O")

# mol = {id: "1", smile_notation: "CC(=O)Oc1ccccc1C(=O)O"}

# response = client.get("/molecules/get_all")

# response = client.get("/molecules/get/2")
# print(response)
# print(type(response))

# def test_find_existing():
#     client.add_mol()
#
# def test_find_not_existing_inNotEmpty():
#     pass
#
# def test_find_inEmpty():
#     pass

# from fastapi.testclient import TestClient
# from main import app
from src.models.Molecule import Molecule
from src.utils.substructure_search import substructure_search
import pytest


def test_substructure_search_valid():

    molecules_db = {
        "1": Molecule(id="1", smile_notation="CCO"),
        "2": Molecule(id="2", smile_notation="c1ccccc1"),
        "3": Molecule(id="3", smile_notation="CC(=O)O"),
        "4": Molecule(id="4", smile_notation="CC(=O)Oc1ccccc1C(=O)O"),
    }
    substructure = "c1ccccc1"

    result = substructure_search(molecules_db, substructure)
    assert result == ["c1ccccc1", "CC(=O)Oc1ccccc1C(=O)O"], "Substructure search failed"


def test_substructure_search_invalid_substructure():
    molecules_db = {
        "1": Molecule(id="1", smile_notation="CCO"),
        "2": Molecule(id="2", smile_notation="c1ccccc1"),
        "3": Molecule(id="3", smile_notation="CC(=O)O"),
        "4": Molecule(id="4", smile_notation="CC(=O)Oc1ccccc1C(=O)O"),
    }
    substructure = "invalid_smiles"

    result = substructure_search(molecules_db, substructure)
    assert result == [], "Substructure search failed"



def test_substructure_search_empty_molecules():
    molecules = []
    substructure = "O"

    result = substructure_search(molecules, substructure)
    assert result == [], "Substructure search should return empty list for empty molecules list"


def test_substructure_search_some_match():
    molecules_db = {
        "1": Molecule(id="1", smile_notation="CCO"),
        "2": Molecule(id="2", smile_notation="CCCO"),
        "3": Molecule(id="3", smile_notation="CCCCO"),
        "4": Molecule(id="4", smile_notation="CCN")
    }
    substructure = "O"

    result = substructure_search(molecules_db, substructure)
    assert result == ["CCO", "CCCO", "CCCCO"], "Substructure search failed to find matching molecules"

# test_substructure_search_valid()
# test_substructure_search_invalid_substructure()
# test_substructure_search_empty_molecules()
# test_substructure_search_some_match()