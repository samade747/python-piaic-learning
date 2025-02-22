class Masjid():
    #common things
    religion = "Islam"
    qibla = "khana e kaba"




    def __init__(self, name, address, minar = 1, gumbad = 1 ) -> None:
        self.name = name
        self.address = address
        self.minar = minar
        self.gumbad = gumbad

    def azan(self, timing):
        return f"(azan, {timing})"

    def namaz(self, timing):
        return f"(namaz, {timing})"
    

masjid1 = Masjid("bilai masjid", "m.ali")
print



