

# Taylor, Mclaurin series




# Some standard expansions


class Taylor_Expansions:
  
    def Sin(N = 10000000000):
        for n in range(abs(N)):
            yield "x" if n==0 else ("- " if n%2!=0 else "+ ")+"x^"+str(2*n+1)+"/"+str(2*n+1)+"!"

if __name__ == '__main__':
    te = Taylor_Expansions
    print(*list(te.Sin(30)), sep='\n')
