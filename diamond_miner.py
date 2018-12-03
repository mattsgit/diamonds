def find_most_diamonds(mat0, n, cell):
    print 'The Input Mat:'
    for i in mat0:
        print mat0[i]
    #Lets build a new mat starting at the end showing total possible diamonds collectible from that point to the end
    total_diamonds_from_point = {k: [0 for i in range(n)] for k in range(n)}

    total_diamonds_from_point = {k: [0 for i in range(n)] for k in range(n)}
    while cell[1] != -1:

        #print 'cell: %s' % cell
        cell_value = mat0[cell[0]][cell[1]]
        # need to track right and below of current mat values and total accumulating diamonds
        try:
            right = mat0[cell[0]][cell[1] + 1]
            right_tot = total_diamonds_from_point[cell[0]][cell[1] + 1]
        except Exception as e:
            right = -1
            right_tot = -1
        try:
            below = mat0[cell[0] + 1][cell[1]]
            below_tot = total_diamonds_from_point[cell[0] + 1][cell[1]]
        except Exception as e:
            below = -1
            below_tot = -1
        #print 'cell value: %s, right of cell is: %s, below cell is %s' % (cell_value, right, below)

        # Insert should be fine here given < 100 items but ill just append and reverse lists at the end for performance
        if ((right == -1 and below == -1) or cell_value == -1) and cell != [n - 1, n - 1]:
            # blocked gtfo
            print 'dont go here: %s' % cell
            total_diamonds_from_point[cell[0]][cell[1]] = -1
        else:
            #print 'adding total of: %s' % (cell_value + max(0, right_tot, below_tot))
            total_diamonds_from_point[cell[0]][cell[1]] = cell_value + max(0, right_tot, below_tot)

        # move up then left when we get to top
        if cell[0] == 0:
            cell[1] -= 1
            cell[0] = n - 1
        else:
            cell[0] -= 1

    print 'max diamonds from position mat: '
    max_total_diamonds = total_diamonds_from_point[0][0]
    for i in total_diamonds_from_point:
        print total_diamonds_from_point[i]

    print 'We will collect %s diamonds this time' % max_total_diamonds
    new_cell = [0, 0]
    best_path = []
    # now we build array of points to traverse, 0 diamonds out in original mat for these points and run the whole thing again
    while new_cell != [n - 1, n - 1]:
        best_path.append([new_cell[0],new_cell[1]])
        try:
            right = total_diamonds_from_point[new_cell[0]][new_cell[1] + 1]
        except Exception as e:
            right = -1
        try:
            below = total_diamonds_from_point[new_cell[0] + 1][new_cell[1]]
        except Exception as e:
            below = -1


        if right == -1 and below == -1:
            print 'GAME OVER'
        elif right > below:
            new_cell[1] += 1
        else:
            new_cell[0] += 1

    best_path.append([n-1,n-1])
    return best_path, mat0, max_total_diamonds

if __name__ == '__main__':

    #Mine some diamonds, get a fresh map
    mat0 = {0:[0,0,0],1:[1,1,-1],2:[1,0,1]}
    n = len(mat0)
    cell = [n-1,n-1]

    bp,new_mat , first_diamonds = find_most_diamonds(mat0,n,cell)
    cell = [n-1,n-1]
    print 'Best path down:'
    print bp
    for i in bp:
        new_mat[i[0]][i[1]] = 0
    print '\nOne more time through:'
    bp, no_mat, second_diamonds = find_most_diamonds(new_mat,n,cell)
    print 'Best path back:'
    print list(reversed(bp))
    print '\nWe collected %s diamonds total' % (first_diamonds + second_diamonds)

