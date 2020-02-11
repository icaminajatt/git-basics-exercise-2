Function RecursiveFactorial(int n)
    if n >= 1 do
        return n * RecursiveFactorial(n-1)
    else
        return 1
    end
end
