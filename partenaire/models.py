from django.db import models



class Partenaire(models.Model):
	nom_organisation = models.CharField(max_length=200)
	description = models.TextField()
	lien_site = models.CharField(max_length=300)
	logo = models.ImageField(upload_to='partenaires',null=False)
	def __unicode__(self):
        	return self.nom_organisation
	
		
	
