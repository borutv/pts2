# pts2
Naprogramujte terminálové "Človeče nehnevaj sa!". Môžte si upraviť pravidlá. Odporúčané úpravy (zjednoduženia): po hodení 6-ky hr=ač nehádže ešte raz, po obkrúžení kolečka panáčikovia nejdu do "domčeka", ale sa točia daľej (teda domček ani neexistuje). Program taktiež nemusí byť úplne user friendly. 
Aktuálny stav hry má byť uložený ako jedna imutable premenná, a referencia na tento stav má byť v podstate jedinou "verejnou" mutovatelnou premennou v programe. To samozrejme neznamená, že v kóde nemajú byť mutable premenné, takéto premenné však majú existovať iba v lokálnom scope. 
Súčasťou odovzdaného repozitára má byť základná používateľská dokumentácia, stručný popis designu a aspoň základné testovacie programy. 
Ako si napríklad máte predstaviť terminálové človeče
Player 2 is on turn.
Dice: 4.
Player 0's pieces are on fields: 0:40 1:41 2:42 3:43
Player 1's pieces are on fields: 0:44 1:45 2:46 3:47
Player 2's pieces are on fields: 0:48 1:49 2:50 3:51
Player 3's pieces are on fields: 0:52 1:53 2:54 3:30
>pass
>throw
Player 3 is on turn.
Dice: 5.
Player 0's pieces are on fields: 0:40 1:41 2:42 3:43
Player 1's pieces are on fields: 0:44 1:45 2:46 3:47
Player 2's pieces are on fields: 0:48 1:49 2:50 3:51
Player 3's pieces are on fields: 0:52 1:53 2:54 3:30
>move 3
Player 0 is on turn.
Dice: 0.
Player 0's pieces are on fields: 0:40 1:41 2:42 3:43
Player 1's pieces are on fields: 0:44 1:45 2:46 3:47
Player 2's pieces are on fields: 0:48 1:49 2:50 3:51
Player 3's pieces are on fields: 0:52 1:53 2:54 3:35
