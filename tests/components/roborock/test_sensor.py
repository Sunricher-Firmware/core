"""Test Roborock Sensors."""

from roborock.const import (
    FILTER_REPLACE_TIME,
    MAIN_BRUSH_REPLACE_TIME,
    SENSOR_DIRTY_REPLACE_TIME,
    SIDE_BRUSH_REPLACE_TIME,
)

from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry


async def test_sensors(hass: HomeAssistant, setup_entry: MockConfigEntry) -> None:
    """Test sensors and check test values are correctly set."""
    assert len(hass.states.async_all("sensor")) == 4
    assert hass.states.get("sensor.roborock_s7_maxv_main_brush_time_left").state == str(
        MAIN_BRUSH_REPLACE_TIME - 74382
    )
    assert hass.states.get("sensor.roborock_s7_maxv_side_brush_time_left").state == str(
        SIDE_BRUSH_REPLACE_TIME - 74382
    )
    assert hass.states.get("sensor.roborock_s7_maxv_filter_time_left").state == str(
        FILTER_REPLACE_TIME - 74382
    )
    assert hass.states.get("sensor.roborock_s7_maxv_sensor_time_left").state == str(
        SENSOR_DIRTY_REPLACE_TIME - 74382
    )
