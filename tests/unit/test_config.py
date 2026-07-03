from loudspeaker_modeling.utils.config import load_yaml, require_keys


def test_load_params_yaml():
    config = load_yaml("params.yaml")
    require_keys(config, ["project", "paths", "measurement", "preprocess", "evaluation"])
    assert config["project"]["sample_rate_hz"] == 48000
