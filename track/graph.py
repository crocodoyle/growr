import numpy as np
import xlrd, xlwt, sys

def importData(excel_file):
    try:        
        book = xlrd.open_workbook(excel_file)    
        sh = book.sheet_by_index(0)
        
        b = np.zeros((sh.ncols-5, (sh.nrows-1)/2))
        g = np.zeros((sh.ncols-5, (sh.nrows-1)/2))

        age = np.zeros((sh.nrows-1)/2)
        
        print >>sys.stderr, 'initialized'
        
        for r in np.arange((sh.nrows-1)/2):
            for c in np.arange(sh.ncols-5):
                age[r] = sh.cell_value(rowx=r+1, colx=1)
                
                b[c][r] = sh.cell_value(rowx=r+1, colx=c+5)
                g[c][r] = sh.cell_value(rowx=r+1+(sh.nrows-1)/2, colx=c+5)        
        
        print >>sys.stderr, 'done'
        data = {'age':age, 'b':b, 'g':g,}
        
        return data
    except Exception as e:
        print >>sys.stderr, 'error: {0}'.format(e.message)
    finally:
        return data
    
def exportData(measurement_set, kid_id):
    w = Workbook()
    s = w.add_sheet('measurements')
    
    s.write(0, 0, 'weight')
    s.write(0, 1, 'height')
    
    for i, m in measurement_set:       
        s.write(i, 0, m.weight)
        s.write(i, 1, m.height)
        
    w.save('/tmp/k{0}_data.xls')
    
    return 0