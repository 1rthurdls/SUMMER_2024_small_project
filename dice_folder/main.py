import pygame
import module_dice



def ecran_acceuil():
    image = "roll_the_dice.png"
    image_acceuil = pygame.image.load(image).convert()
    image_acceuil = pygame.transform.scale(image_acceuil,(1000,600))
    fenetre.blit(image_acceuil,(0,0))
def click_here_acceuil():
    image = "click_here_acceuil.png"
    image_acceuil = pygame.image.load(image).convert()
    image_acceuil = pygame.transform.scale(image_acceuil,(1000,600))
    fenetre.blit(image_acceuil,(0,0))


def lancer():
    rez_1 = "REZ_1.png"
    image_rez_1 = pygame.image.load(rez_1).convert()
    image_rez_1 = pygame.transform.scale(image_rez_1,(1000,600))
    rez_2 = "REZ_2.png"
    image_rez_2 = pygame.image.load(rez_2).convert()
    image_rez_2 = pygame.transform.scale(image_rez_2,(1000,600))
    rez_3 = "REZ_3.png"
    image_rez_3 = pygame.image.load(rez_3).convert()
    image_rez_3 = pygame.transform.scale(image_rez_3,(1000,600))
    rez_4 = "REZ_4.png"
    image_rez_4 = pygame.image.load(rez_4).convert()
    image_rez_4 = pygame.transform.scale(image_rez_4,(1000,600))
    rez_5 = "REZ_5.png"
    image_rez_5 = pygame.image.load(rez_5).convert()
    image_rez_5 = pygame.transform.scale(image_rez_5,(1000,600))
    rez_6 = "REZ_6.png"
    image_rez_6 = pygame.image.load(rez_6).convert()
    image_rez_6 = pygame.transform.scale(image_rez_6,(1000,600))
    resultat = module_dice.dice()
    vrai = True
    while vrai : 
        souris = pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                vrai=False
            if 250 <souris[0]<660 and 450 < souris[1] < 570 and events.type == pygame.MOUSEBUTTONDOWN:
                lancer()
            if resultat ==1 :
                fenetre.blit(image_rez_1,(0,0))
                pygame.display.flip()
            if resultat ==2 :
                fenetre.blit(image_rez_2,(0,0))
                pygame.display.flip()
            if resultat ==3 :
                fenetre.blit(image_rez_3,(0,0))
                pygame.display.flip()
            if resultat ==4 :
                fenetre.blit(image_rez_4,(0,0))
                pygame.display.flip()
            if resultat ==5 :
                fenetre.blit(image_rez_5,(0,0))
                pygame.display.flip()
            if resultat ==6 :
                fenetre.blit(image_rez_6,(0,0))
                pygame.display.flip()   

pygame.display.init()

longueur_fenetre = 600
largeur_fenetre =1000 
fenetre  = pygame.display.set_mode((largeur_fenetre,longueur_fenetre))
pygame.display.set_caption("dice")
noir = (0,0,0)
run = True

while run : 
    souris = pygame.mouse.get_pos()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run=False
        
        if 280 < souris[0] <680 and 340 < souris[1]< 580 :
            click_here_acceuil()
            pygame.display.flip()
            if events.type == pygame.MOUSEBUTTONDOWN:
                lancer()
        

        
        else : 
            ecran_acceuil()
            pygame.display.flip()
   
pygame.quit()