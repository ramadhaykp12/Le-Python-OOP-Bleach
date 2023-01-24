class Karakter :
  def __init__(self,nama,power,health):
    self.nama = nama
    self.power = power
    self.health = health
  def info(self):
    print("Nama : " + self.nama + "Power : " + self.power + "Health : " + self.health)

class Shinigami(Karakter):
  def __init__(self,nama,power,health,bankai):
    Karakter.__init__(self, nama, power, health)
    self.bankai = bankai

  def aktifkanBankai(self):
    print(self.nama + " Mengaktifkan Bankai " + self.bankai )
    self.power += 20
    self.health += 10
    print("Power meningkat menjadi ")
    print(self.power)
    print("health meningkat menjadi")
    print(self.health)

class Quincy(Karakter):
  def __init__(self,nama,power,health,volstanding):
    Karakter.__init__(self,nama,power,health)
    self.volstanding = volstanding

  def aktifkanVolstanding(self):
    print(self.nama + " mengaktifkan volstanding " + self.volstanding)
    self.power += 30
    self.health -= 10
    print("Power meningkat menjadi")
    print(self.power)
    print("health berkurang menjadi")
    print(self.health)

class Arrancar(Karakter):
  def __init__(self,nama,power,health,mode):
    Karakter.__init__(self,nama,power,health)
    self.mode = mode

  def EvolusiMode(self):
    print(self.nama + " Berevolusi menjadi " + self.mode)
    self.power += 10
    self.health += 5
    print("Power meningkat menjadi")
    print(self.power)
    print("health bertambah menjadi")
    print(self.health)

    

ichigo = Shinigami("Ichigo",70, 100, "Tensa Zangetsu")
ichigo.aktifkanBankai()

yhwach = Quincy("Yhwach", 90, 100, "Almighty")
yhwach.aktifkanVolstanding()

stark = Arrancar("Stark", 50, 100, "Vaste Lorde")
stark.EvolusiMode()

    
