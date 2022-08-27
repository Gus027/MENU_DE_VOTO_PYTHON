def lin():
    print('-'*55)


voto = 0
moradores = 0
lindomar = 0
claudio = 0
elmar = 0
while(voto < 100):
        lin()
        print('Insira de 1 a 3 os seus canditatos a sindico:\n- Lindomar (VOTE-01)\n- Claudio (VOTE-02)\n- Elmar(VOTE-03)')
        insert = int(input('Insira o voto: '))
        if (insert > 3 or insert < 1):
            print('ERRO NOS VALORES DO VOTO, INSIRA NOVAMENTE.')
        else:
          if(insert == 1):
            lindomar +=1
            print('VOTO - Lindomar!')
          elif(insert == 2):
            claudio +=1
            print('VOTO - Claudio.')
          else:
            elmar +=1
            print('VOTO - Elmar.')
        voto += 1
     #  print(f'Porcentagem de votos SIM: {sim / (sim + nao) * 100: .1f} %.')
        print(f'Porcentagem: {(lindomar / voto)*100: .1f}%')
        print(f'Porcentagem: {(claudio / voto)*100: .1f}%')
        print(f'Porcentagem: {(elmar / voto )*100: .1f}%')