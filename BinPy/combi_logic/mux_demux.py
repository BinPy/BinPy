from BinPy import *

class MUX:
    '''
    This class can be used to create MUX in your circuit. It has a method for each kind of
    MUX, namely, mux_2_1, mux_4_1, mux_8_1 and mux_16_1
    All the methods take 3 parameters(inputs, select lines and strobe). Strobe is high by default
    inputs and select_inputs are lists. First index of input is 'A', second index is 'B' and so on...
    But last index of select_inputs is 'S0', second last index is 'S1' and so on...
    '''
    def __init__(self):
        self.gates = Gates()

    def run(self,inputs,select_inputs,strobe=1):
        '''
            This method takes 3 parameters [inputs(list),select_inputs(list), optional strobe(int)]
            This method automatically classifies the type of MUX and returns the computed result(int)
        '''
        allowed = [2,4,8,16]
        mux_type = len(inputs)
        if mux_type not in allowed:
            raise Exception("ERROR: only 4 types of MUX are supported, namely, 2:1, 4:1, 8:1 and 16:1")
        if 2**len(select_inputs)!=mux_type:
            raise Exception("ERROR: no of select inputs do not comply with no of inputs")
        if mux_type == 2:
            return self.mux_2_1(inputs,select_inputs,strobe)
        elif mux_type == 4:
            return self.mux_4_1(inputs,select_inputs,strobe)
        elif mux_type == 8:
            return self.mux_8_1(inputs,select_inputs,strobe)
        elif mux_type == 16:
            return self.mux_16_1(inputs,select_inputs,strobe)

    def mux_2_1(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 2:1 MUX using logic gates
        Input and output is same as run() method
        '''
        s = select_inputs[0]
        a = inputs[0]
        b = inputs[1]
        result = self.gates.OR(self.gates.AND(a,self.gates.NOT(s)),self.gates.AND(b,s))
        if strobe==1:
            return result
        else:
            return self.gates.NOT(result)

    def mux_4_1(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 4:1 MUX using logic gates
        Input and output is same as run() method
        '''
        select_inputs = select_inputs[::-1]
        s0 = select_inputs[0]
        s1 = select_inputs[1]
        a,b,c,d = inputs[0],inputs[1],inputs[2],inputs[3]
        term1 = self.gates.AND(a,self.gates.NOT(s0),self.gates.NOT(s1))
        term2 = self.gates.AND(b,s0,self.gates.NOT(s1))
        term3 = self.gates.AND(c,self.gates.NOT(s0),s1)
        term4 = self.gates.AND(d,s0,s1)
        result = self.gates.OR(term1,term2,term3,term4)
        if strobe==1:
            return result
        else:
            return self.gates.NOT(result)

    def mux_8_1(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 8:1 MUX using logic gates
        Input and output is same as run() method
        '''
        select_inputs = select_inputs[::-1]
        s0 = select_inputs[0]
        s1 = select_inputs[1]
        s2 = select_inputs[2]
        a,b,c,d,e,f,g,h = inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6],inputs[7]
        term1 = self.gates.AND(a,self.gates.NOT(s2),self.gates.NOT(s1),self.gates.NOT(s0))
        term2 = self.gates.AND(b,self.gates.NOT(s2),self.gates.NOT(s1),s0)
        term3 = self.gates.AND(c,self.gates.NOT(s2),s1,self.gates.NOT(s0))
        term4 = self.gates.AND(d,self.gates.NOT(s2),s1,s0)
        term5 = self.gates.AND(e,s2,self.gates.NOT(s1),self.gates.NOT(s0))
        term6 = self.gates.AND(f,s2,self.gates.NOT(s1),s0)
        term7 = self.gates.AND(g,s2,s1,self.gates.NOT(s0))
        term8 = self.gates.AND(h,s2,s1,s0)
        result = self.gates.OR(term1,term2,term3,term4,term5,term6,term7,term8)
        if strobe==1:
            return result
        else:
            return self.gates.NOT(result)

    def mux_16_1(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 16:1 MUX using two 8:1 MUX and one 2:1 MUX
        Input and output is same as run() method
        '''
        select_inputs = select_inputs[::-1]
        s0 = select_inputs[0]
        s1 = select_inputs[1]
        s2 = select_inputs[2]
        s3 = select_inputs[3]
        first_mux_8_1 = self.mux_8_1(inputs[0:8],[s2,s1,s0])
        second_mux_8_1 = self.mux_8_1(inputs[8:],[s2,s1,s0])
        result = self.mux_2_1([first_mux_8_1,second_mux_8_1],[s3])
        if strobe==1:
            return result
        else:
            return self.gates.NOT(result)
        

class DEMUX:
    '''
    This class can be used to create DEMUX in your circuit. It has a method for each kind of
    DEMUX, namely, demux_1_2, demux_1_4, demux_1_8 and demux_1_16
    All the methods take 3 parameters(inputs, select lines and strobe). Strobe is high by default
    inputs and select_inputs are lists. First index of input is 'A', second index is 'B' and so on...
    But last index of select_inputs is 'S0', second last index is 'S1' and so on...
    '''
    def __init__(self):
        self.gates = Gates()

    def run(self,inputs,select_inputs,strobe=1):
        '''
            This method takes 3 parameters [inputs(list),select_inputs(list), optional strobe(int)]
            This method automatically classifies the type of DEMUX and returns the computed result(int)
        '''
        allowed = [1,2,3,4]
        mux_type = len(select_inputs)
        if mux_type not in allowed:
            raise Exception("ERROR: only 4 types of DEMUX are supported, namely, 1:2, 1:4, 1:8 and 1:16")
        if len(inputs)!=1:
            raise Exception("ERROR: DEMUX can have only 1 input line")
        if mux_type == 1:
            return self.demux_1_2(inputs,select_inputs,strobe)
        elif mux_type == 2:
            return self.demux_1_4(inputs,select_inputs,strobe)
        elif mux_type == 3:
            return self.demux_1_8(inputs,select_inputs,strobe)
        elif mux_type == 4:
            return self.demux_1_16(inputs,select_inputs,strobe)

    def demux_1_2(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 1:2 DEMUX using logic gates
        Input and output is same as run() method
        '''
        output = {}
        
        s = select_inputs[0]
        a = inputs[0]
        
        output[0] = self.gates.AND(a, self.gates.NOT(s))
        output[1] = self.gates.AND(a, s)

        if strobe == 0:
            for w in output:
                if output[w] == 1:
                    output[w] = self.gates.NOT(output[w])
             
        return output

    def demux_1_4(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 1:4 DEMUX using logic gates
        Input and output is same as run() method
        '''
        output = {}

        select_inputs = select_inputs[::-1]
        s0 = select_inputs[0]
        s1 = select_inputs[1]
        a = inputs[0]

        output[0] = self.gates.AND(self.gates.NOT(s0), self.gates.NOT(s1), a)
        output[1] = self.gates.AND(s0, self.gates.NOT(s1), a)
        output[2] = self.gates.AND(self.gates.NOT(s0), s1, a)
        output[3] = self.gates.AND(s0, s1, a)
        
        if strobe == 0:
            for w in output:
                if output[w] == 1:
                    output[w] = self.gates.NOT(output[w])

        return output

    def demux_1_8(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 1:8 DEMUX using logic gates
        Input and output is same as run() method
        '''
        output = {}

        select_inputs = select_inputs[::-1]
        s0 = select_inputs[0]
        s1 = select_inputs[1]
        s2 = select_inputs[2]
        a = inputs[0]       
        
        output[0] = self.gates.AND(a,self.gates.NOT(s2),self.gates.NOT(s1),self.gates.NOT(s0))
        output[1] = self.gates.AND(a,self.gates.NOT(s2),self.gates.NOT(s1),s0)
        output[2] = self.gates.AND(a,self.gates.NOT(s2),s1,self.gates.NOT(s0))
        output[3] = self.gates.AND(a,self.gates.NOT(s2),s1,s0)
        output[4] = self.gates.AND(a,s2,self.gates.NOT(s1),self.gates.NOT(s0))
        output[5] = self.gates.AND(a,s2,self.gates.NOT(s1),s0)
        output[6] = self.gates.AND(a,s2,s1,self.gates.NOT(s0))
        output[7] = self.gates.AND(a,s2,s1,s0)
        
        if strobe == 0:
            for w in output:
                if output[w] == 1:
                    output[w] = self.gates.NOT(output[w])

        return output

    def demux_1_16(self,inputs,select_inputs,strobe=1):
        '''
        This method implements 1:16 DEMUX using logic gates
        Input and output is the same  as run() method
        '''
        output = {}

        select_inputs = select_inputs[::-1]
        s0 = select_inputs[0]
        s1 = select_inputs[1]
        s2 = select_inputs[2]
        s3 = select_inputs[3]
        a = inputs[0]

        output[0] = self.gates.AND(a,self.gates.NOT(s3),self.gates.NOT(s2),
                        self.gates.NOT(s1),self.gates.NOT(s0))
        output[1] = self.gates.AND(a,self.gates.NOT(s3),self.gates.NOT(s2),self.gates.NOT(s1),s0)
        output[2] = self.gates.AND(a,self.gates.NOT(s3),self.gates.NOT(s2),s1,self.gates.NOT(s0))
        output[3] = self.gates.AND(a,self.gates.NOT(s3),self.gates.NOT(s2),s1,s0)
        output[4] = self.gates.AND(a,self.gates.NOT(s3),s2,self.gates.NOT(s1),self.gates.NOT(s0))
        output[5] = self.gates.AND(a,self.gates.NOT(s3),s2,self.gates.NOT(s1),s0)
        output[6] = self.gates.AND(a,self.gates.NOT(s3),s2,s1,self.gates.NOT(s0))
        output[7] = self.gates.AND(a,self.gates.NOT(s3),s2,s1,s0)

        output[8] = self.gates.AND(a,s3,self.gates.NOT(s2),self.gates.NOT(s1),self.gates.NOT(s0))
        output[9] = self.gates.AND(a,s3,self.gates.NOT(s2),self.gates.NOT(s1),s0)
        output[10] = self.gates.AND(a,s3,self.gates.NOT(s2),s1,self.gates.NOT(s0))
        output[11] = self.gates.AND(a,s3,self.gates.NOT(s2),s1,s0)
        output[12] = self.gates.AND(a,s3,s2,self.gates.NOT(s1),self.gates.NOT(s0))
        output[13] = self.gates.AND(a,s3,s2,self.gates.NOT(s1),s0)
        output[14] = self.gates.AND(a,s3,s2,s1,self.gates.NOT(s0))
        output[15] = self.gates.AND(a,s3,s2,s1,s0)
            
        #todo: can this be made using 1:4 and 1:8 demultiplexers? Code too inefficient
        
        if strobe == 0:
            for w in output:
                if output[w] == 1:
                    output[w] = self.gates.NOT(output[w])

        return output
