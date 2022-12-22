from main.utils.ParsingUtils import ParsingUtils


class Strategy:
    def get_top_n_data_providers(self, frames, n):
        # Implement this in child strategies
        pass

    def get_top_data_providers(self, frames, n):
        # Implement this in child strategies
        pass

    def get_name(self):
        # Implement this in child strategies
        pass

    @staticmethod
    def create_seq_to_source_mapping(frames: list):
        output = dict()
        for (frame_key, frame) in frames.items():
            if frame_key == "Global Header":
                continue

            tick = ParsingUtils.parse_tick_from_frame(frame)
            source_ip = ParsingUtils.parse_source_from_frame(frame)
            arrival_time = ParsingUtils.parse_arrival_time_from_frame(frame)

            seq_no = ParsingUtils.get_seqno(tick)

            if seq_no not in output:
                output[seq_no] = list()
            output[seq_no].append((source_ip, arrival_time))
        return output

    @staticmethod
    def create_source_to_time_mapping(frames: list):
        output = dict()
        for (frame_key, frame) in frames.items():
            if frame_key == "Global Header":
                continue

            source_ip = ParsingUtils.parse_source_from_frame(frame)
            arrival_time = ParsingUtils.parse_arrival_time_from_frame(frame)

            if source_ip not in output:
                output[source_ip] = list()
            output[source_ip].append(float(arrival_time))
        return output