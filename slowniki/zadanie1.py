slownik ={
    '1': 'niedostateczny',
    '2': 'dopuszczający',
    '3': 'dostateczny',
    '4': 'dobry',
    '5': 'bardzo dobry',
    '6': 'celujący'
}

#modyfikowanie slownika
slownik.pop('1')
slownik.pop('6')

slownik['3.5'] = 'dostateczny+'
slownik['4.5'] = 'dobry+'

print(slownik)


