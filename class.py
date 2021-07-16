class demo:
    msg="hello"
    
    def print_msg(self):
        print(self.msg)
        
    def set_msg(self, text):
        self.msg = text

d1=demo()
d1.print_msg()

d1.set_msg("Hii")
d1.print_msg()