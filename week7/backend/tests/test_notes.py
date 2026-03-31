def test_create_list_and_patch_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"
    assert "created_at" in data and "updated_at" in data

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/", params={"q": "Hello", "limit": 10, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    note_id = data["id"]
    r = client.patch(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["title"] == "Updated"

def test_notes_pagination_and_sort(client):
    # Create multiple notes
    client.post("/notes/", json={"title": "B note", "content": "content"})
    client.post("/notes/", json={"title": "A note", "content": "content"})
    client.post("/notes/", json={"title": "C note", "content": "content"})

    # Test sorting ascending
    res = client.get("/notes/?sort=title")
    assert res.status_code == 200
    data = res.json()
    assert data[0]["title"] == "A note"

    # Test sorting descending
    res = client.get("/notes/?sort=-title")
    data = res.json()
    assert data[0]["title"] == "C note"

    # Test limit
    res = client.get("/notes/?limit=2")
    data = res.json()
    assert len(data) == 2

    # Test skip
    res = client.get("/notes/?skip=1")
    data = res.json()
    assert len(data) >= 1
