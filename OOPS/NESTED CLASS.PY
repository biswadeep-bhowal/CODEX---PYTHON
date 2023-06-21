# PROGRAM TO ILLUSTRATE NESTED CLASS

class student : 

	school = "DELHI PUBLIC SCHOOL, RUBY PARK, KOLKATA"

	def __init__( self ) : 
		self.get_info()
		self.device = self.laptop()
		self.display()

	def get_info( self ) : 
		self.name = input( "Student Name : " )
		self.roll_no = input( "Student Roll No. : " )

	def display( self ) : print( "\tStudent Details\n\nSchool : {}\nName : {}\nRoll No. : {}\n\tLaptop Details\n\nBrand : {}\nProcessor : {}\nRam : {}".format( self.school, self.name, self.roll_no, self.device.brand, self.device.cpu, self.device.ram ) )

	class laptop : 

		def __init__( self ) : self.get_info()

		def get_info( self ) : 
			self.brand = input( "Laptop Brand : " )
			self.cpu = input( "Laptop processor : " )
			self.ram = input( "Laptop ram : " )

s1 = student()
