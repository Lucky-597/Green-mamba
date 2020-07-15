import pandas as pd

def main():
    dd = pd.read_csv('ceshi.csv')
    print(dd)
    dd = dd[dd['flag'].isin([0])]
    print(dd)

    dd.to_csv('ceshi.csv')
if __name__ == '__main__':
    main()