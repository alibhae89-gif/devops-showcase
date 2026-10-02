import fakeredis
import app as app_module

def make_client():
    app_module.cache = fakeredis.FakeRedis()
    return app_module.app.test_client()

def test_home_counts_visits():
    client = make_client()
    assert b"Visited 1 times" in client.get("/").data
    assert b"Visited 2 times" in client.get("/").data

def test_health_ok():
    res = make_client().get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}

def test_metrics_exposed():
    assert make_client().get("/metrics").status_code == 200
