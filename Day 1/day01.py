class Solution:
    def __init__(self):
        self.calibrationValues = []
        
    def getCalibrationValues1(self):

        with open('puzzleinput.txt', 'r') as input: 

            line = input.readline() 

            while line:
                nums = []
                for char in line:
                    if char.isdigit():
                        nums.append(int(char))

                self.calibrationValues.append(nums[0]*10 + nums[-1])
                line = input.readline()

        
        return sum(self.calibrationValues)
    
    def getCalibrationValues2(self):

        map = { "one": "o1e",
                "two": "t2o",
                "three": "t3e",
                "four": "f4r",
                "five": "f5e",
                "six": "s6x",
                "seven": "s7n",
                "eight": "e8t",
                "nine": "n9e"
                }
        
        with open('puzzleinput.txt','r') as file:

            lines = file.readlines() 
            for line in lines:

                for key in map:
                    line = line.replace(key,map[key])
                    
                nums = []
                for char in line:
                    if char.isdigit():
                        nums.append(int(char))
                
                self.calibrationValues.append(nums[0]*10 + nums[-1])
                

        return sum(self.calibrationValues)


obj = Solution()
print(obj.getCalibrationValues2())