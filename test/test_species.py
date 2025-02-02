from mhcgnomes import Species
from nose.tools import eq_


def test_HLA():
    for hla in ["HLA", "hla"]:
        species = Species.get(hla)
        assert species is not None, "Could not find Species for '%s'" % hla
        eq_(species.common_species_name, "human")


def test_human():
    for human in ["human", "Human", "HUMAN"]:
        species = Species.get(human)
        assert species is not None, "Could not find Species for '%s'" % human
        eq_(species.common_species_name, "human")



def test_RT1():
    eq_(Species.get("RT1").prefix, "RT1")

def test_Rano():
    eq_(Species.get("Rano").prefix, "Rano")

def test_T2c_in_BoLA():
    cow = Species.get("BoLA")
    assert "T2c" in cow.known_alleles[None]

def test_known_allele_SLA_3_ydy01():
    pig = Species.get("SLA")
    eq_(pig.get_known_allele(gene_name="3", allele_name="ydy01"), ("3", "YDY01"))
