from woocommerce import API


def call_api():
    wcapi = API(
        url=r"http://localhost:8888/site/",
        consumer_key="ck_fd06cbafcb1492a3a278352f9ac8bf4d985c2428",
        consumer_secret="cs_7d5550a5d7487b94008de53ee7032e2b929f2e52",
        version="wc/v3"
    )

    response = wcapi.get("products")

    import pprint
    pprint.pprint(response.json())


if __name__ == "__main__":
    call_api()
