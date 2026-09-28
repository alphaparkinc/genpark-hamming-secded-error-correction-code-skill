"""Hamming (7, 4) and SECDED (8, 4) Engine.
100% Python Standard Library.
"""

class HammingSECDED:
    """Hamming (7, 4) and Extended (8, 4) Single Error Correction, Double Error Detection."""
    @staticmethod
    def encode_7_4(data4):
        d0, d1, d2, d3 = data4
        p0 = d0 ^ d1 ^ d3
        p1 = d0 ^ d2 ^ d3
        p2 = d1 ^ d2 ^ d3
        return [p0, p1, d0, p2, d1, d2, d3]

    @classmethod
    def encode_8_4(cls, data4):
        c7 = cls.encode_7_4(data4)
        p_overall = sum(c7) % 2
        return c7 + [p_overall]

    @staticmethod
    def decode_8_4(word8):
        c = word8[:7]
        p_overall_rcv = word8[7]
        p_overall_calc = sum(c) % 2
        overall_parity_err = (p_overall_rcv != p_overall_calc)

        s0 = c[0] ^ c[2] ^ c[4] ^ c[6]
        s1 = c[1] ^ c[2] ^ c[5] ^ c[6]
        s2 = c[3] ^ c[4] ^ c[5] ^ c[6]
        syndrome = s0 + (s1 << 1) + (s2 << 2)

        corrected = list(c)
        status = "NO_ERROR"

        if syndrome != 0:
            if overall_parity_err:
                status = "SINGLE_ERROR_CORRECTED"
                err_idx = syndrome - 1
                corrected[err_idx] ^= 1
            else:
                status = "DOUBLE_ERROR_DETECTED"

        data4 = [corrected[2], corrected[4], corrected[5], corrected[6]]
        return {"data": data4, "status": status, "syndrome": syndrome}
