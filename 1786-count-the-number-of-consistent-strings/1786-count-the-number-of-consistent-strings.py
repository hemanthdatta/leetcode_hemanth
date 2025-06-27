class Solution:
    def countConsistentStrings(self, a: str, w: List[str]) -> int:
        return sum(map({*a}.issuperset,w))