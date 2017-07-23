import pgtk.geo

def test_deg2degmin():

    coords = pgtk.geo.deg2degmin(50.0412956,14.6473611)
    assert pgtk.geo.coords2str(*coords) == (50, 2.478, 14, 38.842)
