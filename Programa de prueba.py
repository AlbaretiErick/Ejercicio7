from Ejercicio7 import ViajeroFrecuente

if __name__ == '__main__':
    v = ViajeroFrecuente (1234, 'Erick', 'Torres', 12345677, 100)
    if v == 100:
        print ('El viajero {} posee 100 millas acumuladas de izquierda a derecha'.format (v.getNombre()))
    if 100 == v:
        print ('y tambien de derecha a izquierda')
    else:
        print ('El viajero {} no posee 100 millas acumuladas'.format (v.getNombre()))
    v.mostrar ()
    v = 100 + v
    print ('El viajero {} ahora posee {} millas acumuladas. (+100)'.format (v.getNombre(), v.cantidadTotalMillas ()))
    v = 100 - v
    print ('El viajero {} ahora posee {} millas acumuladas. (-100)'.format (v.getNombre(), v.cantidadTotalMillas ()))