from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

LEVEL_CHOICES = [
    ('Fundamental', 'Fundamental'),
    ('Fundamental e Médio', 'Fundamental e Médio'),
    ('Médio', 'Médio'),
    ('Superior', 'Superior'),
]

GOVERNACE_CHOICES = [
    ('Municipal', 'Municipal'),
    ('Estadual', 'Estadual'),
    ('Federal', 'Federal'),
    ('Particular', 'Particular'),
]

REGIONAL_CHOICES = [
    ('1ª Regional - João Pessoa', '1ª Regional - João Pessoa'),
    ('2ª Regional - Guarabira', '2ª Regional - Guarabira'),
    ('3ª Regional - Campina Grande', '3ª Regional - Campina Grande'),
    ('4ª Regional - Cuité', '4ª Regional - Cuité'),
    ('5ª Regional - Monteiro', '5ª Regional - Monteiro'),
    ('6ª Regional - Patos', '6ª Regional - Patos'),
    ('7ª Regional - Itaporanga', '7ª Regional - Itaporanga'),
    ('8ª Regional - Catolé do Rocha', '8ª Regional - Catolé do Rocha'),
    ('9ª Regional - Cajazeiras', '9ª Regional - Cajazeiras'),
    ('10ª Regional - Sousa', '10ª Regional - Sousa'),
    ('11ª Regional - Princesa Isabel', '11ª Regional - Princesa Isabel'),
    ('12ª Regional - Itabaiana', '12ª Regional - Itabaiana'),
    ('13ª Regional - Pombal', '13ª Regional - Pombal'),
    ('14ª Regional - Mamanguape', '14ª Regional - Mamanguape'),
]


class School(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)
    regional = models.CharField('Regional', max_length=40, choices=REGIONAL_CHOICES)
    level = models.CharField('Nível', max_length=20, choices=LEVEL_CHOICES)
    governance = models.CharField('Gestão', max_length=20, choices=GOVERNACE_CHOICES)
    location = models.PointField('Localização', srid=4326)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=False)

    def __str__(self) -> str:
        return self.name
    
    def get_school_first_name(self):
        return self.name.split()[0]
    

""" 1ª Regional - João Pessoa

Endereço: Rua Coronel Benevenuto Gonçalves da Costa, S/N – Mangabeira VI / 58056-020
Fone/Fax: (83) 98654.3110                                      E-mail:  1gre.gerencia2@gmail.com

 

2ª Regional - Guarabira

Endereço: Rua Dr. Sales, 30 – Centro / 58200-000
Fone/Fax: (83) 99127-4397                       E-mail: 2gregba3@gmail.com

 

3ª Regional - Campina Grande

Endereço: Rua José Marques Ferreira, s/n - Malvinas 
Contato / WhatsApp (83) 9 8654-3108            E-mail: 3gre@see.pb.gov.br

 

4ª Regional - Cuité

Endereço: Rua José Cassimiro Dantas, 643 – B. Novo Retiro / 58175-000
Fone/Fax: (83) 3372-2358                         E-mail: 4grec.cuite@gmail.com

 

5ª Regional - Monteiro

Endereço: Rua Poeta Pinto do Monteiro, 80 – Quinta da Bela Vista / CEP: 58550000
Fone/Fax: (83) 3351-2175

 

6ª Regional - Patos

Endereço: Rua Escritor Rui Barbosa, 614 – Centro / 58700 - 060
E-mail: sextagre@hotmail.com

 

7ª Regional - Itaporanga

Endereço: Rua Manoel Moreira Dantas, 26 – Centro / 58780-000

Maria do Carmo : (83)99929-9074          Ricardo Vieira: (83)99977-5663

Email: mariadocarmo@see.pb.gov.br / 7gre@see.pb.gov.br / ferreira@see.pb.gov.br

 

8ª Regional - Catolé do Rocha

Endereço: Rua Manoel Alves Maia, 94 – Centro / 58884-000
Fone: (83) 3441-1285                            Email: nayarakm@see.pb.gov.br

 

9ª Regional - Cajazeiras

Endereço: Rua Padre Rolim, 156 – Centro / 58900-000
Fone: (83) 3531-7010 / 7189                   E-mail: nonagerenciapb@gmail.com  /  valerio.silva@see.pb.gov.br

 

10ª Regional - Sousa

Endereço: Rua Deputado José de Paiva Gadelha, 123 – B. Areias / 58801-620
Fone: (83) 98654-3175 / E-mail: decimagerencia2019@gmail.com

 

11ª Regional - Princesa Isabel

Endereço: Francisco Wanderley, s/n – Centro / 58755-000
Fone: 3457-2401 / 9 9367-1958          E-mail: 11gre@see.pb.gov.br 

 

12ª Regional - Itabaiana

Endereço: Av. Pres. Epitácio Pessoa, 347 – Centro / 58360-000
Fone: (83) 3281-3502/ 2504 / E-mail da GRE: 12gre@see.pb.gov.br / E-mail da Gerente: fabiana.figueiredo@see.pb.gov.br

 

13ª Regional - Pombal

Endereço: Padre Amâncio Leite, N 45 – Centro / 58840000
Fone: (83) 3431-3803                           E-mail: 13gerenciaregional@gmail.com

 

14ª Regional - Mamanguape

Endereço: Av. Sen. Rui Carneiro, 169 – Centro / 58280-000
Fone: (83) 3292-4804                          E-mail - 14gre.mamanguape@gmail.com """