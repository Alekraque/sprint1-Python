def menu (): #função menu (tudo está dentro dela)
  while True: #faz um loop de repetição para sempre retornar ao começo
    
    print( #prints de boas vindas e escolha das opções
      'Bem-vindo ao sistema de informações da AFI Acessibilidades!\n'
      'por gentileza, escolha uma das opções abaixo\n\n'
      '[1] VERIFIQUE SE VOCÊ É UM DEFICIENTE\n'
      '[2] VER ROTAS DISPONÍVEIS\n'
      '[3] CONSULTAR HORÁRIOS DE FUNCIONAMENTO DA SUA LINHA DE METRÔ\n'
      '[0] SAIR\n'
    )

    escolha = input('Digite a opção escolhida: ')

    #verificações da escolha do usuário
    if escolha == '1':
      verificaDeficiente()
    elif escolha == '2':
      verRotas()
    elif escolha == '3':
      consultaHorarios()
    elif escolha == '0':
      print('obrigado pela sua participação, volte sempre!')
      break
    else:
      print('Por favor, digite uma opção válida.')


#função que verifica se o usuário é ou não deficente 
def verificaDeficiente():
  print('Por favor, selecione a opção que melhor descreve sua situação:\n')
  print('[1] você não possui sua visão\n')
  print('[2] seu sistema auditivo é falho ou não funcional\n')
  print('[3] você possui alguma anomalia física (falta de um braço, perna, dedos, etc)\n')
  print('[4] você é diagnosticado com alguma dificuldade intelectual\n')
  print('[5] Não tenho nenhum dos problemas ditos acima\n')
    
  escolha = input('Digite o número da opção desejada (1 a 5): ')
    
    #condicionais para o usuário receber sua resposta
  if escolha in ['1', '2', '3', '4']:
    print('Obrigado por informar. Você se identifica como uma pessoa com deficiência.')
  elif escolha == '5':
    print('Obrigado pela sua participação! Você não se identifica como uma pessoa com deficiência.')
  else:
    print('Opção inválida. Tente novamente.')


#função que verifica as rotas das linhas da ViaMobilidade
def verRotas():
  print('Rotas disponíveis:\n')

  #dicionário que recebe as informações das linhas pré selecionadas
  rotas = {
    'linha 9 - Esmeralda': 'conecta com as estações:\n 4- AMARELA (estação Pinheiros)\n 5- LILÁS (estação Santo Amaro)\n 15- PRATA (estação Osasco e estação Presidente Altino)',
    'linha 8 - Diamante': 'conecta com as estações:\n 3- VERMELHA (estação Palmeiras-Barra Funda)\n 7- Rubi da CPTM (estação Palmeiras-Barra Funda)\n 9- Esmeralda de trens metropolitanos (estações Osasco e Presidente Altino)'
  }
    #loop de repetição que itera uma coleção "rotas"
  for linha in rotas:
    print(f'- {linha}') #para cada linha da coleção "rotas", o programa imprime o nome da linha fornecida

  escolha = input('Digite o nome da linha para mais informações (linha 9 - Esmeralda, linha 8 - Diamante): ') #solicitação do programa para que o usuário digite o nome de uma linha 
                                                                                                              #para obter mais informações ("linha 9 - Esmeralda" e "linha 8 - Diamante")
  #condicional que verifica se o que o usuário 
  # digitou 'escolha' está presente na coleção rotas
  if escolha in rotas:
    print(f'Informações sobre {escolha}: {rotas[escolha]}')
  else:
    print('Linha inválida. Tente novamente.')

#função que consulta os horários de funcionamentos das linhas de metrô da ViaMobilidade
def consultaHorarios():
  print("Bem-vindo ao sistema de consulta de horários da AFI acessibilidades!\n Digite:\n '1' para [LINHA 9 - ESMERALDA]\n '2' para [LINHA 8 - DIAMANTE]")
  #dicionário que recebe informações de abertura e fechamento, 
  # com seus respectivos horários
  horariosMetro = {
    '1': {'Abertura': '05:00am', 'Fechamento': '00:00pm'},
    '2': {'Abertura': '05:30am', 'Fechamento': '01:30am'}
  }
  #função que mostra as linhas de metrô disponíveis
  def mostrarLinhas():
    print("Linhas de Metrô Disponíveis:")

    #loop de repetição que itera sobre as chaves do dicionário e imprime cada uma delas com print()
    for linha in horariosMetro.keys(): #Este método (.keys) retorna uma visão de todas as chaves do dicionário
      print(f"- {linha}")
  mostrarLinhas()

  #solicitação do programa para que o usuário digite qual 
  # linha de metrô ele deseja consultar os horários
  linha = input("Digite o nome da linha de metrô que você deseja consultar: ").strip()
  
  #condicional que verifica se o que o usuário digitou está dentro do dicionário "horariosMetro"
  if linha in horariosMetro:
    horarios = horariosMetro[linha] #se a linha for encontrada, essa linha acessa os horários de funcionamento correspondentes 
                                    #a essa linha no dicionário "horariosMetro"
    #formação dos prints (output's)
    print(f'Horários de Funcionamento da {linha}\n')
    print(f"Abertura: {horarios['Abertura']}\n")
    print(f"Fechamento: {horarios['Fechamento']}\n")
  else:
    print('Linha não encontrada. Por favor, verifique o nome da linha.')
  
menu()