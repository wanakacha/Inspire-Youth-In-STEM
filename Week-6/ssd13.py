# ----------------------------------------------------------------------------
# (| " SSD1306_I2C.py                                                      "|)
# (| " Este es un sencillo sketch que implementa una pantalla OLED SSD1306 "|)
# (| " I2C de 0.96" 128x64, visualizando imagen y texto, con una raspberry "|)
# (| " pi pico y MicroPython.        							                         "|)
# (| "                                                                     "|)
# (| " Se utiliza el modulo de micropython para display OLED SSD1306 de    "|)
# (| " Stefan Lehmann, el cual debe instalarse primero dentro de la        "|)
# (| " raspberry pi pico para que este sketch funcione.                    "|)
# (| "   							                                                     "|)
# (| " Usaremos los valores predeterminados de I2C0, para la OLED 0.96"    "|)
# (| " monocromática I2C 128x64 SCL= Pin GP9, SDA= Pin GP8 de la raspberry "|)
# (| " pi pico.                                                            "|)
# (| "                                                                     "|)
# (| " Este código de ejemplo es de dominio público.                       "|)
# (| "                                                                     "|)
# (| " Maker: jorgechac©                                                   "|)
# (| " Visita  https://jorgechac.blogspot.com                              "|)
# (| "                                                                     "|)
# (| " Venta de accesorios Arduino/Raspberry Pi Pico/ESP32   		           "|)
# (| " Whatsapp y Ventas NEQUI +573177295861                               "|)
# (| " Bucaramanga - Colombia                                              "|)
# (| " Simulaciön https://wokwi.com/projects/339754775704765010            "|)
# (| " Repositorio https://github.com/jorgechacblogspot/micropython_pico   "|)
# (| " https://jorgechac.blogspot.com/2021/04/raspberry-pi-pico-pin-mapping.html "|)
# ----------------------------------------------------------------------------------

from machine import Pin, I2C    # importamos la funcion pin del modulo machine y la función I2C
from ssd1306 import SSD1306_I2C
import framebuf

WIDTH  = 128                                            # declaramos el ancho de pantalla OLED
HEIGHT = 64                                             # declaramos la altura de la pantalla OLED
i2c = I2C(0)                                            # Inicializa I2C usando los valores predeterminados de
                                                        # I2C0, SCL= Pin GP9, SDA= Pin GP8, freq = 400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Muestra la dirección del dispositivo en la shell o consola
print("I2C Configuration: "+str(i2c))                   # Muestra la configuración I2C en la shell o consola
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Inicializa la pantalla oled

# Raspberry Pi logo como 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Carga el raspberry pi logo en el framebuffer (la imagen es de 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# Limpia la pantalla oled en caso de que tenga algo
oled.fill(0)

# Transfiere la imagen del framebuffer a la pantalla oled
oled.blit(fb, 96, 0)

# Agrega el texto
oled.text("Raspberry Pi",5,5)    # escribimos en la columna 5 fila 5
oled.text("Pico",5,15)           # escribimos en la columna 5 fila 15
oled.text("OLED I2C",5,35)       # escribimos en la columna 5 fila 35
oled.text("128x64",5,45)         # escribimos en la columna 5 fila 45

# Finalmente actualiza la pantalla oled para que se muestre la imagen y el texto
oled.show()