class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Fourth Approch : Running Stack
        # As each point is ploted, buildings listed in a dictionary are eliminated if 
        # they are less than the current building 'left'. 
        # If no buildings are left, a node is ploted where the dictionary's 
        # longest building ended. 
        # Otherwise a node is ploted where a dictionary of buildings is used to determine
        # the point to plot. 
        # Once ploted, the dictionary is updated to store the hight and width of 
        
        dic = {1:[first_building_height,first_building_right]}
        output = [first_building_left, first_building_height]
        count = 1
        for i in buildings[1:]:
            count = count + 1
            for j,k in dic.items():
                if i[0] >= k[1]:
                    to_delete.append(j)
            # here, remove point if i[height] = k[right] and i[left] = k[right]???
            if len(dic) == len(to_delete):
                output.append([max(row[1] for row in to_delete),0])
                if m in to_delete:
                    del dic[m]
                continue
            if m in to_delete:
                del dic[m]
            dic_mx_h = [row[1:] for row in dic]
            dic_mx_h_l = max(row[2] for row in dic_mx_h)
            # plot
            output.append([dir_mx_h_l,i[2]])
            # add to dic
            dic.update(count:i)
            


        print(output,count)

        # Approch one:
        #Left to Right
        # Case Omega: No buildings
        # Case One: One building
        # Case two : two seperate buildings
        # Case three: two prefectly overlapping buidlings
        # Case four : two overlapping with one higher than another
        # Case five : two overlapping with one wider than the other
        # Case six : three seperate buildings
        # Case seven : three prefectly overlapping buildings
        # Case eight : two overlaping and one seperate building
        # Case nine : three overlaping buildings the second is lower than first, third overlaps second and is taller. 
        # Case ten :
        # Approch two: 
        # Shortest to tallest.
        # Problem: What if a huge building completely covers all other smaller buildings? Won't you have to reduce the number of nodes?
        # Case eleven : Two towers of equal hight immediatly beside each other.   
        #Approch three: Process of Elimination
        # Plot all nodes, eliminate impossible nodes, plot intersection nodes,
        # an intersecting point must be ploted if these are true
        # 1: a previous building is higher and ends before the current building begins
        # 2: multiple buildings are higher and end before the current building begins

        #Approch four: 
        # Running Stack
        # As each point is ploted, buildings listed in a dictoinary are eliminated if 
        # they are less than the current building 'left'. 
        # If no buildings are left, a node is ploted where the dictionary's 
        # longest building ended. 
        # Otherwise a node is ploted where a dictionary of buildings is used to determine
        # the point to plot. 
        # Once ploted, the dictionary is updated to store the hight and width of 
        # current building.
        # Problems: the most inefficient case would be if each consecuative building is taller
        # then the previous and extended to the far right. In that case, the program will check
        # the building hights n + n-1 +... 1

