from patterns.structural.composite.composite import Particle, Electron, Compound


def test_composite(capsys):
    electron = Electron(1)
    electron2 = Electron(2)
    electron3 = Electron(3)
    assert isinstance(electron, Particle)

    compound = Compound(1)
    compound.add(electron)
    compound.add(electron2)
    compound.rotate()
    out, err = capsys.readouterr()
    assert out == "Compound 1 is rotating...\nElectron 1 is rotating...\nElectron 2 is rotating...\n"
    assert isinstance(compound, Particle)
    assert len(compound._particles) == 2

    compound2 = Compound(2)
    compound2.add(electron3)
    compound2.add(compound)
    compound2.rotate()
    out, err = capsys.readouterr()
    assert out == "Compound 2 is rotating...\nElectron 3 is rotating...\nCompound 1 is rotating...\nElectron 1 is rotating...\nElectron 2 is rotating...\n"
    assert isinstance(compound2, Particle)
    assert len(compound2._particles) == 2

    compound2.remove(compound)
    compound2.rotate()
    out, err = capsys.readouterr()
    assert out == "Compound 2 is rotating...\nElectron 3 is rotating...\n"
    assert len(compound2._particles) == 1
