class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                      ".---","-.-",".-..","--","-.","---",".--.","--.-",
                      ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        visited = {}
        for word in words:
            code = ''
            for ltr in word:
                code += morseCodes[ord(ltr) - 97]
            if code not in visited:
                visited[code] = True
        return len(visited)
        
