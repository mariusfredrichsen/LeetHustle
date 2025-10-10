class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        max_energy = float('-inf')

        for i in range(n-k, n):
            j = i
            current_sum = 0
            while j >= 0:
                current_sum += energy[j]
                max_energy = max(max_energy, current_sum)
                j -= k
        
        return max_energy
