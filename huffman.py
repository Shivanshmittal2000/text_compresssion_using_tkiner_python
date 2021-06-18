import heapq,os
class BinaryTreeNode:
    def __init__(self,value,frequency):
        self.value=value
        self.frequency=frequency
        self.right=None
        self.left=None
    def __lt__(self,other):
        return self.frequency<other.frequency
    def __eq__(self,other):
        return self.frequency==other.frequency
class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        self.__heap=[]
        self.__codes={}
        self.__reversecodes={}
    def __make_frequency_dict(self,text):
        frequency_dict={}
        for char in text:
            if char not in frequency_dict:
                frequency_dict[char]=1
            else :
                frequency_dict[char]+=1
        return frequency_dict
    def __buildheap(self,freq_dict):
        for i in freq_dict:
            frequency=freq_dict[i]
            binary_tree_node=BinaryTreeNode(i,frequency)
            heapq.heappush(self.__heap,binary_tree_node)
    def __buildtree(self):
        while len(self.__heap)>1:
            min1=heapq.heappop(self.__heap)
            min2=heapq.heappop(self.__heap)
            newnode=BinaryTreeNode(None,(min1.frequency+min2.frequency))
            newnode.left=min1
            newnode.right=min2
            heapq.heappush(self.__heap,newnode)
        return 
    def __buildcodeshelper(self,root,string):
        if root is None:
            return
        if root.value is not None: # check it is leaf node or not as only leaf node value is not None
            self.__codes[root.value]=string   # Makes a map for character to their codes
            self.__reversecodes[string]=root.value
            return 
        self.__buildcodeshelper(root.left,string+"0")
        self.__buildcodeshelper(root.right,string+"1")
    def __buildcodes(self):
        root=heapq.heappop(self.__heap)
        self.__buildcodeshelper(root,"")
    def __encodetext(self,text):
        encodedvalue=""
        for i in text:
            encodedvalue+=self.__codes[i]
        return encodedvalue
    def __getPaddedEncoded(self,encodedstring):
        paddedamount=8-(len(encodedstring)%8)
        for i in range(paddedamount):
            encodedstring+="0"
        paddedinfo="{0:08b}".format(paddedamount)
        encodedtext=paddedinfo+encodedstring
        return encodedtext
    def __getarray(self,padded_encodedtext):
        array=[]
        for i in range(0,len(padded_encodedtext),8):
            byte=padded_encodedtext[i:i+8]
            array.append(int(byte,2)) #convert byte from binary to decmal
        return array
    def compress(self):
        file_name,file_extension=os.path.splitext(self.path)
        print(file_name)
        output_path=file_name+".bin"
#         file=open(self.path,"r+")  another way or writing with line
#         output=open(output_path,"wb")
        with open(self.path,"r+") as file ,open(output_path,"wb") as output: #this function close both (output and file) after come out this colun
            text=file.read()
            text=text.rstrip()
            freq_dict=self.__make_frequency_dict(text)
            self.__buildheap(freq_dict)
            self.__buildtree()
            self.__buildcodes()
            encodedstring=self.__encodetext(text)
            padded_encodedtext=self.__getPaddedEncoded(encodedstring)
            bytes_array=self.__getarray(padded_encodedtext)
            final_bytes=bytes(bytes_array)
            output.write(final_bytes)
        print("Compressed")
        return output_path
    def _removepadding(self,text):
        padded_info=text[0:8]
        extrapadding=int(padded_info,2)
        text=text[8:]
        actual_text=text[:-1*extrapadding]
        return actual_text
    def __decodetext(self,text):
        current_bits=""
        decodedtext=""
        for i in text:
            current_bits+=i
            if current_bits in self.__reversecodes:
                character=self.__reversecodes[current_bits]
                decodedtext+=character
                current_bits=""
        return decodedtext
    def decompress(self,input_path):
        file_name,file_extension=os.path.splitext(input_path)
        output_path=file_name+"_decompressed" +".txt"
        with open(input_path,"rb") as file ,open(output_path,"w") as output:
            bit_string=""
            byte=file.read(1)
            while byte:
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,"0")
                bit_string+=bits
                byte=file.read(1)
            actual_text=self._removepadding(bit_string)
            decoded_text=self.__decodetext(actual_text)
            output.write(decoded_text)
            print("Decompressed")
        return
# path="D:/data science assignment/exapl.txt"
# h=HuffmanCoding(path)
# outputpath=h.compress()
# h.decompress(outputpath)
# print(outputpath)