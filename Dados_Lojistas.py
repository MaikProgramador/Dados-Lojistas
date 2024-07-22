import json

dados = {
    "CLIENTES RIO GRANDE DO SUL": [
        {
            "RAZÃO SOCIAL": "SERGIO MAURO LEIVICOFF EIRELI",
            "FANTASIA": "TELESOM PRO-AUDIO",
            "TELEFONE": "(51) 3221-0036",
            "ENDEREÇO": "R CEL VICENTE,420",
            "BAIRRO": "CENTRO",
            "CEP": "90030-040",
            "CIDADE": "PORTO ALEGRE - RS",
            "E-MAIL": "telesomproaudio@hotmail.com",
            "CNPJ": "93.428.654/0003-63"
        },
        {
            "RAZÃO SOCIAL": "RAFAEL DA SILVA PEIXOTO",
            "FANTASIA": "MEGA MUSIC STORE",
            "TELEFONE": "(51) 98641-8259",
            "ENDEREÇO": "R MANOEL M DO NASCIMENTO,269",
            "BAIRRO": "SÃO MIGUEL",
            "CEP": "93025-530",
            "CIDADE": "SÃO LEOPOLDO",
            "E-MAIL": "compras@classicmusicstore.com",
            "CNPJ": "29.106.735/0001-86"
        }
    ],
    "CLIENTES REGIÃO DE CAMPINAS (INTERIOR DE SÃO PAULO)": [
        {
            "RAZÃO SOCIAL": "ÉDSON DA SILVEIRA GERVAZIO SOM E ACESSÓRIO",
            "FANTASIA": "E.N SOM E ACESSORIOS",
            "TELEFONE": "(16) 3625-7028 / (16) 3964-6798 / (16) 3285-1828",
            "ENDEREÇO": "R- MARIANA JUNQUEIRA,195",
            "CEP": "14.015-010",
            "CIDADE": "RIBEIRÃO PRETO",
            "E-MAIL": "egervazio@uol.com.br",
            "CNPJ": "07.833.226/0001-12"
        },
        {
            "RAZÃO SOCIAL": "ANDERSON AFONSO DOS SANTOS – ME",
            "FANTASIA": "VS SOM",
            "TELEFONE": "(17)3324-5623",
            "ENDEREÇO": "AV 7, 1137",
            "BAIRRO": "FORTALEZA",
            "CEP": "14780-240",
            "CIDADE": "BARRETOS SP",
            "E-MAIL": "vssomepecas@hotmail.com",
            "CNPJ": "10.775.621/0001-09"
        }
    ],
    "CLIENTES REGIÃO PRES PRUDENTE (INTERIOR DE SÃO PAULO)": [
        {
            "RAZÃO SOCIAL": "ENTER LIGHT DO BRASIL COM. ELETRONICO",
            "FANTASIA": "ENTER LIGHT",
            "TELEFONE": "(18) 3222-1428",
            "ENDEREÇO": "AV JOAQUIM CONSTANTINO, 3980",
            "BAIRRO": "JARDIM SAO LUIS",
            "CEP": "19061-000",
            "CIDADE": "PRESIDENTE PRUDENTE - SP",
            "E-MAIL": "renato@enterlight.com.br",
            "CNPJ": "17.777.802/0001-05"
        },
        {
            "RAZÃO SOCIAL": "PLUGADOS NA MÚSICA COMERCIO DE INSTRUMENTOS",
            "FANTASIA": "PLUGADOS NA MÚSICA",
            "TELEFONE": "(18) 99632-1217",
            "ENDEREÇO": "R ANITA GARIBALDI, 44",
            "BAIRRO": "CENTRO",
            "CEP": "16010-280",
            "CIDADE": "ARAÇATUBA - SP",
            "E-MAIL": "plugadosata@gmail.com",
            "CNPJ": "34.187.894/0001-92"
        }
    ],
    "CLIENTES REGIÃO DO PARANÁ": [
        {
            "RAZÃO SOCIAL": "COLOMERA E RODRIGUES LTDA",
            "FANTASIA": "COLOMERA",
            "TELEFONE": "(43) 99919-2441",
            "ENDEREÇO": "RUA PREFEITO JOSE DE ASSIS, 113",
            "BAIRRO": "CENTRO",
            "CEP": "88385-000",
            "CIDADE": "PENHA",
            "E-MAIL": "compras@colomeras.com.br",
            "CNPJ": "00.179.569/0004-09"
        },
        {
            "RAZÃO SOCIAL": "OTTENIO RODRIGUES ELETRO ELETRONICOS",
            "FANTASIA": "OTTENIO RODRIGUES ELETRON",
            "TELEFONE": "(43) 99104-1415",
            "ENDEREÇO": "ROD CARLOS J STRASS, 585",
            "BAIRRO": "PARQUE I. ALICANTE",
            "CEP": "86087-350",
            "CIDADE": "LONDRINA",
            "E-MAIL": "oteniofilial@hotmail.com",
            "CNPJ": "35.128.410/0001-05"
        }
    ],
    "CLIENTES REGIÃO DE SANTA CATARINA": [
        {
            "RAZÃO SOCIAL": "A MÚSICAL DE ORLEANS LTDA",
            "FANTASIA": "A MÚSICAL",
            "TELEFONE": "(48) 3466-0750",
            "ENDEREÇO": "RUA JOSE ANTUNES MATOS, 10",
            "BAIRRO": "CENTRO",
            "CEP": "88870-000",
            "CIDADE": "ORLEANS",
            "E-MAIL": "diegomoraes88@gmail.com",
            "CNPJ": "83.730.390/0001-82"
        },
        {
            "RAZÃO SOCIAL": "WE SOL MAIOR COM. E MAN. DE SOM LTDA",
            "FANTASIA": "SOL MAIOR",
            "TELEFONE": "(47) 3326-1798",
            "ENDEREÇO": "R SETE DE SETEMBRO, 2358",
            "BAIRRO": "CENTRO",
            "CEP": "89012-400",
            "CIDADE": "BLUMENAU",
            "E-MAIL": "solmaior.som@terra.com.br",
            "CNPJ": "05.434.887/0001-40"
        }
    ],
    "CLIENTES REGIÃO MATO GROSSO DO SUL": [
        {
            "RAZÃO SOCIAL": "ANATH COMERCIAL LTDA",
            "FANTASIA": "BETEL CENTER",
            "TELEFONE": "(67) 3324-0150",
            "ENDEREÇO": "AV CALOGERAS, 2099",
            "BAIRRO": "CENTRO",
            "CEP": "79002-001",
            "CIDADE": "CAMPO GRANDE",
            "E-MAIL": "adilson@betelcenter.com.br",
            "CNPJ": "12.319.896/0001-55"
        },
        {
            "RAZÃO SOCIAL": "A PRIMOROSA INSTRUMENTOS MUSICAIS EIRELI",
            "FANTASIA": "A PRIMOROSA CG",
            "TELEFONE": "(67) 3325-1922",
            "ENDEREÇO": "R DOS BARBOSAS, 490",
            "BAIRRO": "AMABAI",
            "CEP": "79005-430",
            "CIDADE": "CAMPO GRANDE",
            "E-MAIL": "aprimorosa@terra.com.br",
            "CNPJ": "10.638.725/0001-63"
        }
    ],
    "CLIENTES REGIÃO MATO GROSSO": [
        {
            "RAZÃO SOCIAL": "JAKSON RODRIGUES MACHADO LTDA",
            "FANTASIA": "A MUSICAL",
            "TELEFONE": "(66) 3401-6213",
            "ENDEREÇO": "RUA MATO GROSSO",
            "BAIRRO": "CENTRO",
            "CEP": "78600-023",
            "CIDADE": "BARRA DO GARÇA",
            "E-MAIL": "amusical2000@yahoo.com.br",
            "CNPJ": "03.015.727/0001-30"
        },
        {
            "RAZÃO SOCIAL": "METAL ELETRO LTDA",
            "FANTASIA": "METAL GRADIENTE",
            "TELEFONE": "(65) 3322-9230",
            "ENDEREÇO": "AV: TENENTE-CORONEL DUARTE, 285",
            "BAIRRO": "BANDEIRANTES",
            "CEP": "78015-500",
            "CIDADE": "CUIABA",
            "E-MAIL": "compras.metalgradiente@gmail.com",
            "CNPJ": "00.231.656/0001-15"
        }
    ],
    "CLIENTES REGIÃO RONDONIA": [
        {
            "RAZÃO SOCIAL": "PADRAO 19 COM. VAR. DE INST. MUS. LTDA",
            "FANTASIA": "PADRAO 19 COMERCIO",
            "TELEFONE": "(69) 99397-1715",
            "ENDEREÇO": "AVENIDA PRESIDENTE NASSER, 360",
            "BAIRRO": "JARDIM AMÉRICA",
            "CEP": "76980-764",
            "CIDADE": "VILHENA",
            "E-MAIL": "padrao19vilhena@gmail.com",
            "CNPJ": "35.234.022/0001-09"
        },
        {
            "RAZÃO SOCIAL": "FERREIRA E PASSARELLI INST. MUS. LTDA ME",
            "FANTASIA": "INFOMUSIC",
            "TELEFONE": "(69) 3536-1559",
            "ENDEREÇO": "AV JAMARI, 3278 SETOR 1",
            "BAIRRO": "AREAS E. 01",
            "CEP": "76870-018",
            "CIDADE": "ARIQUEMES",
            "E-MAIL": "infomusiccompras@gmail.com",
            "CNPJ": "28.374.729/0002-28"
        },
        ],
    "CLIENTES REGIÃO PARANA": [
        {
            "Razão Social": "LOJA ROSARIO BRAGANCA LTDA",
            "Fantasia": "LOJA ROSARIO",
            "Telefone": "(91) 98111-5399",
            "Endereço": "AV NAZARENO FERREIRA, 620",
            "Bairro": "CENTRO",
            "CEP": "68600-000",
            "Cidade": "BRAGANÇA",
            "Email": "lojarosariobraganca@gmail.com",
            "CNPJ": "48.448.687/0001-59"
        },
        {
            "Razão Social": "KSB ELETRONICA LTDA",
            "Fantasia": "TIP ELETRONICA",
            "Telefone": "(91) 3212-4341",
            "Endereço": "R TREZE DE MAIO, 386",
            "Bairro": "CAMPINA",
            "CEP": "66013-080",
            "Cidade": "BALEM",
            "Email": "andre@􀆟peletronica.com.br",
            "CNPJ": "05.452.754/0001-04"
        }
    ],
    "Clientes Região Goiânia": [
        {
            "Razão Social": "BORGES & CARRER LTDA",
            "Fantasia": "MERCADÃO DA ELETRONICA",
            "Telefone": "(64) 3621-2700",
            "Endereço": "AV PRES VARGAS, 1200",
            "Bairro": "SETOR CENTRAL",
            "CEP": "",
            "Cidade": "RIO VERDE",
            "Email": "alemercadao@gmail.com",
            "CNPJ": "03.404.245/0001-72"
        },
        {
            "Razão Social": "FUJIMUSIC COM CDS E INST MUSICAIS LTDA",
            "Fantasia": "FUJIMUSIC",
            "Telefone": "(62) 3588-5608",
            "Endereço": "AV DA IGUALDADE, QUADRA, 119 04 SALA 02",
            "Bairro": "SETOR GARAVELO",
            "CEP": "74930-530",
            "Cidade": "APARECIDA DE GOIANIA",
            "Email": "fujimusic@hotmail.com",
            "CNPJ": "05.314.292/0001-50"
        }
    ],
    "Clientes Região Distrito Federal": [
        {
            "Razão Social": "KATIA DOS SANTOS SILVA INST. MUSICAIS",
            "Fantasia": "VITRINI DO AUDIO",
            "Telefone": "(61) 3022-2822",
            "Endereço": "SIA TRECHO 5 EDIFÍCIO VIA IMPORT LOJA 120",
            "Bairro": "ZONA INDUSTRIAL",
            "CEP": "71205-050",
            "Cidade": "GUARA",
            "Email": "vitrinedoaudio@hotmail.com",
            "CNPJ": "25.111.619/0001-02"
        },
        {
            "Razão Social": "CENTRO ELETRICO GAMA EIRELI",
            "Fantasia": "ELETRO GAMA",
            "Telefone": "(61) 3022-4017",
            "Endereço": "Q QUADRA 13, 09",
            "Bairro": "SETOR CENTRAL",
            "CEP": "72405-130",
            "Cidade": "GAMA",
            "Email": "gamaeletron13@outlook.com",
            "CNPJ": "24.639.272/0001-02"
        }
    ],
    "Clientes Região Interior Bahia": [
        {
            "Razão Social": "ESS SONORIZACAO E EMPRENDIMENTOS EIRELI",
            "Fantasia": "MIDIA SOM A LOJA DO POVO",
            "Telefone": "(75) 3261-1944",
            "Endereço": "AV DEP MANOEL NOVAES, 549",
            "Bairro": "CENTRO",
            "CEP": "48700-000",
            "Cidade": "SERRINHA - BA",
            "Email": "midiasomalojadopovo@gmail.com",
            "CNPJ": "06.289.385/0001-35"
        },
        {
            "Razão Social": "SILVANA TEODORO RAMOS - ME",
            "Fantasia": "S/N",
            "Telefone": "(75) 3641-5615",
            "Endereço": "TRAVESSA SILVA JARDIM, 20",
            "Bairro": "CENTRO",
            "CEP": "45400-000",
            "Cidade": "VALENÇA",
            "Email": "tudoemeletronica@live.com",
            "CNPJ": "13.845.232/0001-92"
        },
        {
            "Razão Social": "R. DA ROCHA CAMPOS - ME",
            "Fantasia": "ELETRONICA BRILHA SOM",
            "Telefone": "(75) 3626-8708",
            "Endereço": "R JOSE JOAQUIM SEABRA,175",
            "Bairro": "CENTRO",
            "CEP": "44002-000",
            "Cidade": "FEIRA DE SANTANA",
            "Email": "canutobrilhasom@gmail.com",
            "CNPJ": "13.529.807/0001-68"
        }
    ],
    "Cliente Região Salvador Capital": [
        {
            "Razão Social": "ELIVALDO COSTA CERQUEIRA",
            "Fantasia": "LD ELETRONICA",
            "Telefone": "(71) 98861-7129",
            "Endereço": "LD DA PRAÇA, 04",
            "Bairro": "CENTRO HISTORICO",
            "CEP": "40026-058",
            "Cidade": "SALVADOR",
            "Email": "costaelivaldo009@gmail.com",
            "CNPJ": "54.744.334/0001-07"
        },
        {
            "Razão Social": "JML COMERCIO DE AUDIO E ILUMINACAO EIREL",
            "Fantasia": "JR ELETRONICA",
            "Telefone": "(71) 3321-7252",
            "Endereço": "R JOSE GONCALVES / EDF CHURCHILL LOJA C, 45",
            "Bairro": "CENTRO",
            "CEP": "40026-068",
            "Cidade": "SALVADOR",
            "Email": "jreletronica2012@hotmail.com",
            "CNPJ": "15.630.735/0001-76"
        }
    ],
    "Região Espírito Santo": [
        {
            "Razão Social": "NOVA ALIANCA COMERCIO ELETRONICO LTDA",
            "Fantasia": "LOJA NOVA ALIANCA",
            "Telefone": "(32) 98827-9402",
            "Endereço": "RUA OSWALDO CRUZ, 27",
            "Bairro": "BARRA",
            "CEP": "36884-020",
            "Cidade": "MURIAÉ",
            "Email": "lojaalianca83@gmail.com",
            "CNPJ": "33.011.598/0001-73"
        },
        {
            "Razão Social": "ANDERSON DOS SANTOS COUTINHO",
            "Fantasia": "S/N",
            "Telefone": "(27) 99697-6738",
            "Endereço": "R JOSE B DA SILVA, 93",
            "Bairro": "CAMPO GRANDE",
            "CEP": "29146-120",
            "Cidade": "CARIACICA",
            "Email": "teclas1000@hotmail.com",
            "CNPJ": "30.072.035/0001-05"
        }
    ],
    "Clientes Região Maranhão": [
        {
            "Razão Social": "FERNANDO AUGUSTO CARNEIRO LIRA - ME",
            "Fantasia": "DIGITAL SOM",
            "Telefone": "(85) 3226-3070",
            "Endereço": "R PEDRO PEREIRA, 593",
            "Bairro": "CENTRO",
            "CEP": "60035-000",
            "Cidade": "FORTALEZA",
            "Email": "digitalsom_123@hotmail.com",
            "CNPJ": "69.354.694/0001-61"
        },
        {
            "Razão Social": "GIRLANA MEDEIROS COSTA TORRES - ME",
            "Fantasia": "FENIX ELETRONICA",
            "Telefone": "(85) 3371-2802",
            "Endereço": "R JOAO DE ALENCAR, 45",
            "Bairro": "CENTRO",
            "CEP": "61900-150",
            "Cidade": "MARACANAU",
            "Email": "girlanamedeiros@hotmail.com",
            "CNPJ": "08.978.825/0001-97"
        },
        {
            "Razão Social": "ELETRONICA CENTRAL MUSIC EIRELI ME",
            "Fantasia": "PUTIU CENTRAL MUSIC",
            "Telefone": "(85) 3023-5305",
            "Endereço": "R PEDRO PEREIRA, 614",
            "Bairro": "CENTRO",
            "CEP": "60035-000",
            "Cidade": "FORTALEZA",
            "Email": ["centralmusic@outlook.com.br", "eletronicacentral.real@hotmail.com"],
            "CNPJ": "60035-000"
        }
    ],
    "Cliente Região Pernambuco": [
        {
            "Razão Social": "VANUZA DIAS ARRUDA OLIVEIRA - ME",
            "Fantasia": "S/N",
            "Telefone": "(81) 3722-2524",
            "Endereço": "R JOAO CONDE, 62",
            "Bairro": "NOSSA S. DAS DORES",
            "CEP": "55004-220",
            "Cidade": "CARUARU",
            "Email": "eletronicademetrius@hotmail.com",
            "CNPJ": "18.940.877/0001-28"
        },
        {
            "Razão Social": "MIX MUSIC LTDA - EPP",
            "Fantasia": "MIX MUSIC",
            "Telefone": "(81) 3224-3925",
            "Endereço": "R DA CONCORDIA, 289",
            "Bairro": "SÃO JOSE",
            "CEP": "50020-050",
            "Cidade": "RECIFE",
            "Email": ["financeiro@mixmusicstore.com.br", "lojamixassistencia@hotmail.com", "renan@casadostransformadores.com.br"],
            "CNPJ": "10.526.700/0001-78"
        }
    ],
    "Região Interior de São Paulo": [
        {
            "Razão Social": "M.F. PASSARINHO ARTIGOS ELETRONICOS",
            "Fantasia": "PIU SHOP",
            "Telefone": ["(14) 3737-0919", "(14) 98129-6065"],
            "Endereço": "R: ANTENOR LARA CAMPOS, 175",
            "Bairro": "CASCATA",
            "CEP": "17400-136",
            "Cidade": "GARÇA - SP",
            "Email": "comercial@piushop.com.br",
            "CNPJ": "13.206.514/0001-40"
        },
        ],
    "CLIENTES RIO GRANDE DO SUL": [
         {
            "Razão Social": "SERGIO MAURO LEIVICOFF EIRELI",
            "Fantasia": "TELESOM PRO-AUDIO",
            "Telefone": "(51) 3221-0036",
            "Endereço": "R CEL VICENTE,420",
            "Bairro": "CENTRO",
            "CEP": "90030-040",
            "Cidade": "PORTO ALEGRE - RS",
            "E-mail": "telesomproaudio@hotmail.com",
            "CNPJ": "93.428.654/0003-63"
        },
        {
            "Razão Social": "RAFAEL DA SILVA PEIXOTO",
            "Fantasia": "MEGA MUSIC STORE",
            "Telefone": "(51) 98641-8259",
            "Endereço": "R MANOEL M DO NASCIMENTO,269",
            "Bairro": "SÃO MIGUEL",
            "CEP": "93025-530",
            "Cidade": "SÃO LEOPOLDO",
            "E-mail": "compras@classicmusicstore.com",
            "CNPJ": "29.106.735/0001-86"
        }
    ],
    "Clientes Região de Campinas (Interior de São Paulo)": [
        {
            "Razão Social": "ÉDSON DA SILVEIRA GERVAZIO SOM E ACESSÓRIO",
            "Fantasia": "E.N SOM E ACESSORIOS",
            "Telefone": "(16) 3625-7028 / (16) 3964-6798 / (16) 3285-1828",
            "Endereço": "R- MARIANA JUNQUEIRA,195",
            "CEP": "14.015-010",
            "Cidade": "RIBEIRÃO PRETO",
            "E-mail": "egervazio@uol.com.br",
            "CNPJ": "07.833.226/0001-12"
        },
        {
            "Razão Social": "ANDERSON AFONSO DOS SANTOS – ME",
            "Fantasia": "VS SOM",
            "Telefone": "(17)3324-5623",
            "Endereço": "AV 7, 1137",
            "Bairro": "FORTALEZA",
            "CEP": "14780-240",
            "Cidade": "BARRETOS SP",
            "E-mail": "vssomepecas@hotmail.com",
            "CNPJ": "10.775.621/0001-09"
        }
    ],
    "Clientes Região Presidente Prudente (Interior de São Paulo)": [
        {
            "Razão Social": "ENTER LIGHT DO BRASIL COM. ELETRONICO",
            "Fantasia": "ENTER LIGHT",
            "Telefone": "(18) 3222-1428",
            "Endereço": "AV JOAQUIM CONSTANTINO, 3980",
            "Bairro": "JARDIM SAO LUIS",
            "CEP": "19061-000",
            "Cidade": "PRESIDENTE PRUDENTE - SP",
            "E-mail": "renato@enterlight.com.br",
            "CNPJ": "17.777.802/0001-05"
        },
        {
            "Razão Social": "PLUGADOS NA MÚSICA COMERCIO DE INSTRUMENTOS",
            "Fantasia": "PLUGADOS NA MÚSICA",
            "Telefone": "(18) 99632-1217",
            "Endereço": "R ANITA GARIBALDI, 44",
            "Bairro": "CENTRO",
            "CEP": "16010-280",
            "Cidade": "ARAÇATUBA -SP",
            "E-mail": "plugadosata@gmail.com",
            "CNPJ": "34.187.894/0001-92"
        }
    ],
    "Clientes Região do Paraná": [
        {
            "Razão Social": "COLOMERA E RODRIGUES LTDA",
            "Fantasia": "COLOMERA",
            "Telefone": "(43) 99919-2441",
            "Endereço": "RUA PREFEITO JOSE DE ASSIS, 113",
            "Bairro": "CENTRO",
            "CEP": "88385-000",
            "Cidade": "PENHA",
            "E-mail": "compras@colomeras.com.br",
            "CNPJ": "00.179.569/0004-09"
        },
        {
            "Razão Social": "OTTENIO RODRIGUES ELETRO ELETRONICOS",
            "Fantasia": "OTTENIO RODRIGUES ELETRON",
            "Telefone": "(43) 99104-1415",
            "Endereço": "ROD CARLOS J STRASS, 585",
            "Bairro": "PARQUE I. ALICANTE",
            "CEP": "86087-350",
            "Cidade": "LONDRINA",
            "E-mail": "oteniomusic@gmail.com",
            "CNPJ": "35.128.410/0001-05"
        }
    ],
    "Clientes Região Santa Catarina": [
        {
            "Razão Social": "A MÚSICAL DE ORLEANS LTDA",
            "Fantasia": "A MÚSICAL",
            "Telefone": "(48) 3466-0750",
            "Endereço": "RUA JOSE ANTUNES MATOS, 10",
            "Bairro": "CENTRO",
            "CEP": "88870-000",
            "Cidade": "ORLEANS",
            "E-mail": "diegomoraes88@gmail.com",
            "CNPJ": "83.730.390/0001-82"
        },
        {
            "Razão Social": "WE SOL MAIOR COM. E MAN. DE SOM LTDA",
            "Fantasia": "SOL MAIOR",
            "Telefone": "(47) 3326-1798",
            "Endereço": "R SETE DE SETEMBRO, 2358",
            "Bairro": "CENTRO",
            "CEP": "89012-400",
            "Cidade": "BLUMENAU",
            "E-mail": "solmaior.som@terra.com.br",
            "CNPJ": "05.434.887/0001-40"
        }
    ],
    "Clientes Região Mato Grosso do Sul": [
        {
            "Razão Social": "ANATH COMERCIAL LTDA",
            "Fantasia": "BETEL CENTER",
            "Telefone": "(67) 3324-0150",
            "Endereço": "AV CALOGERAS, 2099",
            "Bairro": "CENTRO",
            "CEP": "79002-001",
            "Cidade": "CAMPO GRANDE",
            "E-mail": "adilson@betelcenter.com.br",
            "CNPJ": "12.319.896/0001-55"
        },
        {
            "Razão Social": "A PRIMOROSA INSTRUMENTOS MUSICAIS EIRELI",
            "Fantasia": "A PRIMOROSA CG",
            "Telefone": "(67) 3325-1922",
            "Endereço": "R DOS BARBOSAS, 490",
            "Bairro": "AMABAI",
            "CEP": "79005-430",
            "Cidade": "CAMPO GRANDE",
            "E-mail": "aprimorosa@terra.com.br",
            "CNPJ": "10.638.725/0001-63"
        }
    ],
    "Clientes Região Mato Grosso": [
        {
            "Razão Social": "JAKSON RODRIGUES MACHADO LTDA",
            "Fantasia": "A MUSICAL",
            "Telefone": "(66) 3401-6213",
            "Endereço": "RUA MATO GROSSO",
            "Bairro": "CENTRO",
            "CEP": "78600-023",
            "Cidade": "BARRA DO GARÇA",
            "E-mail": "amusical2000@yahoo.com.br",
            "CNPJ": "03.015.727/0001-30"
        },
        {
            "Razão Social": "METAL ELETRO LTDA",
            "Fantasia": "METAL GRADIENTE",
            "Telefone": "(65) 3322-9230",
            "Endereço": "AV: TENENTE-CORONEL DUARTE, 285",
            "Bairro": "BANDEIRANTES",
            "CEP": "78015-500",
            "Cidade": "CUIABA",
            "E-mail": "compras.metalgradiente@gmail.com",
            "CNPJ": "00.231.656/0001-15"
        }
    ],
    "Clientes Região Rondônia": [
        {
            "Razão Social": "PADRAO 19 COM. VAR. DE INST. MUS. LTDA",
            "Fantasia": "PADRAO 19 COMERCIO",
            "Telefone": "(69) 99397-1715",
            "Endereço": "AVENIDA PRESIDENTE NASSER, 360",
            "Bairro": "JARDIM AMÉRICA",
            "CEP": "76820-000",
            "Cidade": "PORTO VELHO",
            "E-mail": "padraonineteen@uol.com.br",
            "CNPJ": "23.757.550/0001-02"
        },
        {
            "Razão Social": "ARALAPTO INSTRUMENTOS MUSICAIS LTDA",
            "Fantasia": "ARALAPTO MUSICAIS",
            "Telefone": "(69) 99222-8777",
            "Endereço": "RUA RIO DE JANEIRO, 721",
            "Bairro": "CENTRO",
            "CEP": "76801-209",
            "Cidade": "PORTO VELHO",
            "E-mail": "aralapto.instruments@outlook.com",
            "CNPJ": "21.126.895/0001-20"
        }
    ],
    "Clientes Região Goiás": [
        {
            "Razão Social": "CAMPOS & ALMEIDA LTDA",
            "Fantasia": "ALMEIDA SOM",
            "Telefone": "(62) 3245-0302",
            "Endereço": "RUA 17, 475",
            "Bairro": "SETOR CENTRAL",
            "CEP": "74000-000",
            "Cidade": "GOIANIA",
            "E-mail": "camposalmeida@uol.com.br",
            "CNPJ": "03.440.328/0001-24"
        },
        {
            "Razão Social": "DRUM SHOP COM. LTDA",
            "Fantasia": "DRUM SHOP",
            "Telefone": "(62) 3298-2718",
            "Endereço": "AV DA IGUALDADE, 120",
            "Bairro": "SETOR NOVO HORIZONTE",
            "CEP": "74310-260",
            "Cidade": "GOIANIA",
            "E-mail": "drumshop@gmail.com",
            "CNPJ": "04.597.558/0001-47"
        }
    ],
    "Clientes Região Pará": [
        {
            "Razão Social": "LOJA ROSARIO BRAGANCA LTDA",
            "Fantasia": "LOJA ROSARIO",
            "Telefone": "(91) 98111-5399",
            "Endereço": "AV NAZARENO FERREIRA, 620",
            "Bairro": "CENTRO",
            "CEP": "68600-000",
            "Cidade": "BRAGANÇA",
            "E-mail": "lojarosariobraganca@gmail.com",
            "CNPJ": "48.448.687/0001-59"
        },
        {
            "Razão Social": "KSB ELETRONICA LTDA",
            "Fantasia": "TIP ELETRONICA",
            "Telefone": "(91) 3212-4341",
            "Endereço": "R TREZE DE MAIO, 386",
            "Bairro": "CAMPINA",
            "CEP": "66013-080",
            "Cidade": "BALEM",
            "E-mail": "andre@tipeletronica.com.br",
            "CNPJ": "05.452.754/0001-04"
        }
    ],
    "Clientes Região Goiânia": [
        {
            "Razão Social": "BORGES & CARRER LTDA",
            "Fantasia": "MERCADÃO DA ELETRONICA",
            "Telefone": "(64) 3621-2700",
            "Endereço": "AV PRES VARGAS, 1200",
            "Bairro": "SETOR CENTRAL",
            "CEP": "75901-002",
            "Cidade": "RIO VERDE",
            "E-mail": "alemercadao@gmail.com",
            "CNPJ": "03.404.245/0001-72"
        },
        {
            "Razão Social": "FUJIMUSIC COM CDS E INST MUSICAIS LTDA",
            "Fantasia": "FUJIMUSIC",
            "Telefone": "(62) 3588-5608",
            "Endereço": "AV DA IGUALDADE, QUADRA, 119 04 SALA 02",
            "Bairro": "SETOR GARAVELO",
            "CEP": "74930-530",
            "Cidade": "APARECIDA DE GOIANIA",
            "E-mail": "fujimusic@hotmail.com",
            "CNPJ": "05.314.292/0001-50"
        }
    ],
    "Clientes Região Distrito Federal": [
        {
            "Razão Social": "KATIA DOS SANTOS SILVA INST. MUSICAIS",
            "Fantasia": "VITRINI DO AUDIO",
            "Telefone": "(61) 3022-2822",
            "Endereço": "SIA TRECHO 5 EDIFÍCIO VIA IMPORT LOJA 120",
            "Bairro": "ZONA INDUSTRIAL",
            "CEP": "71205-050",
            "Cidade": "GUARA",
            "E-mail": "vitrinedoaudio@hotmail.com",
            "CNPJ": "25.111.619/0001-02"
        },
        {
            "Razão Social": "CENTRO ELETRICO GAMA EIRELI",
            "Fantasia": "ELETRO GAMA",
            "Telefone": "(61) 3022-4017",
            "Endereço": "Q QUADRA 13, 09",
            "Bairro": "SETOR CENTRAL",
            "CEP": "72405-130",
            "Cidade": "GAMA",
            "E-mail": "gamaeletron13@outlook.com",
            "CNPJ": "24.639.272/0001-02"
        }
    ],
    "Clientes Região Interior Bahia": [
        {
            "Razão Social": "ESS SONORIZACAO E EMPRENDIMENTOS EIRELI",
            "Fantasia": "MIDIA SOM A LOJA DO POVO",
            "Telefone": "(75) 3261-1944",
            "Endereço": "AV DEP MANOEL NOVAES, 549",
            "Bairro": "CENTRO",
            "CEP": "48700-000",
            "Cidade": "SERRINHA - BA",
            "E-mail": "midiasomalojadopovo@gmail.com",
            "CNPJ": "06.289.385/0001-35"
        },
        {
            "Razão Social": "SILVANA TEODORO RAMOS - ME",
            "Fantasia": "S/N",
            "Telefone": "(75) 3641-5615",
            "Endereço": "TRAVESSA SILVA JARDIM, 20",
            "Bairro": "CENTRO",
            "CEP": "45400-000",
            "Cidade": "VALENÇA",
            "E-mail": "tudoemeletronica@live.com",
            "CNPJ": "13.845.232/0001-92"
        },
        {
            "Razão Social": "R. DA ROCHA CAMPOS - ME",
            "Fantasia": "ELETRONICA BRILHA SOM",
            "Telefone": "(75) 3626-8708",
            "Endereço": "R JOSE JOAQUIM SEABRA,175",
            "Bairro": "CENTRO",
            "CEP": "44002-000",
            "Cidade": "FEIRA DE SANTANA",
            "E-mail": "canutobrilhasom@gmail.com",
            "CNPJ": "13.529.807/0001-68"
        }
    ],
    "Clientes Região Salvador Capital": [
        {
            "Razão Social": "ELIVALDO COSTA CERQUEIRA",
            "Fantasia": "LD ELETRONICA",
            "Telefone": "(71) 98861-7129",
            "Endereço": "LD DA PRAÇA, 04",
            "Bairro": "CENTRO HISTORICO",
            "CEP": "40026-058",
            "Cidade": "SALVADOR",
            "E-mail": "costaelivaldo009@gmail.com",
            "CNPJ": "54.744.334/0001-07"
        },
        {
            "Razão Social": "JML COMERCIO DE AUDIO E ILUMINACAO EIREL",
            "Fantasia": "JR ELETRONICA",
            "Telefone": "(71) 3321-7252",
            "Endereço": "R JOSE GONCALVES / EDF CHURCHILL LOJA C, 45",
            "Bairro": "CENTRO",
            "CEP": "40026-068",
            "Cidade": "SALVADOR",
            "E-mail": "jreletronica2012@hotmail.com",
            "CNPJ": "15.630.735/0001-76"
        }
    ],
    "Clientes Região Espírito Santo": [
        {
            "Razão Social": "NOVA ALIANCA COMERCIO ELETRONICO LTDA",
            "Fantasia": "LOJA NOVA ALIANCA",
            "Telefone": "(32) 98827-9402",
            "Endereço": "RUA OSWALDO CRUZ, 27",
            "Bairro": "BARRA",
            "CEP": "36884-020",
            "Cidade": "MURIAÉ",
            "E-mail": "lojaalianca@novaaliança.com.br",
            "CNPJ": "39.447.118/0001-05"
        }
    ],
    "Clientes Região São Paulo": [
        {
            "Razão Social": "MICRO SHOPPING ELETRONICA LTDA - EPP",
            "Fantasia": "MICRO SHOPPING",
            "Telefone": "(11) 2443-0068",
            "Endereço": "R SETE DE SETEMBRO, 277",
            "Bairro": "CENTRO",
            "CEP": "07011-020",
            "Cidade": "GUARULHOS",
            "E-mail": "financeiro@micromusical.com.br / financeiro@micromusical.com.br / comercial@micromusical.com.br",
            "CNPJ": "54.762.737/0001-70"
        },
        {
            "Razão Social": "PRO MUSIC & SOUND COM DE EQUIP DE SOM",
            "Fantasia": "PRO MUSIC",
            "Telefone": "(11) 2229-6935 / (11)98325-8331",
            "Endereço": "R PE CELESTINO, 130",
            "Bairro": "CENTRO",
            "CEP": "07013-100",
            "Cidade": "GUARULHOS",
            "E-mail": "promusic821@gmail.com",
            "CNPJ": "03.837.179/0001-24"
        },
        {
            "Razão Social": "MP STORE COMERCIAL LTDA",
            "Fantasia": "MP STORE",
            "Telefone": "(11) 97055-1818",
            "Endereço": "R MARCELO MULLER, 413",
            "Bairro": "JARDIM INDEPENDENCIA",
            "CEP": "03223-060",
            "Cidade": "SÃO PAULO",
            "E-mail": "compras1@procomputer.com.br / jnascimento@procomputer.com.br",
            "CNPJ": "53.621.340/0001-04"
        },
        {
            "Razão Social": "MC MUSIC COMERCIO E DISTRIBUICAO LTDA",
            "Fantasia": "MC MUSIC",
            "Telefone": "(11) 99236-3031",
            "Endereço": "RUA DOS FLOX, 1419",
            "Bairro": "PORTAIS (POLVILHO)",
            "CEP": "07791-030",
            "Cidade": "CAJAMAR",
            "E-mail": "vendas.homefamily@gmail.com / financeiro@mcmusicstore.com.br",
            "CNPJ": "53.899.262/0001-04"
        },
        {
            "Razão Social": "",
            "Fantasia": "LIQUIDA MEGA STORE",
            "Telefone": "(11) 94984-3948 / (11) 99725-0116",
            "Endereço": "R VICENTE R DA SILVA, 475",
            "Bairro": "PIRATININGA",
            "CEP": "06230-094",
            "Cidade": "OSASCO",
            "E-mail": "financeiroliquidamegastore@gmail.com / jonatasfontes@msn.com",
            "CNPJ": "38.312.979/0001-06"
        },
        {
            "Razão Social": "RCK AUDIO LTDA",
            "Fantasia": "RCK AUDIO & ENTERTAINMENT",
            "Telefone": "(11) 97625-7606",
            "Endereço": "R SEVERA,466",
            "Bairro": "VILA M. BAIXA",
            "CEP": "02111-000",
            "Cidade": "SÃO PAULO",
            "E-mail": "rckaudio@icloud.com / atendimento@rckaudio.com.br",
            "CNPJ": "19.731.313/0001-48"
        }
    ],
    "Clientes Região Rio de Janeiro": [
        {
            "Razão Social": "PENIEL COMERCIO DE INST. MUSICAIS LTDA",
            "Fantasia": "PENIEL INSTRUMENTOS",
            "Telefone": "(21) 2671-0208 / (21) 3842-6114 / (21) 3842-3266",
            "Endereço": "AVENIDA PRESIDENTE VARGAS, 63",
            "Bairro": "CENTRO",
            "CEP": "25070-330",
            "Cidade": "DUQUE DE CAXIAS",
            "E-mail": "penieladm@hotmail.com / penieladm@hotmail.com / elmpeniel@gmail.com",
            "CNPJ": "12.669.096/0001-64"
        },
        {
            "Razão Social": "PLEISHOW INSTRUMENTOS MUSICAIS LTDA",
            "Fantasia": "PLEIDISCO",
            "Telefone": "(21) 2671-7662",
            "Endereço": "R MARIANO SENDRA DOS SANTOS, 01 COMPL/ SL 26,27,28,29,30 QD 1 LJ BD 71 E 73",
            "Bairro": "CENTRO",
            "CEP": "25010-080",
            "Cidade": "DUQUE DE CAXIAS",
            "E-mail": "pleiidisco@terra.com.br",
            "CNPJ": "05.660.464/0001-48"
        }
    ]
}

# Salvando os dados em um arquivo JSON
with open('clientes.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("Dados salvos em clientes.json")
print(dados)