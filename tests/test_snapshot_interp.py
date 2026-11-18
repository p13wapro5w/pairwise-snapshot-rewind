import pytest
from net import snapshot_interp as mod

CASES = [
    ("alpha_mid", "m.tick_alpha(15, 10, 20) == approx(0.5)"),
    ("alpha_before", "m.tick_alpha(5, 10, 20) == approx(0.0)"),
    ("alpha_after", "m.tick_alpha(25, 10, 20) == approx(1.0)"),
    ("extrap_clamp", "m.clamp_extrapolation(10.0, 2.0) == approx(2.0)"),
    ("extrap_inside", "m.clamp_extrapolation(1.0, 2.0) == approx(1.0)"),
    ("pose_pair", "m.pose_sync((1.0, 2.0), 30.0) == ((1.0, 2.0), 30.0)"),
    ("rollback_players", "m.rollback_world([1, 2], [3])[0] == [1, 2]"),
    ("rollback_doors", "m.rollback_world([1, 2], [3])[1] == [3]"),
    ("seq_new", "m.sequence_ok(5, 4) is True"),
    ("seq_old", "m.sequence_ok(3, 4) is False"),
    ("clock_offset", "m.clock_offset(10.0, 7.0) == approx(3.0)"),
    ("blend_start", "m.blend_prediction(1.0, 5.0, 0.0) == approx(1.0)"),
    ("blend_end", "m.blend_prediction(1.0, 5.0, 1.0) == approx(5.0)"),
    ("hit_rewind", "m.hit_at_rewind((10.0, 0.0), (8.0, 0.0)) == (8.0, 0.0)"),
    ("alpha_equal_ticks", "m.tick_alpha(10, 10, 10) == approx(1.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
