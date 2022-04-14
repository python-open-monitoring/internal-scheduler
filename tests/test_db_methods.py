import pytest

from database import methods


@pytest.mark.asyncio
async def test_get_monitors():
    result = await methods.select_monitors()
    assert result
