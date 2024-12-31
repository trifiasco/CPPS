def firstMissingPositive(self, A):
        A.sort();
        
        missing = 1;
        for i in range(len(A)):
            
            if(A[i] < 1):
                continue;
            if(A[i] == missing):
                missing+=1;
                continue;
            else:
                break;
        
        return missing
