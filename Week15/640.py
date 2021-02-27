### DO NOT REMOVE THIS
from typing import List
### DO NOT REMOVE THIS
class Solution:
    def solveEquation(self, equation: str) -> str:
        slope_right=0
        slope_left=0
        intercept_right=0
        intercept_left=0
        right=True
        string=""
        dau=""
        for i in range(0,len(equation)):
            if equation[i]=="x":
                if right==True:
                    if dau=="":
                        if string!="":
                            slope_right+=int(string)
                        else:
                            slope_right+=1
                        dau=""
                        string=""
                    else:
                        if dau=="-":
                            if string!="":
                                slope_right-=int(string)
                            else:
                                slope_right-=1
                        else:
                            if string!="":
                                slope_right+=int(string)
                            else:
                                slope_right+=1
                        dau=""
                        string=""
                            
                else:
                    if dau=="":
                        if string!="":
                            slope_left+=int(string)
                        else:
                            slope_left+=1
                        dau=""
                        string=""
                    else:
                        if dau=="-":
                            if string!="":
                                slope_left-=int(string)
                            else:
                                slope_left-=1
                        else:
                            if string!="":
                                slope_left+=int(string)
                            else:
                                slope_left+=1
                        dau=""
                        string=""
                
            elif equation[i] in ["1","2","3","4","5","6","7","8","9","0"]:
                string+=equation[i]
            
            elif equation[i]=="=":
                right=False
                if string!="":
                    if dau=="-":
                        intercept_right-=int(string)
                    else:
                        intercept_right+=int(string)
                dau=""
                string=""
            else:
                
                if right==True:
                    if dau=="":
                        if string!="":
                            intercept_right+=int(string)
                        
                        dau=equation[i]
                        string=""
                    else:
                        if dau=="-":
                            if string!="":
                                intercept_right-=int(string)
                            
                        else:
                            if string!="":
                                intercept_right+=int(string)
                            
                        dau=equation[i]
                        string=""
                            
                else:
                    if dau=="":
                        if string!="":
                            intercept_left+=int(string)
                        
                        dau=equation[i]
                        string=""
                    else:
                        if dau=="-":
                            if string!="":
                                intercept_left-=int(string)
                           
                        else:
                            if string!="":
                                intercept_left+=int(string)
                            
                        dau=equation[i]
                        string=""
        if dau=="":
            if string!="":
                intercept_left+=int(string)

            dau=equation[i]
            string=""
        else:
            if dau=="-":
                if string!="":
                    intercept_left-=int(string)

            else:
                if string!="":
                    intercept_left+=int(string)

            dau=equation[i]
            string=""
        print(slope_right)
        print(intercept_right)
        print(slope_left)
        print(intercept_left)
        
        if intercept_left==intercept_right and slope_right==slope_left:
            return "Infinite solutions"
        elif slope_right==slope_left:
            return "No solution"
        elif intercept_left==intercept_right:
            return "x=0"
        else:
            return "x={0}".format(int((intercept_left-intercept_right)/(slope_right-slope_left))
