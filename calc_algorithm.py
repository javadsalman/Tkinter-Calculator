class CalcAlg(object):
    def _-calc(self, first, exp, second):
        if exp == '*':
            result = float(first) * float(second)
        elif exp == '/':
            result = float(first) / float(second)
        elif exp == '+':
            result = float(first) + float(second)
        elif exp == '-':
            result = float(first) - float(second)
        else:
            raise(f'ValueError: {exp}')
        
        return float(result)
            
    def _calc_exp(self, array):
        counter = 0
        muldiv = 0
        exps = ['*/', '-+']
        passed_array = array.copy()
        while True:
            if len(array) == 1: 
                return array[0]
            
            s = array[counter]
            
            if str(s) in exps[muldiv]:
                first = array[counter-1]
                second = array[counter+1]
                res = self.calc(first, s, second)
                array[counter-1: counter+2] = [res]
                counter -= 1
                
            counter += 1
                
            if counter >= len(array):
                muldiv = 1
                counter = 0
            
            
    
    def evaluate(self, string):
        array = string.split()
        lenght = len(string)
        counter = 0
        result = 0
        left_par = right_par = -1
        there_is_par = False
        last_left_par = 0
        while array:
            if '(' not in array:
                return float(self.calc_exp(array))
            
            s = array[counter]
            
            if s == '(':
                last_left_par = counter
                there_is_par = True
            elif s == ')':
                slice = array[last_left_par+1: counter]
                res = self.calc_exp(slice)
                array[last_left_par: counter+1] = [res]
                
                counter = 0
                last_left_par = 0
                there_is_par = False
            
            
            counter += 1
