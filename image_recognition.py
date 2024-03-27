import cv2
import numpy as np

# CONSTANTES
threshold = .80  # Valor mínimo para aceptar una coincidencia
blue = (255, 99, 71)  # Color para los objetos de Blue Djinn
green = (0, 255, 0)  # Color para los objetos Green Djinn
yellow = (0, 255, 255)  # Color para los objetos de Rashid


def detect_items(bp_img, blue_images, green_images, rashid_images):
    # Lista de tuplas que contiene las imágenes y los colores asociados
    categories = [(blue_images, blue), (green_images, green), (rashid_images, yellow)]

    # Iterar sobre cada categoría (Blue Djinn, Green Djinn, Rashid)
    for category_images, color in categories:
        # Iterar sobre las imágenes de la categoría actual
        for item_img in category_images:
            # Calcular la correlación de plantilla entre la imagen principal y la imagen actual
            result = cv2.matchTemplate(bp_img, item_img, cv2.TM_CCOEFF_NORMED)
            # Obtener el ancho (w) y la altura (h) de la imagen actual
            w, h = item_img.shape[1], item_img.shape[0]
            # Encontrar las ubicaciones donde la correlación es mayor o igual que el umbral
            yloc, xloc = np.where(result >= threshold)

            # Iterar sobre cada ubicación encontrada
            for (x, y) in zip(xloc, yloc):
                # Dibujar un rectángulo alrededor del objeto detectado en la imagen principal
                cv2.rectangle(bp_img, (x, y), (x + w, y + h), color, 2)

    # Guardar la imagen con los rectángulos dibujados
    cv2.imwrite('result.jpg', bp_img)


# CARGA DE IMÁGENES

# Lista de imágenes de objetos de Blue Djinn
blue_item_images = [cv2.imread(f'Blue/{i}.png', cv2.IMREAD_UNCHANGED) for i in
                    ['woi', 'woi2', 'woi3', 'wop', 'wov', 'boh', 'c_armor', 'c_shield', 'crusader_helmet',
                     'dragon_shield', 'fire_sword', 'guardian_shield', 'noble_armor', 'rh', 'war_hammer']]

# Lista de imágenes de objetos de Green Djinn
green_item_images = [cv2.imread(f'Green/{i}.png', cv2.IMREAD_UNCHANGED) for i in
                     ['tempest', 'tempest2', 'tempest3', 'quagmire', 'dragon_hammer', 'k_armor', 'k_legs',
                      'k_axe', 'onyx_flail', 'serpent_sword', 'warrior_helmet']]

# Lista de imágenes de objetos de Rashid
rashid_item_images = [cv2.imread(f'Rashid/{i}.png', cv2.IMREAD_UNCHANGED) for i in ['dbs', 'dbs2']]
