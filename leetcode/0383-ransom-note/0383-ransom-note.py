class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazin_map={}
        for char in magazine:
            if char in magazin_map:
                magazin_map[char]+=1
            else:
                magazin_map[char]=1
        for char in ransomNote:
            if char not in magazin_map or magazin_map[char]==0:
               return False
            magazin_map[char]-=1
        return True                  