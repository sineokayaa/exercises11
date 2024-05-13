class AirConditioning:
    '''
    A class representing an air conditioning system.

    Attributes:
        __status (bool): The status of the air conditioning system (True for on, False for off).
        __temperature (int or None): The temperature setting of the air conditioning system.
            None if the system is off.
    '''
    __status = False
    __temperature = None

    @property
    def status(self):
        '''
        Get the status of the air conditioning system.
        '''
        if AirConditioning.__status:
            return f'Кондиционер включен.'
        else:
            return f'Кондиционер выключен.'

    @status.setter
    def status(self, value):
        '''
        Set the status of the air conditioning system.
        '''
        AirConditioning.__status = AirConditioning.__status

    @status.getter
    def status(self):
        '''
        Get the status of the air conditioning system.
        '''
        return AirConditioning.__status

    @property
    def temperature(self):
        '''
        Get the temperature setting of the air conditioning system.
        '''
        return AirConditioning.__temperature

    @temperature.setter
    def temperature(self, value):
        '''
        Set the temperature setting of the air conditioning system.
        '''
        AirConditioning.__temperature = AirConditioning.__temperature

    @temperature.getter
    def temperature(self):
        '''
        Get the temperature setting of the air conditioning system.
        '''
        return AirConditioning.__temperature

    @classmethod
    def __str__(cls):
        if AirConditioning.__status:
            return (f'Кондиционер включен.'
                    f' Температурный режим: {AirConditioning.__temperature}'
                    f' градусов.')
        return f'Кондиционер выключен.'

    @classmethod
    def switch_on(cls):
        '''
        Turn on the air conditioning system with a
        default temperature setting of 18 degrees.
        '''
        AirConditioning.__status = True
        AirConditioning.__temperature = 18

    @classmethod
    def switch_off(cls):
        '''
        Turn off the air conditioning system.
        '''
        AirConditioning.__status = False
        AirConditioning.__temperature = None

    @classmethod
    def reset(cls):
        '''
        Reset the temperature setting to default (18 degrees)
        if the air conditioner is on.
        '''
        if AirConditioning.__status:
            AirConditioning.__temperature = 18

    @classmethod
    def get_temperature(cls):
        '''
        Get the temperature setting of the air conditioning system.
        '''
        return AirConditioning.__temperature

    @classmethod
    def raise_temperature(cls):
        '''
        Raise the temperature setting by 1 degree if the air
        conditioner is on and the temperature is below 43 degrees.
        '''
        if AirConditioning.__status and AirConditioning.__temperature < 43:
            AirConditioning.__temperature += 1

    @classmethod
    def lower_temperature(cls):
        '''
        Lower the temperature setting by 1 degree if the
        air conditioner is on and the temperature is above 0 degrees.
        '''
        if AirConditioning.__status and AirConditioning.__temperature > 0:
            AirConditioning.__temperature -= 1


conditioning = AirConditioning()
print(conditioning)
print(conditioning.temperature)
print(conditioning.status)
conditioning.status = True
print(conditioning)
print(conditioning.status)
conditioning.temperature = 20
print(conditioning.temperature)
conditioning.reset()
print(conditioning)
print(conditioning.get_temperature())
conditioning.raise_temperature()
print(conditioning.get_temperature())
conditioning.lower_temperature()
print(conditioning.get_temperature())
conditioning.switch_on()
print(conditioning)
print(conditioning.get_temperature())
print(conditioning.temperature)
conditioning.temperature = 30
print(conditioning.temperature)
conditioning.status = False
print(conditioning)
for _ in range(16):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(5):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(40):
    conditioning.raise_temperature()
print(conditioning)
for _ in range(5):
    conditioning.raise_temperature()
print(conditioning)
conditioning.switch_off()
print(conditioning)
