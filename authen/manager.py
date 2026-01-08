from django.contrib.auth.models import BaseUserManager
class UserManeger(BaseUserManager):
    def create_user(self, phone_number,email, password=None, **extra_field):
        if not phone_number:
            raise ValueError("Phone number is needed")
            
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_field)
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self, phone_number,email, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_active', True)
        extra_field.setdefault('is_superuser', True)
    
        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_field.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone_number, email,password, **extra_field)
   