from loudspeaker_modeling.data.manifest import REQUIRED_COLUMNS, read_manifest, validate_columns


def test_manifest_template_has_required_columns():
    recordings = read_manifest("data/raw/manifest.csv")
    assert recordings == []


def test_required_columns_are_valid():
    validate_columns(REQUIRED_COLUMNS)
