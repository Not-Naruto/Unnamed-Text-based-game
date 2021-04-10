import pickle

with open('profile.dat','wb') as f:
    x={'health':160,'maxh':160, 'level':3, 'pot':5,'coins':450, 'atk':40, 'def':10}
    pickle.dump(x,f)
