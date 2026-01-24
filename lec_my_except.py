class Myerr(Exception):
    def __str__(self):
        return 'Натворил делов'
    
    
raise Myerr
raise ValueError