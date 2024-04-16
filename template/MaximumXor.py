
class MaximumXor:
    @staticmethod
    def maximum_xor(nums: list):
        ans = msk = 0
        high_bit = max(nums).bit_length() - 1
        for i in range(high_bit, -1, -1):
            msk |= 1 << i
            new_ans = ans | (1 << i)
            vis = set()
            for x in nums:
                x &= msk
                if new_ans ^ x in vis:
                    ans = new_ans
                    break
                vis.add(x)
        return ans




