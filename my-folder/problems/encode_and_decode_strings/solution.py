class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        # print(res)
        return res


        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        2#hi3#hel
        res = []
        i = 0
        length = ""
        # check if we are at #
        while i < len(s):
            print(i)
            lengthStr = ""

            while s[i] != '#':
                lengthStr += s[i]
                i+=1

            length = int(lengthStr)
            i += 1
            res.append(s[i: i+length])
            # print(i)
            i += length
            # print(i)

        return res





        






            

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))