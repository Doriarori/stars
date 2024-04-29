import asyncpg
import pytest
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / 'nasa_service/app'))
sys.path.append(str(BASE_DIR / 'planet_service/app'))

from nasa_service.app.main import service_alive as nasa_service_status
from planet_service.app.main import service_alive as planet_service_status

@pytest.mark.asyncio
async def test_database_connection():
    try:
        connection = await asyncpg.connect('postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/query')
        assert connection
        await connection.close()
    except Exception as e:
        assert False, f"Не удалось подключиться к базе данных: {e}"

@pytest.mark.asyncio
async def test_nasa_service_connection():
    r = await nasa_service_status()
    assert r == {'message': 'Service alive'}

@pytest.mark.asyncio
async def test_planet_service_connection():
    r = await planet_service_status()
    assert r == {'message': 'Service alive'}
