from django.contrib.auth.models import BaseUserManager

#Para criar um usuario usando o padrão do django você preciso sobrescrever dois metodos, 
# o que o django faz quando você cria um user e um superuser 

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, cpf=None, **extra_fields): #extra é para todos os campoas que não estão aqui mas posso querer adicionar
        if None in (email, password, cpf): # se não tiver email senha e cpf...
            raise ValueError("Campo: e-mail, senha e/ou CPF não informados") # da problema 
        
        email_ok = self.normalize_email(email)

        extra_fields.setdefault("is_active", True) #se alguem na hora de cadastrar não passar a informação se vai ficar ativo ou não vai sim automatico
        #prepara para salvar no banco (construção do objeto)
        user = self.model(email=email_ok, cpf=cpf, **extra_fields)

        #seta a senha e acriptografia
        user.set_password(password)

        #salva no banco
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email, password=None, cpf=None, **extra_fields):
        #usuario podera acessar a tela admin do django
        extra_fields.setdefault("is_staff", True)

        # seta no banco de dados do django a propiedade super user para este usuario
        extra_fields.setdefault("is_superuser", True)


        #chama o metodo padrao de criação de usuario
        return self.create_user(email,password,cpf,**extra_fields)