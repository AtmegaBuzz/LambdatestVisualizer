from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")



a = {
        "method": "Network.responseReceived",
        "params": {
            "frameId": "4C9B6C5612A4284C424939DC571D99F1",
            "hasExtraInfo": True,
            "loaderId": "FB10B42944AE2D5A1444877B31866F42",
            "requestId": "62358.7",
            "response": {
                "alternateProtocolUsage": "unspecifiedReason",
                "connectionId": 26,
                "connectionReused": True,
                "encodedDataLength": 242,
                "fromDiskCache": False,
                "fromPrefetchCache": False,
                "fromServiceWorker": False,
                "headers": {
                    "age": "6558",
                    "cache-control": "public, max-age=18000",
                    "cf-cache-status": "HIT",
                    "cf-ray": "7a6e070278d7f3d9-BOM",
                    "content-encoding": "br",
                    "content-security-policy": "default-src * 'unsafe-inline' 'unsafe-eval'; script-src * 'unsafe-inline' 'unsafe-eval'; connect-src * 'unsafe-inline'; img-src * data: blob: 'unsafe-inline'; frame-src *; style-src * 'unsafe-inline'; font-src * data: blob: 'unsafe-inline'",
                    "content-type": "text/css",
                    "date": "Sun, 12 Mar 2023 18:16:17 GMT",
                    "etag": 'W/"e66386a01142b3940c76f876ab529769"',
                    "expires": "Sun, 12 Mar 2023 23:16:17 GMT",
                    "last-modified": "Fri, 10 Mar 2023 16:31:22 GMT",
                    "permissions-policy": "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()",
                    "referrer-policy": "no-referrer-when-downgrade",
                    "server": "cloudflare",
                    "strict-transport-security": "max-age=31536000; includeSubDomains; preload",
                    "vary": "Accept-Encoding",
                    "via": "1.1 95de318e1a7dd6c72c9869d80089c7d2.cloudfront.net (CloudFront)",
                    "x-amz-cf-id": "0bD_AgtQJBElq5YMow9eHDeJGOgmjgoNg3-zX7roHV-7A-CR2go9lA==",
                    "x-amz-cf-pop": "IAD12-P4",
                    "x-cache": "Miss from cloudfront",
                },
                "mimeType": "text/css",
                "protocol": "h2",
                "remoteIPAddress": "104.18.4.65",
                "remotePort": 443,
                "responseTime": 1678644977042.071,
                "securityDetails": {
                    "certificateId": 0,
                    "certificateTransparencyCompliance": "compliant",
                    "cipher": "AES_128_GCM",
                    "encryptedClientHello": False,
                    "issuer": "Cloudflare Inc ECC CA-3",
                    "keyExchange": "",
                    "keyExchangeGroup": "X25519",
                    "protocol": "TLS 1.3",
                    "sanList": [
                        "sni.cloudflaressl.com",
                        "*.lambdatest.com",
                        "lambdatest.com",
                    ],
                    "serverSignatureAlgorithm": 1027,
                    "signedCertificateTimestampList": [
                        {
                            "hashAlgorithm": "SHA-256",
                            "logDescription": "Google 'Xenon2023' log",
                            "logId": "ADF7BEFA7CFF10C88B9D3D9C1E3E186AB467295DCFB10C24CA858634EBDC828A",
                            "origin": "Embedded in certificate",
                            "signatureAlgorithm": "ECDSA",
                            "signatureData": "30440220512BE5054B8F57E5A55A14D4C30C8CC5012297AF5512DC2F693CACC90586565B0220088C580090905E79A4227131E6D05C1224942A0A137C2E4299D6CF8888AFA8D5",
                            "status": "Verified",
                            "timestamp": 1667525992739.0,
                        },
                        {
                            "hashAlgorithm": "SHA-256",
                            "logDescription": "DigiCert Nessie2023 Log",
                            "logId": "B3737707E18450F86386D605A9DC11094A792DB1670C0B87DCF0030E7936A59A",
                            "origin": "Embedded in certificate",
                            "signatureAlgorithm": "ECDSA",
                            "signatureData": "3045022100EFA26C17004B1C3518F429AD728308908F9678528BEC91AE0C611CB6C743F38302201931AA03155550C17C8DAA96D3E73219E206775D93669675E132EAC01097D8BA",
                            "status": "Verified",
                            "timestamp": 1667525992753.0,
                        },
                        {
                            "hashAlgorithm": "SHA-256",
                            "logDescription": "Let's Encrypt 'Oak2023' log",
                            "logId": "B73EFB24DF9C4DBA75F239C5BA58F46C5DFC42CF7A9F35C49E1D098125EDB499",
                            "origin": "Embedded in certificate",
                            "signatureAlgorithm": "ECDSA",
                            "signatureData": "3045022075D83DE5ADC229ADEC8E68CBF55700D7C42E83DD66862EBDC77955F6FEAC7F07022100AD1B5213387466E45AF29C3E6E2F642DC4FDE92FC9EAD18208AF657B431A7E10",
                            "status": "Verified",
                            "timestamp": 1667525992696.0,
                        },
                    ],
                    "subjectName": "sni.cloudflaressl.com",
                    "validFrom": 1667520000,
                    "validTo": 1699142399,
                },
                "securityState": "secure",
                "status": 200,
                "statusText": "",
                "timing": {
                    "connectEnd": -1,
                    "connectStart": -1,
                    "dnsEnd": -1,
                    "dnsStart": -1,
                    "proxyEnd": -1,
                    "proxyStart": -1,
                    "pushEnd": 0,
                    "pushStart": 0,
                    "receiveHeadersEnd": 33.521,
                    "requestTime": 29031.946711,
                    "sendEnd": 0.472,
                    "sendStart": 0.407,
                    "sslEnd": -1,
                    "sslStart": -1,
                    "workerFetchStart": -1,
                    "workerReady": -1,
                    "workerRespondWithSettled": -1,
                    "workerStart": -1,
                },
                "url": "https://www.lambdatest.com/_next/static/css/898a7af19dc98577.css",
            },
            "timestamp": 29031.981551,
            "type": "Stylesheet",
        },
    }


d = es.search(index="network_logs",body={
  "query": {
    
            "multi_match":{
                "query": "Network.responseReceived",
                "type": "phrase",
            }
        }
    
})


print(d["hits"]["hits"][1])


# es.index(index="network_logs",id=2,body=a)

# res = es.get(index="network_logs",id=1)
# print(res)

# res = es.search(index="network_logs",body={
#     "from":0,
#     "size":10,
#     "query":{
#         "match":{
#             "method":"Network.responseReceived"
#         }
#     }
# })

# print(res)


# res = es.delete_by_query(index="network_logs",body={
#     "query":{
#         "match":{
#             "method":"Network.responseReceived"
#         }
#     }
# })

# print(res)



# docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.9
