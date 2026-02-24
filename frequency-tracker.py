from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        # number -> frequency
        self.count = defaultdict(int)
        
        # frequency -> how many numbers have this frequency
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        old_freq = self.count[number]
        
        # Decrease old frequency count
        if old_freq > 0:
            self.freq[old_freq] -= 1
        
        # Increase number frequency
        self.count[number] += 1
        new_freq = self.count[number]
        
        # Increase new frequency count
        self.freq[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.count[number]
        
        if old_freq == 0:
            return
        
        # Decrease old frequency count
        self.freq[old_freq] -= 1
        
        # Decrease number frequency
        self.count[number] -= 1
        new_freq = self.count[number]
        
        if new_freq > 0:
            self.freq[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
