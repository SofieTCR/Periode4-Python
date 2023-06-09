import rewards

skins = []
for i in range(5):
    skins.append(rewards.get_new_skin())
resultaat = "Je hebt {} LEGENDARY skins, {} EPIC skins, {} RARE skins en {} COMMON skins gekregen!"

print(resultaat.format(skins.count("LEGENDARY"), skins.count("EPIC"), skins.count("RARE"), skins.count("COMMON")))