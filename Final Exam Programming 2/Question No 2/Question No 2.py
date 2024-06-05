#---------------------------------------------Hello Welcome to Question No 2--------------------------------------

print("Question No 2")


              

                      

class Property:
    def __init__(self,property_id,name,location,description,price_per_night,availability):                     
        self.property_id = property_id                    
        self.name = name                     
        self.location = location                         
        self.description = description                 
        self.price_per_night = price_per_night                                                                                                              
        self.availability = availability 
                                                                                      

                                                                                      

                                                                                      
    def tell_availability(self, status):
        self.tell_availability = status 
                                                                                      


                                                                                      


    def get_details(self):                              
        return {           
            "property_id": self.property_id,             
            "name": self.name,                      
            "location": self.location,               
            "description": self.description,            
            "price_per_night": self.price_per_night,                
            "availability": self.availability              
               }                   
                                
                               
           
                      

            
                            
class user:
    def __init__(self,user_id,name,age,phone):          
        self.user_id = user_id                          
        self.name = name                  
        self.age = age              
        self.phone = phone                           




    def get_profile(self):                   
        return {                      
            "user_id": self.user_id,                    
            "Age" : self.age,           
            "name": self.name,    
            "phone": self.phone
               }                                              
     
       
                    
      
        
           
        
class Host(user):                
    def __init__(self, user_id, name, age, phone):                              
        super().__init__(user_id, name, age, phone)                                             
                              
        self.listed_properties = []            
                      
    def list_property(self, property):                   
        self.listed_properties.append(property)                                     
                         
    def get_properties(self):
        return [property.get_details() for property in self.listed_properties]          


         
    
     
    
                   
class Guest(user):                                              
    def __init__(self, user_id, name, age, phone):                            
        super().__init__(user_id, name, age, phone)                                                         
                                                               
        self.bookings_made = []      
               
    def make_booking(self, property, check_in_date, check_out_date):                       
        booking = Booking_system(property, self, check_in_date, check_out_date)                         
        self.bookings_made.append(booking)                            
                                                            
    def get_bookings(self):               
        return [booking.get_details() for booking in self.bookings_made]            
             
                  

                                   
class Booking_system:
    def __init__(self,property,guests,check_in_date,che_out_date):               
        self.booking_id = None                            
        self.property = property                                      
        self.guests = guests
        self.check_in_date = check_in_date                               
        self.check_out_date = che_out_date
        self.booking_status = "confirmed"
                     

    def update_booking_status(self, status):
        self.booking_status = status

    def get_details(self):
        return {
            "booking_id": self.booking_id,
            "property": self.property.get_details(),
            "guest": self.guests.get_profile(),                                        
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,                      
            "booking_status": self.booking_status
        }     

    

      

            
host1 = Host("001", "Waleed Chaudhry", 20, "03200049739")
                                                  
#----------------------------------------------------------------------------------                      

property1 = Property("501", "WM Tower", "Lahore", "A beautiful Appartemnt with views of DHA Raya", 50000,"yes")                   
property2 = Property("502", "WM Tower", "Lahore", "A beautiful Appartemnt with views of DHA Raya", 60000,"Yes")               
                            

                                               
host1.list_property(property1)              
host1.list_property(property2)             
                                      
                        
#------------------------------------------------------------------------------------

guest = Guest(1, "sufyan", 25, "000002010")             
                            
                
guest.make_booking(property1, "2024-05-5", "2024-06-8")                     
              
#------------------------------------------------------------------------------------


print("Host's listed properties:")                                       
for prop in host1.get_properties():                     
    print(prop)

print("\nGuest 1's bookings:")
for booking in guest.get_bookings():              
    print(booking)

print("Thank You Choosing Our Service --_--")