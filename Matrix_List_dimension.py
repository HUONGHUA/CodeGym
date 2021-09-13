
# lst2 = [1, 3, 4, 6, 7, 1, 5, 7, 8]

# def get_matrix(m,n):
#     a = len(lst2)
#     new_lst2 = lst2[0:m]
#     new1_lst2 = lst2[m:m+n]
#     new2_lst2 = lst2[n+m:a]
#     maxtrix = [new_lst2, new1_lst2, new2_lst2]
#     for x in maxtrix:
#         print(x)
import random

class Matrix:
    def __init__(self, m):
        self.m = m
        self.matrix_list = []

    def add(self):
        number = 1
        for i in range(self.m):
            lst2 = []
            for j in range(self.m):
                lst2.append(number)
                number += 1
            self.matrix_list.append(lst2)

        '''
        import random
        
        def matrix(m,n):
            for i in range(m):
                lst2 = [random.randint(0, 9) for j in range(n)]
                print(lst2)
        
        a = matrix(3,4)
        b = matrix(2,9)
        '''
        return self.matrix_list

    def sum_diagonal(self):
        sum_list = []
        i = 0
        sum_m = 0

        for mtrix in self.matrix_list:
            sum_list.append(mtrix[i])
            i += 1
        for s in sum_list:
            sum_m += s
        print("Tong cac duong cheo cua List la : ", sum_m)
        return sum_m

    def print_matrix(self):
        for new_matrix in self.matrix_list:
            print(new_matrix)

    def get_flat_list(self):
        new_flat_list = []
        k = 0
        for matrix1 in self.matrix_list:
            if k % 2 == 0:
                for i in matrix1:
                    new_flat_list.append(i)
            else:
                n_ls = [i for i in matrix1]
                rev_ls = sorted(n_ls, reverse=True)
                for i in rev_ls:
                    new_flat_list.append(i)
            k += 1
        print("Reverse cua List so le la : ", new_flat_list)


    def sum_row_elements(self):
        i = 0
        new_matr = [0 for x in self.matrix_list]

        if self.m == 1:
            for colo in self.matrix_list:
                new_matr.append(colo)
                print(new_matr)

        else:
            for colo in self.matrix_list:
                for i in range(self.m):
                    new_matr[i] += colo[i]

        print("List of Sum_row : ", new_matr)


        # sum_row_list = [sum(x) for x in zip(*self.matrix_list)]
        # print(sum_row_list)
        # return sum_row_list


class App(Matrix):
    m = int(input("Please enter column number: "))
    # n = int(input("Please enter row number : "))
    a = Matrix(m)
    a.add()
    a.print_matrix()
    a.sum_diagonal()
    a.get_flat_list()
    a.sum_row_elements()









