import re


class ParsingUtils:

    @staticmethod
    def parse_tick_from_frame(frame):
        ethernet = frame["ethernet"]
        ipv4_message = ethernet["ipv4"]
        udp = ipv4_message["udp"]
        raw = udp["raw"]
        packet = raw["packet"]
        return packet["value"]

    @staticmethod
    def parse_source_from_frame(frame):
        return frame["ethernet"]["ipv4"]["src"]

    @staticmethod
    def parse_arrival_time_from_frame(frame):
        return frame["time_epoch"]

    @staticmethod
    def get_tick(packet_payload):
        symbol = ParsingUtils.get_symbol(packet_payload)
        seqno = ParsingUtils.get_seqno(packet_payload)
        price = ParsingUtils.get_price(packet_payload)

        return symbol, seqno, price

    @staticmethod
    def get_symbol(packet_payload):
        return re.search(r"Symbol: (\D{1,4}) ", packet_payload).group(1)

    @staticmethod
    def get_seqno(packet_payload):
        return re.search(r"\sSeqno: (\d+) ", packet_payload).group(1)

    @staticmethod
    def get_price(packet_payload):
        return re.search(r"Price: (\d+)", packet_payload).group(1)
