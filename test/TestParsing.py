import json

import pytest

from main.strategy.utils.ParsingUtils import ParsingUtils


@pytest.fixture(scope="module")
def valid_value():
    return "Symbol: APPL Seqno: 0 Price: 1623"


@pytest.fixture(scope="module")
def valid_frame():
    returned_json = json.loads("""   
    {
       "frame_info": {
            "ts_sec": 1473411962,
            "ts_usec": 413131,
            "incl_len": 75,
            "orig_len": 75
        },
        "time": "2016-09-09T04:06:02.413131",
        "number": 2,
        "time_epoch": "1473411962.413131",
        "len": 75,
        "cap_len": 75,
        "ethernet": {
            "dst": "01:00:5e:16:00:01",
            "src": "3c:07:54:0d:62:3c",
            "type": {
                "name": "EtherType::Internet_Protocol_version_4",
                "value": 2048
            },
            "ipv4": {
                "version": 4,
                "hdr_len": 20,
                "tos": {
                    "pre": {
                        "name": "ToSPrecedence::Routine",
                        "value": 0
                    },
                    "del": {
                        "name": "ToSDelay::NORMAL",
                        "value": 0
                    },
                    "thr": {
                        "name": "ToSThroughput::NORMAL",
                        "value": 0
                    },
                    "rel": {
                        "name": "ToSReliability::NORMAL",
                        "value": 0
                    },
                    "ecn": {
                        "name": "ToSECN::Not_ECT",
                        "value": 0
                    }
                },
                "len": 61,
                "id": 1,
                "flags": {
                    "df": false,
                    "mf": false
                },
                "offset": 0,
                "ttl": 64.0,
                "protocol": {
                    "name": "TransType::UDP",
                    "value": 17
                },
                "checksum": {
                    "type": "bytes",
                    "value": "w\ufffd",
                    "hex": "778d"
                },
                "src": "10.10.10.1",
                "dst": "239.22.0.1",
                "udp": {
                    "srcport": 33000,
                    "dstport": 51000,
                    "len": 41,
                    "checksum": {
                        "type": "bytes",
                        "value": "\ufffdk",
                        "hex": "b16b"
                    },
                    "raw": {
                        "protocol": 51000,
                        "packet": {
                            "type": "bytes",
                            "value": "Symbol: APPL Seqno: 0 Price: 1623",
                            "hex": "53796d626f6c3a204150504c205365716e6f3a20302050726963653a2031363233"
                        },
                        "error": null
                    }
                }
            }
        },
        "protocols": "Ethernet:IPv4:UDP:Raw"
    }
    """)
    return returned_json


def test_parse_tick_from_frame(valid_frame):
    assert ParsingUtils.parse_tick_from_frame(valid_frame) == "Symbol: APPL Seqno: 0 Price: 1623"


def test_parse_src_from_frame(valid_frame):
    assert ParsingUtils.parse_source_from_frame(valid_frame) == "10.10.10.1"


def test_parse_timestamp_from_frame(valid_frame):
    assert ParsingUtils.parse_arrival_time_from_frame(valid_frame) == "1473411962.413131"


def test_get_symbol(valid_value):
    assert "APPL" == ParsingUtils.get_symbol(valid_value)


def test_get_seqno(valid_value):
    assert "0" == ParsingUtils.get_seqno(valid_value)


def test_get_price(valid_value):
    assert "1623" == ParsingUtils.get_price(valid_value)


if __name__ == "__main__":
    pytest.main(["-x", "TestParsing.py"])
