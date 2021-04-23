import anvil.server
class Healthcheck:

    def anvilcheck(self):
        print("Checking Health check")
        try:
            anvil.server.connect("PQHMGGR25KYIUFC4ISNXZQOD-BDAVHYXEEACMTHCG-DEV")
        except Exception as e:
            print("Problem connecting: %s" % e)
            print("Error: Caught an exception")

        anvil.server.wait_forever()

@anvil.server.callable
def anvil_health_check(text):
    if text != None:
        print("Connection with Anvil UI is successfull")
        print("Bravo! Text from Anvil UI :"+text)
        return True
    return False

if __name__ == "__main__":
    ck = Healthcheck()
    print(ck.anvilcheck())