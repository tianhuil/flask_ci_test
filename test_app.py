from io import BytesIO

import pytest


@pytest.fixture(scope="session")
def app():
    from app import app
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    return app


def test_upload(app):
    client = app.test_client()

    img = b"1234567890TESERT"
    test_img = BytesIO(img)

    response = client.post("/img/", data={"picture": (test_img, "test.png")})
    assert response.data == img
