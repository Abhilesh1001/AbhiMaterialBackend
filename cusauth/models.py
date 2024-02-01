from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None):
        """
        Creates and saves a regular user with the given email, name, tc, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name, tc, and password.
        """
        user = self.create_user(
            email=email,
            name=name,
            tc=tc,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255, 
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "tc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Check if the user has a specific permission.
        """
        # Superusers have all permissions
        return self.is_admin or self.user_permissions.filter(codename=perm).exists()

    def has_module_perms(self, app_label):
        """
        Check if the user has permissions to view the app `app_label`.
        """
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """
        Check if the user is a member of staff.
        """
        return self.is_admin



class ProfileUpdate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Date_of_Birth = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='auth/media')
    pan_number = models.CharField(max_length=50)
    pan_picture = models.ImageField(upload_to='auth/media') 
    

    
